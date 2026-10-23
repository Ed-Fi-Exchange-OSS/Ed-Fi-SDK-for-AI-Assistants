# assessmentBatteryParts

`/ed-fi/assessmentBatteryParts`

The parts organized for administering an assessessment which together provide a comprehensive assessment of
the students.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentBatteryPartName` | yes | string max 65 | The name of the part of an assessment battery. |
| `assessmentReference` | yes | reference; supply `assessmentIdentifier`, `namespace` | This entity represents a tool, instrument, process, or exhibition composed of a systematic sampling of behavior for measuring a student's competence, knowledge… |
| `objectiveAssessments` |  | array of edFi_assessmentBatteryPartObjectiveAssessment | An unordered collection of assessmentBatteryPartObjectiveAssessments. |

### Items in `objectiveAssessments`

| Field | Required | Type | Description |
|---|---|---|---|
| `objectiveAssessmentReference` | yes | reference; supply `assessmentIdentifier`, `identificationCode`, `namespace` | This entity represents subtests that assess specific learning objectives. |

## Endpoints

- `GET /ed-fi/assessmentBatteryParts`
- `POST /ed-fi/assessmentBatteryParts`
- `GET /ed-fi/assessmentBatteryParts/deletes`
- `GET /ed-fi/assessmentBatteryParts/keyChanges`
- `GET /ed-fi/assessmentBatteryParts/partitions`
- `GET /ed-fi/assessmentBatteryParts/{id}`
- `PUT /ed-fi/assessmentBatteryParts/{id}`
- `DELETE /ed-fi/assessmentBatteryParts/{id}`
