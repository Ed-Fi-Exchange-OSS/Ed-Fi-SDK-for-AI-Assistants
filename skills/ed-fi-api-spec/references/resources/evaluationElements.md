# evaluationElements

`/tpdm/evaluationElements`

The lowest-level Elements or criterion of performance being evaluated by rubric, quantitative measure, or
aggregate survey response.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationElementTitle` | yes | string max 255 | The name or title of the evaluation element. |
| `evaluationObjectiveReference` | yes | reference; supply `educationOrganizationId`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | A subcomponent of an Evaluation, a specific educator Objective or domain of performance that is being evaluated. |
| `evaluationTypeDescriptor` |  | descriptor URI | The type of the evaluation (e.g., observation, principal, peer, student survey, student growth). |
| `maxRating` |  | number (double) | The maximum summary numerical rating or score for the evaluation element. |
| `minRating` |  | number (double) | The minimum summary numerical rating or score for the evaluation element. |
| `ratingLevels` |  | array of tpdm_evaluationElementRatingLevel | An unordered collection of evaluationElementRatingLevels. |
| `sortOrder` |  | integer (int32) | The sort order of this Evaluation Element. |

### Items in `ratingLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationRatingLevelDescriptor` | yes | descriptor URI | The title for a level of rating or evaluation band (e.g., Excellent, Acceptable, Needs Improvement, Unacceptable). |
| `maxRating` |  | number (double) | The maximum numerical rating or score to achieve the evaluation rating level. |
| `minRating` |  | number (double) | The minimum numerical rating or score to achieve the evaluation rating level. |

## Endpoints

- `GET /tpdm/evaluationElements`
- `POST /tpdm/evaluationElements`
- `GET /tpdm/evaluationElements/deletes`
- `GET /tpdm/evaluationElements/keyChanges`
- `GET /tpdm/evaluationElements/partitions`
- `GET /tpdm/evaluationElements/{id}`
- `PUT /tpdm/evaluationElements/{id}`
- `DELETE /tpdm/evaluationElements/{id}`
