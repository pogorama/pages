# design_qna.md

**Information‑structure questions for the manifesto‑style site.**

This file complements [`web-design-manifesto.md`](./web-design-manifesto.md).
The manifesto says _what_ to build. This file argues _how_ to organise the
words inside it.

Every question follows the same shape:

> **Framing** — what's actually being decided.
> **A / B / C** — three honest options with their consequences.
> **Recommended** — the default for most pages on this site.
> **Why** — the research or principle behind it.

The current personal default is **one HTML file per page, inlined CSS, no
build step.** Questions are written from that bias. Where the bias changes
the answer, it's called out. **LLMS** — _Lots of Little htMl pageS_, Jim
Nielsen's acronym — is the long‑term destination, see Q7.

66 questions, in 15 parts:

- **I. Before you write: content analysis** — Q1–Q6
- **II. Macro architecture** — Q7–Q14
- **III. Order, arc, openings, endings** — Q15–Q20
- **IV. Section design** — Q21–Q24
- **V. Paragraphs and sentences** — Q25–Q27
- **VI. Headings & hierarchy** — Q28–Q31
- **VII. Skim layer: bullets, lists, tables** — Q32–Q38
- **VIII. Voice and narration** — Q39–Q43
- **IX. Density, length, cuts** — Q44–Q47
- **X. Emphasis, callouts, pull quotes** — Q48–Q50
- **XI. Cross‑references, anchors, ToC, reading‑time** — Q51–Q54
- **XII. Footnotes, definitions, asides, attribution** — Q55–Q58
- **XIII. Layout: figures, code, dark mode** — Q59–Q61
- **XIV. Reader workflows: CTA, print, Ctrl‑F** — Q62–Q64
- **XV. Decision hygiene** — Q65–Q66

A short **Retrospective: failure modes I have already shipped** sits at
the very end of this file. Read it. Each entry is a real mistake from a
real page in this repo, with the question it violated and the fix.

> **If you read nothing else, read Q1, Q2, Q15 and Q56.** Those four
> questions answer _who_ the page is for, _what_ they're trying to do,
> _what_ the page must say in the first 200 words, and _which_ words to
> define inline before using them. Almost every editorial failure on the
> open web is one of those four skipped.

---

## Part I — Before you write: content analysis

## Q1 — Who is this page for?

**Framing.** Every later structural choice descends from a single sentence:
who is going to read this, and what do they want from the time they spend
here?

- **A. One specific reader, named in your notes.** Write as if to that one
  person; you can imagine their face. Most personal essays.
- **B. A primary audience + a secondary audience, in that priority.**
  Optimise for the primary; let the structure serve the secondary (layered
  information). Most product/landing/docs pages.
- **C. "Everyone."** Generic, audience‑less prose.

**Recommended:** **A** for essays and opinion. **B** for product, docs and
landing pages. Never **C**.

**Why.** Krug, _Don't Make Me Think_ (3rd ed., 2014): "writing for everyone
is writing for no one." Schriver, _Dynamics in Document Design_ (1997),
shows reader‑specific drafts outperform generic ones on every comprehension
measure. The named‑reader trick is a discipline, not a literary device —
it's for the author.

> **Failure mode I have shipped.** Designing for the audience I _imagine_
> (a procurement-savvy IT manager) instead of the audience that actually
> exists (a volunteer treasurer with no IT background). The named-reader
> sentence prevents this only if it is honest. See **Retrospective** at
> the end of this file.

---

## Q2 — What is the reader's job‑to‑be‑done?

**Framing.** Before drafting, write one sentence: _"Someone like {A} visits
this page to {B} so they can {C}."_ That sentence stays in your notes; it
is the brief against which every later edit is judged.

- **A. Write the JTBD sentence explicitly.** One line in your notes,
  deleted before publishing.
- **B. Hold it implicitly.** You "know" the job; you don't write it down.
- **C. Skip; the structure will reveal itself.**

**Recommended:** **A**, always. The sentence costs nothing and prevents the
single biggest editorial failure mode: writing what's easy instead of what's
useful.

**Why.** Christensen & Moesta, _Jobs to Be Done_ (HBR, 2016), applied to
content. The same idea sits under Krug's "trunk test" — could a stranger
answer "what am I supposed to do here?" within 5 seconds.

---

## Q3 — What if the page serves two audiences (e.g. dev + manager)?

**Framing.** Two audiences with different vocabularies, different time
budgets, and different definitions of "the answer." The page either layers
them or splits them.

- **A. One sequenced page, layered.** Lead with the manager‑level summary;
  let the dev keep reading and find the detail below. Same URL.
- **B. Two parallel sections at the top of the page.** Signposted
  ("For product managers" / "For engineers"). The reader self‑selects.
- **C. Two separate pages, linked from a landing.** Different URLs.

**Recommended:** **A** for ≤2 audiences whose interests are nested (the dev
also wants the summary). **C** when the audiences want different things or
share little vocabulary. Avoid **B** — explicit self‑selection signposts
look amateurish and the second audience always feels like an afterthought.

