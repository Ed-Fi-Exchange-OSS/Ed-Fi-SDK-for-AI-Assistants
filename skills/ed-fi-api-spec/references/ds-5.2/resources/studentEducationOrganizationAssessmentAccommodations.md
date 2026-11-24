# studentEducationOrganizationAssessmentAccommodations

`/ed-fi/studentEducationOrganizationAssessmentAccommodations`

The accommodation(s) required or expected for administering assessments as determined by the education
organization.

## Natural key

`educationOrganizationId`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `generalAccommodations` |  | array of edFi_studentEducationOrganizationAssessmentAccommodationGeneralAccommodation | An unordered collection of studentEducationOrganizationAssessmentAccommodationGeneralAccommodations. |

### Items in `generalAccommodations`

| Field | Required | Type | Description |
|---|---|---|---|
| `accommodationDescriptor` | yes | descriptor URI | The special variation(s) to be used in how assessments (in general) are presented, how it is administered, or how the test taker is allowed to respond. |

## Endpoints

- `GET /ed-fi/studentEducationOrganizationAssessmentAccommodations`
- `POST /ed-fi/studentEducationOrganizationAssessmentAccommodations`
- `GET /ed-fi/studentEducationOrganizationAssessmentAccommodations/deletes`
- `GET /ed-fi/studentEducationOrganizationAssessmentAccommodations/keyChanges`
- `GET /ed-fi/studentEducationOrganizationAssessmentAccommodations/partitions`
- `GET /ed-fi/studentEducationOrganizationAssessmentAccommodations/{id}`
- `PUT /ed-fi/studentEducationOrganizationAssessmentAccommodations/{id}`
- `DELETE /ed-fi/studentEducationOrganizationAssessmentAccommodations/{id}`
