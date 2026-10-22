# Ed-Fi Agent Skills

[Agent Skills](https://agentskills.io) that give AI coding assistants accurate, Ed-Fi-specific guidance.
Each skill is a folder with a `SKILL.md` entry point. The assistant reads the short `SKILL.md` first and
opens the files under `references/` only when the task needs them.

| Skill | Use it for |
|---|---|
| [ed-fi-api-client](ed-fi-api-client/SKILL.md) | Building, reviewing or debugging a client of an Ed-Fi API: authentication, push and pull integrations, error diagnosis |
| [ed-fi-api-spec](ed-fi-api-spec/SKILL.md) | Looking up resources, natural keys, fields, references and descriptor types (Data Standard 5.2) without loading the OpenAPI spec |

Skills are added through pull requests; see the
[authoring guide](../docs/skills/authoring-guide.md).

## Installing a skill

Both tools below find skills through the `skills/*/SKILL.md` convention, so they work with this repository
as is. Replace `ed-fi-api-client` with the skill you want, and `claude-code` with your assistant
(`github-copilot`, `codex`, and many others; see each tool's help). Both install at project level by default.

### With the GitHub CLI

[`gh skill`](https://cli.github.com/manual/gh_skill) is in preview in recent GitHub CLI releases.

```bash
gh skill install Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants ed-fi-api-client --agent claude-code
```

- `--scope user` installs for your user instead of the current project.
- `--pin <tag-or-commit-sha>` installs a specific version; otherwise the latest release (or the default
  branch) is used.
- `gh skill update` updates installed skills; `gh skill list` lists them.

### With the `skills` CLI

The [`skills`](https://github.com/vercel-labs/skills) CLI runs through `npx` (Node.js required).

```bash
npx skills add Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants --skill ed-fi-api-client --agent claude-code
```

- `--list` shows the skills in the repository without installing; `-g` installs for your user.
- `--copy` copies the files instead of symlinking them.
- `npx skills update` updates installed skills.

### Manually

Copy (or symlink) the skill folder into the location your assistant reads skills from.

| Assistant | Project-level location | User-level location |
|---|---|---|
| Claude Code | `.claude/skills/<skill-name>/` | `~/.claude/skills/<skill-name>/` |
| GitHub Copilot (VS Code agent mode) | `.github/skills/<skill-name>/` | `~/.copilot/skills/<skill-name>/` |
| Codex | `.agents/skills/<skill-name>/` | `~/.codex/skills/<skill-name>/` |

The CLIs above install for GitHub Copilot and Codex into `.agents/skills/`, a project folder both read.

> [!NOTE]
> Skill locations are still evolving across assistants. Check your assistant's documentation if the skill is
> not picked up. In VS Code, agent skills may need the `chat.useAgentSkills` setting enabled.
