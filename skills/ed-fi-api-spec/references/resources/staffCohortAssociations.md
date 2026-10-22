# staffCohortAssociations

`/ed-fi/staffCohortAssociations`

This association indicates the staff associated with a cohort of students.

## Natural key

`beginDate`, `cohortReference`, `staffReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | Start date for the association of staff to this cohort. |
| `cohortReference` | key | reference: `cohortIdentifier`, `educationOrganizationId` |  |
| `staffReference` | key | reference: `staffUniqueId` |  |
| `endDate` |  | string (date) | End date for the association of staff to this cohort. |
| `studentRecordAccess` |  | boolean | Indicator of whether the staff has access to the student records of the cohort per district interpretation of FERPA and other privacy laws, regulations, and po… |

## Endpoints

- `DELETE /ed-fi/staffCohortAssociations/{id}`
- `GET /ed-fi/staffCohortAssociations/deletes`
- `GET /ed-fi/staffCohortAssociations/keyChanges`
- `GET /ed-fi/staffCohortAssociations/partitions`
- `GET /ed-fi/staffCohortAssociations/{id}`
- `GET /ed-fi/staffCohortAssociations`
- `POST /ed-fi/staffCohortAssociations`
- `PUT /ed-fi/staffCohortAssociations/{id}`
