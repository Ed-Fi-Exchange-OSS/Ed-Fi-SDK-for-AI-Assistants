# evaluationObjectives

`/ed-fi/evaluationObjectives`

A sub-component of an evaluation, a specific educator objective or domain of performance that is being
evaluated.

## Natural key

`evaluationObjectiveTitle`, `educationOrganizationId`, `evaluationPeriodDescriptor`, `evaluationTitle`,
`performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationObjectiveTitle` | yes | string max 50 | The name or title of the evaluation objective. |
| `evaluationReference` | yes | reference; supply `educationOrganizationId`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | An evaluation instrument applied to evaluate an educator. |
| `evaluationObjectiveDescription` |  | string max 255 | The long description of the evaluation objective. |
| `evaluationTypeDescriptor` |  | descriptor URI | The type of the evaluation objective. |
| `maxNumericRating` |  | number (double) | The maximum summary numerical rating or score for the evaluation objective. |
| `minNumericRating` |  | number (double) | The minimum summary numerical rating or score for the evaluation objective. |
| `ratingLevels` |  | array of edFi_evaluationObjectiveRatingLevel | An unordered collection of evaluationObjectiveRatingLevels. |
| `sortOrder` |  | integer (int32) | The sort order of the evaluation objective. |

### Items in `ratingLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationRatingLevelDescriptor` | yes | descriptor URI | The title for a level of rating or evaluation band. |
| `maxNumericRating` |  | number (double) | The maximum numerical rating or score to achieve the evaluation rating level. |
| `minNumericRating` |  | number (double) | The minimum numerical rating or score to achieve the evaluation rating level. |

## Endpoints

- `GET /ed-fi/evaluationObjectives`
- `POST /ed-fi/evaluationObjectives`
- `GET /ed-fi/evaluationObjectives/deletes`
- `GET /ed-fi/evaluationObjectives/keyChanges`
- `GET /ed-fi/evaluationObjectives/partitions`
- `GET /ed-fi/evaluationObjectives/{id}`
- `PUT /ed-fi/evaluationObjectives/{id}`
- `DELETE /ed-fi/evaluationObjectives/{id}`
