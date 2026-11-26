# Modeling an extension in MetaEd

How to set up the extension project and write its `.metaed` files. Sources: the MetaEd
[Language Specification](https://docs.ed-fi.org/reference/metaed/language-specification/), the
[Cookbook](https://docs.ed-fi.org/reference/metaed/cookbook/), and
[Creating and Maintaining Your Extension](https://docs.ed-fi.org/reference/metaed/ide-user-guide/creating-and-maintaining-your-extension).

## The project

An extension project is a folder with a `package.json` and one subfolder per kind of file. Create only the
folders you use:

```text
MyExtension/
  Association/      Choice/       Common/     Descriptor/   Domain/
  DomainEntity/     Enumeration/  Interchange/  Shared/
  package.json
```

```json
{
  "metaEdProject": {
    "projectName": "SampleStudentTranscript",
    "projectVersion": "1.0.0"
  }
}
```

- `projectName` starts with an uppercase letter, has at least two letters, and has no special characters
  (they are stripped from the generated names). It is the **namespace** other projects use to refer to it.
- The API derives the extension's URL segment, `projectEndpointName`, from it in kebab case:
  `SampleStudentTranscript` becomes `sample-student-transcript`, so the resources are at
  `/data/sample-student-transcript/...` and the claim URIs use the same segment.
- `projectVersion` follows SemVer: major for a breaking change to the API model, minor for additions, patch for
  fixes.
- One entity per file, named after the entity (`DomainEntity/PostSecondaryOrganization.metaed`), in the
  folder for its kind.

## Choose the kind of extension

| The need | MetaEd | Example |
|---|---|---|
| A new thing with its own identity | `Domain Entity X` | `PostSecondaryOrganization` (Student Transcript) |
| A new relationship between two entities | `Association X` with two `domain entity` properties | |
| A specialization of a core association, such as a program | `Association X based on EdFi.Y` | `StudentAlternativeEducationProgramAssociation` based on `EdFi.GeneralStudentProgramAssociation` |
| A specialization of a core domain entity | `Domain Entity X based on EdFi.Y` | |
| A new code set | `Descriptor X` (the values are data, loaded through the API) | `AlternativeEducationEligibilityReason` |
| New fields on a core resource | `Domain Entity EdFi.Y additions` or `Association EdFi.Y additions` | `EdFi.StudentAcademicRecord additions` |
| New fields on a core common type | `Common EdFi.Y additions`, plus `common extension EdFi.Y` in the additions of the entity that uses it (doesn't deploy on Ed-Fi API 8.1.0; see [Known issues](deploy.md#known-issues)) | `EdFi.ClassRanking additions` |
| A group of properties reused by several entities | `Common X` | |

`additions` keeps the core resource and adds the new properties under `_ext`, in an object named after the
`projectName` in lowercase: `"_ext": { "samplestudenttranscript": { ... } }`. A subclass
(`based on`) creates a new resource that inherits the base's properties and identity.

## Writing a file

```metaed
Domain Entity PostSecondaryOrganization
    documentation "A postsecondary institution that a student applies to or enrolls in."
    shared string EdFi.NameOfInstitution
        documentation "The name of the institution."
        is part of identity
    descriptor InstitutionLevel
        documentation "The level of the institution."
        is required
    bool AcceptanceIndicator
        documentation "An indication of acceptance."
        is required
```

- Indent with four spaces, as the core model does: properties under the entity, `documentation` and modifiers
  under each property. MetaEd doesn't require it, but it keeps files readable.
- Every entity (except `additions`) and every property has `documentation`, right after its name.
- Entity and property names start with an uppercase letter.
- Each property has exactly one cardinality: `is part of identity`, `is required`, `is optional`,
  `is required collection` or `is optional collection`.
- `string` needs `max length` (and takes an optional `min length`): the build fails without it, although the
  Language Specification shows it as optional. `decimal` needs `total digits` and `decimal places`.
- Other simple types: `bool`, `currency`, `date`, `datetime`, `duration`, `integer`, `percent`, `short`,
  `time`, `year`.
- References: `domain entity EdFi.School`, `association X`, `descriptor X`, `common EdFi.MeetingTime`,
  `shared string EdFi.NameOfInstitution`. When an entity has two properties of the same type, give one a
  `role name`.

## Namespaces

Anything defined outside the extension project needs its namespace and a period: `EdFi.` for the core model,
or the other project's `projectName`. Names defined in the extension project have no prefix. Namespaces are
case sensitive. Without the prefix, MetaEd looks for the name in the extension project and the build fails.

## Identity

- A domain entity needs at least one `is part of identity` property. Choose properties that never change for
  the record; changing an identity value is a delete and re-create for clients.
- An association's identity is the identity of both entities plus any properties marked `is part of identity`.
- `additions`, subclasses (`based on`), common extensions and descriptors can't add identity properties.
- In entities about a student, put the `Student` reference first.

## Rules

Follow the [extension modeling rules](rules.md) while writing; the `ed-fi-extension-review` skill uses the same
ones. In short:

- Don't change the core model or duplicate it, and use `EdFi.` for core names (CORE-1 to CORE-3). An
  extension can't remove, rename or change the identity of core entities and properties.
- Don't model descriptor values; they are data (CORE-4).
- Keep additions to core resources optional (CORE-5).
- Singular PascalCase names; `Association` suffix on associations, none on descriptors (NAME-1, NAME-2).
- Documentation that says what each element means, in plain words (DOC-1 to DOC-5).
- No deprecated keywords such as `queryable` and `renames identity property` (HYG-2).
