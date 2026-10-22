# evaluationElements

`/tpdm/evaluationElements`

The lowest-level Elements or criterion of performance being evaluated by rubric, quantitative measure, or aggregate survey response.

## Natural key

`evaluationElementTitle`, `evaluationObjectiveReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationElementTitle` | key | string max 255 | The name or title of the evaluation element. |
| `evaluationObjectiveReference` | key | reference: `educationOrganizationId`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` |  |
| `evaluationTypeDescriptor` |  | descriptor URI | The type of the evaluation (e.g., observation, principal, peer, student survey, student growth). |
| `maxRating` |  | number (double) | The maximum summary numerical rating or score for the evaluation element. |
| `minRating` |  | number (double) | The minimum summary numerical rating or score for the evaluation element. |
| `ratingLevels` |  | array of tpdm_evaluationElementRatingLevel | An unordered collection of evaluationElementRatingLevels. |
| `sortOrder` |  | integer (int32) | The sort order of this Evaluation Element. |

## Endpoints

- `DELETE /tpdm/evaluationElements/{id}`
- `GET /tpdm/evaluationElements/deletes`
- `GET /tpdm/evaluationElements/keyChanges`
- `GET /tpdm/evaluationElements/partitions`
- `GET /tpdm/evaluationElements/{id}`
- `GET /tpdm/evaluationElements`
- `POST /tpdm/evaluationElements`
- `PUT /tpdm/evaluationElements/{id}`
