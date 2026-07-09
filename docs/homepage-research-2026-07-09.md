# Homepage research report — buyer, market, copy

**Date:** 2026-07-09 · **Branch:** `corporate-positioning` · **Scope:** `src/pages/index.astro` (+ `/guide/`)

Method: 19 research agents across six lenses (buyer psychology, buying process, competitors, proof points, AI-copy tropes, dev-audience copywriting) plus a three-persona critique of the current page. Every statistic below marked **✓** was independently fact-checked against its primary source; one widely-circulated stat was refuted and is listed in "do not use."

---

## Executive summary

The offer is right and the page's bones are good — the terminal aesthetic, the honest social-proof framing, the Infineon quote, and the practitioner bios are genuinely strong assets. Five things hold it back:

1. **The conversion path undermines everything above it.** The sole CTA is `mailto:dominik.grusemann@gmail.com` — a personal Gmail for a quote-based corporate offer. Research says instant call-booking converts ~2x vs. email-and-wait, and DACH buyers expect a named-human + structured-intake flow.
2. **The page still sells the meetup.** The 12:00–17:00 "Networking + beers" agenda, the hero Date/Time/Venue block, the "side projects" audience line, and the sponsor grid are public-event leftovers that contradict the private-workshop promise.
3. **It sells adoption; the 2026 buyer is buying accountability.** They already bought the licenses. Their board asks "are we seeing returns?" and 86% of engineering leaders can't answer. The pitch that matches the moment: *make the AI spend you already committed pay off, without the quality decay.*
4. **The strongest proof asset in the category is buried.** No competitor we found publishes a measurable customer outcome. "His team migrated hundreds of repos" from a named Director of Engineering at Infineon is arguably the best proof point in the European market — and it sits fifth on the page.
5. **The copy has an AI-tell density problem** — fatal irony for this brand. "Practitioners, not academics.", "Two workshops. One discipline.", ~10 em dashes, symmetric card grids. The audience (engineers whose trust in AI output is at an all-time low) judges pattern *density*, and the current page is over the threshold.

**This week:** set up `hello@unvibe.org` + a Cal.com scheduler; replace the meetup agenda; move the Infineon quote up; swap the vaporware secondary CTA for the guide; run the copy through the linter in §5.

---

## 1. The buyer

An EM / Director / CTO, mid-size company, DACH-first. Their 2026 situation, per fact-checked sources:

**Under board pressure to show ROI, not to adopt.**
- ✓ Gartner 2026 CIO survey (n=2,501): 64% of tech execs plan to deploy agentic AI within 24 months; only ~17% have deployed agents to date. Gartner's own framing: "2025 was about AI pilots… 2026 will be about delivering agentic AI ROI."
- ✓ DX research (Laura Tacho): measured productivity gains plateaued around 10% (~3.6–4 hrs/week), flat since Q2 2025. Best-in-class large orgs cap out around **60% weekly habitual usage** of AI coding tools; one 500-person org saw only 45% weekly opens. DX survey of 50 engineering budget holders: ~$1,000/dev/year is the common AI budget target, **86% are uncertain which AI tools are providing benefit**, 40% lack the data to build an ROI story.

**Sitting on top of a trust crisis among their own engineers.**
- ✓ Stack Overflow 2025 (n≈49k): 84% use or plan to use AI tools (up from 76%) — but 46% actively distrust output accuracy vs 33% who trust it; 3% highly trust. #1 frustration (66%): AI solutions that are "almost right, but not quite." 45% say debugging AI code takes longer.
- ✓ DORA 2025 (n≈5,000): 90% adoption, median 2 hrs/day of AI use, only 24% trust the output "a lot"/"a great deal." Throughput now correlates *positively* with AI adoption but instability *still rises* — DORA's words: "AI is an amplifier. It magnifies the strengths of high-performing organizations and the dysfunctions of struggling ones." Also DORA's phrase: time saved generating is "re-allocated to **verification overhead**."
- ✓ METR RCT (Jul 2025): 16 experienced OSS devs, 246 real tasks on their own mature repos — **19% slower with AI, while estimating they'd been ~20% faster**. Feb 2026 update: after fixing selection bias, the newer cohort measured −4% (CI −15%…+9%). This is the study every skeptical staff engineer quotes; knowing about the *revision* is a credibility flex.

