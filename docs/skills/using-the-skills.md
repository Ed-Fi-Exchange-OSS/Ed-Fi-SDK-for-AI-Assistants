# Installing and using the Ed-Fi skills

How to install the skills in this repository, check that your assistant uses them, and keep them up to date.
The steps are the same for every skill; replace the skill name in the commands.

| Skill | Use it for |
|---|---|
| `ed-fi-api-client` | Writing, reviewing or debugging code that calls an Ed-Fi API: authentication, push and pull integrations, error diagnosis |
| `ed-fi-api-spec` | Finding the right Ed-Fi resource, its required fields, references and endpoints without loading the OpenAPI specification |

The two skills work well together: install both, and `ed-fi-api-client` uses `ed-fi-api-spec` to look up
resources and fields.

## Install

Install at **project level** (the skill travels with the repository and the whole team gets it) or at **user
level** (available in every project on your machine). The examples install `ed-fi-api-client` for Claude Code
at project level.

### With the GitHub CLI

[`gh skill`](https://cli.github.com/manual/gh_skill) is in preview in recent GitHub CLI releases.

```bash
gh skill install Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants ed-fi-api-client --agent claude-code
```

- Use `--agent github-copilot` for GitHub Copilot, `--scope user` for user level.
- `--pin <tag-or-commit-sha>` installs a specific version; otherwise the latest release (or the default
  branch) is used.

### With the `skills` CLI

The [`skills`](https://github.com/vercel-labs/skills) CLI runs through `npx` (Node.js required).

```bash
npx skills add Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants --skill ed-fi-api-client --agent claude-code
```

- Use `--agent github-copilot` for GitHub Copilot, `-g` for user level.
- `--list` shows the skills in the repository without installing anything.

### Manually

Copy the skill folder (for example `skills/ed-fi-api-client/`) into the folder your assistant reads:

| Assistant | Project level | User level |
|---|---|---|
| Claude Code | `.claude/skills/<skill-name>/` | `~/.claude/skills/<skill-name>/` |
| GitHub Copilot (VS Code) | `.github/skills/<skill-name>/` or `.agents/skills/<skill-name>/` | `~/.copilot/skills/<skill-name>/` |

The two CLIs install Copilot skills into `.agents/skills/`, a folder Copilot shares with other assistants
such as Codex.

## Turn on skills in GitHub Copilot

In VS Code, skills are used in Copilot Chat's **Agent** mode. Make sure the `chat.useAgentSkills` setting is
enabled (Settings, search for "agent skills"). Claude Code needs no setup.

## Use a skill

Ask for what you need in your own words; the assistant loads a skill when the request matches its description.
For example:

- "Write a script that loads students and their school enrollments from CSV files into our Ed-Fi API."
- "Review the API client code in `src/sync/` against the Ed-Fi guidance."
- "We get a 409 when posting a studentSchoolAssociation. What's wrong?"
- "Which Ed-Fi resource holds daily attendance, and which fields are required?"

**Check that the skill was used.** Claude Code shows a **Skill** step for `ed-fi-api-client` before it
answers. Copilot shows "Read skill `ed-fi-api-client`" at the top of its answer, followed by the reference
files it read.

**If the assistant does not load it on its own**, invoke it by name: type `/ed-fi-api-client` (or
`/ed-fi-api-spec`) followed by your request. This works in both Claude Code and Copilot, and can help in large
repositories with many other skills or project instructions. When you invoke a skill this way, its content is
added to your request directly, so no separate Skill step appears.

**In Copilot agent mode**, the assistant may try to run changes against an API instead of answering. Say so
when you only want an answer, for example "show me the HTTP requests; don't run anything".

## Keep skills up to date

| Installed with | Update |
|---|---|
| `gh skill` | `gh skill update` |
| `skills` CLI | `npx skills update` |
| Manually | Copy the skill folder again from the latest release |

Remove a skill by deleting its folder, or with `npx skills remove <skill-name>`.

## Include your host's extensions

`ed-fi-api-spec` covers the core Ed-Fi Resources and Descriptors (Data Standard 5.2). Extensions exist only in
each host's own metadata. To include them, regenerate the skill's content from your host with the generator in
[`eng/spec-knowledge-graph/`](../../eng/spec-knowledge-graph/README.md), writing the output into your installed
copy of the skill.

## Supported versions

- **Ed-Fi APIs:** ODS/API 7.x and Ed-Fi API 8.1 and newer, Data Standard 5.2.
- **Assistants:** verified in Claude Code and GitHub Copilot (VS Code agent mode). The skills follow the
  [Agent Skills](https://agentskills.io) format, so other assistants that support it, such as Codex, can use
  them from their own skills folder.
