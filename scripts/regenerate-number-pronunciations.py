#!/usr/bin/env python3
"""Regenerate every numeric narration with dynamic Swahili place values."""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
import re
import shutil
from collections import defaultdict
from pathlib import Path

VOICE = "sw-TZ-RehemaNeural"

UNITS = {
    0: "sifuri",
    1: "moja",
    2: "mbili",
    3: "tatu",
    4: "nne",
    5: "tano",
    6: "sita",
    7: "saba",
    8: "nane",
    9: "tisa",
}
TENS = {
    10: "kumi",
    20: "ishirini",
    30: "thelathini",
    40: "arobaini",
    50: "hamsini",
    60: "sitini",
    70: "sabini",
    80: "themanini",
    90: "tisini",
}
SCALES = (
    (1_000_000_000_000, "trilioni"),
    (1_000_000_000, "bilioni"),
    (1_000_000, "milioni"),
    (100_000, "laki"),
    (1_000, "elfu"),
)

NUMBER = r"(?:\d{1,3}(?:,\d{3})+|\d+)"
DASH_GROUP = re.compile(rf"(?<!\d){NUMBER}(?:[-–—]{NUMBER})+(?!\d)")
PLAIN_NUMBER = re.compile(NUMBER)
DASH_SPLIT = re.compile(r"[-–—]")
QUESTION_START = re.compile(rf"^\s*({NUMBER})\s*[.)]\s*")


def number_to_words(value: int) -> str:
    if value < 0:
        raise ValueError("Negative numbers are not used by the ADT pronunciation rule")
    if value < 10:
        return UNITS[value]
    if value < 100:
        tens = value // 10 * 10
        remainder = value % 10
        return TENS[tens] if remainder == 0 else f"{TENS[tens]} na {UNITS[remainder]}"
    if value < 1_000:
        hundreds = value // 100
        remainder = value % 100
        prefix = f"mia {number_to_words(hundreds)}"
        if remainder == 0:
            return prefix
        connector = " na " if remainder < 20 else " "
        return prefix + connector + number_to_words(remainder)
    for divisor, label in SCALES:
        if value >= divisor:
            quotient, remainder = divmod(value, divisor)
            prefix = f"{label} {number_to_words(quotient)}"
            if remainder == 0:
                return prefix
            connector = " na " if remainder < 100 else " "
            return prefix + connector + number_to_words(remainder)
    raise AssertionError(value)


def numeric_group_to_words(raw: str) -> str:
    compact = raw.replace(",", "")
    if len(compact) > 1 and compact.startswith("0"):
        return " ".join(UNITS[int(digit)] for digit in compact)
    return number_to_words(int(compact))


def narration_text(source: str) -> str:
    question = QUESTION_START.match(source)
    if question:
        source = (
            f"Swali namba {numeric_group_to_words(question.group(1))}. "
            f"{source[question.end():]}"
        ).rstrip()
    text = source.replace("©", "Hati miliki ya")
    text = re.sub(r"\bISBN\b", "Ai es bi en", text, flags=re.IGNORECASE)
    text = re.sub(r"S\.?\s*L\.?\s*P\.?", "Sanduku la posta", text, flags=re.IGNORECASE)
    text = re.sub(r"(?<=\d)\s*/\s*(?=\+\d)", "; au ", text)
    text = re.sub(r"\+(?=\d)", "alama ya kumjulisha, ", text)

    def replace_dash_group(match: re.Match[str]) -> str:
        groups = DASH_SPLIT.split(match.group(0))
        return ", dash, ".join(numeric_group_to_words(group) for group in groups)

    text = DASH_GROUP.sub(replace_dash_group, text)
    text = re.sub(r"\s*[-–—]\s*", ", dash, ", text)
    text = PLAIN_NUMBER.sub(lambda match: numeric_group_to_words(match.group(0)), text)
    return re.sub(r"[ \t]+", " ", text).strip()


def run_self_tests() -> None:
    examples = {
        "978": "mia tisa sabini na nane",
        "765": "mia saba sitini na tano",
        "9912": "elfu tisa mia tisa na kumi na mbili",
        "25": "ishirini na tano",
        "128": "mia moja ishirini na nane",
        "2025": "elfu mbili na ishirini na tano",
        "04": "sifuri nne",
        "75,000": "elfu sabini na tano",
        "108,550": "laki moja elfu nane mia tano hamsini",
        "120,000": "laki moja elfu ishirini",
    }
    for source, expected in examples.items():
        actual = numeric_group_to_words(source)
        if actual != expected:
            raise AssertionError(f"{source}: {actual!r} != {expected!r}")

    isbn = narration_text("ISBN 978-9912-765-04-7")
    expected_isbn = (
        "Ai es bi en mia tisa sabini na nane, dash, "
        "elfu tisa mia tisa na kumi na mbili, dash, "
        "mia saba sitini na tano, dash, sifuri nne, dash, saba"
    )
    if isbn != expected_isbn:
        raise AssertionError(f"ISBN example: {isbn!r} != {expected_isbn!r}")
    question = narration_text("12. Eleza jibu lako.")
    if question != "Swali namba kumi na mbili. Eleza jibu lako.":
        raise AssertionError(f"Question example: {question!r}")

    postal_box = narration_text("S.L.P. 35094")
    expected_postal_box = "Sanduku la posta elfu thelathini na tano na tisini na nne"
    if postal_box != expected_postal_box:
        raise AssertionError(
            f"Postal-box example: {postal_box!r} != {expected_postal_box!r}"
        )


