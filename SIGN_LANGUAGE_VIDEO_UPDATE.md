# Sign-language video update — 13 September 2026

Seven supplied videos were compressed with High2Min 0.11.9. Both covers were added and five existing reader-page clips were replaced. Reader numbering includes the front cover as page 1; it is not the printed page number.

| Reader position | Website page | Published video | Size (MiB) |
|---:|---|---|---:|
| 1 | `index.html` | `page_1.mp4` | 0.50 |
| 6 | `pg005_sec001.html` | `page_6.mp4` | 3.55 |
| 75 | `pg074_sec001.html` | `page_75.mp4` | 4.80 |
| 92 | `pg091_sec001.html` | `page_92.mp4` | 4.73 |
| 95 | `pg094_sec001.html` | `page_95.mp4` | 4.41 |
| 127 | `pg126_sec001.html` | `page_127.mp4` | 4.40 |
| 130 | `back-cover.html` | `page_130.mp4` | 0.40 |

Total size: **869,097,573 → 23,892,519 bytes**, a **97.25% reduction**. Every output is H.264 MP4, silent, below 5 MiB, and retains its source frame rate. High2Min measured SSIM between 0.969734 and 0.980371 at the delivered resolution. Longer clips were proportionately downscaled to meet the size limit.

## Video background and sound

The seven videos retain their original green background. All audio tracks, including background noise, were removed by High2Min. The native video controls, close button, and dragging remain available. No visual background-removal adapter is included.

## Preserved material

All 130 reader pages now have a valid video mapping. The other 123 pages retain their original video content, verified by SHA-256. Six legacy clips were renamed to `legacy_...mp4` and their original mappings updated to avoid collisions with the newly published filenames. The five replaced clips remain recoverable from earlier GitHub commits. Source videos on the external drive were untouched.

High2Min synchronized the offline data and all 130 embedded page snapshots, advanced the bundle version to 6, repaired missing manifest entries, and installed its media-independence and draggable-player helpers. Compiled runtime bundles, inside-page text, existing narration files, and reading order are unchanged.

## Cover read-aloud

Both covers now have five narration passages connected to the standard TTS player through stable `data-id`, text, and audio mappings. Existing recordings provide the title, subtitle, grade, publisher, and ISBN. Three new MP3s use the book’s `sw-TZ-RehemaNeural` voice for the back-cover heading, list of books, and shared government ownership notice. The transcripts are accessible to screen readers without changing the cover artwork. All required audio files are declared in the manifest, and offline data is synchronized.

Chrome verified all ten passages, both covers on a 320-pixel viewport, pause and resume, narration alongside the silent green-screen sign videos, and direct-file offline playback. The sign player uses its native layer so it cannot cover the TTS toolbar.

## Verification

- All seven compressed outputs passed High2Min media, size, and quality checks.
- All 130 mappings resolve with exact filename case; seven published files match their compressed copies.
- The seven clips retain their green background and have zero audio streams. Visual background removal has been removed from all live and embedded offline pages.
- Narration and sign video play independently in both playback orders.
- Video mappings and compression remain unchanged after restoring the original green background.
- High2Min website validation passed; offline JSON and embedded HTML exactly match their files.

The repository contains the finished reader assets. Compression work files, virtual environments, previews, temporary files, and local Git data are excluded from the published website.
