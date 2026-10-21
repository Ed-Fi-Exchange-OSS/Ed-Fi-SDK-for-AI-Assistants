# Ed-Fi Agent Skills

[Agent Skills](https://agentskills.io) that give AI coding assistants accurate, Ed-Fi-specific guidance.
Each skill is a folder with a `SKILL.md` entry point. The assistant reads the short `SKILL.md` first and
opens the files under `references/` only when the task needs them.

_No skills have been published yet._ Skills are added through pull requests; see the [authoring guide](../docs/skills/authoring-guide.md).

## Installing a skill

Copy (or symlink) the skill folder into the location your assistant reads skills from.

| Assistant | Project-level location | User-level location |
|---|---|---|
| Claude Code | `.claude/skills/<skill-name>/` | `~/.claude/skills/<skill-name>/` |
| GitHub Copilot (VS Code agent mode) | `.github/skills/<skill-name>/` | `~/.copilot/skills/<skill-name>/` |
| Codex | `.agents/skills/<skill-name>/` | `~/.codex/skills/<skill-name>/` |

> [!NOTE]
> Skill locations are still evolving across assistants. Check your assistant's documentation if the skill is
> not picked up. In VS Code, agent skills may need the `chat.useAgentSkills` setting enabled.
