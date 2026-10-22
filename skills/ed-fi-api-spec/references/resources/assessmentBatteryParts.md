# assessmentBatteryParts

`/ed-fi/assessmentBatteryParts`

The parts organized for administering an assessessment which together provide a comprehensive assessment of
the students.

## Natural key

`assessmentBatteryPartName`, `assessmentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentBatteryPartName` | key | string max 65 | The name of the part of an assessment battery. |
| `assessmentReference` | key | reference: `assessmentIdentifier`, `namespace` |  |
| `objectiveAssessments` |  | array of edFi_assessmentBatteryPartObjectiveAssessment | An unordered collection of assessmentBatteryPartObjectiveAssessments. |

## Endpoints

- `DELETE /ed-fi/assessmentBatteryParts/{id}`
- `GET /ed-fi/assessmentBatteryParts/deletes`
- `GET /ed-fi/assessmentBatteryParts/keyChanges`
- `GET /ed-fi/assessmentBatteryParts/partitions`
- `GET /ed-fi/assessmentBatteryParts/{id}`
- `GET /ed-fi/assessmentBatteryParts`
- `POST /ed-fi/assessmentBatteryParts`
- `PUT /ed-fi/assessmentBatteryParts/{id}`
