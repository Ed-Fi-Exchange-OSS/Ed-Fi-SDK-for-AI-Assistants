# evaluations

`/ed-fi/evaluations`

An evaluation instrument applied to evaluate an educator. The evaluation could be internally developed, or
could be an industry recognized instrument such as TTESS or Marzano.

## Natural key

`evaluationTitle`, `educationOrganizationId`, `evaluationPeriodDescriptor`, `performanceEvaluationTitle`,
`performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationTitle` | yes | string max 50 | The name or title of the evaluation. |
| `performanceEvaluationReference` | yes | reference; supply `educationOrganizationId`, `evaluationPeriodDescriptor`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | A performance evaluation of an educator, typically regularly scheduled and uniformly applied, composed of one or more evaluations. |
| `evaluationDescription` |  | string max 255 | The long description of the evaluation. |
| `evaluationTypeDescriptor` |  | descriptor URI | The type of the evaluation. |
| `interRaterReliabilityScore` |  | integer (int32) | A score indicating how much homogeneity, or consensus, there is in the ratings given by judges. |
| `maxNumericRating` |  | number (double) | The maximum summary numerical rating or score for the evaluation. |
| `minNumericRating` |  | number (double) | The minimum summary numerical rating or score for the evaluation. |
| `ratingLevels` |  | array of edFi_evaluationRatingLevel | An unordered collection of evaluationRatingLevels. |

### Items in `ratingLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationRatingLevelDescriptor` | yes | descriptor URI | The title for a level of rating or evaluation band. |
| `maxNumericRating` |  | number (double) | The maximum numerical rating or score to achieve the evaluation rating level. |
| `minNumericRating` |  | number (double) | The minimum numerical rating or score to achieve the evaluation rating level. |

## Endpoints

- `GET /ed-fi/evaluations`
- `POST /ed-fi/evaluations`
- `GET /ed-fi/evaluations/deletes`
- `GET /ed-fi/evaluations/keyChanges`
- `GET /ed-fi/evaluations/partitions`
- `GET /ed-fi/evaluations/{id}`
- `PUT /ed-fi/evaluations/{id}`
- `DELETE /ed-fi/evaluations/{id}`