**Why.** NN/g, [_"Layered Presentation Reduces Cognitive Load"_](https://www.nngroup.com/articles/layered-presentation/)
(Loranger, 2014). Inverted pyramid + progressive disclosure. Schriver's
reader‑centred design.

---

## Q4 — Outline first, or free‑write first?

**Framing.** Two writing processes with different failure modes.
Outline‑first fails by being lifeless. Free‑write‑first fails by never
converging.

- **A. Outline first; then write to the outline.** Best when the structure
  is the value (reference, docs, how‑to).
- **B. Free‑write first; extract the outline from the draft.** Best when
  the argument is the value (essay, opinion, manifesto).
- **C. Parallel: a rough outline and a rough draft growing together.** Best
  for collaborative work and longer pieces where you cycle through both.

**Recommended:** **B** for any opinion piece. **A** for reference. **C**
when you've been at the topic long enough to know your blind spots.

**Why.** Peter Elbow, _Writing Without Teachers_ (1973): "meaning is not
what you start out with but what you end up with." Anne Lamott,
_Bird by Bird_ (1994), on "shitty first drafts." Pinker, _The Sense of
Style_ (2014). The trap is doing **A** for an essay — the outline freezes
the conclusion before you've thought.

---

## Q5 — How aggressively should the second pass cut?

**Framing.** The second draft is where structure earns its keep. The
question is how brutal to be.

- **A. ≤ 10% — copy edits and typos.** You're polishing.
- **B. 20–30% — line edits plus the weakest paragraph of each section.**
  Realistic.
- **C. 50%+ — Zinsser's standard.** "Half of what you wrote was filler."

**Recommended:** Aim for **C**, land at **B**. The 50% target sets the
right attitude; the 25% reality is what survives contact with the page.

**Why.** William Zinsser, _On Writing Well_ (7th ed., 2006): "the second
draft is the first draft minus 50 percent." Strunk & White, _The Elements
of Style_ (4th ed., 2000): "omit needless words." Stephen King, _On
Writing_ (2000): "kill your darlings."

---

## Q6 — How do you test that the structure works?

**Framing.** Three tests, increasing in cost and signal. Most authors skip
all three.

- **A. Read it aloud.** Catches rhythm, sentence length, awkward
  transitions. Costs 10 minutes.
- **B. Skim test.** Cover the prose; ask whether headings + first lines
  carry the argument. Tests scan‑readability.
- **C. Hand it to one reader and ask "what did you take away?"** Highest
  signal; reveals what the reader actually constructs in their head.

**Recommended:** Do all three. Minimum is **B** plus **C**. **A** is free;
**B** is cheap; **C** is the only way to discover what you assumed.

**Why.** Nielsen, [_"Why You Only Need to Test with 5 Users"_](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)
(2000). Journalism skim‑test tradition. Reading aloud catches what the
silent eye glides over (Hayes & Flower writing‑process model, 1981).

---

## Part II — Macro architecture

## Q7 — One single‑file page, lots of little HTML pages, or a JS SPA?

**Framing.** The most fundamental information‑architecture decision. Every
later question depends on it.

- **A. One single‑file page that holds everything.** A single `index.html`
  with inlined CSS. No build, no router. Anchor links (`#section-id`) for
  deep links. Zero‑build, instant load, archivable.
- **B. LLMS — lots of little HTML pages, navigated by links.** Each topic
  gets its own URL; transitions animated by CSS view‑transitions. Per‑topic
  caching, URL‑addressable, scalable.
- **C. A JS SPA pretending to be many pages.** Don't. Discarded.

**Recommended:** **A for now, B as the destination.** **B is the right
answer on the open web** — Jim Nielsen's _"lots of little HTML pages"_
pattern (LLMS) is overwhelmingly correct: each page is a real URL,
individually cacheable, shareable, archivable, indexable, fast, and
survives the next twenty years of browser changes. The reason this site
defaults to **A** today is that I don't yet have a clean way to author many
small files without copy‑paste drift across shared headers, footers, navs
and styles. Until that authoring pipeline exists, one file beats five
copy‑pasted ones. Promote to **B** when _either_ the page would scroll past
~3 screen heights of unrelated content _or_ the authoring pipeline is in
place. Never **C**.

**Why.** Jim Nielsen, [_"Building Websites With LLMS (Lots of Little HTML
Pages)"_](https://blog.jim-nielsen.com/2025/lots-of-little-html-pages/)
(2025). NN/g, _"How Little Do Users Read?"_ (2008): average visit reads ≤
20 % of the page — short single pages and small per‑topic pages both
honour this; long single pages punish it. HTTP Archive _Web Almanac_
(2024): median desktop page weight 2.7 MB — zero‑build HTML pages
routinely score 100 on Lighthouse.

---

## Q8 — Should URLs encode hierarchy?

**Framing.** A URL is a bookmark first and an information‑architecture
artefact second.

- **A. Flat slug.** `/post-title/`. No category, no date.
- **B. Hierarchical.** `/category/post-title/`. Encodes the section the
  post lives in.
- **C. Dated.** `/2026/05/post-title/`. Locks the post into when it was
  written.

**Recommended:** **A**. Categories change; dates date; flat slugs survive.
Use tags inside the page, not in the URL.

**Why.** Tim Berners‑Lee, [_"Cool URIs Don't Change"_](https://www.w3.org/Provider/Style/URI)
(1998). Jim Nielsen's site is flat. Most static‑site reorganisations in
2010–2020 broke because their URLs encoded a hierarchy that later moved.

---

## Q9 — A multi‑part topic: one big page or a series?

**Framing.** Long content can live as one big page with internal anchors
or as a series of linked smaller pages.

- **A. One big page with a ToC.** Single bookmark, single Ctrl‑F, easy to
  print.
- **B. A series with a shared landing page and prev/next links.** Each
  part cacheable, each part shareable.
- **C. A series with no landing page — just cross‑links.** Lightweight,
  but readers struggle to see the shape.

**Recommended:** **A** for reference content the reader will dip into.
**B** for content meant to be read in sequence (a tutorial, a thesis).
Never **C** unless the parts genuinely stand alone.

**Why.** Andy Bell, [_buildexcellentwebsit.es_](https://buildexcellentwebsit.es/),
is itself a series with a landing page. NN/g, _"Pagination, Galleries, and
Continuous Scrolling"_ (Schade, 2016). Reader‑orientation research.

---

## Q10 — When do you splice a long single‑file page into multiple pages?

**Framing.** The editorial counterpart to Q7. Splitting is irreversible in
practice — once a URL exists it must keep working.

- **A. When the page passes ~3,000 words or ~7 top‑level sections.**
  Length trigger.
- **B. When two distinct audiences would land on different parts of the
  page.** Audience trigger.
- **C. When a section becomes worth bookmarking on its own.** Bookmark
  trigger.

**Recommended:** Apply **all three** as triggers. If any is true, promote
the section to its own page (`/topic-name/`) and leave a one‑paragraph
stub plus a link on the original so existing anchors still resolve.

**Why.** Jim Nielsen's LLMS pattern. Donna Spencer, _A Practical Guide to
Information Architecture_ (2nd ed., 2014): card‑sort affinity rule. The
bookmark test is the cleanest of the three — if a reader would tell a
friend "go read that bit of that page," the bit deserves a URL.

---

## Q11 — How many top‑level sections should a single page have?

**Framing.** Working‑memory limits set the upper bound; section pacing
sets the lower.

- **A. 3–5.** Reads as an essay; each section 300–800 words.
- **B. 6–10.** Reads as a chapter; needs a ToC and anchor links.
- **C. 11+.** Reference document.

**Recommended:** **A** by default. **B** when the topic is genuinely
chaptered (this Q&A is **B** because it _is_ a reference doc and declares
itself as such). Past 10, flip to multiple pages (Q10).

**Why.** Miller, _"The Magical Number Seven, Plus or Minus Two"_
(_Psychological Review_, 1956). Cowan, _"The Magical Number 4 in
Short‑Term Memory"_ (_Behavioral and Brain Sciences_, 2001). NN/g, _"Long
vs. Short Articles"_ (Loranger, 2017).

---

## Q12 — Should every page have visible metadata (date, byline, revisions)?

**Framing.** Three small pieces of front matter. Each carries a different
trust signal.

- **A. Date only.** Published date near the title.
- **B. Date + byline + last‑updated marker.** Authorship and currency both
  visible.
- **C. Date + byline + full revision log.** Wikipedia‑style transparency.

**Recommended:** **B**. Date and "Last updated 2026‑05‑12" near the title,
byline at the top, no full changelog unless the page is a specification.

**Why.** Stanford Web Credibility Project (Fogg et al., 2002): visible
authorship and currency are the two strongest non‑design credibility cues.
Journalism standard. Stripe API docs use the same pattern.

---

## Q13 — Tags / categories / related links on each page?

**Framing.** Three navigation aids of decreasing value‑per‑pixel.

- **A. None.** Trust the page to stand alone.
- **B. 1–3 hand‑picked tags + 3–5 hand‑picked related links at the
  bottom.** Curated, light, useful.
- **C. Many auto‑generated tags driving an auto‑generated related list.**
  Algorithmic; drifts into noise.

**Recommended:** **B**. Tags help wayfinding when picked sparingly;
related links work when picked by a human who read both pieces.
Auto‑related is almost always spam.

**Why.** Spencer, _A Practical Guide to Information Architecture_ (2014):
"tag soup" problem. Peter Morville, _Ambient Findability_ (2005): tags
multiply faster than meaning. NN/g, _"Related Content That's Worth
Reading"_ (Whitenton, 2018).

---

## Q14 — `<title>` and the page's `<h1>` — same or different?

**Framing.** Two strings that look the same but do different jobs.

- **A. Identical.** Simplest.
- **B. `<title>` includes site name; h1 is just the topic.** "Q&A on IA —
  pogorama" in title; "Q&A on information architecture" in h1.
- **C. Completely different.** Marketing in title, plainer h1.

**Recommended:** **B**. The title is for the browser tab, the bookmark bar
and the search‑results listing; the h1 is for the reading view.

**Why.** Moz, _Title Tag SEO Guide_; Ahrefs research. WCAG 2.4.2 _Page
Titled_. The two strings serve different surfaces; making them identical
means one of them is wrong for its job.

---

## Part III — Order, arc, openings, endings

## Q15 — Inverted pyramid, narrative arc, or chronological?

**Framing.** What order do you present ideas in?

- **A. Inverted pyramid.** Conclusion first, then key facts, then context,
  then optional detail. The journalism standard since the 1880s.
- **B. Narrative arc.** Setup → tension → resolution. Engaging if the
  reader stays; bad if they leave at paragraph 2.
- **C. Chronological.** "Here's how I did it, step by step." Necessary
  when sequence is the content.

**Recommended:** **A** for informational pages, dashboards, docs, product
pages, landing pages, and any reference. **B** for personal essays where
_why_ matters more than _what_. **C** only when the reader is going to
follow along (cookbook, tutorial, runbook).

**Why.** NN/g, [_"Inverted Pyramid: Writing for Comprehension"_](https://www.nngroup.com/articles/inverted-pyramid/)
(Moran, 2017): 124 % gain in task success when key information was
front‑loaded. F‑pattern research (Pernice & Nielsen, 2006, reaffirmed
2017): eye‑tracking is biased to the top‑left first two paragraphs.
Front‑load.

---

## Q16 — Where does the TL;DR / summary go?

**Framing.** Three placements, three trade‑offs.

- **A. First paragraph of the page, before any heading.** Maximum reach.
- **B. A dedicated "Summary" section near the top, after the h1.**
  Discoverable, copyable; one scroll away.
- **C. At the bottom as a recap.** Helps finishers; useless to scanners.

**Recommended:** **A** for pages with a clear thesis. Supplement with **B**
when the page is long enough to deserve a named anchor (`#summary`). Never
rely on **C** alone.

**Why.** NN/g, _"Why Web Users Scan Instead of Reading"_ (Liu, 2014). The
first paragraph carries disproportionate weight in deciding whether the
visitor stays. The inverted pyramid again.

---

## Q17 — How do you open a page?

**Framing.** The first sentence does more work than any other sentence on
the page.

- **A. Thesis.** State the page's claim in one sentence.
- **B. Scene.** A single concrete image, example or anecdote.
- **C. Question.** Pose the question the page will answer.

**Recommended:** **A** for reference, manifesto and decision pages. **B**
for essays, where the scene earns the reader's attention. **C** for
landing pages, tutorials, and Q&A pages (this one).

**Why.** Classical rhetoric: the _exordium_. Journalism's "lede"
tradition. Heath brothers, _Made to Stick_ (2007): concrete openings
outperform abstract ones on retention by ~2×.

---

## Q18 — How do you end a page?

**Framing.** Endings either restate, redirect, or stop. Each has a place.

- **A. A short conclusion that restates the thesis.** Closure for long
  pieces.
- **B. A call to action or a question to the reader.** Redirect — keeps
  energy moving.
- **C. Just stop. The last section is the conclusion.** No formal close.

**Recommended:** **C** for essays and reference. **B** for landing and
marketing pages. **A** only when the page is long enough that the reader
genuinely needs a recap (rare under 3,000 words).

**Why.** Classical rhetoric: the _peroratio_. Krug, _Don't Make Me Think_:
closure cues; redundant restatement reads as padding on short web pieces.
Hemingway omitted endings on principle — the reader's mind finishes the
sentence.

---

## Q19 — How do you transition between sections?

**Framing.** Bridges between sections can be silent, explicit, or
prospective.

- **A. No transition — the next heading is the transition.** Standard for
  manifesto‑style pages.
- **B. A one‑sentence bridge at the start of each new section.** Standard
  for narrative essays.
- **C. A bridge at the end of each section pointing forward to the next.**
  Standard for tutorials.

**Recommended:** **A** on this site. **B** for narrative essays. **C**
only in tutorials where sequence matters.

**Why.** Pinker, _The Sense of Style_ (2014): "show, don't tell" applied
to structure. Bridges that say "now we'll look at X" are meta‑noise.
Headings on the web do the job that bridges did in print.

---

## Q20 — Should you repeat the key idea?

**Framing.** "Tell them, tell them, tell them you told them" vs. "say it
once and trust the reader."

- **A. Say it once.** Trust the reader.
- **B. Twice — in the lead and in the conclusion.** Bookend.
- **C. Three times — Aristotelian repetition.** Tell, show, recap.

**Recommended:** **B** by default. **C** for long pages where retention
matters. **A** only when the entire page is the idea (a one‑page manifesto
chapter).

**Why.** Ebbinghaus's forgetting curve (1885). Spaced‑repetition learning
research. Modern UX writing guides (Mailchimp, Stripe). The Aristotelian
rule of three survives in marketing copy because it works on attention,
not on intellect.

---

## Part IV — Section design

## Q21 — How do you separate sections visually?

**Framing.** Three weights of separator, each with a cost.

- **A. Generous whitespace + a heading.** Nothing else.
- **B. Whitespace + a heading + an `<hr>` rule.** Slightly more emphatic
  break, useful between truly different topics.
- **C. A coloured background band or card.** Maximum visual break;
  introduces chrome.

**Recommended:** **A** in 90 % of cases. **B** between top‑level chapters
in long pages. **C** never on a manifesto‑style reading page; reserve it
for landing pages where each band is a different _kind_ of content (hero,
CTA, testimonial).

**Why.** Tufte, _The Visual Display of Quantitative Information_ (2nd
ed., 2001): the data‑ink principle applied to whitespace — every
non‑content element must justify itself. Whitespace alone, sized to a real
scale, reads as intent. Coloured bands almost always reduce reading
comfort by breaking the column rhythm.

---

## Q22 — How long should one section be?

**Framing.** Sections too short feel hectic; too long feel like walls.

- **A. Tight — one screen‑height max (~150 words on mobile).**
  Landing‑page rhythm.
- **B. Medium — 300–800 words.** Essay rhythm.
- **C. As long as the idea demands.** Chapter rhythm.

**Recommended:** **B** for body sections on essay/reference pages. **A**
for landing pages. **C** only when "the idea" really is a chapter — rare
on a single‑file page.

**Why.** Pernice / NN/g scan patterns. Bringhurst, _The Elements of
Typographic Style_ (4th ed., 2012), on section pacing. Sweller's cognitive
load theory (1988): chunks of 300–800 words match working‑memory limits for
a single concept.

---

## Q23 — One idea per section, or a cluster of related ideas?

**Framing.** Atomicity is a quality measure for information architecture.

- **A. Strictly one idea per section.** Reference standard.
- **B. One idea per section + ≤ 2 closely related tangents.** Essay
  standard.
- **C. A cluster of related ideas under one heading.** Only with explicit
  sub‑headings.

**Recommended:** **A** for reference and decision pages (this Q&A). **B**
for essays. **C** only when you can give each idea its own h3.

**Why.** Miller / Cowan working‑memory limits. Spencer, _A Practical
Guide to Information Architecture_: affinity grouping. Sweller: chunking
reduces cognitive load only when chunks are coherent.

---

## Q24 — Where does a section actually end?

**Framing.** Knowing where to cut is the hardest part of structuring.

- **A. By topic.** The next idea isn't a sub‑topic of this one.
- **B. By rhythm.** The reader needs a breath; the section has gone long.
- **C. By length.** Every ~500 words, regardless.

**Recommended:** **A** as primary criterion. **B** as a tiebreaker on long
sections. Never **C** — length‑based breaks read as arbitrary and break
the reader's argument map.

**Why.** Editorial practice (Bringhurst, Zinsser). Mandler & Johnson,
_"Remembrance of Things Parsed"_ (_Cognitive Psychology_, 1977):
boundaries that match the conceptual structure improve recall; arbitrary
boundaries make recall worse than no boundaries at all.

---

## Part V — Paragraphs and sentences

## Q25 — How long should a paragraph be?

**Framing.** Paragraph length is a rhythm decision and a comprehension
decision at once.

- **A. 1–2 sentences.** Web‑native; high scannability.
- **B. 3–5 sentences.** Essay standard.
- **C. Whatever the idea demands.** Academic standard.

**Recommended:** **B** for this site's prose. **A** for marketing/landing
copy. **C** only when you're explicitly writing long‑form.

**Why.** Hayes & Flower writing‑process model (1981). Pinker on cadence.
Eye‑tracking shows readers chunk by paragraph; a 1‑sentence paragraph
between two 5‑sentence ones reads as emphasis (use sparingly).

---

## Q26 — Should paragraph lengths vary or stay even?

**Framing.** Sameness is a rhythm choice too.

- **A. Vary deliberately.** A short paragraph after a long one is the
  cheapest emphasis on the page.
- **B. Keep paragraphs roughly equal length.** Bricklayer rhythm.
- **C. Don't think about it.** Whatever comes out.

**Recommended:** **A**. The short paragraph after a long one is among the
most under‑rated tools in editing.

**Why.** Gary Provost's _"vary your sentences"_ passage
(_100 Ways to Improve Your Writing_, 1985), applied at the paragraph
level. Zinsser, Pinker, Strunk & White all agree.

---

## Q27 — Average sentence length?

**Framing.** Sentences too short read as telegraphic; too long as
pretentious.

- **A. Short — 10–15 words.** Hemingway.
- **B. Mixed — 15–25, with deliberate variation.** Modern web standard.
- **C. Long — 25+.** Classical / academic.

**Recommended:** **B**. Variation matters more than the average.

**Why.** Flesch Reading Ease (Flesch, 1948). Plain‑language research
(plainlanguage.gov; GDS): 15‑to‑20‑word sentences are read fluently by
the widest audience. Hemingway / Tolstoy / Pinker divergence shows the
extremes both work — for very different audiences.

---

## Part VI — Headings & hierarchy

## Q28 — How deep should headings go (h1, h2, h3, h4…)?

**Framing.** Hierarchy depth is a contract with the screen‑reader user
and the scanner.

- **A. h1 + h2 only.** Simplest hierarchy.
- **B. h1 + h2 + h3.** Three‑level hierarchy.
- **C. h1 → h4+.** Documentation depth.

**Recommended:** **B**. One h1 (page title), h2 per top‑level section, h3
sparingly for sub‑topics within long sections. h4+ only in reference docs.

**Why.** WebAIM Screen Reader User Survey #10 (2024): 68 % of
screen‑reader users navigate by heading level. Skipping levels (h2 → h4)
is reported as a defect by every accessibility audit tool. Bringhurst:
three levels are all the eye reliably distinguishes without coloured
chrome.

---

## Q29 — How frequently should sub‑headings (h3) appear?

**Framing.** Sub‑headings are scan anchors.

- **A. Every 3–5 paragraphs.** Dense skim layer.
- **B. Every 6–10 paragraphs.** Light skim layer.
- **C. None — let the prose flow.** Narrative.

**Recommended:** **A** for reference/decision content. **B** for essays.
**C** for personal posts where the prose is the artefact.

**Why.** Nielsen, [_"How Users Read on the Web"_](https://www.nngroup.com/articles/how-users-read-on-the-web/)
(1997, reaffirmed through 2020). [F‑Shaped Pattern](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)
(Pernice, 2017). A sub‑heading every screen‑height gives the scan
something to land on.

---

## Q30 — Should headings be questions, statements, or noun phrases?

**Framing.** A heading's grammar tells the reader what's coming.

- **A. Noun phrase.** _"Section design."_ Indexical.
- **B. Statement.** _"Sections should hold one idea."_ Editorial — each
  heading is the claim.
- **C. Question.** _"How long should a section be?"_ Conversational.

**Recommended:** **C** for Q&A / FAQ content (this file). **B** for
manifestos (the manifesto uses statements). **A** for reference docs.

**Why.** Schriver, _Dynamics in Document Design_. NN/g plain‑language
guidance. Each form has a use; mixing them inside one section reads as
sloppy.

---

## Q31 — How long should a heading be?

**Framing.** Long headings stop being scan anchors and become prose.

- **A. ≤ 5 words.** Pure index.
- **B. 5–10 words.** Index that hints at the claim.
- **C. A full sentence (10+).** Mini‑deck slide.

**Recommended:** **B** by default. **A** for top‑level headings on landing
pages. **C** only in question‑style FAQ headings.

**Why.** Eye‑tracking shows readers stop reading a heading at ~5 words on
first scan (Pernice, NN/g, 2017). Past 10 words the heading duplicates
the first sentence below it.

---

## Part VII — Skim layer: bullets, lists, tables

## Q32 — Bullets first then prose, or prose first with a bullet summary?

**Framing.** Which layer leads — the scan layer or the prose layer?

- **A. Bullets first, prose for detail.** Each section opens with a 2–5
  item list; prose expands the items that need it.
- **B. Prose first, bullets as summary.** A short paragraph states the
  idea; bullets recap key takeaways at the end.
- **C. Pure prose, no bullets.** Reads as essay; harder to skim.

**Recommended:** **A** for reference / decision / how‑to content. **B**
for narrative essays where the prose itself is the value. Avoid **C** for
any page expected to be skimmed.

**Why.** Eye‑tracking shows readers fixate on bulleted items 2–3× more
than on equivalent prose (Pernice & Whitenton, NN/g, 2017). Lead with
bullets when the goal is _decide_ or _do_; lead with prose when the goal
is _convince_ or _change a mind_.

---

## Q33 — Should bullet points be expandable, or always fully visible?

**Framing.** Progressive disclosure is a sharp tool: cuts well when it
cuts secondary content, badly when it cuts primary.

- **A. Always visible.** All details inline; reader scrolls past what they
  don't need.
- **B. Bullets visible, details inside `<details>` elements.** Native HTML
  disclosure; no JS; preserves URL; Ctrl‑F opens them automatically in
  modern browsers.
- **C. Hidden behind JS‑powered tabs or accordions.** Heavier; fragile
  without JS; can hide content from search and Ctrl‑F.

**Recommended:** **A** when each bullet's detail is ≤ ~50 words. **B**
when each bullet's detail is a paragraph or more, _and_ when the bullets
work as a scanable index in their own right (FAQs, decision lists). **C**
never, on this site.

**Why.** NN/g, [_"Progressive Disclosure"_](https://www.nngroup.com/articles/progressive-disclosure/)
(Nielsen, 2006, updated 2024). `<details>` is the only safe
implementation: keyboard‑accessible, indexable by search engines, and
Ctrl‑F opens it in modern Chromium and Firefox
(`hidden=until-found`).

---

## Q34 — Bullets, numbered list, or a table?

**Framing.** Decide by intent, not aesthetics.

- **A. Bulleted list.** Order doesn't matter.
- **B. Numbered list.** Sequence matters, or you'll refer back to
  "step 3."
- **C. Table.** Each row has the same structured fields (compare across
  rows).

**Recommended:** Bullets when items are peers and order is loose. Numbered
when the reader will follow them or you will reference them. A table only
when there are ≥ 3 rows _and_ ≥ 2 columns of comparable data.

**Why.** Tables are powerful but heavy on cognitive load (Few, _Now You
See It_, 2009): the reader has to scan two axes. Numbered lists carry
implicit sequence semantics that screen readers announce; using them where
order is arbitrary is a small lie that compounds.

---

## Q35 — How long should a single bullet or list item be?

**Framing.** Bullets are a contract: scannable.

- **A. ≤ 1 line (≤ ~12 words).** Pure scan layer.
- **B. ≤ 1 short paragraph (~30–50 words).** Scan layer with substance.
- **C. Multiple paragraphs.** Effectively a sub‑section with a bullet.

**Recommended:** **B** for this site's lists. Drop to **A** when the list
is a genuine index. Avoid **C** — promote it to a sub‑section with its
own h3.

**Why.** Eye‑tracking shows readers commit to a bullet within ~6 words
(Pernice, NN/g, 2017). A 3‑word bullet next to a 50‑word bullet creates a
rhythm break that reads as defect.

---

## Q36 — Nested lists — when, if ever?

**Framing.** Lists inside lists feel structured; they read worse.

- **A. Never.** Flatten with sub‑headings.
- **B. One level of nesting max.** Genuine taxonomies only.
- **C. Whatever the data demands.** Outline‑style nesting.

**Recommended:** **A** by default. **B** when the nesting is genuine
taxonomy (file trees, ingredient hierarchies). Never **C**.

**Why.** Pernice / NN/g scan patterns: nested bullets break the
F‑pattern. Screen readers announce nesting depth verbosely. WCAG 1.3.1
_Info and Relationships_ requires nesting to be semantically real.

---

## Q37 — Inline numbering ("first… second… third…") in prose?

**Framing.** Inline numbering is the prose tool that does the same job as
a bullet list, in line.

- **A. Use real `<ul>` / `<ol>` lists always.** Strict
  lists‑are‑lists.
- **B. Inline numbering in prose is fine for short items in a
  conversational context.** Hybrid.
- **C. Mix freely with no rule.**

**Recommended:** **B**. Promoting every triplet to a bullet list breaks
rhythm; inline numbering is part of fluent prose.

**Why.** Pinker, _The Sense of Style_ (2014): strict‑list dogma is its
own anti‑pattern. Zinsser. Strunk & White: "make every word tell" —
sometimes that word is "first."

---

## Q38 — How do you decide between bullet, prose, table, and `<details>`?

**Framing.** The meta‑question that ties Q32–Q37 together.

- **A. By feeling — pick whatever looks right.**
- **B. By a quick decision rule applied every time.**
- **C. By a strict template the whole site follows.**

**Recommended:** **B**. The rule to apply every time:

> 1. Reader needs to act, decide, or remember in order? → **numbered
>    list**.
> 2. Items are peers, no order, each ≤ 50 words? → **bulleted list**.
> 3. ≥ 2 axes to compare across ≥ 3 rows? → **table**.
> 4. Scan‑then‑maybe‑expand? → **bullets + `<details>`**.
> 5. None of the above? → **prose**.
> 6. Still ambiguous? → **prose**. (When in doubt, write the sentence.)

**Why.** A consistent rule is faster than a fresh choice and protects the
rhythm of the site over time. Encodes Pernice's scan‑first /
read‑second model and Few's table‑use criteria. The "when in doubt,
prose" escape hatch protects against the failure mode where everything
becomes a list and the page reads as a slide deck.

---

## Part VIII — Voice and narration

## Q39 — First, second, or third person?

**Framing.** Person is the single biggest decision about voice.

- **A. First person ("I think…").** Personal essay; the author is the
  authority.
- **B. Second person ("You should…").** Manifesto, how‑to, product copy
  (this Q&A).
- **C. Third person / passive ("One does…").** Formal, academic.

**Recommended:** **A** for personal essays. **B** for manifestos, docs,
and product copy. **C** only for formal / legal writing.

**Why.** [GOV.UK content design guide](https://www.gov.uk/guidance/content-design):
second person for instructional content. Microsoft Writing Style Guide:
same. Mailchimp Content Style Guide: first person for the brand, second
for the user. Third person reads as distance.

---

## Q40 — Active or passive voice?

**Framing.** Active voice is shorter, clearer, and assigns responsibility.

- **A. Active by default; passive only when the actor is unknown or
  unimportant.**
- **B. Mostly passive (academic / formal).**
- **C. Mix freely with no rule.**

**Recommended:** **A**. The passive has its place — exactly the place the
active voice doesn't fit.

**Why.** Strunk & White: "use the active voice." Orwell, _"Politics and
the English Language"_ (1946). Plain‑language research: active prose
tests 20–40 % faster to read than passive equivalents.

---

## Q41 — Register: formal, conversational, or playful?

**Framing.** Register is how the page sounds when read aloud.

- **A. Formal.** Distance, gravitas, distance from the reader.
- **B. Conversational.** Modern‑web standard.
- **C. Playful / jokey.** High‑energy; exhausting at length.

**Recommended:** **B**. Conversational is the unmarked register of the
open web; formal sounds stiff; playful tires.

**Why.** Mailchimp, GOV.UK, Stripe and Apple style guides converge on
conversational‑plus‑confident. Nielsen on web writing: _"talk like a
person."_

---

## Q42 — Humour: when, how much?

**Framing.** Humour amplifies what's already true; misapplied it ages
badly.

- **A. None.** Humour dates.
- **B. One landed joke per section at most; never at the reader's
  expense.**
- **C. Throughout — humour is the voice.**

**Recommended:** **B**. The under‑written joke does the work of three
paragraphs of energy.

**Why.** Comedy‑writing principle (Cleese, Sedaris): humour reveals,
doesn't decorate. Schriver: low‑dose humour increases retention. Heavy
humour fails the multi‑audience test (Q3).

---

## Q43 — Quote directly or paraphrase?

**Framing.** Quoting borrows authority; paraphrasing borrows substance.

- **A. Quote directly (with attribution) when the original phrasing
  matters.**
- **B. Paraphrase, with citation.**
- **C. Quote everything.**

**Recommended:** **A** when the original wording is the value (an
aphorism, a specific phrase). **B** for facts and figures. Never **C** —
reads as literature review.

**Why.** Academic citation norms. Editorial practice. Copyright fair‑use
guidance: short, transformative, attributed.

---

## Part IX — Density, length, cuts

## Q44 — How long is too long for a single page?

**Framing.** Single‑file pages have a comfortable ceiling.

- **A. ≤ 1,000 words.** One essay.
- **B. 1,000–5,000.** Long‑form essay or chapter.
- **C. 5,000+.** Book‑length single page.

**Recommended:** **B**. Past 5,000 words, split (Q10).

**Why.** Medium / Substack average article length data. NN/g long‑form
research (Loranger, 2017): reader fatigue measurably worsens past ~5,000
words on a single page.

---

## Q45 — When do you expand a section vs leave it terse?

**Framing.** Expansion serves the reader's next likely question; not your
desire to be thorough.

- **A. Expand when the reader's next likely question isn't answered.**
- **B. Expand whenever you have more to say.**
- **C. Always terse — let the reader follow a link.**

**Recommended:** **A**. The "next‑question" test is the cleanest
expansion heuristic.

**Why.** Mike Caulfield, _The Garden and the Stream_ (2015): layered
information for self‑directed reading. NN/g progressive disclosure. **B**
is the author's indulgence; **C** punishes the reader who wanted the
answer here.

---

## Q46 — How many examples per idea?

**Framing.** One example can be a fluke; three is repetition.

- **A. One concrete example.**
- **B. Two — one familiar, one edge case.**
- **C. Three or more.**

**Recommended:** **B**. The familiar example earns trust; the edge case
proves the principle.

**Why.** Heath brothers, _Made to Stick_ (2007): concrete‑plus‑unexpected
pairing. Bruner's pedagogy on rule‑of‑three.

---

## Q47 — Numbers and statistics — inline, table, or chart?

**Framing.** The container should match the comparison.

- **A. Inline prose with the number.** _"Median page weight is 2.7 MB."_
- **B. Small table.** When there are ≥ 3 comparable numbers.
- **C. Chart.** When there are ≥ 6 numbers and the shape matters.

**Recommended:** All three by case. Use the simplest container that shows
the comparison.

**Why.** Tufte, _The Visual Display of Quantitative Information_ (2nd
ed., 2001). Few, _Now You See It_ (2009): tables for look‑up, charts for
shape, prose for one number.

---

## Part X — Emphasis, callouts, pull quotes

## Q48 — When do you use pull quotes / callouts?

**Framing.** Pull quotes are a second entry point for the scanner.

- **A. Never on this site.** Trust the prose.
- **B. Pull quotes for the single most important sentence of a long
  section.** Visual emphasis, not duplication.
- **C. Frequent callouts (Note / Tip / Warning) styled distinctly.**
  Documentation pattern.

**Recommended:** **B** sparingly (at most one per top‑level section). Add
**C** when the page _is_ documentation, with consistent semantics.

**Why.** Pernice, NN/g (2018): pull quotes work because they break
reading rhythm and create a second entry point for scanners. Microsoft
Style Guide on callouts: semantics must be visually distinct and
consistent.

---

## Q49 — Bold, italic, links — how much emphasis is too much?

**Framing.** Emphasis is a finite resource.

- **A. Almost none.** Weight and italic only for the rare critical word.
- **B. Bold the key phrase in roughly every paragraph; italicise quotes.**
- **C. Heavy use of bold, italic, colour, and highlight.**

**Recommended:** **B** for skim‑heavy content. **A** for narrative essays.
Never **C**.

**Why.** Tschichold, _The New Typography_ (1928): when everything is
emphasised, nothing is. Lupton, _Thinking with Type_ (2010). NN/g
eye‑tracking confirms a single bolded phrase per paragraph is read 2–3×
more than the surrounding prose; ten are read at the same rate as none.

---

## Q50 — Coloured text for emphasis?

**Framing.** Colour is reserved for semantic states.

- **A. Never colour the text itself.**
- **B. One accent colour for links + one for warnings, that's it.**
- **C. Use colour freely.**

**Recommended:** **B**.

**Why.** [WCAG 1.4.1 _Use of Color_](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color):
colour must never be the only way of conveying information.
Colour‑as‑emphasis fails for ~8 % of male readers (deuteranopia /
protanopia). Bringhurst: colour is meaning; spend it deliberately.

---

## Part XI — Cross‑references, anchors, ToC, reading‑time

## Q51 — Table of contents at the top, sticky sidebar, or none?

**Framing.** A ToC is itself information; you only need one when the
reader is unlikely to read top‑to‑bottom.

- **A. None.** Trust the headings and the scroll.
- **B. A flat ToC near the top.** Skimmable index.
- **C. A sticky sidebar ToC that highlights the current section.**

**Recommended:** **A** for pages of ≤ 5 sections. **B** for anything
longer, including this Q&A. **C** only for reference docs.

**Why.** Krug: _"If the user has to think about whether they can find
something, they've already lost the page."_ On a short page, the headings
_are_ the ToC.

---

## Q52 — Should every section have its own anchor link / `#id`?

**Framing.** Stable anchors are how the web quotes itself.

- **A. Only on headings you expect people to deep‑link.**
- **B. Every `<h2>` and `<h3>` gets an `id` automatically.**
- **C. No anchors anywhere.**

**Recommended:** **B**. Auto‑generate slugs from heading text. Render the
anchor as a small `¶` or `#` symbol that appears on hover or focus. Add
`scroll-margin-block: 1lh` so anchored content doesn't hide under any
sticky header.

**Why.** GitHub‑style anchor links are the de facto standard; users
expect them. Adding them is one line of CSS plus an `id` per heading.

---

## Q53 — Reading‑time / word‑count indicators?

**Framing.** Reading‑time chips are tiny chrome that change behaviour.

- **A. Nothing.** Let the scrollbar do the talking.
- **B. A small "~7 min read" near the title.**
- **C. A live progress bar at the top of the page.**

**Recommended:** **A** by default. **B** when the page is genuinely long
(> ~10 min). Never **C** on a manifesto‑style page; it adds reading
pressure.

**Why.** Schwartz / Chartbeat (2014): reading‑time labels slightly
increase click‑through but slightly decrease completion of longer
articles. The scrollbar gives the same information for free.

---

## Q54 — Cross‑references inside the same page?

**Framing.** Same‑page cross‑refs respect the reader and avoid
duplication drift.

- **A. Inline link to the referenced section (_"see Q12"_).**
- **B. The reader navigates via the ToC; no inline cross‑refs.**
- **C. Repeat the relevant content in both sections.**

**Recommended:** **A**. Cross‑refs are the web's native quoting
mechanism.

**Why.** Tim Berners‑Lee on hypertext (1989): the link _is_ the citation.
Donald Knuth, _Literate Programming_ (1992): DRY applied to prose.
Duplicated content drifts; linked content stays in sync.

---

## Part XII — Footnotes, definitions, asides, attribution

## Q55 — Footnotes, inline asides, or "learn more" links?

**Framing.** Tangents have three weights.

- **A. Footnotes.** Superscript anchor + numbered list at the bottom.
- **B. Inline `<aside>` or italicised parenthetical.** Tangent in flow.
- **C. Inline "learn more" links.** Lowest weight.

**Recommended:** **C** for almost everything on this site. **A** for
attribution‑heavy writing. **B** for short factual clarifications.

**Why.** Footnotes interrupt twice — jumping down and back. Krug: a link
is a self‑documenting footnote. WCAG 2.4.4 _Link Purpose_: use
descriptive link text, never "click here."

---

## Q56 — How do you handle definitions and jargon?

**Framing.** Define inline, glossary at the end, or assume the reader
knows?

- **A. Define inline the first time, then use the term freely.**
- **B. Use `<dfn>` + a `<dl>` glossary at the bottom.**
- **C. Don't define; assume your reader knows.**

**Recommended:** **A** for most pages. **B** when there are > ~5 domain
terms and the audience may not be expert. **C** only for explicitly
expert audiences.

**Why.** Plain‑language research (plainlanguage.gov; GDS content design
guide): inline definition beats glossary lookup on comprehension because
the reader doesn't context‑switch.

> **Failure mode I have shipped.** Using _"Azure"_, _"GitHub Copilot"_,
> _"Power Automate premium connectors"_ in a page written for nonprofit
> volunteers — without ever defining what those things _are_. The
> inverted-pyramid TL;DR (Q15) does not rescue a reader who cannot parse
> the headline. **Definition precedes comparison.** See **Retrospective**
> at the end of this file.

---

## Q57 — Parenthetical aside, `<aside>` element, or sidebar?

**Framing.** Three forms of "this isn't the main point but…"

- **A. Parenthetical inline.** _"(see also Q12)"_ — light, short.
- **B. HTML `<aside>` rendered as an indented block.** Paragraph‑length.
- **C. A true sidebar floated next to the prose.** Magazine layout.

**Recommended:** **A** for one‑clause asides. **B** for paragraph‑length
asides. Never **C** on a single‑column page.

**Why.** HTML5 semantics. Reading‑flow research. Floats fall through to
the bottom on narrow viewports anyway; the magazine pattern doesn't
survive mobile.

---

## Q58 — Where does the source / attribution / quote credit go?

**Framing.** Trust on the open web is built by visible,
instantly‑checkable sourcing.

- **A. Right after the quote, in parentheses or em‑dash form.** Classic
  print style.
- **B. As a footnote / endnote.** Clean reading line; one extra jump.
- **C. As an inline link on the quoted phrase.** Web‑native; lowest
  visual weight.

**Recommended:** **A** with the link _embedded_ in the source title.
Combines print‑style credibility with web‑native discoverability.
Reserve **B** for academic writing.

**Why.** Stanford Web Credibility Project (Fogg et al., 2002). A reader
who sees the author's name and source title beside a quote can decide
whether to follow the link without breaking flow.

---

## Part XIII — Layout: figures, code, dark mode

## Q59 — Where do figures, images, and diagrams go?

**Framing.** A column is a contract.

- **A. Inline, full column width, between paragraphs.** Standard book
  layout.
- **B. Inline, allowed to break out wider than the prose column.** For
  diagrams.
- **C. Floated alongside the prose.** Magazine.

**Recommended:** **A** by default. **B** as an opt‑in escape hatch (a
`.full-bleed` or `.wide` class on the `<figure>`) for diagrams that lose
meaning at column width. Avoid **C**.

**Why.** A column is a contract: every line starts in the same place.
Floats break the contract and fail on narrow viewports. The wide‑figure
escape hatch covers the legitimate cases (data viz, screenshots) without
compromising the reading column.

---

## Q60 — Where do code blocks go, and how long can they be?

**Framing.** Code is reference, not narrative.

- **A. Inline, same width as the prose column; wrap if needed.**
- **B. Inline, allowed to break out wider when line length matters.**
- **C. In a separate scrollable "code panel."**

**Recommended:** **B**. Allow horizontal scroll on long lines
(`overflow-x: auto`) rather than forcing wraps that change semantics. Cap
any single example at ~30 lines; longer, link to a Gist.

**Why.** Long code blocks are skipped by most readers (Pernice, NN/g,
2021). They are reference inserts; treat them as such.

---

## Q61 — Should the page support dark mode?

**Framing.** Three positions on dark mode.

- **A. No.** Design for one palette; trust the user's OS to do nothing.
- **B. Yes, via `prefers-color-scheme` and CSS variables.** Two palettes,
  one media query, zero JS.
- **C. Yes, with a manual toggle.** JS, localStorage, the works.

**Recommended:** **B**. Cheapest implementation, respects user
preference, no UI to maintain.

**Why.** Apple HIG, Microsoft Fluent guidelines. Some low‑vision users
require dark mode. OLED battery saving.
[`prefers-color-scheme`](https://www.w3.org/TR/mediaqueries-5/#prefers-color-scheme)
(W3C Media Queries Level 5) is supported in all current browsers.

---

## Part XIV — Reader workflows

## Q62 — Where does the call to action (CTA) go on a landing page?

**Framing.** CTAs are decisions; readers decide at different points.

- **A. Above the fold, in the hero.** Maximum visibility.
- **B. After the first benefit section.** Once the visitor has agreed
  with the premise.
- **C. Repeated 2–3 times at natural decision points.** Multiple chances.

**Recommended:** **C** for commerce / landing pages. **B** for
informational pages with a single CTA. **A** alone rarely works on
content‑heavy pages.

**Why.** [Baymard Institute](https://baymard.com/research) and Unbounce
conversion research consistently show one CTA is rarely enough on pages
longer than two screens. Classical AIDA model (Attention‑Interest‑Desire‑
Action) implies multiple opportunities to act. Keep CTA wording identical
so repetition reads as confidence.

---

## Q63 — Print stylesheet — yes, no, or effort?

**Framing.** People print and save as PDF more than you think.

- **A. None — the screen styles will print "fine."**
- **B. Minimal `@media print` block.** Hide nav, dark mode off, larger
  margins, black on white.
- **C. Bespoke print stylesheet.** Magazine‑grade.

**Recommended:** **B**. ~10 lines of CSS make the print output dignified.

**Why.** Bringhurst (the canonical reference on type for print). People
save articles as PDF for offline reading; broken print is a slow form of
rudeness.

---

## Q64 — Optimise for in‑page search (Ctrl‑F)?

**Framing.** Ctrl‑F is the second most‑used navigation aid after the
scrollbar.

- **A. No — assume scrolling.**
- **B. Yes — keep important keywords in headings and visible text; don't
  hide content in JS components.**
- **C. Provide a custom on‑page search widget.**

**Recommended:** **B**. Don't break the back button; don't break Ctrl‑F.
`<details hidden="until-found">` lets folded content participate in
Ctrl‑F in modern Chromium.

**Why.** Bruce Lawson and many others on Ctrl‑F as a usability baseline.
Custom search widgets are almost always worse than the native one and
add JS for no benefit.

---

## Part XV — Decision hygiene

## Q65 — How strictly should every page on the site follow the same template?

**Framing.** Consistency is the brand; the content varies.

- **A. Strictly identical.** Same skeleton everywhere.
- **B. Same skeleton, varied details.** Header, footer, type, colour
  stay; body adapts.
- **C. Each page a snowflake.** No template.

**Recommended:** **B**. The skeleton is the brand; the details are the
content.

**Why.** [Jakob's Law](https://www.nngroup.com/articles/jakobs-law-internet-ux/)
(Nielsen, 2017): users spend most of their time on other sites and bring
those expectations. Brad Frost, _Atomic Design_ (2016). Karen McGrane,
_Content Strategy for Mobile_ (2012).

---

## Q66 — When is it OK to break your own style guide?

**Framing.** A style guide is a default, not a law.

- **A. Never.** Consistency above all.
- **B. When the content genuinely demands it AND you can articulate the
  reason in one sentence.**
- **C. Whenever you feel like it.**

**Recommended:** **B**. The one‑sentence test (_"I broke the rule
because…"_) catches 90 % of bad exceptions.

**Why.** Editorial practice. Brad Frost on design systems: "conventions
that can't be broken aren't conventions, they're constraints." Karen
McGrane: a style guide that admits its exceptions ages better than one
that pretends to be universal.

---

## References

Books, papers, and articles cited above (organised by source).

**Information architecture & UX research**
- Donna Spencer, _A Practical Guide to Information Architecture_, 2nd ed.,
  Five Simple Steps, 2014.
- Peter Morville, _Ambient Findability_, O'Reilly, 2005.
- Steve Krug, _Don't Make Me Think, Revisited_, 3rd ed., New Riders,
  2014.
- Karen Schriver, _Dynamics in Document Design_, Wiley, 1997.
- Brad Frost, [_Atomic Design_](https://atomicdesign.bradfrost.com/), 2016.
- Karen McGrane, _Content Strategy for Mobile_, A Book Apart, 2012.

**Nielsen Norman Group**
- [Inverted Pyramid: Writing for Comprehension](https://www.nngroup.com/articles/inverted-pyramid/)
  (Moran, 2017).
- [F‑Shaped Pattern of Reading on the Web](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)
  (Pernice, 2017).
- [How Little Do Users Read?](https://www.nngroup.com/articles/how-little-do-users-read/)
  (Nielsen, 2008).
- [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/)
  (Nielsen, 2006; updated 2024).
- [How Users Read on the Web](https://www.nngroup.com/articles/how-users-read-on-the-web/)
  (Nielsen, 1997).
- [Why Web Users Scan Instead of Reading](https://www.nngroup.com/articles/why-web-users-scan-instead-reading/)
  (Liu, 2014).
- [Layered Presentation Reduces Cognitive Load](https://www.nngroup.com/articles/layered-presentation/)
  (Loranger, 2014).
- [Jakob's Law of Internet User Experience](https://www.nngroup.com/articles/jakobs-law-internet-ux/)
  (Nielsen, 2017).
- [Why You Only Need to Test with 5 Users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)
  (Nielsen, 2000).

**Cognitive psychology & reading research**
- George A. Miller, _"The Magical Number Seven, Plus or Minus Two,"_
  _Psychological Review_, 1956.
- Nelson Cowan, _"The Magical Number 4 in Short‑Term Memory,"_
  _Behavioral and Brain Sciences_, 2001.
- John Sweller, _"Cognitive Load During Problem Solving,"_ _Cognitive
  Science_, 1988.
- John R. Hayes & Linda Flower, _"A Cognitive Process Theory of
  Writing,"_ _College Composition and Communication_, 1981.
- Jean M. Mandler & Nancy S. Johnson, _"Remembrance of Things Parsed,"_
  _Cognitive Psychology_, 1977.
- Hermann Ebbinghaus, _Über das Gedächtnis_ (1885) — the forgetting curve.

**Writing craft**
- William Zinsser, _On Writing Well_, 7th ed., HarperCollins, 2006.
- Strunk & White, _The Elements of Style_, 4th ed., Pearson, 2000.
- Steven Pinker, _The Sense of Style_, Viking, 2014.
- Peter Elbow, _Writing Without Teachers_, Oxford, 1973.
- Anne Lamott, _Bird by Bird_, Anchor, 1994.
- Stephen King, _On Writing_, Scribner, 2000.
- George Orwell, _"Politics and the English Language,"_ _Horizon_, 1946.
- Gary Provost, _100 Ways to Improve Your Writing_, Mentor, 1985.
- Chip & Dan Heath, _Made to Stick_, Random House, 2007.
- Mike Caulfield, [_The Garden and the Stream: A Technopastoral_](https://hapgood.us/2015/10/17/the-garden-and-the-stream-a-technopastoral/),
  2015.

**Typography & visual design**
- Robert Bringhurst, _The Elements of Typographic Style_, 4th ed.,
  Hartley & Marks, 2012.
- Ellen Lupton, _Thinking with Type_, 2nd ed., Princeton Architectural
  Press, 2010.
- Jan Tschichold, _The New Typography_ (1928), trans. McLean, UC Press,
  1995.
- Edward Tufte, _The Visual Display of Quantitative Information_, 2nd
  ed., Graphics Press, 2001.
- Stephen Few, _Now You See It_, Analytics Press, 2009.

**Plain language & content style**
- [GOV.UK Content Design Guide](https://www.gov.uk/guidance/content-design).
- [plainlanguage.gov](https://www.plainlanguage.gov/) — US Federal Plain
  Language Guidelines, 2011.
- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/).
- [Google developer documentation style guide](https://developers.google.com/style).
- Rudolf Flesch, _"A New Readability Yardstick,"_ _Journal of Applied
  Psychology_, 1948.
- [Mailchimp Content Style Guide](https://styleguide.mailchimp.com/).

**Accessibility**
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — W3C Recommendation, 2023.
  Especially 1.3.1 _Info and Relationships_, 1.4.1 _Use of Color_,
  2.4.4 _Link Purpose_, 2.4.10 _Section Headings_.
- [WebAIM Screen Reader User Survey #10](https://webaim.org/projects/screenreadersurvey10/),
  2024.

**Web standards & web culture**
- Tim Berners‑Lee, [_Cool URIs Don't Change_](https://www.w3.org/Provider/Style/URI),
  1998.
- Jim Nielsen, [_Building Websites With LLMS (Lots of Little HTML
  Pages)_](https://blog.jim-nielsen.com/2025/lots-of-little-html-pages/),
  2025.
- Andy Bell, [_Build Excellent Websites_](https://buildexcellentwebsit.es/).
- Manuel Matuzović, [matuzo.at](https://www.matuzo.at/).

**Credibility, trust & conversion**
- B.J. Fogg et al., _Stanford Web Credibility Project_, 2002.
- [Baymard Institute](https://baymard.com/research) — e‑commerce UX
  research.
- Dan Schwartz, _"How much of an article do people read?"_ Chartbeat,
  2014.
- AIDA model — classical marketing literature.

> _"A document is not a building. It does not need to stand on its own.
> It stands on the reader."_ — paraphrased from Bringhurst.


---

## Retrospective: failure modes I have already shipped

These are real mistakes from real pages in this repo. Each one is a
question of this file that I had read but didn't actually apply.
Listed here so the failure mode is concrete, not abstract.

### 1. Comparison-table-before-definition  *(Q1, Q15, Q56)*

**What I shipped.** A nonprofit-procurement page that opened with a
five-column "free vs paid" table covering Microsoft 365, Azure, Power
Automate, DreamSpace, Windows, GitHub and GitHub Copilot — for an
audience that had never heard of "Azure" or "GitHub Copilot" and
couldn't parse the table headers.

**What was wrong.** I had the inverted pyramid correct (Q15) for a
procurement-savvy reader, but the named reader (Q1) was a volunteer
treasurer with no IT background. The apex of the pyramid is not the
TL;DR; it is _"what is this even, and why should I care?"_ The TL;DR
comes after.

**The fix.** A new Section 0 _"Start here"_ — three pillars, framed
by **outcome** ("what your committee uses every day", "what runs in
the background for you", "what lets your people grow"), not by
Microsoft business unit. Product names appear only in a one-line
footer at the bottom of each pillar: _"In Microsoft's words:
Microsoft 365 Business Basic + Windows 11 Pro."_

**The principle.** **Definition precedes comparison.** Before you
table the trade-offs, the reader must know what's being traded.

### 2. Categorising by the source's mental model  *(Q1, Q39)*

**What I shipped.** A first draft of Section 0 with pillars named
_Software / Cloud / Skilling_ — Microsoft's own organisational
categories, lifted unchanged.

**What was wrong.** A volunteer thinks _"send a newsletter"_, not
_"that's cloud"_. Mapping the offer onto Microsoft's business units
forces the reader to translate. It is the source's lens, not the
audience's.

**The fix.** Reframe by job-to-be-done (the outcomes the society
actually pursues), then translate _back_ to product names in a footer.
Same content, different opening lens.

**The principle.** **When the source and the audience speak different
languages, write in the audience's.** Translate _into_ the page; do
not translate _from_ it.

### 3. Jargon left undefined  *(Q56)*

**What I shipped.** Inline use of "Azure", "GitHub", "Copilot",
"Power Automate premium connectors", "RPA", "Dataverse", "SSO" — all
without inline definition — on a page targeting nonprofit volunteers.

**What was wrong.** Q56 says: define inline the first time, then use
the term freely. I had jumped past the definition because _I_ knew
what the words meant.

**The fix.** First mention of every proper noun gets a short inline
gloss. _"Azure — Microsoft's rented data-centre service for hosting
websites, sending email at scale, and running small databases."_

**The principle.** **Plain English is not condescension.** It is the
cost of admission for any page that isn't explicitly for experts.

### 4. Procurement-savvy reader, by accident  *(Q1)*

**What I shipped.** A "five-check rule" section that opened with
_"Before you commit to any free grant or discount, walk through these
five questions"_ — a meta-procurement framework — as Section 1.

**What was wrong.** That sentence assumes a reader who is already
committed to procurement. The actual named reader is _earlier_ in the
funnel: _"what is this and could it possibly be useful to me?"_

**The fix.** Demote the five-check rule from Section 1 to Section 2,
behind the plain-English overview.

**The principle.** **Ordering follows the reader's state, not the
author's.** Frameworks are for readers who have already decided to
read carefully. Plain English is for everyone else.

### 5. Colour borrowed from the source, not the page  *(Manifesto Ch. 6, Q50)*

**What I shipped.** Microsoft-blue as the page accent, used for "free"
in the comparison table, on a page illustrated with black-figure Greek
vase paintings (clay-orange + black on cream).

**What was wrong.** The illustration aesthetic and the UI palette
were two different palettes. Blue is what Microsoft uses; it is not
what the page uses.

**The fix.** Drop the blue. Single terracotta accent (`#a44a1f`),
deep oxblood warning (`#5d1818`), passe-partout mat (`#efe6d4`) for
figures. The website now lives in the same world as its images.

**The principle.** **The illustration sets the palette, not the
brand of the subject.** A page about Microsoft does not have to be
blue.

---

> _Each of these was caught only after I had shipped the page.
> The discipline is to catch them at the outline stage, by walking
> through Q1, Q2, Q15 and Q56 honestly before drafting._