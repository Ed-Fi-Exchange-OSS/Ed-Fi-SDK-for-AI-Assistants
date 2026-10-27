# assessmentAdministrations

`/ed-fi/assessmentAdministrations`

The anticipated administration of an assessment under the purview of an education organization.

## Natural key

`administrationIdentifier`, `assessmentIdentifier`, `namespace`, `assigningEducationOrganizationId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `administrationIdentifier` | yes | string max 255 | The title or name of the assessment in the context of its administration. |
| `assessmentReference` | yes | reference; supply `assessmentIdentifier`, `namespace` | This entity represents a tool, instrument, process, or exhibition composed of a systematic sampling of behavior for measuring a student's competence, knowledge… |
| `assigningEducationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `assessmentBatteryParts` |  | array of edFi_assessmentAdministrationAssessmentBatteryPart | An unordered collection of assessmentAdministrationAssessmentBatteryParts. |
| `periods` |  | array of edFi_assessmentAdministrationPeriod | An unordered collection of assessmentAdministrationPeriods. |

### Items in `assessmentBatteryParts`

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentBatteryPartReference` | yes | reference; supply `assessmentBatteryPartName`, `assessmentIdentifier`, `namespace` | The parts organized for administering an assessessment which together provide a comprehensive assessment of the students. |

### Items in `periods`

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The month, day, and year for the start of the period. |
| `endDate` |  | string (date) | The month, day, and year for the end of the period. |

## Endpoints

- `GET /ed-fi/assessmentAdministrations`
- `POST /ed-fi/assessmentAdministrations`
- `GET /ed-fi/assessmentAdministrations/deletes`
- `GET /ed-fi/assessmentAdministrations/keyChanges`
- `GET /ed-fi/assessmentAdministrations/partitions`
- `GET /ed-fi/assessmentAdministrations/{id}`
- `PUT /ed-fi/assessmentAdministrations/{id}`
- `DELETE /ed-fi/assessmentAdministrations/{id}`
