# Plan: booking call instead of email

The homepage's main call to action becomes a 20-minute call booked through
Cal.com.

Background and evidence: `workshops/research/linkedin-to-lead-funnel.md`.
The path for developers who cannot book is planned in
`docs/bring-this-to-your-team-plan.md`.

## Why

- Every "Book a workshop" button opens an email to
  `dominik.grusemann@gmail.com`. Writing an email from scratch is a big step
  for a visitor who has only just heard of us.
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

### 4. Privacy page

- Section 5 ("External links") names Cal.com for booking calls and drops
  Luma, which the site no longer uses.

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

## Measuring it

- **Clicks:** the PostHog funnel "Homepage visit to booking click, by source"
  (https://eu.posthog.com/project/289357/insights/0ZNu5ycu).
- **Bookings:** Cal.com bookings of the `workshop` event type, with the
  answers to "How did you hear about us?".

## Open questions

- Should the booking go to Dominik alone, or rotate across instructors through
  a Cal.com team event?
