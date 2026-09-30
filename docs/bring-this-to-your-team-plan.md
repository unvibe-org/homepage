# Plan: "Bring this to your team"

A homepage section for developers who want the workshop but cannot book it.
It gives them something to send their engineering manager, who can.

Background and evidence: `workshops/research/linkedin-to-lead-funnel.md`.
The booking call it leads to is planned in `docs/cta-change-plan.md`.

## Why

- Most visitors from LinkedIn are developers. The buyer is their engineering
  manager (`workshops/2-marketing/positioning.md` §4).
- The site gives a developer nothing to forward. They have to explain the
  workshop to their manager in their own words, or send a link to a page
  written for developers.
- Developer conferences solve the same problem with "Convince your boss"
  letters (SmashingConf, KubeCon).

## The assets

Both live in the workshops repo under
`2-marketing/channels/outreach/pitch-your-manager/` (PR unvibe-org/workshops#129).

| File | What it is |
|---|---|
| `one-pager.pdf` | Two A4 pages for the manager. Page one: what we run, price, takeaways, the Kliotzkin quote, logo strip, and the Cal.com link with `utm_medium=pdf`. Page two: the usual questions. Rendered from `one-pager.md` with `mise run render-docs` in that repo. |
| `en-email.md`, `de-email.md` | The email a developer sends their manager, with one bracket for their own reason. Links carry `utm_source=pitch-kit&utm_medium=email`. |
| `en-slack.md`, `de-slack.md` | The same for Slack or Teams. |

The one-pager states the price, from EUR 4,000 per workshop day for up to ten
engineers. This is the public price. The homepage keeps saying "get a quote" in
the core info section, so the price appears in one place only.

## What changes on the homepage

A short section after the example workshop, before the core info, written for
the developer. Two actions:

- **Download the one-pager.** The PDF, served from `public/public/` as
  `agentic-engineering-workshop.pdf`, the same way
  `agentic-engineering-guide.pdf` is served. It is a copy of the workshops
  file; repos do not link into each other. The kit README in the workshops repo
  says the copy must be refreshed after every render.
- **Send this to your manager.** A `mailto:` link with no recipient, and the
  subject and body from `en-email.md` URL-encoded. The bracket for the
  developer's own reason stays in the body as written, so they see where to
  type. The line "The one-pager is attached" changes to a link to the PDF on
  the site, because a mailto cannot attach a file. The German email is offered
  as a second, smaller link, "auf Deutsch".

Suggested copy, to be checked against `../workshops/WRITING.md` before it goes
in:

> **Want this for your team?**
> Your manager books the workshop, and most managers say yes to a day that
> comes with a plan. Send them the one-pager, or the email we wrote for you.
> [Download the one-pager] [Send this to your manager] auf Deutsch

Each action sends its own PostHog event, following the pattern of
`guide_downloaded` in `src/pages/guide/index.astro`:

| Action | Event | Property |
|---|---|---|
| Download the one-pager | `one_pager_downloaded` | `placement: "bring_to_team"` |
| Send this to your manager | `manager_email_opened` | `placement: "bring_to_team"`, `language: "en"` or `"de"` |

The privacy page's Analytics section lists both events next to the three that
exist.

## Order of work

1. Copy `one-pager.pdf` from the workshops repo to
   `public/public/agentic-engineering-workshop.pdf`.
2. Add the section to `src/pages/index.astro`, the two events in the page's
   script block, and the privacy page lines. One PR.
3. `npm run build` must pass. Screenshot the section on desktop and at phone
   width. The LinkedIn in-app browser opens links on phones first, so the
   phone view is the one that matters.
4. Open the mailto in a mail client and check that subject, body, line
   breaks, and the two links survive the encoding.
5. Confirm both events arrive in PostHog.

## Measuring it

- `one_pager_downloaded` and `manager_email_opened` in PostHog, split by
  `utm_source`.
- Cal.com bookings with `utm_medium=pdf`, which can only come from the sheet.
- Bookings whose "How did you hear about us?" answer names a colleague or a
  forwarded email.

## Open questions

- Whether the section also appears on the guide page, where a developer who
  downloaded the guide is already convinced.
- Whether the PDF should carry a version date in its footer, so an old copy
  forwarded months later is recognizable.
