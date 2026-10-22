# studentCohortAssociations

`/ed-fi/studentCohortAssociations`

This association represents the cohort(s) for which a student is designated.

## Natural key

`beginDate`, `cohortReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | The month, day, and year on which the student was first identified as part of the cohort. |
| `cohortReference` | key | reference: `cohortIdentifier`, `educationOrganizationId` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `endDate` |  | string (date) | The month, day, and year on which the student was removed as part of the cohort. |
| `sections` |  | array of edFi_studentCohortAssociationSection | An unordered collection of studentCohortAssociationSections. |

## Endpoints

- `DELETE /ed-fi/studentCohortAssociations/{id}`
- `GET /ed-fi/studentCohortAssociations/deletes`
- `GET /ed-fi/studentCohortAssociations/keyChanges`
- `GET /ed-fi/studentCohortAssociations/partitions`
- `GET /ed-fi/studentCohortAssociations/{id}`
- `GET /ed-fi/studentCohortAssociations`
- `POST /ed-fi/studentCohortAssociations`
- `PUT /ed-fi/studentCohortAssociations/{id}`
