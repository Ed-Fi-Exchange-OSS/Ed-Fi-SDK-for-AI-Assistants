# studentAssessmentRegistrationBatteryPartAssociations

`/ed-fi/studentAssessmentRegistrationBatteryPartAssociations`

The association to the part(s) of the assessment battery that the student is to be tested for this
administration of the assessment.

## Natural key

`assessmentBatteryPartReference`, `studentAssessmentRegistrationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentBatteryPartReference` | key | reference: `assessmentBatteryPartName`, `assessmentIdentifier`, `namespace` |  |
| `studentAssessmentRegistrationReference` | key | reference: `administrationIdentifier`, `assessmentIdentifier`, `assigningEducationOrganizationId`, `educationOrganizationId`, `namespace`, `studentUniqueId` |  |
| `accommodations` |  | array of edFi_studentAssessmentRegistrationBatteryPartAssociationAccommodation | An unordered collection of studentAssessmentRegistrationBatteryPartAssociationAccommodations. |

## Endpoints

- `DELETE /ed-fi/studentAssessmentRegistrationBatteryPartAssociations/{id}`
- `GET /ed-fi/studentAssessmentRegistrationBatteryPartAssociations/deletes`
- `GET /ed-fi/studentAssessmentRegistrationBatteryPartAssociations/keyChanges`
- `GET /ed-fi/studentAssessmentRegistrationBatteryPartAssociations/partitions`
- `GET /ed-fi/studentAssessmentRegistrationBatteryPartAssociations/{id}`
- `GET /ed-fi/studentAssessmentRegistrationBatteryPartAssociations`
- `POST /ed-fi/studentAssessmentRegistrationBatteryPartAssociations`
- `PUT /ed-fi/studentAssessmentRegistrationBatteryPartAssociations/{id}`
