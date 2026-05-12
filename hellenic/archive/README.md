# `hellenic/archive/`

Old versions of `hellenic/index.html`, kept for reference only.

## Naming convention

```
index.vN.YYYY-MM-DD.html
```

- `vN` — the version number being archived (the version of the file
  *before* the change that supersedes it).
- `YYYY-MM-DD` — the date the file was archived (the date the new
  version replaced it on `main`).
- ISO date format means the directory sorts oldest-first by name.

## What every archived file gets

Before moving a file in here, add these signals so the archive is
unambiguous even when accessed via a direct URL:

1. A top-of-file HTML comment with version, date, reason, and a link
   back to the current page.
2. `<meta name="robots" content="noindex,nofollow">` in `<head>`.
3. `<link rel="canonical" href="../index.html">` in `<head>` so search
   engines that do crawl it understand which page is canonical.
4. A `[Archived vN · YYYY-MM-DD]` prefix in `<title>`.
5. A visible banner at the very top of `<body>` saying the page is
   archived, with a link to the current version.

## Workflow

```powershell
# from repo root
git mv hellenic/index.html  hellenic/archive/index.v1.2026-05-12.html
git mv hellenic/index_v2.html hellenic/index.html
# then edit the archived file to add the 5 signals above.
```

## Current archive

| File                              | Archived   | Reason |
|-----------------------------------|------------|--------|
| `index.v1.2026-05-12.html`        | 2026-05-12 | Superseded by v2 redesign: plain-English Section 0, collapsed Details group, earthy terracotta/oxblood palette, vase-style imagery, Next Steps flow. |
