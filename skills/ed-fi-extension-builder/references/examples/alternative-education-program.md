# Example: Alternative Education Program

A **new resource** and a **new descriptor**: a program association based on a core association. From
[How To: Extend the Ed-Fi API - Alternative Education Program Example](https://docs.ed-fi.org/reference/ed-fi-api/8/how-to-guides/how-to-extend-the-ed-fi-ods-api-alternative-education-program-example/)
(Ed-Fi API 8.1).

## The need

Track students in an alternative education program, with the reason each student is eligible and the times
the program meets. The core model has general student program associations, but no eligibility reason for
this program, so the design subclasses `GeneralStudentProgramAssociation`.

## The files

```text
AlternativeEducationProgram/
  Association/StudentAlternativeEducationProgramAssociation.metaed
  Descriptor/AlternativeEducationEligibilityReason.metaed
  package.json
```

```json
{
  "metaEdProject": {
    "projectName": "SampleAlternativeEducationProgram",
    "projectVersion": "1.0.0"
  }
}
```

```metaed
Association StudentAlternativeEducationProgramAssociation based on EdFi.GeneralStudentProgramAssociation
    documentation "This association represents Students in an Alternative Education Program."
    descriptor AlternativeEducationEligibilityReason
        documentation "The reason the student is eligible for the program."
        is required
    common EdFi.MeetingTime
        documentation "The times at which this Alternative Education Program is scheduled to meet."
        is optional collection
```

```metaed
Descriptor AlternativeEducationEligibilityReason
    documentation "This descriptor describes the reason a student is eligible for an Alternative Education Program"
```

What to notice:

- `based on EdFi.GeneralStudentProgramAssociation`: the new association inherits the base's identity
  (education organization, program, student, begin date), so it adds no identity properties.
- `AlternativeEducationEligibilityReason` has no prefix (it is in this project); `EdFi.MeetingTime` does.
- The descriptor name has no `Descriptor` suffix; the API resource does.

## The build result

With the config in [build.md](../build.md) (`projectName` `SampleAlternativeEducationProgram`), the build
succeeds and `ApiSchema-EXTENSION.json` has:

- `projectEndpointName`: `sample-alternative-education-program`
- resources: `alternativeEducationEligibilityReasonDescriptors` and
  `studentAlternativeEducationProgramAssociations`

After deployment the association is at
`/data/sample-alternative-education-program/studentAlternativeEducationProgramAssociations`.

## Deploying it

The claims fragment in [security.md](../security.md) puts the descriptor under `systemDescriptors` and the
association under `relationshipBasedData`. Deployed on 2026-11-23 with [deploy.md](../deploy.md): Discovery
listed `SampleAlternativeEducationProgram`, both endpoints returned `200`, and a descriptor value was written
and read back.