**Has already watched mandates backfire.**
- ✓ Writer/Workplace Intelligence (Mar 2025): 75% of C-suite thought their AI rollout succeeded vs 45% of employees; 42% of C-suite said AI adoption is "tearing their company apart" (54% in the 2026 follow-up). LeadDev documents AI-code-volume leaderboards breeding resentment; the cited success (ChargeLab, ~40% gain) came from letting engineers choose tools plus real enablement.

**Personally exhausted by exactly this topic.**
- ✓ LeadDev Engineering Leadership Report 2026 (n=600): CTOs reporting weekly emotional drain jumped **24% → 54%** in one year; 41% say their team is less motivated than 12 months ago; a third of managers are considering going back to IC; **84% believe AI makes it harder for juniors to enter and grow** — which makes upskilling existing staff the fallback strategy.

**Watching the codebase decay.**
- ✓ GitClear (211M changed lines, 2020–2024): duplicated blocks (5+ lines) up 8x in 2024; moved/refactored lines down 24.1% → 9.5%; copy/paste exceeded refactoring for the first time. The 2026 follow-up (623M changes) is starker: refactoring 21% (2022) → 3.8%, duplication +81%. (Caveat: GitClear sells code analytics; correlational, not causal — cite as "longitudinal data on 600M+ code changes.")
- ✓ Veracode 2025 (reconfirmed Spring 2026): 45% of AI-generated code samples failed security tests; **newer/larger models were no better** — the fix is review discipline, not the next model. Strong with DACH security sensitivity.

