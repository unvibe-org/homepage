# Plan: booking call instead of email

The homepage's main call to action becomes a 20-minute call booked through
Cal.com. A second path, "Bring this to your team", lets a developer who cannot
book pass the workshop on to their engineering manager.

Background and evidence: `workshops/research/linkedin-to-lead-funnel.md`.

## Why

- Every "Book a workshop" button opens an email to
  `dominik.grusemann@gmail.com`. Writing an email from scratch is a big step
  for a visitor who has only just heard of us.
- Most visitors from LinkedIn are developers. The buyer is their engineering
  manager, and the site gives the developer nothing to forward.
- A booked call is a clear conversion we can count. An email opened in a mail
  app is invisible to us after the click.

## What changes

### 1. Cal.com event type for the call

Create a dedicated event type through the Cal.com MCP server. The existing
`20min` event type is generic and requires manual confirmation, which slows a
first contact down.

| Setting | Value |
|---|---|
| Title | Workshop for your team |
| Slug | `workshop` |
| Length | 20 minutes |
| Location | Cal Video |
| Confirmation | Not required |
| Minimum notice | 2 hours (same as the other event types) |
| Description | What the call covers: team size, dates, what the team works on, and what a workshop day looks like |

Booking fields, in addition to name and email:

| Field | Required | Why |
|---|---|---|
| Company | Yes | We sell to companies. |
| Team size | No | Scopes the quote. |
| How did you hear about us? | No | Catches what analytics cannot see: a forwarded email, a Slack message, a colleague. Free text. |

Booking URL: `https://cal.com/dominik1001/workshop`.

### 2. Buttons point to Cal.com

- `bookMailto` in `src/pages/index.astro` becomes `bookingUrl`, the Cal.com
  link. The header CTA (`Header.astro`) uses the same value.
- The four buttons keep their `data-booking-placement` attributes, so the
  PostHog event `workshop_booking_initiated` and the saved funnel keep working
  without changes.
- The link opens in the same tab. LinkedIn's in-app browser handles new tabs
  poorly.
- The visitor's UTM parameters are appended to the Cal.com link, so a booking
  carries its source. Check on a test booking that Cal.com stores them; if it
  does not, the "How did you hear about us?" field is the fallback.
- We link to Cal.com and do not embed its booking widget. An embed loads a
  third-party script on our page, and we have not checked what it stores in
  the browser. A plain link keeps the site free of a consent banner.

### 3. FAQ and fallback

- "How do we book?" names the call first and keeps the email address as the
  alternative for visitors who prefer to write.
- The footer "Contact" link stays an email link.

### 4. "Bring this to your team" section

This depends on two assets in the workshops repo that do not exist yet:

- an email and a Slack message a developer sends to their manager
  (`2-marketing/channels/outreach/pitch-your-manager/`, English and German)
- a one-page PDF for the manager: outcome, format, price range, and answers to
  questions about security, data handling, and tools

Once they exist, the homepage gets a short section after the example workshop
with two actions:

- **Send this to your manager**: a `mailto:` with the developer-to-manager
  email already filled in, subject and body, and no recipient.
- **Download the one-pager**: the PDF, served from `public/`.

Each action sends its own PostHog event (`manager_email_opened`,
`one_pager_downloaded`) with a `placement` property, following the pattern of
`guide_downloaded`.

### 5. Privacy page

- Section 5 ("External links") names Cal.com for booking calls and drops
  Luma, which the site no longer uses.
- Section 4 ("Analytics") lists the new events once "Bring this to your team"
  ships.

## Copy

All visible text follows the `unvibe-writing` skill in the workshops repo
(`workshops/.agents/skills/unvibe-writing/SKILL.md`). The button label stays
"Book a workshop →" unless testing shows the call needs saying. Under the hero
button, a short line can set the expectation, for example "A 20-minute call
to scope the day for your team."

## Order of work

1. Create the Cal.com event type and make a test booking.
2. Switch the buttons, FAQ, and privacy page in one PR. Build, check the four
   buttons and the header on desktop and at phone width, and confirm in
   PostHog that `workshop_booking_initiated` still arrives.
3. Write the manager kit and one-pager in the workshops repo.
4. Add the "Bring this to your team" section in a second PR.

## Measuring it

- **Clicks:** the PostHog funnel "Homepage visit to booking click, by source"
  (https://eu.posthog.com/project/289357/insights/0ZNu5ycu).
- **Bookings:** Cal.com bookings of the `workshop` event type, with the
  answers to "How did you hear about us?".
- **Forwarding:** `manager_email_opened` and `one_pager_downloaded` in PostHog, once
  "Bring this to your team" ships.

## Open questions

- Should the booking go to Dominik alone, or rotate across instructors through
  a Cal.com team event?
- Does the site show a price range, or does it stay on the one-pager only?
