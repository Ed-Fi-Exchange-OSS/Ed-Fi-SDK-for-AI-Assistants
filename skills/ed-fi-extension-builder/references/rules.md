# Extension modeling rules

Rules for MetaEd extension source, used both to write an extension ([modeling.md](modeling.md)) and to review
one ([review.md](review.md)). They adapt the Ed-Fi-Model review checklist (`review-model-pr` in
[AI-Tools-for-Ed-Fi-SDLC](https://github.com/Ed-Fi-Alliance-OSS/AI-Tools-for-Ed-Fi-SDLC)) to extensions, and
add checks that only apply to extensions.

Levels: **Required** rules are blocking; **Preferred** rules are suggestions. Each rule says how to detect it.

## Build

- **BUILD-1 (Required): The model builds without errors.** Run the build ([build.md](build.md)). Any
  `"level":"error"` line or exit code `1` is a finding, reported with its file and line.

## Core model

- **CORE-1 (Required): The core model isn't changed.** *Detect:* edits to files in the core model package,
  `allianceMode: true` in the config, or an extension file that redeclares a core entity without `EdFi.` and
  `additions`. The build still succeeds, with a warning such as `Domain Entity named Staff already exists in
  project Ed-Fi`, and the API gets a second, unrelated `staffs` resource under the extension's URL segment.
  Treat that warning as a finding.
- **CORE-2 (Required): Core names have the `EdFi.` prefix.** *Detect:* a reference to a core entity, common,
  descriptor or shared type without it. The build fails, unless the extension defines the same name (with the
  `already exists in project Ed-Fi` warning): then the reference silently points to the extension's own type.
- **CORE-3 (Required): The extension doesn't duplicate the core model.** *Detect:* a new entity, descriptor or
  property with the meaning of an existing core one (a new `GradeLevel` descriptor, a `FirstName` string on a
  staff extension). Look the name and its synonyms up in the Data Standard. Reason: duplicates split the same
  data across two places, and the Extension Framework best practices rule them out.
- **CORE-4 (Required): Descriptor values aren't modeled.** *Detect:* `with map type` items in a descriptor.
  Values are data, loaded into the descriptor through the API.
- **CORE-5 (Preferred): Additions to core resources are optional.** *Detect:* `is required` (or
  `is required collection`) on a property in `Domain Entity EdFi.X additions` or `Association EdFi.X
  additions`. Reason: a required addition asks every client that writes the core resource for the extension's
  data, including clients that don't know the extension. If it must be required, say so in the documentation.

## Project

- **PROJ-1 (Required): The project name is consistent.** *Detect:* `projectName` in `package.json`, the
  extension's `namespaceName` and `projectName` in the MetaEd config, and the namespace used by other
  projects must match exactly. If a claims fragment is part of the change, its claim URIs must use the
  `projectEndpointName` (the kebab-case project name) and include every new resource and descriptor.
- **PROJ-2 (Required): The project name follows MetaEd's rules.** *Detect:* a name that doesn't start with
  an uppercase letter, has fewer than two letters, or has special characters.
- **PROJ-3 (Preferred): `projectVersion` follows SemVer.** Major for a breaking change to the API model.

## Documentation

- **DOC-1 (Required): No typos, missing words or broken sentences** in `documentation` strings.
- **DOC-2 (Preferred): Documentation says what the element means.** *Detect:* documentation that repeats the
  name (`documentation "PostSecondaryOrganization"`), or that narrows the use more than intended.
- **DOC-3 (Preferred): No database language.** "staff member", not "staff record"; "individual", not "person
  record".
- **DOC-4 (Preferred): Descriptor documentation gives realistic examples** ("Examples include: Home, Hospital,
  School"), not placeholders.
- **DOC-5 (Preferred): Date properties carry the core date note.** The core model adds "Note: Date
  interpretation may vary. Ed-Fi recommends inclusive dates, but states may define dates as inclusive or
  exclusive. For calculations, align with local guidelines." to begin and end dates.

## Identity

- **KEY-1 (Required): Every new domain entity has an identity**, made of values that don't change for the
  record. The build fails without one; review whether the chosen properties are stable.
- **KEY-2 (Preferred): In entities about a student, the `Student` reference comes first.**
- **KEY-3 (Preferred): `required` and `optional` fit the data.** A value that every record has is
  `is required`; don't make a property required only because it is usually present.

## Naming

- **NAME-1 (Preferred): Entity names are singular PascalCase**, without filler such as `Information` and
  without trailing numbers.
- **NAME-2 (Preferred): Associations end in `Association`.** Descriptors must not end in `Descriptor`: MetaEd
  adds the suffix, and a descriptor named `BusTypeDescriptor` fails the build (`Descriptor names cannot be suffixed
  with 'Descriptor'`), so report it under BUILD-1.
- **NAME-3 (Preferred): Each file holds one entity, is named after it, and sits in the folder for its kind**
  (`Descriptor/InstitutionLevel.metaed`). Files with `additions` to a core entity are named
  `<Entity>Extension.metaed`, as in the how-to guides (`StudentAcademicRecordExtension.metaed`).
- **NAME-4 (Preferred): Existing shared types are reused** (`shared string EdFi.NameOfInstitution`) instead
  of a new `string` with the same meaning.

## Model hygiene

- **HYG-1 (Required): No slowly changing dimensions.** *Detect:* `BeginDate`/`EndDate` pairs added to
  demographic or identity data without a calendar reason (enrollment, employment and program participation
  are calendar reasons). The Data Standard doesn't track history this way; flag it for discussion.
- **HYG-2 (Preferred): No deprecated keywords** (`queryable`, `renames identity property`) and no elements
  that are `deprecated` from the start.
- **HYG-3 (Preferred): Collections use `is optional collection` or `is required collection`** when a record
  can have more than one value.

## Not checked for Ed-Fi API 8

Interchange and Domain files affect only the XSD and the handbook, not the Ed-Fi API 8 schema. Mention a
missing one only if the host uses the XML bulk load client or publishes the handbook. The generated
`ApiSchema-EXTENSION.json` is not reviewed; it comes from the `.metaed` source.