**The format we sell has third-party validation from inside Microsoft.**
- ✓ arXiv 2607.01418 (Jul 2026, Microsoft's Claude Code / Copilot CLI rollout, tens of thousands of engineers): the strongest adoption driver was **peer visibility** — +216% odds when >25% of skip-level peers used the tools, +82% when the manager did. Seniors adopted *more* than juniors. Engineers using agents 5+ days/week merged +50% more PRs. Microsoft's own internal enablement format was literally a hands-on **"Agentic Engineering Day."** A 20-engineer workshop manufactures exactly that peer-visibility critical mass in one day — nobody markets it that way.

**DACH-specific levers no US competitor can pull.**
- ✓ EU AI Act Article 4: role-specific AI-literacy measures have been mandatory for deployers since 2 Feb 2025; **national enforcement begins early August 2026** — weeks from now. The Commission FAQ says relying on tool documentation is likely "ineffective and insufficient"; internal training records are the recommended evidence. A documented engineer-specific workshop plausibly contributes to compliance → a second budget line.
- ✓ Works councils: §87(1)(6) BetrVG gives the Betriebsrat co-determination over AI coding tools whose usage data the employer can access. Practitioner guidance: 6–12 weeks negotiation *with* a prepared draft. "Training, not surveillance — no individual usage data, no leaderboards" is a load-bearing line for German buyers.
- ✓ Bitkom (Sept 2025): top German AI-adoption barriers are legal uncertainty (53%) and **lack of technical know-how (53%)**. Pragmatic Engineer 2026: EU orgs "want to see clear value-add" before approving even $30–50/month per-engineer spend — a bounded, quote-based, one-day engagement fits EU procurement psychology far better than another subscription.

**Implication for the page voice:** speak to a tired, skeptical buyer who will forward the link to an even more skeptical staff engineer. The top third of the page answers the buyer (outcome, proof, logistics, next step); the middle answers the forwarded engineer (real agenda, real tools, what happens to our codebase). Every hype adjective removed is protection for the champion who has to defend this purchase internally.

---

## 2. The market

We are not early, even locally. Mid-2026 DACH landscape:

| Competitor | Offer | Price signal | Weakness to exploit |
|---|---|---|---|
| **instructa.ai** (Kevin Kern, Vienna) | Agentic coding workshop, remote, 2 half-days | €6,850 / 5 seats + €850/seat ⇒ **~€19.6k for 20** | Remote-only, not own-codebase-first |
| **Pexon Consulting** (Grünwald — Munich suburb) | 3-day Claude Code Schulung, 10–15 devs | from €7,500 | Claude-only, 3 days off the roadmap, zero testimonials, consultant-taught. Claims to be "the only German-language Claude Code training in DACH" — directly contestable |
| **EclipseSource** (Munich) | "AI Coding Training" — async course + guided adoption | €199/person; from €2,900/team | Course-first, anchors cheap; same "systematic discipline" language as us |
| **Zartis** (Anthropic Preferred Partner) | Claude Code workshops, up to 40 people | quote | 40-person sessions dilute hands-on depth; Claude-branded; staff-aug upsell |
| **claudeworkshop.com / codexworkshop.com** | Bespoke own-codebase workshops (two Claude ambassadors) | quote | Side-business feel, no outcomes, per-tool split concedes tool-agnosticism; but they own the English SERPs |
| **INNOQ, GFU, workshops.de, cmt, NobleProg** | 2–5-day catalog seminars (€1,349–2,030/person) | public | Fixed curricula on sample projects, trainer-not-practitioner |
| **Matt Pocock (AI Hero)** | "Claude Code for Real Engineers" — B2C async cohorts | per-seat | Owns the anti-vibe-coding narrative for *individuals*; not own-codebase, not team-level |
| **Anthropic + SIs** (PwC, Accenture, Deloitte) | Free/bundled enablement at 30k–470k-person scale | bundled | Captures Fortune-500; structurally ignores DACH mid-market |

**The unoccupied intersection** (no competitor found combines more than two): one day · your codebase · tool-agnostic (Claude Code *and* Codex) · German or English · practitioner-founders · named enterprise outcome.

**Proof standard in the category is remarkably low** — vague praise quotes, anonymous stars, borrowed stats. The Infineon Director-of-Engineering quote with "migrated hundreds of repos" is arguably the strongest proof point on any European competitor page. Lead with it.

**Pricing guidance:** comparables support quoting **€8–18k** for a one-day 20-engineer workshop; below ~€5k underprices the AI-specialist tier. Keep quote-based (the norm at the premium end — hidden pricing generates *more* form fills at lower quality, and gating is defensible at this ticket size) but **publish the model**: flat per-workshop, up to 20 engineers, no per-seat licensing, on-site or remote. Optional anchor: "typically less than public-course tickets for the same team" (€1,349–1,679/person at other providers). German context: companies already spend ~€1,347/employee/year on Weiterbildung (IW 2024) — this is inside normal budget. And say "AI enablement," not "training/Weiterbildung": the same purchase gets cut as training and approved as AI initiative.

**Cheap wins:** the Claude Partner Network badge is free (Zartis brandishes it); German-language delivery breaks Pexon's exclusivity claim with one sentence; German SEO pages ("Claude Code Schulung", "KI-Coding Workshop inhouse") face weak competition.

**Positioning warning:** don't lean on the vibe-coding slogan for differentiation — Pocock and EclipseSource already occupy that ground. Attach the frame to *team-level* outcomes (shared conventions, review discipline, rollout) that no B2C course delivers.

---

## 3. Conversion mechanics

1. **Replace the Gmail mailto everywhere** (`index.astro:15`, FAQ answer) with `hello@unvibe.org`. A personal Gmail on a corporate quote-based offer reads "side project."
2. **Primary CTA → "Book an intro call"** with an embedded scheduler (Cal.com). Chili Piper's benchmark of 4M B2B form fills: instant booking converts 66.7% of interest to meetings vs ~30% for email-and-wait; average B2B response lag is 42 hours; 78% of buyers go with the first responder. Keep a plain-text email as the secondary path for procurement-minded buyers. Relabel from "Book a workshop" (nothing can be booked; the click starts a scoping exchange) to something honest: "Get a quote" / "Book an intro call."
3. **Add a 3-step "How it works" strip** — the market-standard DACH flow: ① 30-min scoping call → ② fixed quote (Angebot) within 48h → ③ workshop on-site or remote, **invoice after delivery**. GFU leads with "Keine Vorkasse" — in Germany these are conversion features, not fine print.
4. **Procurement strip:** Angebot & PO accepted · German VAT invoice after delivery · German or English · on-site or remote · we sign your NDA.
5. **New FAQ items** (the ones a DACH buyer must have answered before emailing): confidentiality/NDA + "work happens on your machines"; German or English; more than 20 engineers (multiple cohorts); what happens after I get in touch (response time, process); works-council friendliness (training, no individual usage data); and the two killer objections — *why not let engineers self-learn* and *why not Anthropic's own enablement* (answer: tool-agnostic discipline on your actual codebase, from practitioners who ship — not vendor onboarding).
6. **Secondary CTA → the guide.** The hero and final-CTA second slots currently promote a waitlist for a product that doesn't exist. Point them at the free 33-page guide instead — the low-commitment path for the 95% not ready to email. Keep the Advanced waitlist inside its course tab.
7. **Fix the guide page's job.** The PDF is ungated *and* disconnected from the email form, and the workshop gets one 12px footer link. Either soft-gate ("we'll email you the link + future editions") or keep it ungated as a trust play — but then add a real workshop cross-sell block: "The guide is the theory. The workshop is your team doing it on your codebase, with us alongside."
8. **Make a forwardable one-pager (PDF):** agenda, outcomes, logistics, pricing model. The champion needs an artifact to circulate to their boss — distinct from the 33-page guide.
9. **List the leave-behind artifacts** — solo competitors have trained buyers to expect this: a CLAUDE.md tailored to your repos, agent-ready conventions, a review workflow for AI-speed PRs, a rollout plan for the next sprint. "What your team has on Monday morning."
10. **Add a "what you report upward" block for the buyer:** documented AI-literacy evidence (Article 4), shared team conventions, an adoption playbook, before/after workflow. 84% of eng leaders say productivity is a top management priority; only 46% can measure AI impact — sell the defensible story, not vague enablement.

---

## 4. Proof points — use / handle with care / do not use

**Safe to cite (fact-checked, with attribution inline — this audience right-click-searches numbers):**

| Stat | Source | Use for |
|---|---|---|
| "AI is an amplifier" — throughput ↑ *and* instability ↑; verification overhead | DORA 2025 (Google) | The thesis, in the most EM-trusted voice |
| 84% use AI; 46% distrust output; 66% "almost right, but not quite" | Stack Overflow 2025 | Engineers' felt pain, their words |
| Felt 20% faster, measured 19% slower (n=16; Feb 2026 revision → −4%) | METR RCT | Perception gap; cite the *debate*, incl. revision |
| Refactoring 21% → 3.8% of changed lines; duplication +81% | GitClear 2026 | The codebase shows the decay |
| 45% of AI-generated code fails security tests; newer models no better | Veracode 2025/26 | DACH security anxiety; why review discipline |
| Peer visibility +216% adoption; Microsoft ran an internal "Agentic Engineering Day" | arXiv 2607.01418 | Third-party validation of our exact format |
| 64% plan agentic AI in 24 months; ~17% deployed; "2026 is about ROI" | Gartner 2026 CIO survey | Board-pressure framing |
| 75% of C-suite vs 45% of employees think the rollout worked | Writer 2025 | Mandates backfire; enablement works |
| Art. 4 AI-literacy duty; enforcement from early Aug 2026 | EU AI Act / EC FAQ | Compliance budget line, urgency |
| ~60% weekly-usage ceiling; 86% of leaders can't tell which tools deliver | DX | The sunk-license pain |

**Handle with care:** MIT NANDA "95% of GenAI pilots fail" (methodologically criticized; if used at all, say "MIT researchers" and use only its external-partner-success angle) · McKinsey "57% vs 20% invested in hands-on workshops" (found only in secondary aggregators — verify the primary before printing) · Atlassian/Jellyfish/Harness figures (vendor reports; directional).

**Do not use:** GitHub's "55% faster" (2022, one toy task, n≤95, the most-misquoted stat in the space — being ready to *counter* it is a credibility asset) · "~30% of AI seats sit idle / $108k wasted per 1,000 users" (**refuted in our fact-check** — appears in neither cited source) · DORA 2024's negative throughput finding (obsolete; 2025 flipped it) · "16% of Copilot pilots convert" as a coding-tools stat (it's about M365 Copilot).

---

## 5. Sounding human — the copy linter

Why it matters more for us than anyone: perceived AI authorship carries a measured trust penalty (31% trust a brand less vs 7% more — Klaviyo/Datalily; the NIM study showing AI labels depress purchase intent is literally German). Our attendees are the most AI-cynical population measured. And an AI-coding company with AI-sounding copy is the "almost right, but not quite" failure they already resent. Detection is *cumulative*: one marker is nothing; two-three per screen flips the reader from reading to sneering.

**DON'T (flag in every draft):**
- Words: delve, seamless, robust, leverage, elevate, landscape, unlock, empower, supercharge, transformative, cutting-edge, journey, pivotal, crucial, foster, showcase, boasts, meticulous, game-changer
- Constructions: "it's not X, it's Y" / "X, not Y" / "isn't just" (the #1 live tell as of late 2025, ahead of the em dash); "serves as"/"stands as" for "is"; trailing "-ing" significance clauses ("…ensuring", "…highlighting the importance of")
- Structure: >1 em dash per screen; >1 rule-of-three per page; identical-length sentences; symmetric card grids of punchy one-liners; Title Case headings; bold-term-colon bullets; emoji bullets; "In today's…", "But here's the thing", "Stay tuned", "Let's dive in"
- The meta-test: if a paragraph's point can't be restated concretely, or a competitor could paste it onto their site unchanged, cut it.

**DO (the positive signals):**
- Named specifics over adjectives: "15 engineers, Munich, May 2026" · "Infineon, BSH, QPLIX, CoCrafter" · "hundreds of repos" · "33 pages" · "Claude Code and Codex"
- First person with a stance someone could disagree with: "We think unreviewed AI PRs are debt. We've paid that debt ourselves."
- Plain verbs (is/has/does), varied sentence length, one deliberately long section next to a two-line one
- One human rough edge per section: an admitted limitation ("remote works; on-site is better"), an opinionated aside, an unevenly long FAQ answer
- The Fly.io editing rule: write it like an HN comment under your real name, then shorten the sentences.

**Current page audit (the density is the problem, not any single item):**
- "Practitioners, not academics." — textbook "X, not Y." → "The people teaching it ship code for a living." (the bios carry the proof)
- "Two workshops. One discipline." — paired-fragment cadence, and half-false (one is vaporware). → "The workshops." or "What we teach."
- ~10 em dashes in visible copy, several doing the "setup — twist" move. Cut to 2–3 page-wide. (The Infineon testimonial comment records the customer asking for em dashes to be removed "so it reads like a real quote" — the surrounding page fails the same test.)
- "actually" ×2 as load-bearing intensifier ("skills that actually work", "agents you can actually trust") — drop both.
- The four why-cards: uniform h3 + one-liner grid = the flagged symmetric rhythm. Keep the substance (it's good, real pain, real language), vary the shapes and lengths.
- "Stay in the loop." — filler cliché.
- Keep exactly one deliberate punchy fragment. "Done vibe coding? Train your team." is the strongest and most on-brand — let it be the only one.
- Rule for the rewrite: never ship an unedited model draft; run the grep list; read aloud once for metronomic rhythm.

---

## 6. Section-by-section action plan (`index.astro`)

**Critical**
1. `:15`, `:503` — Gmail mailto → `hello@unvibe.org` + scheduler as primary CTA (§3.1–2).
2. `:146-161` — meetup agenda (12:00 start, "Networking + beers") → sample full-day corporate agenda: "09:30 Foundations & setup on your stack → hands-on on your codebase, instructors alongside → 16:00 wrap-up: what your team adopts on Monday. (Sample — we tailor timing.)"

**Major**
3. `:59-74`, `:110` — hero Date/Time/Venue block reads as a fixed public event under a private-workshop CTA. Remove from hero, or reframe: "Next open session: {date} · {venue} — or book a private day for your team."
4. `:44-51` — hero: put the positioning where the name pays off. H1: "From vibe coding to agentic engineering." Sub: "A one-day hands-on workshop for up to 20 of your engineers, on your codebase, with Claude Code or Codex. On-site or remote, German or English." Specific and falsifiable beats category-generic.
5. `:54-57`, `:592-595` — secondary CTA slots → "Get the free guide →" (§3.6).
6. `:284-309` — audience section addresses the attendee ("side projects" is a B2C leftover) and contradicts the FAQ on prerequisites. Reframe as "Who to send" for the buyer; fix the contradiction ("prior agent experience helps but isn't required").
7. `:249-281` — #why diagnoses engineer pain but never gives the buyer their board sentence. Add the outcomes/artifacts block (§3.9–10): concrete leave-behinds beat productivity-percentage claims we can't back.
8. `:410-455` — move the Infineon quote up (after hero or after #courses); singular header ("From the first edition"); consider pulling "we used it to migrate hundreds of repos" + name/title into the hero as the proof line.
9. `:458-511` — add the six missing FAQ items (§3.5).
10. Guide page — lead capture / workshop cross-sell (§3.7).

**Minor**
11. `:560-577` — "Backed by builders" sponsor grid = founders' own companies presented as backers. Cut, or relabel truthfully ("Partners who supported our first open session") and move below #updates.
12. `:98`, `:314`, `:587` + em dashes + "actually" ×2 — copy linter pass (§5).
13. `:210-214` — "Waitlist members get launch pricing" is incoherent for a quote-based product; reword for the buyer ("we'll contact you first when team dates open").
14. CTA labels — "Book a workshop" over-promises a mailto; "Get a quote →" matches the pricing row; put the plain-text email next to the button.

**Keep (do not lose in the rewrite):** the terminal aesthetic and shell-prompt motifs; "Engineers from teams at" nominative honesty; the consented-verbatim Infineon quote; instructor bios that prove with nouns (Databricks, Twitter, BMW, acquired startup); the disqualifying "Not for you if" mechanic; the concrete FAQ answers (named tools, Cursor caveat, 20-cap rationale); the GDPR-conscious details (EU-based MailerLite, privacy links) — buyer-visible compliance signaling that costs nothing.

---

## Sources (primary)

DORA 2025: dora.dev/research/2025 · METR: metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study (+ 2026-02-24 uplift update) · Stack Overflow 2025: survey.stackoverflow.co/2025/ai · GitClear: gitclear.com/the_ai_code_quality_maintainability_gap · Veracode: veracode.com 2025 GenAI Code Security Report · Microsoft rollout study: arxiv.org/abs/2607.01418 · Gartner 2026 CIO Agenda: gartner.com/en/articles/cio-agenda · LeadDev ELR 2026: leaddev.com/the-engineering-leadership-report-2026 · Writer survey via leaddev.com/ai/ai-coding-mandates-are-driving-developers-to-the-brink · EU AI Act Art. 4 FAQ: digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers · Bitkom Sept 2025 · DX: getdx.com · Chili Piper form benchmark · Evil Martians devtool-landing-page study · Wikipedia: Signs of AI writing · instructa.ai, pexon-consulting.de, eclipsesource.com, zartis.com, workshops.de, gfu.net (competitor pricing pages, retrieved 2026-07-09)
