---
name: ed-fi-extension-review
description: Reviews MetaEd source for an Ed-Fi Data Standard extension (.metaed files and the project package.json) against Ed-Fi modeling rules adapted from the Ed-Fi-Model review checklist, for Ed-Fi API 8.1 and later. Runs the MetaEd build from the command line, then reports blocking issues and suggestions with file and line - core model changes, duplicates of core entities, missing EdFi. prefixes, identity, naming, documentation, deprecated keywords and slowly changing dimensions. Use whenever a task asks to review, check, audit or approve a Data Standard extension, MetaEd files or a pull request that changes them.
---

# Ed-Fi Data Standard Extension Review

Reviews the source of a Data Standard **extension**: the `.metaed` files and the project's `package.json`,
as files, a branch or a pull request. The generated `ApiSchema-EXTENSION.json` is not reviewed; it comes from
the source.

This skill targets **Ed-Fi API 8.1 and later**, with **MetaEd 4.9 or later** and **Data Standard 5.2**. To
write, build or deploy an extension, use the `ed-fi-extension-builder` skill; both skills apply the same
[rules](references/rules.md).

## How to review

1. **Scope:** find the extension project and list what it declares and what it extends.
2. **Build:** run the MetaEd build from the command line ([references/build.md](references/build.md)) and
   report every error and every `already exists in project Ed-Fi` warning.
3. **Check each rule** in [references/rules.md](references/rules.md): Required rules give blocking issues,
   Preferred rules give suggestions.
4. **Report** in the format in [references/review.md](references/review.md), with file and line for every
   finding.

The full procedure, the outcome table and the report template are in
[references/review.md](references/review.md).

## Rules for every review

1. Don't change the files. Report findings, and propose a fix only in the text.
2. Ask the developer before accepting the Ed-Fi license for them to run the build. If the build can't run, say
   so under "Not checked" and review by reading.
3. Look names up in the Data Standard (the `ed-fi-api-spec` skill, if installed, or the core model's
   `.metaed` files) before reporting a duplicate of the core model. Don't rely on memory.
4. Keep each finding at its rule's level, and cite the file, the line and the source.

## Route to the right reference

| Situation | Read |
|---|---|
| The review procedure, outcomes and report template | [references/review.md](references/review.md) |
| The rules, by ID and level | [references/rules.md](references/rules.md) |
| Installing MetaEd for the command line, running the build, reading errors | [references/build.md](references/build.md) |

## Further reading

- [Extension Framework best practices](https://docs.ed-fi.org/reference/data-exchange/extensions-framework/)
- [MetaEd Language Specification](https://docs.ed-fi.org/reference/metaed/language-specification/)
