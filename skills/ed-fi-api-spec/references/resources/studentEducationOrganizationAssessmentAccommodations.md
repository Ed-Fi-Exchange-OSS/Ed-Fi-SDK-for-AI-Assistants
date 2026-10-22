# studentEducationOrganizationAssessmentAccommodations

`/ed-fi/studentEducationOrganizationAssessmentAccommodations`

The accommodation(s) required or expected for administering assessments as determined by the education
organization.

## Natural key

`educationOrganizationReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `generalAccommodations` |  | array of edFi_studentEducationOrganizationAssessmentAccommodationGeneralAccommodation | An unordered collection of studentEducationOrganizationAssessmentAccommodationGeneralAccommodations. |

## Endpoints

- `DELETE /ed-fi/studentEducationOrganizationAssessmentAccommodations/{id}`
- `GET /ed-fi/studentEducationOrganizationAssessmentAccommodations/deletes`
- `GET /ed-fi/studentEducationOrganizationAssessmentAccommodations/keyChanges`
- `GET /ed-fi/studentEducationOrganizationAssessmentAccommodations/partitions`
- `GET /ed-fi/studentEducationOrganizationAssessmentAccommodations/{id}`
- `GET /ed-fi/studentEducationOrganizationAssessmentAccommodations`
- `POST /ed-fi/studentEducationOrganizationAssessmentAccommodations`
- `PUT /ed-fi/studentEducationOrganizationAssessmentAccommodations/{id}`
