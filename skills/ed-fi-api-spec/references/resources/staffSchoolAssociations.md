# staffSchoolAssociations

`/ed-fi/staffSchoolAssociations`

This association indicates the school(s) to which a staff member provides instructional services.

## Natural key

`programAssignmentDescriptor`, `schoolReference`, `staffReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programAssignmentDescriptor` | key | descriptor URI | The name of the program for which the individual is assigned. |
| `calendarReference` |  | reference: `calendarCode`, `schoolId`, `schoolYear` |  |
| `schoolReference` | key | reference: `schoolId` |  |
| `schoolYearTypeReference` |  | reference: `schoolYear` |  |
| `staffReference` | key | reference: `staffUniqueId` |  |
| `academicSubjects` |  | array of edFi_staffSchoolAssociationAcademicSubject | An unordered collection of staffSchoolAssociationAcademicSubjects. |
| `gradeLevels` |  | array of edFi_staffSchoolAssociationGradeLevel | An unordered collection of staffSchoolAssociationGradeLevels. |

## Endpoints

- `DELETE /ed-fi/staffSchoolAssociations/{id}`
- `GET /ed-fi/staffSchoolAssociations/deletes`
- `GET /ed-fi/staffSchoolAssociations/keyChanges`
- `GET /ed-fi/staffSchoolAssociations/partitions`
- `GET /ed-fi/staffSchoolAssociations/{id}`
- `GET /ed-fi/staffSchoolAssociations`
- `POST /ed-fi/staffSchoolAssociations`
- `PUT /ed-fi/staffSchoolAssociations/{id}`
