---
name: ed-fi-api-spec
description: Look up Ed-Fi API resources and descriptor types without loading the OpenAPI (swagger) specification — which resource to use for a concept (e.g. enrollment, attendance, grades, parents, addresses), its collection path, natural key, required fields, the fields to supply in each reference, the fields of nested collections, and its endpoints. Covers Data Standard 5.2 and 6.1 side by side, and upgrade / migration instructions from versions 4.0, 5.0 and 5.1. Use when writing or reviewing code against an Ed-Fi API and the resource name, its fields or its key are not known.
---

# Ed-Fi API spec lookup

A Markdown index of the Ed-Fi Resources and Descriptors API specifications, one per Data Standard version
(5.2 and 6.1, generated from the ODS/API 7.3 sandbox metadata). The full specifications are about 2.7 million
tokens for 5.2; a lookup here usually needs 8–10 thousand.

## Pick the Data Standard version first

Resources and fields differ between versions, so use the index of the version the host runs:

- Read `dataModels` from the host's Discovery API (`GET` on the API root): the entry named `Ed-Fi` has the
  version, for example `"version": "6.1.0"`. If you can't call the host, ask the developer which version it
  runs. Don't assume one.
- **5.2:** [references/ds-5.2/](references/ds-5.2/index.md).
- **6.1:** [references/ds-6.1/](references/ds-6.1/index.md).
- Any other version: say that this skill has no index for it, and use the closest one only with that warning.

Below, `<ds>` is that folder (`ds-5.2` or `ds-6.1`). Don't mix files from the two folders in one answer.

## How to look something up

1. **Find the resource.** Search `references/<ds>/index.md` for the developer's term. Each line has the
   resource name, its collection path and the first sentence of its description, plus common synonyms
   ("Also: …"). If the first term finds nothing, try other wordings: singular and plural, the business term
   ("enrolled", "enrollment", "registration") and the Ed-Fi term ("association").
2. **Open only the resource files you need**, under `references/<ds>/resources/<name>.md`, where `<name>` is
   the plural collection name from the index (`students.md`, `grades.md`, `studentSchoolAssociations.md`).
   Each file has:
   - the **natural key**, as the field names you would filter a GET by (see below);
   - every **field**, marked `yes` when required, with its type, the fields to supply inside each
     `...Reference`, and which fields are descriptors;
   - the fields of each **nested collection** (for example `classPeriods` in `sections`), with their own
     required flags;
   - the **endpoints**, including `/deletes`, `/keyChanges` and `/partitions` where they exist, and whether
     `PUT` can change the resource's identifying values (cascading key updates).
3. **For descriptor types**, search `references/<ds>/descriptors.md`. Descriptor *values* are data, not part
   of the spec: read them from the target API.
4. **For upgrades between Data Standard versions**, open the matching change list: 4.0 to 5.0
   ([whats-new-v50.md](references/whats-new-v50.md)), 5.0 to 5.1
   ([whats-new-v51.md](references/whats-new-v51.md)) or 5.1 to 5.2
   ([whats-new-v52.md](references/whats-new-v52.md)). Each lists added, renamed, changed and removed resources,
   fields and descriptors, and marks breaking changes. Read only the versions between the source and target.

Don't open `index.md` and many resource files "just in case"; open what the task needs.

## Changes from 5.2 to 6.1 that break client code

- **Student and staff demographics, contact information and identification codes have their own
  resources.** In 6.1 they are no longer in `studentEducationOrganizationAssociations`, `students` or
  `staffs`: use `studentDemographics`, `studentDirectories` (addresses, telephones, email),
  `studentIdentificationCodes`, `staffDemographics`, `staffDirectories` and `staffIdentificationCodes`.
  Student disabilities, characteristics and `limitedEnglishProficiencyDescriptor` are in `studentDemographics`.
- **`staffEducationOrganizationContactAssociations` is removed.** Staff contact information for an education
  organization is in `staffDirectories` (addresses, telephones, email); it has no `contactTitle` or
  `contactTypeDescriptor`.
- **TPDM resources are in the `ed-fi` namespace** (`/ed-fi/candidates`, not `/tpdm/candidates`).
- Resources whose description starts with **EARLY ACCESS** (for example `studentIEPs`) may still change; say
  so when you use one.

Check the resource file of the version in use rather than relying on this list.

## Limits

- **Data Standard 5.2 and 6.1 only.** Earlier versions are covered only by the change lists in step 4. Paths
  are shown as in the spec (`/ed-fi/students`); build full URLs from the host's Discovery API
  (`urls.dataManagementApi`), which differs between ODS/API 7.x (`.../data/v3/`) and Ed-Fi API 8
  (`.../data/`).
- **Host extensions are not included.** Extensions appear only in each host's own metadata; regenerate this
  index from that host with `eng/spec-knowledge-graph/generate.py` (see its README in the repository).
- **Natural keys are field names, not references.** They come from the GET query parameters marked
  `x-Ed-Fi-isIdentity`, which list every identity field with references flattened: `schoolId` is supplied
  in `schoolReference`, and a role-prefixed name such as `gradingPeriodSchoolYear` is the `schoolYear` in
  `gradingPeriodReference`. A required reference is not necessarily part of the key (for example
  `chartOfAccountReference` in `localAccounts`): use the natural key list, not the required fields.

For how to call the API (authentication, push, pull, errors), use the `ed-fi-api-client` skill.
