---
name: ed-fi-extension-builder
description: Guidance for extending the Ed-Fi Data Standard on an Ed-Fi API 8.1 or later host with MetaEd. Covers deciding whether an extension is needed, modeling it in MetaEd (new domain entities, associations based on core associations, descriptors, additions to core resources and common types, references to core entities), running the MetaEd build from the command line, explaining and fixing build errors, deploying the extension to a local Ed-Fi API with a claims fragment, verifying it with API calls, and reviewing extension source against Ed-Fi modeling rules. Use whenever a task mentions a Data Standard extension, MetaEd, .metaed files, ApiSchema-EXTENSION.json, _ext properties, or adding resources or fields to an Ed-Fi API.
---

# Ed-Fi Data Standard Extension Builder

An **extension** adds entities, descriptors or properties that the Ed-Fi Data Standard doesn't have. It is
modeled in [MetaEd](https://docs.ed-fi.org/reference/metaed), in a project of its own next to the core model,
and the MetaEd build turns it into `ApiSchema-EXTENSION.json`, the file the Ed-Fi API loads.

This skill targets **Ed-Fi API 8.1 and later**, with **MetaEd 4.9 or later** and **Data Standard 5.2**. ODS/API
7.x extensions use a different deployment (a C# extension project, SQL claims scripts, `initdev`); don't apply
those steps to Ed-Fi API 8.

## The flow

1. **Decide whether an extension is needed.** See below. Most needs fit the core model.
2. **Model it** in a MetaEd project: [references/modeling.md](references/modeling.md).
3. **Build it** from the command line and fix any errors: [references/build.md](references/build.md).
4. **Secure**: write a claims fragment for every new resource and descriptor:
   [references/security.md](references/security.md). Core resources that only get `additions` need no new
   claims.
5. **Deploy**: stage the core and extension schemas and the claims, and start the API on a clean database:
   [references/deploy.md](references/deploy.md).
6. **Verify** with Discovery and authenticated calls to the new resources and the `_ext` properties:
   [references/verify.md](references/verify.md).

## Step 1: Decide whether an extension is needed

Extensions add work for every data provider, so the
[Extension Framework best practices](https://docs.ed-fi.org/reference/data-exchange/extensions-framework/)
say to avoid them where possible. Before modeling, check with the developer:

- Does the Data Standard already have the entity or element, maybe under another name? Look it up (the
  `ed-fi-api-spec` skill, if installed, or the Data Standard documentation).
- Would a **descriptor value** do? New code values are data loaded into an existing descriptor, not an
  extension.
- Is it an aggregate (a count, a total)? Collect the underlying records instead.
- Will an upcoming Data Standard release cover it?

If an extension is still needed, say which kind fits (see the table in
[references/modeling.md](references/modeling.md#choose-the-kind-of-extension)) and why.

## Route to the right reference

| Situation | Read |
|---|---|
| New project, `package.json`, choosing the kind of extension, writing `.metaed` files, identity, naming | [references/modeling.md](references/modeling.md) |
| Installing MetaEd for the command line, running the build, reading errors, finding the output | [references/build.md](references/build.md) |
| Staging the schemas, resetting and starting the local Ed-Fi API, ports, deployment errors | [references/deploy.md](references/deploy.md) |
| Claims fragments, claim names, which claim sets get access, descriptor namespaces | [references/security.md](references/security.md) |
| Checking a deployed extension, API clients, reading `403`, `404`, `409` responses | [references/verify.md](references/verify.md) |
| Reviewing or checking existing extension source (`.metaed` files, a pull request) | [references/review.md](references/review.md) |
| The modeling rules, by ID | [references/rules.md](references/rules.md) |
| A new resource and descriptor, worked end to end | [references/examples/alternative-education-program.md](references/examples/alternative-education-program.md) |
| Properties added to a core resource and common type, worked end to end | [references/examples/student-transcript.md](references/examples/student-transcript.md) |

## Rules for every extension

1. Never change core Data Standard files, and never turn on MetaEd **Alliance Mode**. Extend core entities
   with `additions` in the extension project instead.
2. Prefix every core entity, common, descriptor or shared type with `EdFi.`; names defined in the extension
   project need no prefix.
3. Don't mark properties `is part of identity` in `additions` or in a subclass; MetaEd doesn't allow it.
4. Give every entity and property a `documentation` string that says what it means, in plain words.
5. Run the build after every change, and fix errors before any deployment step.
6. Ask the developer before accepting the Ed-Fi license for them, before changing their `.metaed` files to fix
   an error, and before any step that deletes databases.
7. Treat an installed extension as fixed: changing it needs a new database and reloading the data through the
   API.

## Further reading

- [How To: Extend the Ed-Fi API - Alternative Education Program Example](https://docs.ed-fi.org/reference/ed-fi-api/8/how-to-guides/how-to-extend-the-ed-fi-ods-api-alternative-education-program-example/)
- [How To: Extend the Ed-Fi API - Student Transcript Example](https://docs.ed-fi.org/reference/ed-fi-api/8/how-to-guides/how-to-extend-the-ed-fi-ods-api-student-transcript-example/)
- [MetaEd Cookbook](https://docs.ed-fi.org/reference/metaed/cookbook/) and
  [Language Specification](https://docs.ed-fi.org/reference/metaed/language-specification/)
