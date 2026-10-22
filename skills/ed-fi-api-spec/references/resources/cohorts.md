# cohorts

`/ed-fi/cohorts`

This entity represents any type of list of designated students for tracking, analysis, or intervention.

## Natural key

`cohortIdentifier`, `educationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `cohortIdentifier` | key | string max 36 | The name or ID for the cohort. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `academicSubjectDescriptor` |  | descriptor URI | The academic subject associated with an academic intervention. |
| `cohortDescription` |  | string max 1024 | The description of the cohort and its purpose. |
| `cohortScopeDescriptor` |  | descriptor URI | The scope of cohort (e.g., school, district, classroom). |
| `cohortTypeDescriptor` | yes | descriptor URI | The type of cohort (e.g., academic intervention, classroom breakout). |
| `programs` |  | array of edFi_cohortProgram | An unordered collection of cohortPrograms. |

## Endpoints

- `DELETE /ed-fi/cohorts/{id}`
- `GET /ed-fi/cohorts/deletes`
- `GET /ed-fi/cohorts/keyChanges`
- `GET /ed-fi/cohorts/partitions`
- `GET /ed-fi/cohorts/{id}`
- `GET /ed-fi/cohorts`
- `POST /ed-fi/cohorts`
- `PUT /ed-fi/cohorts/{id}`
