# Example: Student Transcript

A **new domain entity**, four **descriptors**, and **additions** to a core resource and a core common type.
From
[How To: Extend the Ed-Fi API - Student Transcript Example](https://docs.ed-fi.org/reference/ed-fi-api/8/how-to-guides/how-to-extend-the-ed-fi-ods-api-student-transcript-example/)
(Ed-Fi API 8.1).

## The need

Record where students enroll in college after graduation, whether graduates were in a special education
program, and whether a transcript is an official submission. That needs a new entity for postsecondary
institutions and new fields on the existing `StudentAcademicRecord` and its `ClassRanking` common type.

## The files

```text
StudentTranscript/
  Common/ClassRankingExtension.metaed
  Descriptor/InstitutionControl.metaed
  Descriptor/InstitutionLevel.metaed
  Descriptor/SpecialEducationGraduationStatus.metaed
  Descriptor/SubmissionCertification.metaed
  DomainEntity/PostSecondaryOrganization.metaed
  DomainEntity/StudentAcademicRecordExtension.metaed
  package.json
```

`package.json` sets `projectName` to `SampleStudentTranscript`. The new entity:

```metaed
Domain Entity PostSecondaryOrganization
    documentation "PostSecondaryOrganization"
    shared string EdFi.NameOfInstitution
        documentation "The name of the institution."
        is part of identity
    descriptor InstitutionLevel
        documentation "The level of the institution."
        is required
    descriptor InstitutionControl
        documentation "The type of control of the institution (i.e., public or private)."
        is required
    bool AcceptanceIndicator
        documentation "An indication of acceptance."
        is required
```

The additions to the core resource and common type:

```metaed
Domain Entity EdFi.StudentAcademicRecord additions
    domain entity PostSecondaryOrganization
        documentation "A reference to the postsecondary organization."
        is optional
    descriptor SubmissionCertification
        documentation "The type of submission certification."
        is optional
    common extension EdFi.ClassRanking
        documentation "Class Ranking Extension"
        is optional
```

```metaed
Common EdFi.ClassRanking additions
    descriptor SpecialEducationGraduationStatus
        documentation "The graduation status for special education."
        is required
```

Each descriptor file is two lines, for example:

```metaed
Descriptor InstitutionControl
    documentation "The type of control for an institution (e.g., public or private)."
```

What to notice:

- `PostSecondaryOrganization` reuses the core `EdFi.NameOfInstitution` shared type as its identity.
- `additions` adds properties without identity; the core resource keeps its identity and its URL.
- The common type extension takes two declarations: `Common EdFi.ClassRanking additions`, and
  `common extension EdFi.ClassRanking` in the additions of the entity that uses it.
- The documentation of `PostSecondaryOrganization` only repeats its name. In your own extensions, say what the
  entity means.

## The build result

With `projectName` `SampleStudentTranscript`, the build succeeds and `ApiSchema-EXTENSION.json` has:

- `projectEndpointName`: `sample-student-transcript`
- new resources: `postSecondaryOrganizations` and the four descriptors (`institutionControlDescriptors`,
  `institutionLevelDescriptors`, `specialEducationGraduationStatusDescriptors`,
  `submissionCertificationDescriptors`)
- `studentAcademicRecords`, marked as a resource extension. Its new properties go under
  `_ext.samplestudenttranscript` in the payload of the core `/data/ed-fi/studentAcademicRecords` resource.

## Deploying it

As written, this example **doesn't deploy on Ed-Fi API 8.1.0**: the additions to `StudentAcademicRecord` and
to its `ClassRanking` common map to the same table, and the start fails (see
[deploy.md](../deploy.md#known-issues)). Without the `ClassRanking` additions (the `Common` file, and the
`common extension EdFi.ClassRanking` property), it deploys and works: on 2026-11-23, Discovery listed
`SampleStudentTranscript`, the four descriptors and `postSecondaryOrganizations` accepted writes, and a
`studentAcademicRecords` record with `_ext.samplestudenttranscript` was stored and read back with its
reference to the postsecondary organization. The claims fragment is in [security.md](../security.md).
