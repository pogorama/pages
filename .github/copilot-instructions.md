# Copilot instructions for `pogorama_pages`

This repo holds personal, HTML-first websites built to one style guide.
Read this before touching any page — especially when you are about to
"design" or "redesign" something.

## Where rules live

**All persistent rules live in this repo, in plain markdown, in the
docs you can read here.** When the user gives a new rule, preference
or convention, you write it into the relevant file — this file, the
manifesto, `design_qna.md`, or a folder-level `README.md`. You do
**not** put it into any external "memory" tool, "store_memory" call,
or other hidden side-channel. Rules must be visible in the repo,
version-controlled, reviewable in a PR, and readable on a phone.

If the user tells you something is a rule, add it here (or the right
doc) in the same response. Cite the user's wording in the commit
message.

## Never leak internal docs into a public page (mandatory)

The files in `docs/` (`web-design-manifesto.md`, `design_qna.md`,
`azure-apim-image-generation.md`), this `copilot-instructions.md`,
and any `README.md` outside the rendered HTML tree are **private
working notes**. The user has not chosen to publish them. They are
not a manifesto for the world; they are scaffolding for me.

A page deployed to GitHub Pages must contain **zero** of the
following in visible HTML (`<body>`, `<title>`, `<meta description>`,
`alt` text, link text, footer):

- The word **manifesto**, **Q&A**, **design rationale**, or any phrase
  that frames the page as a portfolio piece or a design exercise.
- Links to anything under `docs/`, `.github/`, or any sibling
  `*.md` file in the repo.
- Q-numbers (Q1, Q15, Q56 …) or "Manifesto Ch N" references.
- "Design follows the project's own X" / "Built as a single HTML
  file" / "uses inlined CSS" / any meta-commentary on how the page
  was authored.
- Crediting tools, styles or frameworks unless the reader needs them.

These are fine to keep inside **HTML comments** (`<!-- -->`) or
inside `<style>` comments, because those don't render. The test is:
"would a reader who knows nothing about this repo ever see this
phrase?" If yes, it must go.

### Why this matters

1. **Privacy.** The internal docs are personal working notes. The
   user has not chosen to publish them. Linking to them on a live
   site publishes them by inclusion — and they end up in search
   engines, the Wayback Machine and link previews forever.
2. **Audience violation.** Every public page in this repo has a
   named non-technical reader (e.g. Hellenic Community committee
   members). Their job-to-be-done has nothing to do with how the
   page was designed. Meta-commentary in the footer is noise that
   signals "this is a portfolio piece, not a tool for you."
3. **No marketing voice.** Pages are written explicitly to avoid
   marketing language. "Design follows our manifesto" *is*
   marketing voice. Don't.
4. **Brittle anchors.** Internal docs get renamed and refactored.
   A live link to `../docs/web-design-manifesto.md` will silently
   404 the moment that file is reorganised.
5. **Attack surface.** Internal docs may contain unpolished drafts,
   critiques of third parties, half-formed opinions, or notes about
   security, money or people that should not be one click away from
   a member of the public.

### Pre-deploy checklist (run before every `git push` of a Pages site)

In the deployed page, search for: `manifesto`, `design_qna`,
`docs/`, `Q\d+`, `Ch \d+`, `inlined CSS`, `single HTML file`,
`design rationale`, `portfolio`. **Any hit in visible content is a
bug to fix before push.**

## What this repo is

- `docs/web-design-manifesto.md` — the **what**: ten chapters, fifty rules,
  HTML-first, single column, calm type, one accent, generous space.
- `docs/design_qna.md` — the **how**: 66 questions on information design,
  each with three options and a recommended default.
- `docs/azure-apim-image-generation.md` — how the
  `scripts/generate_image_apim.py` script talks to the Azure APIM gateway
  to generate or edit images.
- `hellenic/` — first applied project: a plain-English guide to Microsoft
  for Nonprofits, written for a small Greek-Irish community society.

## Mandatory pre-flight, before writing any HTML

Run this in your head — or out loud in the chat — **before** you start
designing or rewriting a page. These four questions match Q1, Q2, Q15
and Q56 of the Q&A. They are not optional.

