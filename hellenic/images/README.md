# `hellenic/images/`

Images used by `hellenic/index.html`. **Never overwrite** an existing
image — always generate to a new versioned filename.

## Naming convention

```
<slot>.v<N>.<ext>
```

- `<slot>` — semantic slot on the page: `hero`, `skilling`, …
- `<N>` — version number, starting at `1`. A new generation for the
  same slot increments to the next integer.
- `<ext>` — `jpg` (preferred for photographs of clay), `png` for
  diagrams with hard edges.

When a file currently has no version suffix (legacy), the next
generation creates `<slot>.v2.<ext>` and the legacy file is treated as
`v1`.

## Current images

| Slot     | Live file            | Date generated | Used as     |
|----------|----------------------|----------------|-------------|
| hero     | `hero.v2.jpg`        | 2026-05-12     | masthead — female teacher with children, alphabet tablet, cloud + Windows logo motifs |
| reader   | `reader.v1.jpg`      | 2026-05-11     | Reading Rule details body — philosopher reading from a tablet (renamed from `hero.v1.jpg`) |
| skilling | `skilling.v1.jpg`    | 2026-05-12     | Next Steps · parallel skilling band |

## Workflow

```powershell
# from repo root — generate the next version into the same folder
python scripts/generate_image_apim.py `
  --env-file "<...>" `
  --output-dir hellenic/images `
  --orientation landscape `
  --output-format jpeg `
  --quality high `
  --max-attempts 20 `
  --prompt "<vase-style description>"

# rename the just-generated timestamped file to the next version
Rename-Item hellenic/images/<auto-named>.jpg  hellenic/images/hero.v2.jpg

# update the <img src> in hellenic/index.html and this README's table
```

Keep prior versions on disk so we can roll back without regenerating.
