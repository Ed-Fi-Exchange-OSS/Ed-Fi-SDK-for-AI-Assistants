# evaluationElements

`/ed-fi/evaluationElements`

The lowest-level elements or criterion of performance being evaluated by rubric, quantitative measure, or
aggregate survey response.

## Natural key

`evaluationElementTitle`, `educationOrganizationId`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`,
`evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`,
`termDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationElementTitle` | yes | string max 255 | The name or title of the evaluation element. |
| `evaluationObjectiveReference` | yes | reference; supply `educationOrganizationId`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | A sub-component of an evaluation, a specific educator objective or domain of performance that is being evaluated. |
| `evaluationTypeDescriptor` |  | descriptor URI | The type of the evaluation. |
| `maxNumericRating` |  | number (double) | The maximum summary numerical rating or score for the evaluation element. |
| `minNumericRating` |  | number (double) | The minimum summary numerical rating or score for the evaluation element. |
| `ratingLevels` |  | array of edFi_evaluationElementRatingLevel | An unordered collection of evaluationElementRatingLevels. |
| `sortOrder` |  | integer (int32) | The sort order of the evaluation element. |

### Items in `ratingLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationRatingLevelDescriptor` | yes | descriptor URI | The title for a level of rating or evaluation band. |
| `maxNumericRating` |  | number (double) | The maximum numerical rating or score to achieve the evaluation rating level. |
| `minNumericRating` |  | number (double) | The minimum numerical rating or score to achieve the evaluation rating level. |

## Endpoints

- `GET /ed-fi/evaluationElements`
- `POST /ed-fi/evaluationElements`
- `GET /ed-fi/evaluationElements/deletes`
- `GET /ed-fi/evaluationElements/keyChanges`
- `GET /ed-fi/evaluationElements/partitions`
- `GET /ed-fi/evaluationElements/{id}`
- `PUT /ed-fi/evaluationElements/{id}`
- `DELETE /ed-fi/evaluationElements/{id}`
