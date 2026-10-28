# staffCohortAssociations

`/ed-fi/staffCohortAssociations`

This association indicates the staff associated with a cohort of students.

## Natural key

`beginDate`, `cohortIdentifier`, `educationOrganizationId`, `staffUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | Start date for the association of staff to this cohort. |
| `cohortReference` | yes | reference; supply `cohortIdentifier`, `educationOrganizationId` | This entity represents any type of list of designated students for tracking, analysis, or intervention. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `endDate` |  | string (date) | End date for the association of staff to this cohort. |
| `studentRecordAccess` |  | boolean | Indicator of whether the staff has access to the student records of the cohort per district interpretation of FERPA and other privacy laws, regulations, and po… |

## Endpoints

- `GET /ed-fi/staffCohortAssociations`
- `POST /ed-fi/staffCohortAssociations`
- `GET /ed-fi/staffCohortAssociations/deletes`
- `GET /ed-fi/staffCohortAssociations/keyChanges`
- `GET /ed-fi/staffCohortAssociations/partitions`
- `GET /ed-fi/staffCohortAssociations/{id}`
- `PUT /ed-fi/staffCohortAssociations/{id}`
- `DELETE /ed-fi/staffCohortAssociations/{id}`
