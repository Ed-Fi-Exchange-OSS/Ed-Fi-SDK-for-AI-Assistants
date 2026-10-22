# evaluationElementRatings

`/tpdm/evaluationElementRatings`

The lowest-level rating for an Evaluation Element for an individual educator.

## Natural key

`evaluationElementReference`, `evaluationObjectiveRatingReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationElementReference` | key | reference: `educationOrganizationId`, `evaluationElementTitle`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` |  |
| `evaluationObjectiveRatingReference` | key | reference: `educationOrganizationId`, `evaluationDate`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `personId`, `schoolYear`, `sourceSystemDescriptor`, `termDescriptor` |  |
| `areaOfRefinement` |  | string max 1024 | Area identified for person to refine or improve as part of the evaluation. |
| `areaOfReinforcement` |  | string max 1024 | Area identified for reinforcement or positive feedback as part of the evaluation. |
| `comments` |  | string max 1024 | Any comments about the performance evaluation to be captured. |
| `evaluationElementRatingLevelDescriptor` |  | descriptor URI | The rating level achieved based upon the rating or score. |
| `feedback` |  | string max 2048 | Feedback provided to the evaluated person. |
| `results` |  | array of tpdm_evaluationElementRatingResult | An unordered collection of evaluationElementRatingResults. |

## Endpoints

- `DELETE /tpdm/evaluationElementRatings/{id}`
- `GET /tpdm/evaluationElementRatings/deletes`
- `GET /tpdm/evaluationElementRatings/keyChanges`
- `GET /tpdm/evaluationElementRatings/partitions`
- `GET /tpdm/evaluationElementRatings/{id}`
- `GET /tpdm/evaluationElementRatings`
- `POST /tpdm/evaluationElementRatings`
- `PUT /tpdm/evaluationElementRatings/{id}`
