# Repository‑wide Agent Guidance

- **Dual purpose repo** – Contains a collection of OpenCode skill definitions under `.opencode/skills/` **and** a Next.js example application in `client/`. Identify which area you are working on before acting.
- **Running the example app** – In `client/` run `npm install` first, then use one of the scripts from `client/package.json`:
  - `npm run dev` starts the development server
  - `npm run build` produces a production build
  - `npm run start` runs the built app
  - `npm run lint` checks code style (ESLint v9)
- **Next.js version warning** – The client uses Next.js **16.2.4**, which has breaking API changes. Before editing any Next.js code, read the official docs in `client/node_modules/next/dist/docs/` (see `client/AGENTS.md`).
- **Do not edit `node_modules`** – Both the root and `client/` contain generated `node_modules` directories. Changes there will be overwritten and are irrelevant to the repository’s purpose.
- **Adding a new skill** – Place it under `.opencode/skills/<skill‑name>/` with a `SKILL.md` that starts with the YAML header:
  ```yaml
  ---
  name: <SkillName>
  description: <Brief description>
  ---
  ```
  Optionally add an `AGENTS.md` for that skill to capture special workflow notes.
- **Skill loading** – The repo is configured with the `superpowers` plugin (`opencode.json`). Load any required skill with the `skill` tool **before** performing actions that rely on it.
- **Task tracking** – For multi‑step work, create a todo list using the `todowrite` tool. Keep only one `in_progress` item at a time and mark tasks `completed` as soon as they finish.
- **Verification before claiming success** – Run appropriate checks before stating a task is finished, honoring the `verification-before-completion` skill. Example for client work:
  ```bash
  npm run lint && npm run build
  ```
  For skill work, run any provided test or lint command in that skill’s directory.
- **Git hygiene** – The repository is a Git worktree. Use non‑interactive Git commands (`git status`, `git add <files>`, `git commit -m "..."`). Do **not** amend existing commits unless explicitly requested.
- **Example sub‑skill projects** – Paddle‑webhooks examples live under `.opencode/skills/paddle-webhooks/examples/`. To experiment, `cd` into the example folder, run `npm install`, then execute the test suite (e.g., `npm test` if defined).
- **Avoid accidental broad edits** – When using `edit`, `replaceAll`, or `write`, target files within the relevant subdirectory (`client/` for UI work, `.opencode/skills/<name>/` for skill work). Do not modify unrelated parts of the repo.
- **Reference existing agent docs** – For Next.js specifics see `client/AGENTS.md`. For Redis‑development specifics see `.opencode/skills/redis-development/AGENTS.md`.
