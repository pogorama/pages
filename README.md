# pogorama/pages

Static GitHub Pages site.

## Structure

- `/` — intentionally blank landing page.
- `/hellenic/` — Microsoft offers summary for eligible nonprofits (Hellenic context).

## Local preview

Open `index.html` or `hellenic/index.html` directly in a browser, or serve the
folder with any static file server (e.g. `python -m http.server`).

## Deployment

GitHub Pages is expected to serve this repository from the `main` branch root.
The `.nojekyll` file disables Jekyll processing so paths are preserved as-is.
