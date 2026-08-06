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
- Corrected six table-of-contents links that still named redirect-only legacy section files. They now open the corresponding canonical reading-spine page, while the legacy URLs remain available for existing bookmarks.
- Added the existing book favicon and web-manifest links to every live page head. Updated the web-manifest name and short name to this book; it no longer presents an unrelated Spanish book title when installed.

## Audio follow-up

The active narration library now contains 5,620 text/audio IDs. The two obsolete hidden-cover IDs and MP3 files were removed. The audio review identifies issues that need newly narrated Swahili MP3 files: dates and numbers, Roman numerals, figure numbers, image descriptions, and the listed word-level pronunciations.

The human-recording handoff is prepared at `/Volumes/MINJA/ADT/Marekebisho/HISTORIA_NA_MAADILI_STD5_HUMAN_NARRATION/`. It contains a 5,620-item manifest and empty `recordings/` directory. The recordings are pending; existing MP3 files must not be replaced or published as reviewed narration until approved human WAV files are supplied. Priority examples are page 5 abbreviations (`Bw.`, `Dkt.`), page 7 nineteenth-century dates, pages 8–9 historical years and exercise numbers, page 80 `telegramu`, page 111 the *Fikiri* passage, and page 128 exercise 5.

## Verification performed

1. Rendered and visually inspected the two Darasa la 5 review documents.
2. Parsed the 166-entry reading spine and checked every retired secondary-section URL is excluded from it but still present as a redirect.
3. Synchronized every edited fallback HTML string with `content/i18n/sw-TZ/texts.json`.
4. Rebuilt the embedded offline JSON data, verified 5,620 active text/audio mappings with no missing MP3 files, and checked the working tree for whitespace errors.
5. Completed a whole-bundle static audit: all 166 reading-spine files exist; every live-page `data-id` resolves to `texts.json`; all local HTML assets resolve; the table of contents contains no redirect-only target; every live page has the five favicon/manifest links; and the offline preloader contains the current text and spine data.

## Remaining release gates

- The supplied audio-review document still requires approved human Kiswahili replacements. No recordings were supplied, so the existing MP3s were retained and this narration gate remains open.
- A full page-by-page visual comparison against the source PDF, plus representative desktop, tablet, and phone interaction/console testing, remains required before claiming complete source-equivalence under the conversion guide.
