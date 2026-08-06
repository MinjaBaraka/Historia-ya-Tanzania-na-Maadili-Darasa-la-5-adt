# Darasa la 5 correction audit

## Review sources

- `HISTORIA NA MAADILI STD5.docx` — content and layout review.
- `HISTORIA NA MAADILI STD-5-AUDIO STD5.docx` — narration and pronunciation review.

`HISTORIA NA MAADILI STD4.docx` was intentionally excluded: it is for Darasa la 4 and must not be mixed into this Darasa la 5 bundle.

## Implemented in this release

- Removed the hidden, non-source **“FOR ONLINE READING ONLY”** reader message. This does not remove a watermark when it is visibly part of the original title-page artwork.
- Corrected source and fallback HTML text on pages 70, 76, 80, 82, 94, 111, 114, and 115. This includes `mwendelezo`, `alichukua`, `mababu`, `telegramu`, `kibepari`, `alitoalo`, `aliyeukiuka`, `kukiuka`, `kuzilinda`, `Ina maana kwamba`, `hauigizwi`, `anayetii`, and `kuzikuza`.
- Updated the matching Easy Read entries for `telegramu`, `kibepari`, `mababu`, and `anayetii`.
- Corrected further reviewed source-text defects on pages 86, 92, 102, 103, 105, 108, 115, 118, and 120, including `waliokuwa`, `zilitegemea`, `utawala`, `waliamua`, `kinachoongoza`, `wanajamii`, `mdundiko`, `ilisababishwa`, `inamaanisha`, `Kuienzi`, and `hujiita`.
- Refreshed `assets/offline-preloader.js`, so the same corrected texts work when the book is opened offline.
- Confirmed that consolidated secondary sections are no longer in `content/pages.json`. Their old URLs remain as redirect-only compatibility files, preventing broken bookmarks and the previous GitHub Pages 404 error.

## Audio follow-up

The active narration library now contains 5,620 text/audio IDs. The two obsolete hidden-cover IDs and MP3 files were removed. The audio review identifies issues that need newly narrated Swahili MP3 files: dates and numbers, Roman numerals, figure numbers, image descriptions, and the listed word-level pronunciations.

The human-recording handoff is prepared at `/Volumes/MINJA/ADT/Marekebisho/HISTORIA_NA_MAADILI_STD5_HUMAN_NARRATION/`. It contains a 5,620-item manifest and empty `recordings/` directory. The recordings are pending; existing MP3 files must not be replaced or published as reviewed narration until approved human WAV files are supplied. Priority examples are page 5 abbreviations (`Bw.`, `Dkt.`), page 7 nineteenth-century dates, pages 8–9 historical years and exercise numbers, page 80 `telegramu`, page 111 the *Fikiri* passage, and page 128 exercise 5.

## Verification performed

1. Rendered and visually inspected the two Darasa la 5 review documents.
2. Parsed the 166-entry reading spine and checked every retired secondary-section URL is excluded from it but still present as a redirect.
3. Synchronized every edited fallback HTML string with `content/i18n/sw-TZ/texts.json`.
4. Rebuilt the embedded offline JSON data, verified 5,620 active text/audio mappings with no missing MP3 files, and checked the working tree for whitespace errors.