def collect_records(root: Path):
    texts = json.loads((root / "content/i18n/sw-TZ/texts.json").read_text(encoding="utf-8"))
    audios = json.loads((root / "content/i18n/sw-TZ/audios.json").read_text(encoding="utf-8"))
    records = []
    for text_id, source in texts.items():
        filename = audios.get(text_id)
        if not filename or not re.search(r"\d|©|\+(?=\d)", source):
            continue
        spoken = narration_text(source)
        if re.search(r"\d", spoken):
            raise RuntimeError(f"Unconverted digit in {text_id}: {spoken}")
        records.append(
            {"id": text_id, "source": source, "spoken": spoken, "filename": filename}
        )
    return records


async def synthesize(root: Path, records, concurrency: int) -> None:
    import edge_tts

    by_spoken = defaultdict(list)
    for record in records:
        by_spoken[record["spoken"]].append(record)

    temp = Path("/private/tmp/adt_number_pronunciation_audio")
    if temp.exists():
        shutil.rmtree(temp)
    source_dir = temp / "source"
    staged_dir = temp / "staged"
    source_dir.mkdir(parents=True)
    staged_dir.mkdir(parents=True)
    limiter = asyncio.Semaphore(max(1, concurrency))

    async def one(position: int, spoken: str):
        digest = hashlib.sha256(spoken.encode("utf-8")).hexdigest()[:20]
        output = source_dir / f"{digest}.mp3"
        async with limiter:
            for attempt in range(1, 5):
                try:
                    await edge_tts.Communicate(spoken, VOICE).save(str(output))
                    if output.exists() and output.stat().st_size > 0:
                        print(f"[{position}/{len(by_spoken)}] {spoken}", flush=True)
                        return spoken, output
                except Exception as exc:
                    if attempt == 4:
                        raise RuntimeError(f"TTS failed after 4 attempts: {spoken}") from exc
                    await asyncio.sleep(attempt * 1.5)
            raise RuntimeError(f"Empty TTS output: {spoken}")

    generated = dict(
        await asyncio.gather(
            *(one(position, spoken) for position, spoken in enumerate(by_spoken, 1))
        )
    )

    install_generated(root, records, generated, temp)


def install_generated(root: Path, records, generated, temp: Path) -> None:
    staged_dir = temp / "staged"
    staged_dir.mkdir(parents=True, exist_ok=True)
    for record in records:
        shutil.copyfile(generated[record["spoken"]], staged_dir / record["filename"])

    target = root / "content/i18n/sw-TZ/audio"
    for record in records:
        os.replace(staged_dir / record["filename"], target / record["filename"])
    shutil.rmtree(temp)


def install_existing(root: Path, records) -> None:
    temp = Path("/private/tmp/adt_number_pronunciation_audio")
    source_dir = temp / "source"
    generated = {}
    for spoken in {record["spoken"] for record in records}:
        digest = hashlib.sha256(spoken.encode("utf-8")).hexdigest()[:20]
        source = source_dir / f"{digest}.mp3"
        if not source.exists() or source.stat().st_size == 0:
            raise RuntimeError(f"Missing staged TTS output: {source}")
        generated[spoken] = source
    install_generated(root, records, generated, temp)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--install-existing", action="store_true")
    parser.add_argument("--leading-number-only", action="store_true")
    parser.add_argument("--concurrency", type=int, default=6)
    parser.add_argument(
        "--ids",
        help="Optional comma-separated text IDs for a targeted regeneration retry",
    )
    parser.add_argument("--report", default="/private/tmp/adt-number-pronunciation-audit.json")
    args = parser.parse_args()

    run_self_tests()
    root = Path(args.root).resolve()
    records = collect_records(root)
    if args.leading_number_only:
        records = [record for record in records if QUESTION_START.match(record["source"])]
    if args.ids:
        requested = {text_id.strip() for text_id in args.ids.split(",") if text_id.strip()}
        records = [record for record in records if record["id"] in requested]
        found = {record["id"] for record in records}
        missing = requested - found
        if missing:
            raise RuntimeError(f"Requested numeric narration IDs not found: {sorted(missing)}")
    unique_spoken = {record["spoken"] for record in records}
    report = {
        "voice": VOICE,
        "mapped_numeric_narrations": len(records),
        "unique_spoken_texts": len(unique_spoken),
        "standard": sum(not record["id"].endswith("_easy_read") for record in records),
        "easy_read": sum(record["id"].endswith("_easy_read") for record in records),
        "records": records,
    }
    Path(args.report).write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"Audited {len(records)} mapped numeric narrations; "
        f"{len(unique_spoken)} unique Rehema segments."
    )
    for example in (
        "978",
        "9912",
        "978-9912-765-04-7",
        "75,000",
        "108,550",
        "2025",
    ):
        print(f"{example} -> {narration_text(example)}")
    if args.dry_run:
        return 0
    if args.install_existing:
        install_existing(root, records)
        print(f"Installed {len(records)} validated staged numeric MP3 files.")
        return 0
    asyncio.run(synthesize(root, records, args.concurrency))
    print(f"Replaced {len(records)} numeric MP3 files with {VOICE}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
