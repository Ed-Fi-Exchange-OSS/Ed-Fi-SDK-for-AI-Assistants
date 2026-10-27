---
name: ed-fi-api-spec
description: Look up Ed-Fi API resources and descriptor types without loading the OpenAPI specification — which resource to use for a concept (e.g. enrollment, attendance, grades, parents), its collection path, natural key, required fields, the fields to supply in each reference, the fields of nested collections, and its endpoints. Data Standard 5.2. Use when writing or reviewing code against an Ed-Fi API and the resource name, its fields or its key are not known.
---

# Ed-Fi API spec lookup

A Markdown index of the Ed-Fi Resources and Descriptors API specifications (Data Standard 5.2, generated from
the ODS/API 7.3 sandbox metadata). The full specifications are about 2.7 million tokens; a lookup here
usually needs 8–10 thousand.

## How to look something up

1. **Find the resource.** Search [references/index.md](references/index.md) for the developer's term. Each
   line has the resource name, its collection path and the first sentence of its description, plus common
   synonyms ("Also: …"). If the first term finds nothing, try other wordings: singular and plural, the
   business term ("enrolled", "enrollment", "registration") and the Ed-Fi term ("association").
2. **Open only the resource files you need**, under `references/resources/<name>.md`, where `<name>` is the
   plural collection name from the index (`students.md`, `grades.md`, `studentSchoolAssociations.md`). Each
   file has:
   - the **natural key**, as the field names you would filter a GET by (see below);
   - every **field**, marked `yes` when required, with its type, the fields to supply inside each
     `...Reference`, and which fields are descriptors;
   - the fields of each **nested collection** (for example `classPeriods` in `sections`), with their own
     required flags;
   - the **endpoints**, including `/deletes`, `/keyChanges` and `/partitions` where they exist, and whether
     `PUT` can change the resource's identifying values (cascading key updates).
3. **For descriptor types**, search [references/descriptors.md](references/descriptors.md). Descriptor
   *values* are data, not part of the spec: read them from the target API.

Don't open `index.md` and many resource files "just in case"; open what the task needs.

## Limits

- **Data Standard 5.2 only.** Paths are shown as in the spec (`/ed-fi/students`); build full URLs from the
  host's Discovery API (`urls.dataManagementApi`), which differs between ODS/API 7.x (`.../data/v3/`) and
  Ed-Fi API 8 (`.../data/`).
- **Host extensions are not included.** Extensions appear only in each host's own metadata; regenerate this
  index from that host with `eng/spec-knowledge-graph/generate.py` (see its README in the repository).
- **Natural keys are field names, not references.** They come from the GET query parameters marked
  `x-Ed-Fi-isIdentity`, which list every identity field with references flattened: `schoolId` is supplied
  in `schoolReference`, and a role-prefixed name such as `gradingPeriodSchoolYear` is the `schoolYear` in
  `gradingPeriodReference`. A required reference is not necessarily part of the key (for example
  `chartOfAccountReference` in `localAccounts`): use the natural key list, not the required fields.

For how to call the API (authentication, push, pull, errors), use the `ed-fi-api-client` skill.
