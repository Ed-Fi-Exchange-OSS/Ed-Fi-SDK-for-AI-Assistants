# assessmentAdministrations

`/ed-fi/assessmentAdministrations`

The anticipated administration of an assessment under the purview of an education organization.

## Natural key

`administrationIdentifier`, `assessmentReference`, `assigningEducationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `administrationIdentifier` | key | string max 255 | The title or name of the assessment in the context of its administration. |
| `assessmentReference` | key | reference: `assessmentIdentifier`, `namespace` |  |
| `assigningEducationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `assessmentBatteryParts` |  | array of edFi_assessmentAdministrationAssessmentBatteryPart | An unordered collection of assessmentAdministrationAssessmentBatteryParts. |
| `periods` |  | array of edFi_assessmentAdministrationPeriod | An unordered collection of assessmentAdministrationPeriods. |

## Endpoints

- `DELETE /ed-fi/assessmentAdministrations/{id}`
- `GET /ed-fi/assessmentAdministrations/deletes`
- `GET /ed-fi/assessmentAdministrations/keyChanges`
- `GET /ed-fi/assessmentAdministrations/partitions`
- `GET /ed-fi/assessmentAdministrations/{id}`
- `GET /ed-fi/assessmentAdministrations`
- `POST /ed-fi/assessmentAdministrations`
- `PUT /ed-fi/assessmentAdministrations/{id}`
