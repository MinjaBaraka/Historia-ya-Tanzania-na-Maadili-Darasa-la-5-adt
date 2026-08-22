# PDF-to-ADT QA Audit Log

This log follows `ADT_BOOK_TO_WEBSITE_CONVERSION_GUIDE.md`. The source PDF is authoritative.

| PDF page | HTML file | Components checked | Problems found | Fixes applied | Desktop | Tablet | Phone | Console | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `index.html` | Cover title, class marker, certificate, publisher line, source order, desktop/tablet/phone reflow | The PDF cover title uses two lines; the exported title used one. | Constrained the title measure so it consistently wraps as `Historia ya Tanzania` / `na Maadili`, matching the PDF. | Pass | Pass | Pass | No relevant errors | PASS |
| 17 | `pg017_sec001.html` | Body typography, heading, source text sequence, watermark, page footer, desktop/tablet/phone reflow | Body paragraphs were left-aligned on wide screens although the PDF uses justified text. Enabling justification at phone width produced excessive word spacing. | Added PDF-faithful justification on tablet/desktop and a mobile left-alignment override below 640px. | Pass | Pass | Pass | No relevant errors | PASS |

## Next pages

Audit resumes at PDF page 1 and proceeds in source order. A page is added as PASS only after PDF comparison, live rendering, responsive checks, and relevant interaction checks.
