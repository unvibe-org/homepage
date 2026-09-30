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

## What it needs first

Two assets in the workshops repo, neither of which exists yet:

- **Manager message:** an email and a Slack message a developer sends to their
  manager, in English and German, in
  `2-marketing/channels/outreach/pitch-your-manager/`. The existing
  `team-forward-message/` goes the other way (manager to team) and stays as it
  is.
- **One-pager:** a one-page PDF for the manager covering the outcome, the
  format, the price range, and answers to the usual questions about security,
  data handling, and tools. Rendered with the `render-docs` skill.

## What changes on the homepage

A short section after the example workshop, with two actions:

- **Send this to your manager:** a `mailto:` link with the English manager
  email already filled in, subject and body, and no recipient. The German
  version sits in the one-pager.
- **Download the one-pager:** the PDF, served from `public/`.

Each action sends its own PostHog event with a `placement` property, following
the pattern of `guide_downloaded`:

| Action | Event |
|---|---|
| Send this to your manager | `manager_email_opened` |
| Download the one-pager | `one_pager_downloaded` |

The privacy page's Analytics section lists both events.

## Copy

All visible text follows the `unvibe-writing` skill in the workshops repo
(`workshops/.agents/skills/unvibe-writing/SKILL.md`). The section is written
for the developer; the email and the one-pager are written for the manager.

## Order of work

1. Write the manager message and the one-pager in the workshops repo.
2. Add the section, the two events, and the privacy page line in one PR.
   Build, check the section on desktop and at phone width, and confirm both
   events arrive in PostHog.

## Measuring it

- `manager_email_opened` and `one_pager_downloaded` in PostHog, split by
  `utm_source`.
- Bookings whose "How did you hear about us?" answer names a colleague or a
  forwarded email.

## Open questions

- Does the one-pager show a price range, and does the homepage repeat it?
- Does the section also appear on the guide page?
