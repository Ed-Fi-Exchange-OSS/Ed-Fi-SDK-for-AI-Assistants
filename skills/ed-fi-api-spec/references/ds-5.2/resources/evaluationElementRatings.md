# evaluationElementRatings

`/tpdm/evaluationElementRatings`

The lowest-level rating for an Evaluation Element for an individual educator.

## Natural key

`educationOrganizationId`, `evaluationElementTitle`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`,
`evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`,
`termDescriptor`, `evaluationDate`, `personId`, `sourceSystemDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationElementReference` | yes | reference; supply `educationOrganizationId`, `evaluationElementTitle`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | The lowest-level Elements or criterion of performance being evaluated by rubric, quantitative measure, or aggregate survey response. |
| `evaluationObjectiveRatingReference` | yes | reference; supply `educationOrganizationId`, `evaluationDate`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `personId`, `schoolYear`, `sourceSystemDescriptor`, `termDescriptor` | The rating for the component Evaluation Objective for an individual educator. |
| `areaOfRefinement` |  | string max 1024 | Area identified for person to refine or improve as part of the evaluation. |
| `areaOfReinforcement` |  | string max 1024 | Area identified for reinforcement or positive feedback as part of the evaluation. |
| `comments` |  | string max 1024 | Any comments about the performance evaluation to be captured. |
| `evaluationElementRatingLevelDescriptor` |  | descriptor URI | The rating level achieved based upon the rating or score. |
| `feedback` |  | string max 2048 | Feedback provided to the evaluated person. |
| `results` |  | array of tpdm_evaluationElementRatingResult | An unordered collection of evaluationElementRatingResults. |

### Items in `results`

| Field | Required | Type | Description |
|---|---|---|---|
| `rating` | yes | number (double) | The numerical summary rating or score for the evaluation. |
| `ratingResultTitle` | yes | string max 50 | The title of Rating Result. |
| `resultDatatypeTypeDescriptor` | yes | descriptor URI | The datatype of the result. |

## Endpoints

- `GET /tpdm/evaluationElementRatings`
- `POST /tpdm/evaluationElementRatings`
- `GET /tpdm/evaluationElementRatings/deletes`
- `GET /tpdm/evaluationElementRatings/keyChanges`
- `GET /tpdm/evaluationElementRatings/partitions`
- `GET /tpdm/evaluationElementRatings/{id}`
- `PUT /tpdm/evaluationElementRatings/{id}`
- `DELETE /tpdm/evaluationElementRatings/{id}`
