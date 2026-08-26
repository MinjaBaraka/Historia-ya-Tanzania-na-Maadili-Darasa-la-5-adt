# Full-book ADT audit — Historia ya Tanzania na Maadili

Date: 2026-08-24

Source of truth: the current 128-page PDF supplied for this project. Execution checklist: `ADT_BOOK_TO_WEBSITE_CONVERSION_GUIDE.md`.

## Release-gate summary

- PDF ↔ HTML visual comparison: all 128 pages inspected through eight PDF and eight HTML contact sheets, with every page represented.
- Spine/order: 128/128 files present; section metadata and reading order match `content/pages.json`.
- Semantic/accessibility gate: no whole-page raster content, missing local asset, placeholder, unlabeled control, live DOM duplicate `data-id`, broken image, hidden page content, or horizontal overflow.
- Interactivity: 171 learner-response controls across 35 pages were filled/toggled successfully; labels remained accessible.
- Simultaneous media: read-aloud narration and sign-language video now keep independent playback state. Browser regression on `pg005_sec001.html` passed in both start orders (audio → video and video → audio); stopping narration left video playing, and closing video left narration and yellow word highlighting active.
- Narration runtime: playback and active yellow word highlighting (or active-image state for image descriptions) were exercised on all 128 pages. All 5,445 mapped MP3 files currently in the bundle are present, non-zero, decodable and have positive duration.
- Dynamic-number narration: 633 standard/Easy Read audio mappings containing numbers were regenerated from 441 unique textbook excerpts with Microsoft Rehema Natural `sw-TZ`. The shared converter reads numbers by Swahili place value, treats every dash-separated numeric group independently, says `dash`, and preserves leading zeroes. All 633 installed MP3 files passed decode and positive-duration validation; visible PDF text remains unchanged.
- Question-number cleanup: 44 standalone number narration IDs and their standard/Easy Read audio were removed so a question number is not spoken separately.
- Responsive: every page passed 320×568, 768×1024 and 1440×900.
- Online/offline parity: all remote font dependencies were removed; every page now uses bundled fonts and local resources only. Offline embedded JSON was refreshed and the browser console reported no errors on all 128 pages.
- Printed navigation: 100 decorative PDF footer/page-navigation blocks were removed; the default ADT dock is the sole runtime navigation.
- Printed-navigation final gate: front-matter Roman-numeral footers/capsules (`ii`, `iv`, `vi`), empty footer ribbons on pg003/pg005/pg086, and all remaining printed-page metadata were removed. A live DOM sweep passed 128/128 pages with no printed footer, capsule, ribbon, duplicate counter, broken image, hidden content, or horizontal overflow.
- TOC/spine gate: `content/toc.json` was rebuilt as 39 source-of-truth contents entries mapped directly to current ADT spine indices. The visible Yaliyomo links passed 39/39 click tests, and the default ADT Menyu Kuu TOC independently passed 39/39 click tests; every destination file, section ID, `page-section-id`, and `N/128` counter matched.
- TOC narration gate: all 39 contents entries were regenerated with Microsoft Rehema Natural `sw-TZ` using only the spoken current-page index without saying “ADT” or the total page count (for example, “Ukurasa namba tano”). The 39 standard and 39 Easy Read MP3 files replaced the former audio, passed 78/78 decode/duration checks, and contain no Roman printed-page references. During playback, the visible TOC title mirrors the reader's active-word state with the required yellow mark. The offline preloader refreshes and embeds all 129 HTML sources as well as the nine data catalogs, so the updated narration and highlighting structure is identical online and offline.
- ADT-only page list: 124 PDF `page_number` fields were removed from the runtime spine. The default page list now exposes ADT indices 1–128 only and no longer presents a second “Chapisha Ukurasa …” numbering system.
- Navigation responsive regression: pg002, pg003, pg004, pg005, pg006 and pg086 passed 18/18 checks across 320×568, 768×1024 and 1440×900 after footer/TOC changes.
- Outstanding release blocker: 155 mapped exercise narrations (71 unique excerpts) still require a separate Rehema Natural `sw-TZ` pass with the exact spoken prefix “Swali namba …”. The approved 441-excerpt/633-file dynamic-number batch is complete; the separate question-prefix synthesis attempt did not start because the external execution approval service timed out twice.

