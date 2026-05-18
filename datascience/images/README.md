# datascience/images

Silly fat-cat ukiyo-e illustrations for the datascience page. Style:
early-19th-century Japanese woodblock print, colourful, textless, all
characters are unmistakably round fat cats (allowed to dress up).

Generated 2026-05-18 via `scripts/generate_image_apim.py`, quality
`high`, orientation `landscape`, format `jpeg`, model `gpt-image-2`,
size 3840x2160.

## Current versions

| Slot                       | File                          | Maps to page section          |
| -------------------------- | ----------------------------- | ----------------------------- |
| `01-speed-race`            | `01-speed-race.v1.jpeg`       | §3 COO — felt vs. measured    |
| `02-peacock-archer`        | `02-peacock-archer.v1.jpeg`   | §4 CEO — confidence ≠ accuracy |
| `03-iceberg-ship`          | `03-iceberg-ship.v1.jpeg`     | §2 CFO — true cost of GenAI   |
| `04-chorus`                | `04-chorus.v3.jpeg`           | "All four in one meeting"     |

`04-chorus.v1.jpeg` and `v2` both rendered the outer cats with blank
uncanny oval voids instead of proper faces. `v3` is a fresh generation
that drops the Noh-mask concept: the four outer cats are now shown from
behind (backs to viewer), revealing only richly patterned kimonos and
thick striped tails, while the central calm cat faces the viewer with a
real cat face. The balance-scale and writing-tablet are clearly visible.

## Versioning rule

Never overwrite. Next generation for a slot creates `.v2.jpeg`, etc.

## Prompts used (v1)

See chat session 2026-05-18. Prompts were tuned through four style
iterations: vase → ink → pixel-art → ukiyo-e fat cats (final).
