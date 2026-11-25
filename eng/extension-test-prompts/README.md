# Extension Builder test prompts

Runs the [Extension Builder test prompts](../../docs/skills/extension-builder-test-prompts.md) in Claude Code
or the GitHub Copilot CLI, headless, with and without the `ed-fi-extension-builder` skill. Results are in
[extension-builder-test-results.md](../../docs/skills/extension-builder-test-results.md).

## How it runs

- The prompts are read from the test prompts document, so it stays the only copy.
- Each condition gets a work folder with the files in [`fixtures/`](fixtures/) (the `BusRoutes` extension
  for T11) and, for the *with* condition, the skill taken from a git ref (`--skill-ref`, default `HEAD`).
- Each prompt runs in a fresh session with that folder as the working directory.
- The sessions are read-only: Claude Code denies file writes, shell and web tools; Copilot denies shell and
  write and excludes web fetch, web search and code search. Answers come from the model plus, when installed,
  the skill.
- User-level skills and instructions still load. Check that none of them is about Ed-Fi before running.

## Run

Python 3.12 or later, with `claude` and `copilot` on the `PATH` and signed in. From the repository root:

```bash
python eng/extension-test-prompts/run_prompts.py --out ../ext-runs --assistant claude
python eng/extension-test-prompts/run_prompts.py --out ../ext-runs-copilot --assistant copilot --model claude-sonnet-5.5
```

- `--tasks T4,T11` runs some prompts only; `--conditions with` runs one condition.
- `--extra-skills ed-fi-api-spec` installs other skills next to the extension builder in the *with* condition.
- Put `--out` outside the repository, so the sessions don't read the repository's files.
- Answers go to `<out>/<assistant>/<condition>/<task>.md`, with the model, skills, tools and files each run
  used; `<out>/runs.jsonl` has one line per run.

Score each answer against the expected outcomes by hand.
