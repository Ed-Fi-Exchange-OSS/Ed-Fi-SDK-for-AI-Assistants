# Spec lookup comparison: results (Q-2)

- **Status:** Claude Code complete; GitHub Copilot pending; second review pending
- **Author:** Rafael Ceballos (Simpat Tech)
- **Addresses:** PRD FR-SPEC-3 and Q-2 (issue #47, DEVOPS-148)
- **Design:** [Spec lookup analysis](spec-lookup-analysis.md), section 6; run plan on issue #47
- **Feeds:** [ADR 0001](adr/0001-api-spec-similarity-search.md)

This document reports the comparison designed in the spec lookup analysis: how well an assistant answers Ed-Fi
API lookup questions with no spec help, with keyword search, and with the `ed-fi-api-spec` skill (option B).

## Summary

<!-- TODO: update with the GitHub Copilot results and the second review before merging. -->

- **Option B meets the decision rule, so it's adopted.** In Claude Code, the spec skill answered every task
  correctly (100%), tied with keyword search and ahead of no spec help (98%). It also reached 100% on the
  natural-language and held-out tasks, above the 80% threshold.
- **The model already knows Ed-Fi well.** Without any spec help it answered 98% of the tasks correctly, so
  correctness separates the setups only a little.
- **The spec skill was the most reliable.** It's the only setup whose two runs always agreed. Without spec help,
  or with keyword search, some answers used Data Standard 4 names (`parents`, `studentParentAssociations`).
  The spec skill had five times fewer invented names than no spec help.
- **Cost:** the spec skill used about 3× the tokens of no spec help, but about 20% fewer than keyword search,
  with fewer steps.

## Setup

| ID | Condition | What the assistant has |
|---|---|---|
| C0 | No spec help | The `ed-fi-api-client` skill only |
| C1 | Keyword search | C0 plus the FTS5 MCP server from archived PR #30 |
| C2 | Option B | C0 plus the `ed-fi-api-spec` skill |

C3 (embedding search) was not built: the decision rule only calls for it if C2 falls short.

- **Tasks:** 29, in three groups: the 18 original tasks, 6 held-out tasks and 5 synonym-sensitivity tasks
  (analysis section 6.2). Every prompt starts with "Ed-Fi API, Data Standard 5.2: ".
- **Expected answers** were verified against the Data Standard 5.2 specification. Tasks 1 and 3 ask for natural
  keys; their expected answers are field names, as the skill gives them since PR #62.
- **Skill version:** the spec skill with natural keys from PR #62 (`2e013ca`).
- **Claude Code:** version 2.1, headless, with its configured default model (Claude Sonnet). Each run is a fresh
  session. Tools that write files, run commands or search the web are disabled; reading files and fetching
  pages are allowed.
- **Runs:** two per task and condition (174), and a third for the 5 pairs whose two runs disagreed.
- **Scoring:** an automated first pass with the rubric (correctness 0–2), then a manual review of every answer
  scored below 2 and of every open-ended task. Invented names are counted by checking every identifier in
  backticks against the specification, because the automated judge's own counts were unreliable.
- **Second review:** Ana Gutierrez scores a blind sample of 30 answers: all those adjusted or scored below 2,
  plus a random sample.

<!-- TODO: add the second reviewer's agreement once the scores are back. -->

## Results: Claude Code

### Correctness

Score per task and condition, as in the design: when the two runs disagree, a third run decides by majority.

| Group | C0 No spec help | C1 Keyword search | C2 Option B |
|---|---|---|---|
| All 29 tasks | 57/58 (98%) | 58/58 (100%) | **58/58 (100%)** |
| Original 18 | 36/36 (100%) | 36/36 (100%) | 36/36 (100%) |
| Original, natural language (10) | 20/20 (100%) | 20/20 (100%) | 20/20 (100%) |
| Held-out 6 | 12/12 (100%) | 12/12 (100%) | 12/12 (100%) |
| Synonym sensitivity 5 | 9/10 (90%) | 10/10 (100%) | 10/10 (100%) |

By task kind:

| Kind | C0 | C1 | C2 |
|---|---|---|---|
| Exact name (4) | 8/8 | 8/8 | 8/8 |
| Natural language (19) | 37/38 | 38/38 | 38/38 |
| Field mapping (1) | 2/2 | 2/2 | 2/2 |
| Descriptor (3) | 6/6 | 6/6 | 6/6 |
| Reference (2) | 4/4 | 4/4 | 4/4 |

Every answer, before the majority rule, which shows how consistent each setup is:

| Group | C0 | C1 | C2 |
|---|---|---|---|
| All 29 tasks | 112/116 (97%) | 114/116 (98%) | **116/116 (100%)** |
| Original, natural language (10) | 38/40 (95%) | 38/40 (95%) | 40/40 (100%) |
| Held-out 6 | 24/24 (100%) | 24/24 (100%) | 24/24 (100%) |
| Synonym sensitivity 5 | 19/20 (95%) | 20/20 (100%) | 20/20 (100%) |

Answers below 2:

- **Task 9 (link a student to a parent):** one run without spec help and one with keyword search answered with
  the Data Standard 4 resource `studentParentAssociations`. The keyword search run said the rename to
  `contact` comes in Data Standard 6. The third runs of both answered `studentContactAssociations`.
- **Task 15 (map `sch_id`):** one run without spec help hedged instead of answering `schoolId`.
- **H10 (a parent's phone and email):** two of three runs without spec help put them on `parents`, the Data
  Standard 4 name, instead of `contacts`.

### Invented names

Identifiers in backticks that don't exist in the Data Standard 5.2 specification. This is an upper bound: it
includes Data Standard 4 names that an answer flags as older, and a few false positives such as
`dataManagementApi`.

| | C0 | C1 | C2 |
|---|---|---|---|
| Unknown identifiers | 30 of 656 | 15 of 702 | **6 of 914** |
| Runs with any | 19/58 | 8/58 | **4/58** |

### Cost and steps

| | C0 | C1 | C2 |
|---|---|---|---|
| Runs that used a tool | 4/58 | 49/58 | 58/58 |
| Input tokens per task (average, cumulative) | ~38 K | ~150 K | ~121 K |
| Steps per task (average) | 0.2 | 4.7 | 3.2 |

## Results: GitHub Copilot

<!-- TODO: GitHub Copilot CLI run (same design: 29 tasks, C0/C1/C2, two runs each). -->

Pending. The run uses the GitHub Copilot CLI in headless mode, with the skills in `.github/skills` and the
keyword search server added as an MCP server. The CLI doesn't report tokens, so cost is compared by steps only.

## Decision

The decision rule (analysis section 6.5) adopts B when C2 scores at least as well as C0 and C1 overall and
reaches at least 80% on the natural-language tasks, also on the held-out tasks:

- C2 scored 100% overall, tied with C1 and ahead of C0 (98%).
- C2 scored 100% on the natural-language tasks and 100% on the held-out tasks.

**B is adopted**, and recorded in [ADR 0001](adr/0001-api-spec-similarity-search.md). C3 (embedding search) is
not needed for this release.

What the scores don't show on their own:

- **Ceiling effect.** The model answers most of these tasks from memory, so this task set can't show a large
  correctness gain. The gains show up as consistency between runs, fewer Data Standard 4 names and fewer
  invented names, and answers that cite the specification instead of hedging.
- **Harder lookups.** Tasks about lesser-known resources, extensions or a host's own specification would
  likely separate the setups more, since the model can't answer those from memory.
