# cohorts

`/ed-fi/cohorts`

This entity represents any type of list of designated students for tracking, analysis, or intervention.

## Natural key

`cohortIdentifier`, `educationOrganizationId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `cohortIdentifier` | yes | string max 36 | The name or ID for the cohort. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `academicSubjectDescriptor` |  | descriptor URI | The academic subject associated with an academic intervention. |
| `cohortDescription` |  | string max 1024 | The description of the cohort and its purpose. |
| `cohortScopeDescriptor` |  | descriptor URI | The scope of cohort (e.g., school, district, classroom). |
| `cohortTypeDescriptor` | yes | descriptor URI | The type of cohort (e.g., academic intervention, classroom breakout). |
| `programs` |  | array of edFi_cohortProgram | An unordered collection of cohortPrograms. |

### Items in `programs`

| Field | Required | Type | Description |
|---|---|---|---|
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |

## Endpoints

- `GET /ed-fi/cohorts`
- `POST /ed-fi/cohorts`
- `GET /ed-fi/cohorts/deletes`
- `GET /ed-fi/cohorts/keyChanges`
- `GET /ed-fi/cohorts/partitions`
- `GET /ed-fi/cohorts/{id}`
- `PUT /ed-fi/cohorts/{id}`
- `DELETE /ed-fi/cohorts/{id}`