## Page-level gate

| PDF file page | ADT page | PDF/layout | Interactivity | Narration/highlight | Responsive/offline | Status |
|---:|---|---|---|---|---|---|
| 1 | `index.html` | PASS | N/A | PASS | PASS | PASS |
| 2 | `pg002_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 3 | `pg003_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 4 | `pg004_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 5 | `pg005_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 6 | `pg006_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 7 | `pg007_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 8 | `pg008_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 9 | `pg009_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 10 | `pg010_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 11 | `pg011_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 12 | `pg012_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 13 | `pg013_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 14 | `pg014_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 15 | `pg015_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 16 | `pg016_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 17 | `pg017_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 18 | `pg018_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 19 | `pg019_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 20 | `pg020_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 21 | `pg021_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 22 | `pg022_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 23 | `pg023_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 24 | `pg024_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 25 | `pg025_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 26 | `pg026_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 27 | `pg027_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 28 | `pg028_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 29 | `pg029_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 30 | `pg030_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 31 | `pg031_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 32 | `pg032_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 33 | `pg033_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 34 | `pg034_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 35 | `pg035_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 36 | `pg036_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 37 | `pg037_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 38 | `pg038_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 39 | `pg039_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 40 | `pg040_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 41 | `pg041_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 42 | `pg042_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 43 | `pg043_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 44 | `pg044_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 45 | `pg045_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 46 | `pg046_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 47 | `pg047_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 48 | `pg048_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 49 | `pg049_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 50 | `pg050_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 51 | `pg051_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 52 | `pg052_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 53 | `pg053_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 54 | `pg054_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 55 | `pg055_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 56 | `pg056_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 57 | `pg057_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 58 | `pg058_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 59 | `pg059_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 60 | `pg060_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 61 | `pg061_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 62 | `pg062_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 63 | `pg063_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 64 | `pg064_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 65 | `pg065_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 66 | `pg066_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 67 | `pg067_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 68 | `pg068_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 69 | `pg069_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 70 | `pg070_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 71 | `pg071_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 72 | `pg072_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 73 | `pg073_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 74 | `pg074_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 75 | `pg075_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 76 | `pg076_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 77 | `pg077_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 78 | `pg078_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 79 | `pg079_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 80 | `pg080_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 81 | `pg081_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 82 | `pg082_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 83 | `pg083_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 84 | `pg084_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 85 | `pg085_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 86 | `pg086_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 87 | `pg087_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 88 | `pg088_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 89 | `pg089_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 90 | `pg090_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 91 | `pg091_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 92 | `pg092_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 93 | `pg093_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 94 | `pg094_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 95 | `pg095_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 96 | `pg096_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 97 | `pg097_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 98 | `pg098_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 99 | `pg099_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 100 | `pg100_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 101 | `pg101_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 102 | `pg102_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 103 | `pg103_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 104 | `pg104_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 105 | `pg105_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 106 | `pg106_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 107 | `pg107_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 108 | `pg108_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 109 | `pg109_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 110 | `pg110_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 111 | `pg111_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 112 | `pg112_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 113 | `pg113_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 114 | `pg114_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 115 | `pg115_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 116 | `pg116_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 117 | `pg117_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 118 | `pg118_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 119 | `pg119_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 120 | `pg120_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 121 | `pg121_sec001.html` | PASS | PASS — controls exercised | PASS | PASS | PASS |
| 122 | `pg122_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 123 | `pg123_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 124 | `pg124_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 125 | `pg125_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 126 | `pg126_sec001.html` | PASS | N/A | PASS | PASS | PASS |
| 127 | `pg127_sec001.html` | PASS | PASS — controls exercised | Playback/highlight PASS; Rehema wording blocked | PASS | BLOCKED — Rehema synthesis approval |
| 128 | `pg128_sec001.html` | PASS | N/A | PASS | PASS | PASS |

## Blocked audio scope

Exercise pages: pg020, pg028, pg036, pg042, pg057, pg065, pg067, pg072, pg076, pg082, pg084, pg088, pg094, pg097, pg099, pg105, pg108, pg117, pg119, pg125, pg127.

No commit or push was made by this audit.
