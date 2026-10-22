# assessmentScoreRangeLearningStandards

`/ed-fi/assessmentScoreRangeLearningStandards`

Score ranges of an assessment associated with one or more learning standards.

## Natural key

`scoreRangeId`, `assessmentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `learningStandards` | yes | array of edFi_assessmentScoreRangeLearningStandardLearningStandard | An unordered collection of assessmentScoreRangeLearningStandardLearningStandards. |
| `scoreRangeId` | key | string max 60 | A unique number or alphanumeric code assigned to the score range associated with one or more learning standards. |
| `assessmentReference` | key | reference: `assessmentIdentifier`, `namespace` |  |
| `objectiveAssessmentReference` |  | reference: `assessmentIdentifier`, `identificationCode`, `namespace` |  |
| `assessmentReportingMethodDescriptor` |  | descriptor URI | The assessment reporting method defined (e.g., scale score, RIT scale score) associated with the referenced learning standard(s). |
| `maximumScore` | yes | string max 35 | The maximum score in the score range. |
| `minimumScore` | yes | string max 35 | The minimum score in the score range. |

## Endpoints

- `DELETE /ed-fi/assessmentScoreRangeLearningStandards/{id}`
- `GET /ed-fi/assessmentScoreRangeLearningStandards/deletes`
- `GET /ed-fi/assessmentScoreRangeLearningStandards/keyChanges`
- `GET /ed-fi/assessmentScoreRangeLearningStandards/partitions`
- `GET /ed-fi/assessmentScoreRangeLearningStandards/{id}`
- `GET /ed-fi/assessmentScoreRangeLearningStandards`
- `POST /ed-fi/assessmentScoreRangeLearningStandards`
- `PUT /ed-fi/assessmentScoreRangeLearningStandards/{id}`
