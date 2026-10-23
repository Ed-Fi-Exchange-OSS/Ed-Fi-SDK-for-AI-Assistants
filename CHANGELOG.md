# Changelog

Notable changes to the Ed-Fi SDK for AI Assistants. Versions follow the Ed-Fi
[software versioning](https://docs.ed-fi.org/community/sdlc/code-contribution-guidelines/software-versioning)
guidelines (`x.y.z`).

## 1.0.0 (unreleased)

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
  5.2) with each resource's natural key, fields, references and endpoints, so assistants can look them up without
  loading the full OpenAPI specification.
- **Spec knowledge graph generator** (`eng/spec-knowledge-graph/`): regenerates the `ed-fi-api-spec` content
  from an Ed-Fi host's metadata, including that host's extensions.
- **Install and usage guide** (`docs/skills/using-the-skills.md`) for Claude Code and GitHub Copilot, with the
  GitHub CLI (`gh skill`), the `skills` CLI or a manual copy.
- Skill authoring guide, test prompts and test results for each skill.

### Verification

- `ed-fi-api-client`: 10/10 test prompts pass in Claude Code (5/10 without the skill) and 10/10 in GitHub
  Copilot. Code that Claude Code wrote with the skill ran unchanged against the Ed-Fi API 8.1 pilot test kit.
- `ed-fi-api-spec`: 10/10 test prompts pass in Claude Code (7/10 without the skill); 3/3 in a GitHub Copilot
  smoke test.

### Deprecated

- The MCP server under `sdk-as-mcp/` is superseded by the skills. The `original-sdk-as-mcp-server` release keeps
  a copy of it.
