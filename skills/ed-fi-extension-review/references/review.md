# Reviewing extension source

Use this procedure when asked to review or check a MetaEd extension: its `.metaed` files and its
`package.json`, as files, a branch or a pull request. It applies the [rules](rules.md) used to write
extensions. The generated `ApiSchema-EXTENSION.json` is not reviewed.

## 1. Scope the review

1. Find the extension project: the folder with `package.json` (`metaEdProject.projectName`) and the `.metaed`
   files. For a pull request, get the diff (`gh pr diff <number>`) and also read the unchanged files the new
   ones reference.
2. List what the extension declares: new entities, associations, descriptors and commons, and the core
   entities and commons it extends with `additions`.
3. Note the target: Ed-Fi API 8.1 and Data Standard 5.2 unless the project says otherwise.

## 2. Build it

Run the MetaEd build ([build.md](build.md)), after asking the developer to accept the Ed-Fi license if they
haven't. Report every error (BUILD-1) and every `already exists in project Ed-Fi` warning (CORE-1). MetaEd
reports those warnings only once the build has no errors, so when it fails, also look for core names
redeclared without `EdFi.` by reading the files. If the build can't run (no Node.js, no access to the package
feed), say so under "Not checked" and review by reading.

## 3. Check each rule

Go through every section of [rules.md](rules.md) for each file. Record one of these outcomes:

| What you find | Rule level | Report as |
|---|---|---|
| The source breaks the rule | Required | **Blocking issue** |
| The source doesn't follow the rule | Preferred | **Suggestion** |
| The source follows the rule | Any | Not a finding |
| Can't tell from the source | Any | "Not checked", with what would settle it |

Guidelines:

- **Cite evidence.** Every finding names the file and line, and quotes or describes the source.
- **Keep the level from the rule.** Don't promote a suggestion because it seems important; say why in the
  text instead.
- **Check meaning, not only syntax.** CORE-3 (duplicates of the core model) and DOC-2 (documentation that says
  what the element means) need the Data Standard; look names up instead of guessing.
- **Don't redesign the extension.** Report what breaks a rule. Propose an alternative design only when a rule
  requires it (for example, `additions` instead of a redeclared core entity).
- **Report defects outside the rules separately**, under "Other issues".

## 4. Report

```markdown
## Review: <project name> <version>

Build: <passed | failed with N errors | not run, because ...>

### Blocking issues
- **[RULE-ID]** `Folder/File.metaed:line`: <what is wrong and how to fix it>

### Suggestions
- **[RULE-ID]** `Folder/File.metaed:line`: <what to change and why>

### Other issues
- `Folder/File.metaed:line`: <defect no rule covers>

### Not checked
- <rule or question>: <why, and what would settle it>

### Looks good
- <what was checked and found clean>
```

Leave out empty sections, except Build. Keep each finding to one or two sentences.
