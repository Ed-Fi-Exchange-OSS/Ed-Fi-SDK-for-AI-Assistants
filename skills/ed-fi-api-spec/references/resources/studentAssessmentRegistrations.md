# studentAssessmentRegistrations

`/ed-fi/studentAssessmentRegistrations`

Identifies an assessment registration that a student is expected to participate in including the testing
organization, reporting organization and assessment delivery details.

## Natural key

`administrationIdentifier`, `assessmentIdentifier`, `assigningEducationOrganizationId`, `namespace`,
`educationOrganizationId`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentAdministrationReference` | yes | reference; supply `administrationIdentifier`, `assessmentIdentifier`, `assigningEducationOrganizationId`, `namespace` | The anticipated administration of an assessment under the purview of an education organization. |
| `reportingEducationOrganizationReference` |  | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `scheduledStudentEducationOrganizationAssessmentAccommodationReference` |  | reference; supply `educationOrganizationId`, `studentUniqueId` | The accommodation(s) required or expected for administering assessments as determined by the education organization. |
| `studentEducationOrganizationAssociationReference` | yes | reference; supply `educationOrganizationId`, `studentUniqueId` | This association represents student information as reported in the context of the student's relationship to the education organization. |
| `studentSchoolAssociationReference` | yes | reference; supply `entryDate`, `schoolId`, `studentUniqueId` | This association represents the school in which a student is enrolled. |
| `testingEducationOrganizationReference` |  | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `assessmentAccommodations` |  | array of edFi_studentAssessmentRegistrationAssessmentAccommodation | An unordered collection of studentAssessmentRegistrationAssessmentAccommodations. |
| `assessmentCustomizations` |  | array of edFi_studentAssessmentRegistrationAssessmentCustomization | An unordered collection of studentAssessmentRegistrationAssessmentCustomizations. |
| `assessmentGradeLevelDescriptor` |  | descriptor URI | The grade level or primary instructional level at which the student is to be assessed. |
| `platformTypeDescriptor` |  | descriptor URI | The environment or format in which the assessment is expected to be administered. |

### Items in `assessmentAccommodations`

| Field | Required | Type | Description |
|---|---|---|---|
| `accommodationDescriptor` | yes | descriptor URI | The special variation(s) to be used in how assessments (in general) are presented, how it is administered, or how the test taker is allowed to respond. |

### Items in `assessmentCustomizations`

| Field | Required | Type | Description |
|---|---|---|---|
| `customizationKey` | yes | string max 60 | An agreed upon identifier for the custom information. |
| `customizationValue` | yes | string max 1024 | Custom value for the indicated CustomizationKey. |

## Endpoints

- `GET /ed-fi/studentAssessmentRegistrations`
- `POST /ed-fi/studentAssessmentRegistrations`
- `GET /ed-fi/studentAssessmentRegistrations/deletes`
- `GET /ed-fi/studentAssessmentRegistrations/keyChanges`
- `GET /ed-fi/studentAssessmentRegistrations/partitions`
- `GET /ed-fi/studentAssessmentRegistrations/{id}`
- `PUT /ed-fi/studentAssessmentRegistrations/{id}`
- `DELETE /ed-fi/studentAssessmentRegistrations/{id}`
