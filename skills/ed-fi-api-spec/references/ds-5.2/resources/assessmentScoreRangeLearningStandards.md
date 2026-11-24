# assessmentScoreRangeLearningStandards

`/ed-fi/assessmentScoreRangeLearningStandards`

Score ranges of an assessment associated with one or more learning standards.

## Natural key

`scoreRangeId`, `assessmentIdentifier`, `namespace`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `learningStandards` | yes | array of edFi_assessmentScoreRangeLearningStandardLearningStandard | An unordered collection of assessmentScoreRangeLearningStandardLearningStandards. |
| `scoreRangeId` | yes | string max 60 | A unique number or alphanumeric code assigned to the score range associated with one or more learning standards. |
| `assessmentReference` | yes | reference; supply `assessmentIdentifier`, `namespace` | This entity represents a tool, instrument, process, or exhibition composed of a systematic sampling of behavior for measuring a student's competence, knowledge… |
| `objectiveAssessmentReference` |  | reference; supply `assessmentIdentifier`, `identificationCode`, `namespace` | This entity represents subtests that assess specific learning objectives. |
| `assessmentReportingMethodDescriptor` |  | descriptor URI | The assessment reporting method defined (e.g., scale score, RIT scale score) associated with the referenced learning standard(s). |
| `maximumScore` | yes | string max 35 | The maximum score in the score range. |
| `minimumScore` | yes | string max 35 | The minimum score in the score range. |

### Items in `learningStandards`

| Field | Required | Type | Description |
|---|---|---|---|
| `learningStandardReference` | yes | reference; supply `learningStandardId` | A statement that describes a specific competency or academic standard. |

## Endpoints

- `GET /ed-fi/assessmentScoreRangeLearningStandards`
- `POST /ed-fi/assessmentScoreRangeLearningStandards`
- `GET /ed-fi/assessmentScoreRangeLearningStandards/deletes`
- `GET /ed-fi/assessmentScoreRangeLearningStandards/keyChanges`
- `GET /ed-fi/assessmentScoreRangeLearningStandards/partitions`
- `GET /ed-fi/assessmentScoreRangeLearningStandards/{id}`
- `PUT /ed-fi/assessmentScoreRangeLearningStandards/{id}`
- `DELETE /ed-fi/assessmentScoreRangeLearningStandards/{id}`
