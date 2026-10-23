# studentAssessmentRegistrationBatteryPartAssociations

`/ed-fi/studentAssessmentRegistrationBatteryPartAssociations`

The association to the part(s) of the assessment battery that the student is to be tested for this
administration of the assessment.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentBatteryPartReference` | yes | reference; supply `assessmentBatteryPartName`, `assessmentIdentifier`, `namespace` | The parts organized for administering an assessessment which together provide a comprehensive assessment of the students. |
| `studentAssessmentRegistrationReference` | yes | reference; supply `administrationIdentifier`, `assessmentIdentifier`, `assigningEducationOrganizationId`, `educationOrganizationId`, `namespace`, `studentUniqueId` | Identifies an assessment registration that a student is expected to participate in including the testing organization, reporting organization and assessment de… |
| `accommodations` |  | array of edFi_studentAssessmentRegistrationBatteryPartAssociationAccommodation | An unordered collection of studentAssessmentRegistrationBatteryPartAssociationAccommodations. |

### Items in `accommodations`

| Field | Required | Type | Description |
|---|---|---|---|
| `accommodationDescriptor` | yes | descriptor URI | The special variation(s) to be used for the specific part of the assessment battery on how is presented, how it is administered, or how the test taker is allow… |

## Endpoints

- `GET /ed-fi/studentAssessmentRegistrationBatteryPartAssociations`
- `POST /ed-fi/studentAssessmentRegistrationBatteryPartAssociations`
- `GET /ed-fi/studentAssessmentRegistrationBatteryPartAssociations/deletes`
- `GET /ed-fi/studentAssessmentRegistrationBatteryPartAssociations/keyChanges`
- `GET /ed-fi/studentAssessmentRegistrationBatteryPartAssociations/partitions`
- `GET /ed-fi/studentAssessmentRegistrationBatteryPartAssociations/{id}`
- `PUT /ed-fi/studentAssessmentRegistrationBatteryPartAssociations/{id}`
- `DELETE /ed-fi/studentAssessmentRegistrationBatteryPartAssociations/{id}`
