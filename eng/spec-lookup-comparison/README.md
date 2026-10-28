# Spec lookup comparison

Scripts and tasks for the comparison in the [spec lookup analysis](../../docs/spec-lookup-analysis.md), section
6: how well an assistant answers Ed-Fi API lookup questions with no spec help (C0), with the keyword search MCP
server from archived PR #30 (C1), and with the [`ed-fi-api-spec`](../../skills/ed-fi-api-spec/SKILL.md) skill
(C2). Results are in [Spec lookup comparison: results](../../docs/spec-lookup-results.md).

Requires Python 3.9 or later, Git, and the assistant's CLI: Claude Code (`claude`) or the GitHub Copilot CLI
(`copilot`). C1 also needs Node.js. `make_review_sheet.py` needs `openpyxl`.

| File | Purpose |
|---|---|
| `tasks.json` | The 29 tasks with their expected answers: 18 original, 6 held-out and 5 synonym-sensitivity |
| `run_ab.py` | Runs the tasks headless, one fresh session per run, and records answers, tool calls and tokens |
| `judge.py` | First-pass correctness score for each run with the rubric (Claude Code) |
| `verify_names.py` | Counts identifiers in the answers that don't exist in the specification |
| `make_review_sheet.py` | Builds a blind spreadsheet for the second reviewer, and a key to map it back |
| `summarize.py` | Prints the result tables, applying the design's majority rule |

## Build the keyword search server (C1)

C1 uses the MCP server from archived PR #30 (commit `c9c748e`), which needs `better-sqlite3`:

```bash
git worktree add ../sdk-mcp-fts5 c9c748e
cd ../sdk-mcp-fts5
npm ci
npm run build
```

Pass its `dist/index.js` to `run_ab.py` with `--mcp-server`.

## Run the comparison

From the repository root, with the skills at the commit to test:

```bash
python eng/spec-lookup-comparison/run_ab.py --out results --mcp-server ../sdk-mcp-fts5/dist/index.js
```

- `--assistant copilot` runs the GitHub Copilot CLI instead of Claude Code. Skills go in `.github/skills`
  and the keyword search server is added with `--additional-mcp-config`. The CLI doesn't report tokens.
- `--skill-ref` takes the skills from another commit (default `HEAD`).
- Each run starts in a work folder that holds only the condition's skills. Tools that write files, run commands
  or search the web are disabled.
- For the task-condition pairs whose two runs disagree, run a third, for example:

  ```bash
  python eng/spec-lookup-comparison/run_ab.py --tasks Q09 --conditions C0 --runs 1 --first-run 3 \
    --out results/third-runs
  ```

## Score

1. First pass: `python eng/spec-lookup-comparison/judge.py results` writes `scores.jsonl`.
2. Manual review: check every score below 2 and every open-ended task, and save the final score of each run as
   `correctness_final` in `results/scores_final.json` (and `results/third-runs/scores_final.json`). The
   automated judge is a first pass only; it isn't stable on open-ended answers.
3. Invented names: download the Resources and Descriptors specifications used for the expected answers, then:

   ```bash
   python eng/spec-lookup-comparison/verify_names.py --resources resources.json --descriptors descriptors.json results
   ```

4. Second review: `python eng/spec-lookup-comparison/make_review_sheet.py results` writes
   `second-review.xlsx` for the second reviewer and `second-review-key.json`, which maps each row back to its
   condition and run. Share only the spreadsheet.
5. Tables: `python eng/spec-lookup-comparison/summarize.py results`.
