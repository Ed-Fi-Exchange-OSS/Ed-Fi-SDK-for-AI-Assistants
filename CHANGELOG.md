# Changelog

Notable changes to the Ed-Fi SDK for AI Assistants. Versions follow the Ed-Fi
[software versioning](https://docs.ed-fi.org/community/sdlc/code-contribution-guidelines/software-versioning)
guidelines (`x.y.z`).

## Unreleased

### Added

- **Spec lookup comparison results** ([`docs/spec-lookup-results.md`](docs/spec-lookup-results.md)) and the
  scripts to repeat it (`eng/spec-lookup-comparison/`). On 29 lookup tasks in Claude Code, the spec skill scored
  100%, tied with keyword search and ahead of no spec help (97%), with five times fewer invented names. ADR 0001
  is accepted with option B.
- **`ed-fi-api-client` skill:** field names that assistants often get wrong: Data Standard 4 names (`parents`,
  `periodSequence`) and data model names (`studentUSI`) instead of the Data Standard 5 API names. New test
  prompt T11 passes 3/3 in Claude Code with the skill and 0/3 without it.

## 1.0.0 (2026-10-29)

First release of the SDK as [Agent Skills](https://agentskills.io), replacing the earlier MCP server (kept in
the `original-sdk-as-mcp-server` release).

### Added

- **`ed-fi-api-client` skill:** guidance for writing, reviewing and debugging Ed-Fi API clients, for ODS/API 7.x
  and Ed-Fi API 8.1 and newer:
  - authentication and token handling, the Discovery API, and URL structure;
  - push integrations: dependency order, POST as upsert, PUT and DELETE by `id`, descriptors, references, dates,
    ETags, and cascading key updates;
  - pull integrations: offset and cursor paging, partitions, change queries, deletes and key changes, and an
    incremental sync algorithm;
  - error diagnosis for `400`–`5xx` responses, with retry and logging guidance;
  - 21 shared rules (discovery, authentication, push, pull, errors) used both to build code and to review it.
- **`ed-fi-api-spec` skill:** a Markdown index of the Ed-Fi Resources and Descriptors specifications (Data Standard
  5.2), so assistants can look up resources without loading the full OpenAPI specification. Each resource file
  lists the natural key (from the GET query parameters marked `x-Ed-Fi-isIdentity`), the required fields, the
  fields to supply in each reference, the fields of nested collections, the endpoints, and whether `PUT` can
  change the resource's identifying values.
- **Spec knowledge graph generator** (`eng/spec-knowledge-graph/`): regenerates the `ed-fi-api-spec` content
  from an Ed-Fi host's metadata, including that host's extensions, with a fixture-based test.
- **Install and usage guide** (`docs/skills/using-the-skills.md`) for Claude Code and GitHub Copilot, with the
  GitHub CLI (`gh skill`), the `skills` CLI or a manual copy.
- Skill authoring guide, test prompts and test results for each skill.

### Verification

- `ed-fi-api-client`: 10/10 test prompts pass in Claude Code (5/10 without the skill) and 10/10 in GitHub
  Copilot (4/10 without the skill). The four prompts that depend on authentication pass again in both
  assistants after the Ed-Fi API 8.1 changes. Code that Claude Code wrote with the skill ran unchanged against
  the Ed-Fi API 8.1 pilot test kit (8.1 pre-release).
- `ed-fi-api-spec`: 12/12 test prompts pass in Claude Code (10/12 without the skill) and 10/12 in GitHub
  Copilot.

### Removed

- The MCP server under `sdk-as-mcp/`, superseded by the skills. The `original-sdk-as-mcp-server` release keeps
  its code.
