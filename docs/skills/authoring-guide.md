# Authoring Agent Skills

How to write and change the skills in [`skills/`](../../skills/). Skills follow the
[Agent Skills](https://agentskills.io) format so that they work in Claude Code, GitHub Copilot, Codex,
Cursor and other harnesses without modification (PRD NFR-PORT-1).

## Layout

One folder per skill under `skills/`, named in kebab-case:

```text
skills/
  README.md                     # list of skills and how to install them
  <skill-name>/
    SKILL.md                    # entry file (required)
    references/                 # detail files, loaded only when needed
      <topic>.md
      rules.md                  # optional: index of numbered rules
      rules/<category>.md       # optional: one file per rule category
      examples/                 # optional: illustrative code
```

- `SKILL.md` starts with YAML front matter containing `name` (the folder name) and `description` (what the
  skill does and when to use it). Harnesses decide whether to load the skill from the description, so name
  the technologies and tasks it covers.
- Files outside a skill folder (such as this guide, test prompts and test results under `docs/skills/`) are
  not installed with the skill.

## Rules for skill content

### Keep the entry file concise

`SKILL.md` is loaded every time the skill is used (PRD NFR-TOK-1). Keep it to the essentials: what applies to
every task, and a routing table that tells the assistant which reference file to open for each situation.
Move everything else to `references/`.

### One topic per file

Each reference file covers one topic (authentication, push, pull, errors…), so the assistant loads only what
the task needs and each topic can be updated independently when the standard changes (PRD NFR-MNT-1). If a
file grows past roughly 100 lines, consider splitting it.

### Never include real credentials

Skills, examples and test prompts **must not contain real keys, secrets, tokens, or personal data** (PRD
NFR-SEC-1). Use placeholders (`YOUR_KEY`, `{id}`), example hosts (`api.example.org`) and fictitious records.
Guidance must recommend secure storage of client secrets and tokens.

### Be accurate and say when something is uncertain

Guidance must match normative Ed-Fi Alliance documentation (PRD NFR-ACC-1). Link to the source. Where the
documentation is ambiguous or a behavior differs between ODS/API 7.x and Ed-Fi API 8, say so explicitly
(NFR-COMP-1) instead of guessing.

### Stay language-neutral

Prefer rules, HTTP examples and pseudocode, so the assistant writes code in the developer's own language.
Language-specific code goes in `references/examples/`, clearly labeled as an illustration.

### Rules, if the skill has them

When a skill defines rules (see `ed-fi-api-client`), each rule has an ID, a level (*Required*,
*Preferred*, *Allowed but discouraged*), the reason, how to detect it in code, and version notes. Guides
reference rules by ID instead of repeating them.

## Formatting

- Markdown is linted in CI with [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2), using
  [`.markdownlint-cli2.jsonc`](../../.markdownlint-cli2.jsonc). Run it locally before opening a pull request:

  ```bash
  npm ci
  npm run lint:md
  ```

  The linter version is pinned in `package-lock.json` (with its integrity hash); update both together.
- Wrap prose at 110 characters (`.editorconfig`); the linter enforces it (MD013). Tables and code blocks
  are exempt.
- Use relative links between files of the same skill, so they work wherever the skill is installed.

## Testing

Each skill needs a documented set of test prompts with expected outcomes (PRD FR-REL-2), verified in at least
Claude Code and GitHub Copilot before the skill is considered done (FR-REL-1). Run each prompt in a fresh
session, with and without the skill installed, and record the results next to the prompts in `docs/skills/`.
