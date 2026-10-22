# studentAssessmentRegistrations

`/ed-fi/studentAssessmentRegistrations`

Identifies an assessment registration that a student is expected to participate in including the testing organization, reporting organization and assessment delivery details.

## Natural key

`assessmentAdministrationReference`, `studentEducationOrganizationAssociationReference`, `studentSchoolAssociationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentAdministrationReference` | key | reference: `administrationIdentifier`, `assessmentIdentifier`, `assigningEducationOrganizationId`, `namespace` |  |
| `reportingEducationOrganizationReference` |  | reference: `educationOrganizationId` |  |
| `scheduledStudentEducationOrganizationAssessmentAccommodationReference` |  | reference: `educationOrganizationId`, `studentUniqueId` |  |
| `studentEducationOrganizationAssociationReference` | key | reference: `educationOrganizationId`, `studentUniqueId` |  |
| `studentSchoolAssociationReference` | key | reference: `entryDate`, `schoolId`, `studentUniqueId` |  |
| `testingEducationOrganizationReference` |  | reference: `educationOrganizationId` |  |
| `assessmentAccommodations` |  | array of edFi_studentAssessmentRegistrationAssessmentAccommodation | An unordered collection of studentAssessmentRegistrationAssessmentAccommodations. |
| `assessmentCustomizations` |  | array of edFi_studentAssessmentRegistrationAssessmentCustomization | An unordered collection of studentAssessmentRegistrationAssessmentCustomizations. |
| `assessmentGradeLevelDescriptor` |  | descriptor URI | The grade level or primary instructional level at which the student is to be assessed. |
| `platformTypeDescriptor` |  | descriptor URI | The environment or format in which the assessment is expected to be administered. |

## Endpoints

- `DELETE /ed-fi/studentAssessmentRegistrations/{id}`
- `GET /ed-fi/studentAssessmentRegistrations/deletes`
- `GET /ed-fi/studentAssessmentRegistrations/keyChanges`
- `GET /ed-fi/studentAssessmentRegistrations/partitions`
- `GET /ed-fi/studentAssessmentRegistrations/{id}`
- `GET /ed-fi/studentAssessmentRegistrations`
- `POST /ed-fi/studentAssessmentRegistrations`
- `PUT /ed-fi/studentAssessmentRegistrations/{id}`
