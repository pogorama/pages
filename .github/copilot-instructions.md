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

## "Remove X" means delete, not paraphrase (mandatory)

When the user says a phrase is **dumb**, **cringe**, **marketing**,
**condescending**, or **shit**, the failure they are pointing at is
**the existence of that phrase**, not its exact wording. The
correct response is to **delete the element entirely**, not to
write a slightly less embarrassing version of the same thing.

Concrete failure pattern I have actually shipped (do not repeat):

1. The page had a hero figcaption reading
   *"What Microsoft offers a small Greek-Irish society in Dublin — in
   plain English."* The user replied: "how fucking dumb is that
   sentence. remove that shit!"
2. I replaced it with
   *"Microsoft's free offer for the Hellenic Community of Ireland —
   in plain English."* — same shape, same register, same problem.
3. The user, correctly, was furious: "i just told you that that is
   shit you moron! […] do NOT HAVE ANY TEXT THERE!"

### The rule

When asked to remove something dismissive, decorative, or
marketing-flavoured, **delete the element entirely**:

- Delete the `<figcaption>`, not just rewrite it.
- Delete the tagline, byline, eyebrow or strap, not just rewrite it.
- Delete the explanatory subtitle under a hero, not just rewrite it.
- Delete the "About this page" footer paragraph, not just rewrite it.

Only restore the element later if the user asks for content there.
The default for hero images on these pages is **no caption at all**;
the alt text covers screen readers.

### Hero images don't get figcaptions on these pages

A hero image is a mood-setting illustration above an H1. The H1 and
lede already tell the reader what the page is about. A figcaption
under the hero just repeats that or worse, slides into a tagline.
Don't add one. If a figcaption is genuinely needed (e.g. citing a
photographer, naming a chart's source), keep it factual and brief.

## Voice: third person, not first-person plural (mandatory)

Pages in this repo are written **for** a named non-technical
audience (e.g. committee members of the Hellenic Community of
Ireland). They are **not** written **by** that audience. The author
is not part of the society. So **do not write in first-person
plural** ("we", "our", "us", "ours") in visible body text. It is
inaccurate, it is presumptuous, and it slides into committee-minutes
voice.

Concrete failure (do not repeat): the page shipped with phrases
like *"a society like ours needs"*, *"on our own domain"*, *"so we
don't enter every payment by hand"*, *"Training for our people"*,
*"for a society our size"*. The user, correctly, called it out:
*"who told you to write in second person plural you idiot! no one!
write training for community members and students"*.

### The rule

- **Default to third person.** "The society", "the committee",
  "the treasurer", "members", "community members", "students".
- **Second person is fine.** "You" addresses the reader directly
  and is appropriate for instructions and questions.
- **First person singular** ("I recommend …") is allowed for the
  author's voice in clearly opinionated sections.
- **First-person plural is banned** unless the user explicitly tells
  you to use it (e.g. a page that is genuinely a society's own
  voice). The default is OFF.

Common substitutions:

| Wrong                          | Right                                 |
| ------------------------------ | ------------------------------------- |
| our society / a society like ours | the society                        |
| our domain                     | the society's domain                  |
| our members                    | members / community members           |
| our people                     | community members and students        |
| for our size                   | for a society of this size            |
| we don't enter payments        | the treasurer does not enter payments |
| does for us                    | does for the society                  |

### Pre-deploy grep

Before pushing, search visible body text for `\b(we|our|us|ours)\b`.
Any hit must be justified by an explicit user instruction.

## Never patronise the reader (mandatory)

Pages in this repo are written for adults with full intellectual
agency who simply do not happen to be IT specialists. **Do not write
sentences that explain why it's "normal" or "okay" that the reader
doesn't know a thing.** Don't reassure them. Don't soften the
information. Just explain the thing.

Concrete failure (do not repeat): the page shipped with the line
*"If you have not heard of 'Azure' or 'GitHub', that is normal —
most committee members of a society this size have not."* The user,
correctly, called it out: *"yes, condescending you moron! remove the
whole sentence […] no replacement"*.

### The rule

- **Never** assert what the reader does or doesn't already know.
- **Never** frame ignorance of a product as the default for the
  reader's role, profession, age, organisation size, or background.
- **Never** prepend a section with a "don't worry if you don't know
  X" disclaimer. Just define X inline the first time it's used.
- If a product name needs translating into plain language, do it via
  a parenthetical the first time it appears (e.g.
  *"a small server in Microsoft's data centre (Microsoft calls it
  Azure)"*) — and then stop explaining.

### Pre-deploy grep

Before pushing, search visible body text for: `that is normal`,
`don't worry`, `most […] have not`, `if you have not heard`, `if
you don't know what`, `in case you're not`. Any hit must be removed.

## Where the APIM image-generation key lives

The image script (`scripts/generate_image_apim.py`) needs
`PINGPINGAPIM_SUBSCRIPTION_KEY`. It is **not** in this repo and
**not** in user/machine environment scope by default. It lives in
the existing dashboard configuration at:

    C:\Users\phgermey\OneDrive - Microsoft\###AO\Dashboard\ui_mockups\.env

Always invoke the script with `--env-file` pointing at that path:

```
python scripts\generate_image_apim.py `
  --env-file "C:\Users\phgermey\OneDrive - Microsoft\###AO\Dashboard\ui_mockups\.env" `
  --prompt "..." `
  --orientation landscape --output-dir hellenic\images\staging `
  --output-format jpeg --max-attempts 40 --compact
```

Do **not** report image generation as "blocked because the env var
isn't set". The key has been usable in this workstation for the
whole project — the failure mode is forgetting where to find it,
not a missing secret. Look here first.

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