1. **Who is going to read this page?** Write the named reader in your
   notes. _("A volunteer treasurer of a 40-person society in Dublin, no
   IT background.")_ — Q1.
2. **What is their job-to-be-done?** One sentence: _"Someone like {A}
   visits this page to {B} so they can {C}."_ — Q2.
3. **What does the reader already know?** List every proper noun and
   acronym you plan to use (Azure, GitHub, Copilot, RPA, SSO, Dataverse
   …). For each, decide: do they already know it, or must you define it
   inline the first time it appears? — Q56.
4. **What does the reader need in the first 200 words?** The page's
   apex is not the TL;DR; it is the one-paragraph plain-English answer
   to _"what is this and why should I care?"_. The TL;DR comes after. —
   Q15, Q16.

If any of those four answers is "I'm not sure" — **stop and ask the
user.** Don't guess.

## Failure modes I have already shipped (do not repeat)

- **Comparison-table-before-definition.** Writing _"Microsoft 365 / Azure
  / Power Automate / GitHub Copilot — here is the free tier of each"_
  for an audience that doesn't know what Azure or GitHub Copilot _are_.
  The fix: a plain-English Section 0 first — _"Microsoft gives nonprofits
  three things: software, cloud infrastructure, and skilling. Here is
  what each means for a small society like yours."_ Concrete outcomes
  before product names.
- **Jargon left undefined.** Every proper noun on first use gets a
  short inline definition. _"Azure — Microsoft's rented data-centre
  service for hosting websites, sending email at scale, and running
  small databases."_ Not _"Azure"_ on its own.
- **Designing for a procurement-savvy reader by accident.** When the
  named reader has _no_ background, every layer of the page has to be
  legible on its own. Inverted pyramid still applies, but the apex is
  _what is this even?_ — not _which tier is cheapest?_.

## Style and code conventions

- One HTML file per page. Inlined `<style>`. No build step. (Manifesto
  Ch. 8 + Q&A Q7.)
- Tokenised colour and spacing in `:root`. Dark mode via
  `prefers-color-scheme`. (Manifesto Ch. 6, Ch. 7; Q&A Q61.)
- Three or four neutrals, one accent, one warning. (Manifesto Ch. 6;
  Q&A Q50.) The Hellenic project uses paper-warm bg `#fafaf7`, accent
  blue `#0b5cab`, warning rust `#a0521d`, plus a passe-partout mat
  `#efe6d4` for figures.
- Serif body, sans headings, single column, ~70 ch measure.
- Native HTML elements first: `<details>`, `<dialog>`, `<table>`,
  `<figure>`, `<aside>`. ARIA only where the native semantics fall
  short.
- Print stylesheet required (Q&A Q63).
- Inline SVG icons; no icon fonts.
- Never load JS to do a layout job a CSS feature can do
  (`@container`, `:has()`, grid, flex).

## How to use the image-generation script

```powershell
python scripts/generate_image_apim.py `
  --env-file "<path to .env with PINGPINGAPIM_SUBSCRIPTION_KEY>" `
  --output-dir <folder> `
  --orientation landscape `
  --output-format jpeg `
  --quality low `
  --max-attempts 8 `
  --prompt "<vase-style description>"
```

- Tier-1 rate limits: **9 RPM** on `gpt-image-2` GlobalStandard.
  The script auto-retries through `EngineOverloaded` 429s with
  exponential backoff (cap 90 s) up to `--max-attempts` (default 6).
- Image style for the Hellenic project: black-figure Attic vase
  painting on warm cream ground, fine ochre-red line details, Greek
  meander frieze along the edges. **Never** include text, faces, or
  logos in prompts (gpt-image-2 renders them badly).
- Figures on the page wear a passe-partout mat
  (`figure { background: var(--mat); border: 1px solid var(--mat-edge) }`)
  so cream-on-paper-warm mismatches read as deliberate.

### Versioning rule for images (mandatory)

**Never overwrite an existing image file.** Images are slow and
expensive to produce, and a newer one is not automatically better than
the prior one. Always version.

- Filenames: `<slot>.v<N>.<ext>` — e.g. `hero.v1.jpg`, `hero.v2.jpg`.
  If a file currently has no version suffix (legacy), the next
  generation creates `hero.v2.jpg` and the legacy file becomes `v1`.
- Generate into the same folder as the live image. Do **not** create
  parallel `images_new/` or `tmp/` folders that you then merge.
- After generation, update the `<img src=...>` in HTML to point to the
  new versioned filename.
- Keep prior versions on disk so we can roll back without re-generating.
- Each image folder contains a short `README.md` listing the current
  version, the date generated, and the prompt used (see
  `hellenic/images/README.md` for the format).

## When in doubt

Re-read this file, then Q1, Q2, Q15, Q56 of `docs/design_qna.md` —
in that order.
