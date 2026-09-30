#  Homepage for unvibe.org

- *Tech Stack:* Astro (static output)

## Writing
Every word on this site — headlines, body copy, FAQ answers, alt text, meta
descriptions — is governed by the unvibe writing guide. It lives in the **workshops**
repo, not this one:

- `workshops/.agents/skills/unvibe-writing/SKILL.md` (the `unvibe-writing` skill):
  sentence-level craft. Canonical for all prose.
- `workshops/2-marketing/positioning.md` §9: marketing voice and messaging. This site
  is a marketing asset, so where the two conflict, positioning wins.

Both are in a sibling checkout: from this repo,
`../workshops/.agents/skills/unvibe-writing/SKILL.md`.

**If you cannot read the `unvibe-writing` skill, do not write or edit copy.** Stop and tell
the user the guide is unreachable and where you looked. Do not work from memory, from
the voice of the surrounding copy, or from a summary of the guide in a previous
conversation — the guide is revised as writing gets rejected in review, so a
remembered version is a stale version. This applies to rewrites and small tweaks, not
just new sections. Code changes that touch no user-visible prose are unaffected.

## Development Process
- Dev server: `npm run dev` → http://localhost:4321 (Astro, hot-reloads). Leave it running.
- After any code change, validate it YOURSELF before reporting done — don't ask the user to eyeball it:
  1. `npm run build` must pass.
  2. Screenshot the running page and actually look at it. For responsive / above-the-fold work, check specific viewport sizes.
- Screenshot method (in order of preference): Playwright MCP if configured → the `webapp-testing` skill → a one-off Playwright script in a venv.
- Don't commit or push unless asked.
