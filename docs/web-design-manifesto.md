# The Manifesto

**A vibe‑coded, HTML‑first style guide for fast, beautiful, evocative websites.**

This is a personal style guide. It reads like a manifesto on purpose. Ten chapters. Five
principles each. Fifty rules in total, all small enough to remember, all chosen so a
website built this way still works in ten years.

The aesthetic it targets is the one the source blogs already practise: a single
column of clear type, generous space, restrained colour, a single quiet accent, and
the browser doing most of the work. Slick, fast, modular, and built almost entirely
out of HTML and CSS.

Read it top to bottom. Cherry‑pick from it forever after.

---

## 1. HTML is the load‑bearing wall

Build the document first. Style it second. Enhance it third. If the HTML on its own
is useful, everything that comes after is a bonus.

1. **Write the page as if CSS will never load.** Headings, paragraphs, lists, a form,
   a `<main>`, a `<nav>`, a `<footer>`. If the unstyled page reads as a document, the
   styled page will read as a website. _“At the root of progressive enhancement is
   solid, organised and semantic HTML. If the absolute worst should happen … then at
   least the user gets a functional, understandable web page.”_ — Andy Bell, _It's
   about time I tried to explain what progressive enhancement actually is_
   ([source](https://piccalil.li/blog/its-about-time-i-tried-to-explain-what-progressive-enhancement-actually-is/)).
2. **Prefer the native element.** `<button>`, `<details>`, `<dialog>`, `<input
   type="…">`, `<a href>`. Each is a free implementation of focus, keyboard
   semantics, screen‑reader output and platform polish — work you don't have to
   re‑do and won't get right.
3. **Use links for navigation, buttons for actions, forms for input.** Don't dress
   a `<div>` as a link with an `onclick`. The browser already knows what a link is
   for and how to break it gracefully across tabs, history, and the back button.
4. **Don't strip semantics with ARIA.** `role="presentation"` and stray
   `aria-hidden` calls erase the very meaning the browser ships for free. _“The
   presentation role causes a given element to be treated as having no role … you'll
   quickly learn that I removed this attribute in all of my suggested fixes, as it's
   just not necessary.”_ — Steve Frenzel, Piccalilli
   ([source](https://piccalil.li/blog/you-might-not-need-rolepresentation)).
5. **One element, one job.** A page made of nested `<div>`s is harder to style and
   impossible to navigate with assistive tech. Choose the most specific tag the
   content allows and let the cascade compose them.

> Research base: Jeremy Keith's _Resilient Web Design_ (resilientwebdesign.com) and
> the W3C ARIA Authoring Practices Guide. The WebAIM Million annual study (2024
> edition: 95.9% of home pages have detectable WCAG failures) shows that the most
> common errors are still missing alt text, low contrast and empty links — all
> faults of the HTML layer, not the design layer
> ([source](https://webaim.org/projects/million/)).

---

## 2. Be the browser's mentor, not its micromanager

Stop pixel‑pushing across imaginary breakpoints. The browser already knows more
about the viewport, the user, and the connection than you do.

1. **Hint, don't dictate.** Set sensible mins, maxes and ideals and let the layout
   engine resolve the rest. _“It makes sense to lose a bit of perceived control and
   instead get even greater control by being the browser's mentor and not its
   micromanager.”_ — Andy Bell, _Build Excellent Websites_
   ([source](https://buildexcellentwebsit.es/)).
2. **Use intrinsic sizing.** `clamp()`, `min()`, `max()`, `minmax()`, `auto`,
   `fr` — these replace 90% of your media queries with a single fluid rule.
3. **Container queries before media queries.** Components should respond to the
   space they're given, not to a global breakpoint that someone invented in 2014.
4. **Forget the magic numbers.** _“The ideal viewport doesn't exist.”_ Set Studio's
   2,300‑unique‑viewport study shows real users on every width imaginable
   ([viewports.fyi](https://viewports.fyi/)). Design a continuum, not a set of
   four screens.
5. **Don't override what the browser does well.** If `text-wrap: balance` ships,
   use it. If `scroll-margin-block` works, use it. If the browser is happy
   keyboard‑managing a `<details>` summary, let it.

> Research base: Ethan Marcotte, _Responsive Web Design_ (A List Apart, 2010);
> Jen Simmons's _Intrinsic Web Design_ talks; the W3C CSS Containment Module Level 3.

---

## 3. Progressive enhancement is the default

Layer the experience. Default off, capability on. Everyone gets something good;
the lucky ones get something great.

1. **Baseline first.** _“We build for everyone. Not just for ourselves or our peer
   groups.”_ — Andy Bell. The minimum viable experience must answer the user's
   question, even with no CSS, no JS, no network
   ([source](https://piccalil.li/blog/its-about-time-i-tried-to-explain-what-progressive-enhancement-actually-is/)).
2. **Declare the fallback first, the upgrade second.** `height: 1.5em; height:
   1cap;` — the cascade does the feature detection for you.
3. **`@supports` over user‑agent sniffing.** Ask the browser what it can do, not
   what badge it wears.
4. **Use `@layer` to keep the cascade predictable.** Wrap resets and third‑party
   styles in an anonymous layer so your own rules always win without `!important`
   theatre. _“If you have a specificity issue within a layer, you can wrap rules
   in an (anonymous) layer to regain control.”_ — Manuel Matuzović
   ([source](https://www.matuzo.at/blog/2026/lowering-specificity-of-multiple-rules)).
5. **JavaScript is an enhancement, never the entry point.** If turning JS off
   collapses the page, the page was never built; it was rendered.

> Research base: Tim Berners‑Lee's _Rule of Least Power_ (W3C TAG Finding, 2006);
> Jeremy Keith's _Resilient Web Design_; Steve Faulkner's accessibility writing
> at TPGi.

---

## 4. Type is the interface

Words are the product. Treat type as the first design decision, not the last.

1. **One body face. Maybe one display face. That's it.** Two families, used
   confidently, beat five families used apologetically. System fonts (the
   default `system-ui, sans-serif` stack) ship in zero bytes and look native
   everywhere.
2. **Set a measure of ~60–75 characters.** Robert Bringhurst's _Elements of
   Typographic Style_ (3.2.2) puts the ideal line at 45–75 characters; 66 is the
   classic target. The Baymard Institute's reading studies confirm comprehension
   drops sharply beyond ~75ch. Use `max-inline-size: 66ch` on prose containers
   ([Baymard](https://baymard.com/blog/line-length-readability)).
3. **Body copy 1rem minimum, line‑height 1.5, headings tighter (1.1–1.2).**
   _“I like a nice legible line height that gets inherited.”_ — Andy Bell,
   _A more modern CSS reset_
   ([source](https://piccalil.li/blog/a-more-modern-css-reset/)).
4. **Scale fluidly.** A type scale generated with `clamp()` (Utopia.fyi) gives
   you a font size that reads correctly from a 360 px phone to a 1920 px desktop
   without a single media query.
5. **Respect the user's text size.** Use relative units (`rem`, `em`, `ch`, `lh`,
   `cap`) everywhere; honour `text-size-adjust` so Mobile Safari stops scaling
   your work; opt in to the new `<meta name="text-scale" content="scale">`
   when it ships ([Matuzo](https://www.matuzo.at/blog/2026/text-scaling-meta-tag)).

> Research base: Bringhurst, _The Elements of Typographic Style_ (Hartley & Marks,
> 4th ed., 2012); Mary C. Dyson, _“How Physical Text Layout Affects Reading from
> Screen”_ (Behaviour & Information Technology, 2004); Kara Pernice & Jakob
> Nielsen, _“How People Read on the Web”_ (NN/g, 2006, 2017, 2020 — the F‑pattern
> studies).

---

## 5. One column is enough

The web is a scroll. Stop fighting it. A single column of well‑set text is the
most evocative layout there is — every blog you admire already does it.

1. **Centre a single column at ~`min(66ch, 100% - 2rem)`.** No sidebars on
   reading pages. Sidebars are for chrome you don't need.
2. **Whitespace is content.** Section spacing should be the largest token on
   your space scale, not the smallest.
3. **One idea per section.** A heading, a paragraph or two, maybe an image,
   maybe a code block. Then a horizontal break and on to the next idea.
4. **Don't fear the long page.** Scrolling is cheaper than a click, cheaper
   than a tab, and infinitely cheaper than a modal. _“Lots of little HTML
   pages”_ is for the navigation; long single‑column reading is for the page
   itself ([Jim Nielsen](https://blog.jim-nielsen.com/2025/lots-of-little-html-pages/)).
5. **Break the column only with intent.** A wide figure, a callout, a full‑bleed
   quote. Use `:not(.full-bleed)` + a single grid track to make full‑bleed an
   opt‑in escape hatch, not the default.

> Research base: Jakob Nielsen, _“How Little Do Users Read?”_ (NN/g, 2008 — users
> read ~20% of text on an average visit, so make the 20% the right 20%);
> Edward Tufte, _The Visual Display of Quantitative Information_ (2nd ed., 2001) on
> data‑ink ratio and the elimination of non‑informative ornament.

---

## 6. Colour is a system, not a paint pot

Restraint reads as taste. Use as few colours as you can, decide them once, and
let them earn their place.

1. **Three or four neutrals, one accent.** Background, foreground, muted‑fore,
   border — plus one accent that means “this is interactive”. If you find
   yourself reaching for a fifth, you're probably encoding state that should be
   shown by typography or spacing instead.
2. **Define colour as CSS custom properties at the root.** Every value becomes
   a token; every component becomes themeable for free; dark mode is one
   `[data-theme]` switch away.
3. **Meet WCAG 2.2 contrast on every text/background pair.** 4.5:1 for body,
   3:1 for large text and UI components. Use the WCAG contrast formula or the
   newer APCA (`color-contrast()` in CSS Color Module 5) and verify, don't
   guess ([WCAG 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)).
4. **Respect the user's mode.** `@media (prefers-color-scheme: …)` and
   `@media (forced-colors: active)` are not optional. If a focus ring vanishes
   in Windows High Contrast, your control is invisible to a real user — _“in
   forced colors mode the `box-shadow` property computes to `none`.”_ — Manuel
   Matuzović
   ([source](https://www.matuzo.at/blog/2026/box-shadow-no-alternative-to-outline)).
5. **Use `currentColor` and `color-mix()`.** Icons that inherit text colour
   match every theme automatically. `color-mix(in oklch, var(--accent) 80%,
   var(--bg))` gives you a tint without inventing a new token.

> Research base: WCAG 2.2 (W3C Recommendation, 2023); Lisa C. Charvat & Andrew
> Somers, APCA contrast research (apcacontrast.com); ColorBrewer (Cynthia
> Brewer) for accessible palette construction.

---

## 7. Spacing is a scale, not a guess

Random margins are how a page starts to look “off”. A spacing scale, applied
consistently, is how it starts to look intentional.

1. **One scale of tokens for space, one for type, one for radius.** Powers of
   1.25 or 1.5 work; a fluid scale from
   [Utopia](https://utopia.fyi/) works better. Pin everything to those tokens.
2. **Use logical properties.** `margin-block-start`, `padding-inline`, `inset-block`.
   They flow with the language; they also mean you never write `margin-top` and
   `margin-bottom` for the same thing again.
3. **One rhythm utility owns vertical flow.** Andy Bell's three‑line darling:
   `.flow > * + * { margin-block-start: var(--flow-space, 1em); }`. Override
   the variable, not the rule, for local exceptions
   ([source](https://andy-bell.co.uk/my-favourite-3-lines-of-css/)).
4. **`box-sizing: border-box` on everything.** It's the first line of every
   modern reset for a reason. Width means width; padding stays inside.
5. **Prefer `gap` for layout, `margin` for flow.** Flex and grid get `gap`;
   long‑form content gets `--flow-space`. Don't mix them.

> Research base: Tim Brown, _Modular Scale_ (modularscale.com, 2011) and his
> book _Flexible Typesetting_ (A Book Apart, 2018); the Material Design 8 dp
> grid research; James Gilyead and Trys Mudford, _Utopia_ (utopia.fyi).

---

## 8. Lots of little HTML pages

When in doubt, make it a link. The browser's most fundamental primitive —
navigation — is also its fastest, most accessible and most maintainable.

> **The destination is Jim Nielsen's _“lots of little HTML pages”_.** The
> arguments for it are overwhelming and, on the open web, basically
> unanswerable: every page is a URL, every URL is shareable, cacheable,
> archivable, indexable, and individually fast; the browser does the routing,
> the history, the back button, the deep‑link, the print, the “open in new
> tab” and the “save as” — for free; the page that the visitor wants is the
> only page that has to load; the codebase scales by _addition_ (drop another
> file in) instead of by _refactor_; a broken page never takes the whole site
> down; and the whole thing keeps working in 2046. _This is the long‑term
> default for this site._
>
> **But until I have a clean way to author them at scale — shared header /
> footer / nav / styles without a heavy framework, no copy‑paste drift,
> no build step I have to remember — the practical default is one HTML
> file with inlined CSS.** A single file beats five copy‑pasted ones today,
> even though five well‑factored little pages would beat the single file
> tomorrow. The single file is the staging ground; **LLMS** — Jim Nielsen's
> acronym for **L**ots of **L**ittle ht**M**l page**S** — is the
> destination. The moment a second page is added — or the moment the
> authoring pipeline (server‑side includes, tiny static generator, plain
> `<iframe>` partials, whatever earns its keep) is in place — flip to
> LLMS. See [`design_qna.md`](./design_qna.md) Q7 and Q10 for the
> trade‑offs and the splitting criteria.

1. **A click should usually be a navigation.** Fly‑out menu? New page. Search?
   New page. Filtered list? New page. _“Avoid in‑page interactions that require
   JavaScript in favour of multi‑page navigations that rely on HTML and are
   enhanced with CSS view transitions.”_ — Jim Nielsen
   ([source](https://blog.jim-nielsen.com/2026/small-html-pages/)).
2. **CSS view transitions, not JS animation.** `@view-transition { navigation:
   auto; }` plus a few `view-transition-name`s, and the static site you already
   have animates like an SPA — for free
   ([Jim Nielsen](https://blog.jim-nielsen.com/2026/out-with-js-in-with-html/)).
3. **URLs are bookmarks.** Every meaningful state of the app should have one.
   `/posts/?filter=hn` is better than `/posts` plus six lines of `localStorage`
   plumbing.
4. **Cache the static HTML, defer the dynamic.** A page that is a flat file is
   a page that is also a CDN edge, an offline cache and a printable artefact.
5. **Use the `<a>` you have.** If something can be expressed as a link with a
   meaningful `href`, do that, even if you also enhance with JS. Then keyboard,
   right‑click‑“Open in new tab”, screen reader and back button all work without
   another line of code.

> Research base: Roy Fielding's REST dissertation (2000) on hypermedia as the
> engine of application state; the HTML Living Standard's
> _“implementation‑defined”_ source‑selection algorithm — _trust the engine_
> ([html.spec](https://html.spec.whatwg.org/multipage/images.html#selecting-an-image-source)).

---

## 9. Accessibility is a feature, not a checklist

“We're all just temporarily abled.” — Cindy Li, quoted by
[Jim Nielsen](https://blog.jim-nielsen.com/2023/temporarily-abled/). 1 in 5
people has a disability today; 100% of people will at some point. Design for
the population you'll be in tomorrow.

1. **Keyboard first.** Tab through every page on every commit. If you can't
   reach it, neither can a third of your users (mouse‑avoiders, screen‑reader
   users, motor‑impaired users, anyone with a broken trackpad on a flight).
2. **Visible focus, always.** Never `outline: none` without a replacement.
   `:focus-visible` with a 2 px solid outline at 2 px offset is the safe
   default — and survives Windows High Contrast if you keep a transparent
   outline alongside any custom shadow
   ([Matuzo](https://www.matuzo.at/blog/2026/box-shadow-no-alternative-to-outline)).
3. **Native elements first, ARIA last.** _“No ARIA is better than bad ARIA.”_
   (W3C ARIA Authoring Practices Guide). Most ARIA bugs disappear when you
   replace the `<div role="button">` with a `<button>`.
4. **Respect user preferences.** `prefers-reduced-motion`, `prefers-color-scheme`,
   `prefers-contrast`, `prefers-reduced-transparency`, `forced-colors`. Each is
   a single‑line media query. Treat them as production code.
5. **A perfect Lighthouse score is not done.** _“You can build the most
   inaccessible site possible with a perfect Lighthouse score.”_ — Manuel
   Matuzović ([source](https://www.matuzo.at/blog/building-the-most-inaccessible-site-possible-with-a-perfect-lighthouse-score/)).
   Add a manual keyboard pass and a VoiceOver/NVDA sweep before you ship.

> Research base: WCAG 2.2 (W3C Recommendation, 2023); WebAIM Million 2024
> ([webaim.org/projects/million](https://webaim.org/projects/million/));
> Microsoft Inclusive Design Toolkit (2016); Heydon Pickering, _Inclusive
> Design Patterns_ (Smashing, 2016).

---

## 10. Ship less, observe more

Performance is a kindness. Maintainability is a kindness to your future self.
Both come from doing fewer things, better.

1. **Inline the CSS that paints the first screen, defer the rest.** A 2–8 KB
   stylesheet that arrives with the HTML is faster than a “tiny” framework
   that arrives in a second round trip. _Build Excellent Websites_ ships **~2 KB
   of CSS in total**
   ([source](https://buildexcellentwebsit.es/)).
2. **Zero‑build is a feature.** A site that reads in `View Source` is a site
   anyone — including you, six months from now — can repair without a Node
   version manager.
3. **Sand the UI.** Click around, find a splinter, fix it, click again. _“It's a
   small thing, but lots of small splinters lead to an agonizing experience.”_
   — Jim Nielsen
   ([source](https://blog.jim-nielsen.com/2024/sanding-ui/)).
4. **Measure breadth and depth.** Page weight is breadth; long‑term usability
   is depth. _“Faster individuals don't make a fast company.”_ — Chris Coyier,
   via [Jim Nielsen](https://blog.jim-nielsen.com/2026/collective-speed-isnt-the-sum-of-individual-speed/).
   A page that loads in 200 ms but isn't readable in five years is slower than
   one that loaded in 800 ms and still works.
5. **Treat dependencies as debt.** Every package is a future security patch,
   breaking change, or rewrite. The smallest dependency graph wins on
   performance, accessibility, security and joy.

> Research base: HTTP Archive's annual _Web Almanac_ (httparchive.org);
> Google's Core Web Vitals research (web.dev/vitals); Steve Souders, _High
> Performance Web Sites_ (O'Reilly, 2007); Alex Russell's “the performance
> inequality gap” series (infrequently.org).

---

## How to use this

1. **Start with the HTML.** A single `<main>` with a heading, a paragraph,
   maybe a `<nav>`, maybe a `<footer>`. Read it. If it reads, continue.
2. **Apply a reset you trust.** Andy Bell's
   [_a more modern CSS reset_](https://piccalil.li/blog/a-more-modern-css-reset/)
   is the safest 30 lines you can paste.
3. **Define your tokens.** Colours, type scale, space scale — all as CSS custom
   properties at `:root`. Five of each is plenty.
4. **Set the column.** `body { font: 1rem/1.5 system-ui, sans-serif; }` and
   `main { max-inline-size: 66ch; margin-inline: auto; padding-inline: 1rem;
   }`. Add `.flow > * + * { margin-block-start: var(--flow-space, 1em); }`.
   You now have a website.
5. **Layer in enhancements only when needed.** A view transition. A container
   query. A dark‑mode toggle. Each one a deliberate addition, not a default.

If a feature can't be added at any of those five layers, ask whether it
belongs on the page at all.

---

## Sources

### Jim Nielsen — [blog.jim-nielsen.com](https://blog.jim-nielsen.com/)

1. [Out With the JS, In With the HTML](https://blog.jim-nielsen.com/2026/out-with-js-in-with-html/) (2026)
2. [Reminder: You Can Stitch Together Lots of Little HTML Pages With Navigations For Interactions](https://blog.jim-nielsen.com/2026/small-html-pages/) (2026)
3. [Collective Speed Is Not the Summation of Individual Speed](https://blog.jim-nielsen.com/2026/collective-speed-isnt-the-sum-of-individual-speed/) (2026)
4. [That's a Skill Issue](https://blog.jim-nielsen.com/2026/skill-issue/) (2026)
5. [Building Websites With LLMS (Lots of Little HTML Pages)](https://blog.jim-nielsen.com/2025/lots-of-little-html-pages/) (2025)
6. [Aspect Ratio in CSS View Transitions](https://blog.jim-nielsen.com/2025/aspect-ratio-in-css-view-transitions/) (2025)
7. [Sanding UI](https://blog.jim-nielsen.com/2024/sanding-ui/) (2024)
8. [Immeasurable Impact](https://blog.jim-nielsen.com/2024/immeasurable-impact/) (2024)
9. [You Are What You Read, Even If You Don't Always Remember It](https://blog.jim-nielsen.com/2024/you-are-what-you-read/) (2024)
10. [“We're All Just Temporarily Abled”](https://blog.jim-nielsen.com/2023/temporarily-abled/) (2023)
11. [CSS Is, In Fact, Awesome](https://blog.jim-nielsen.com/2021/css-is-in-fact-awesome/) (2021)

### Piccalilli — [piccalil.li](https://piccalil.li/)

1. [Three stoic principles for better web accessibility](https://piccalil.li/blog/three-stoic-principles-for-better-web-accessibility) (2026)
2. [The end of responsive images](https://piccalil.li/blog/the-end-of-responsive-images) (2026)
3. [Applying accessibility fixes with stealth for the greater good](https://piccalil.li/blog/applying-accessibility-fixes-with-stealth-for-the-greater-good) (2026)
4. [Building dynamic toggletips using anchored container queries](https://piccalil.li/blog/building-dynamic-toggletips-using-anchored-container-queries) (2026)
5. [A 2026 Piccalilli homepage redesign](https://piccalil.li/blog/a-2026-piccalilli-homepage-redesign) (2026)
6. [An in‑depth guide to customising lists with CSS](https://piccalil.li/blog/an-in-depth-guide-to-customising-lists-with-css)
7. [You might not need role="presentation"](https://piccalil.li/blog/you-might-not-need-rolepresentation)
8. [A (more) modern CSS reset](https://piccalil.li/blog/a-more-modern-css-reset/)
9. [CUBE CSS](https://piccalil.li/blog/cube-css/)
10. [It's about time I tried to explain what progressive enhancement actually is](https://piccalil.li/blog/its-about-time-i-tried-to-explain-what-progressive-enhancement-actually-is/)
11. [My favourite 3 lines of CSS — Andy Bell](https://andy-bell.co.uk/my-favourite-3-lines-of-css/)
12. [Build Excellent Websites](https://buildexcellentwebsit.es/) — Andy Bell
13. [The ideal viewport doesn't exist](https://viewports.fyi/) — Set Studio

### Manuel Matuzović — [matuzo.at](https://www.matuzo.at/blog/) (the third blog)

A blog “about web development, HTML, CSS, JavaScript, and web accessibility” —
Manuel's signature style is single‑column, system‑font, tight type, near‑zero
JavaScript, and pages that read identically with or without CSS. The site
itself is part of the manifesto.

1. [`box-shadow` is no alternative to `outline`](https://www.matuzo.at/blog/2026/box-shadow-no-alternative-to-outline) (2026)
2. [The geolocation element is odd](https://www.matuzo.at/blog/2026/geolocation-is-odd) (2026)
3. [Your skip link targets may not need `tabindex=-1`](https://www.matuzo.at/blog/2026/skip-links-tabindex) (2026)
4. [`role="presentation"` is no alternative for `aria-hidden="true"`](https://www.matuzo.at/blog/2026/role-presentation-no-alternative-for-aria-hidden) (2026)
5. [Put `aria-hidden="true"` on decorative SVGs](https://www.matuzo.at/blog/2026/put-aria-hidden-on-presentational-svgs) (2026)
6. [`aria-haspopup` might not do what you think it does](https://www.matuzo.at/blog/2026/aria-haspopup-menu) (2026)
7. [A new meta tag for respecting text scaling on mobile](https://www.matuzo.at/blog/2026/text-scaling-meta-tag) (2026)
8. [Introduction to the new HTML element `<geolocation>`](https://www.matuzo.at/blog/2026/geolocation-element) (2026)
9. [Lowering the specificity of multiple rules at once](https://www.matuzo.at/blog/2026/lowering-specificity-of-multiple-rules) (2026)
10. [Building the most inaccessible site possible with a perfect Lighthouse score](https://www.matuzo.at/blog/building-the-most-inaccessible-site-possible-with-a-perfect-lighthouse-score/) (2019, still required reading)

### Scientific & design‑research foundations

- **Bringhurst, R.** _The Elements of Typographic Style._ Hartley & Marks, 4th ed.,
  2012. — measure, leading, modular scales.
- **Tufte, E.** _The Visual Display of Quantitative Information._ Graphics Press,
  2nd ed., 2001. — data‑ink ratio; eliminating chartjunk.
- **Fitts, P. M.** _“The information capacity of the human motor system in
  controlling the amplitude of movement.”_ Journal of Experimental Psychology,
  1954. — target size and pointer distance (why hit‑targets are ≥ 44 px and why
  the gap between a label and a radio button should still be clickable, per
  Jim Nielsen's _Sanding UI_).
- **Hick, W. E.; Hyman, R.** Hick–Hyman Law, 1952/1953. — decision time scales
  with the log of the number of options; argues for short menus and few choices
  per screen.
- **Nielsen, J.; Pernice, K.** _“F‑Shaped Pattern of Reading on the Web”_
  (Nielsen Norman Group, 2006; reaffirmed 2017, 2020). — users scan; structure
  the page so the scan still surfaces the meaning.
- **Nielsen, J.** _“How Little Do Users Read?”_ NN/g, 2008. — average users
  read ≤ 20% of words on a page; design for skimmers as well as readers.
- **Dyson, M. C.** _“How physical text layout affects reading from screen.”_
  Behaviour & Information Technology, 2004. — line length, leading and
  comprehension on screen.
- **WCAG 2.2.** W3C Recommendation, October 2023. — the binding accessibility
  baseline this manifesto is calibrated against
  ([w3.org/TR/WCAG22](https://www.w3.org/TR/WCAG22/)).
- **WebAIM Million 2024.** [webaim.org/projects/million](https://webaim.org/projects/million/).
  — the empirical state of accessibility on the top million home pages;
  proves which of the principles above still need defending.
- **HTTP Archive Web Almanac (annual).** [almanac.httparchive.org](https://almanac.httparchive.org/).
  — the empirical state of CSS, HTML, JavaScript and accessibility on the
  public web.
- **Berners‑Lee, T.** _“The Rule of Least Power.”_ W3C TAG Finding, 2006. —
  prefer the least powerful tool that can express the meaning (declarative
  HTML > declarative CSS > imperative JS).
- **Keith, J.** _Resilient Web Design._ resilientwebdesign.com, 2016. — the
  intellectual foundation for everything in chapters 1–3.

---

## Coda

> _“Turns out, if you have a website and you think of the browser as a way to
> navigate documents — rather than a runtime to execute arbitrary code and
> fetch, compile, and present them — things can be a lot simpler than our
> tools often prime us to make them.”_
> — Jim Nielsen, [_Reminder: You Can Stitch Together Lots of Little HTML Pages_](https://blog.jim-nielsen.com/2026/small-html-pages/)

Make small pages. Set good type. Trust the browser. Sand the splinters. Ship.
