#  Homepage for unvibe.org

- *Tech Stack:* Astro (static output)

## Development Process
- Dev server: `npm run dev` → http://localhost:4321 (Astro, hot-reloads). Leave it running.
- After any code change, validate it YOURSELF before reporting done — don't ask the user to eyeball it:
  1. `npm run build` must pass.
  2. Screenshot the running page and actually look at it. For responsive / above-the-fold work, check specific viewport sizes.
- Screenshot method (in order of preference): Playwright MCP if configured → the `webapp-testing` skill → a one-off Playwright script in a venv.
- Don't commit or push unless asked.
