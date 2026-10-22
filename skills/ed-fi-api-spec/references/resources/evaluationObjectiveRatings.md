# evaluationObjectiveRatings

`/tpdm/evaluationObjectiveRatings`

The rating for the component Evaluation Objective for an individual educator.

## Natural key

`evaluationObjectiveReference`, `evaluationRatingReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationObjectiveReference` | key | reference: `educationOrganizationId`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` |  |
| `evaluationRatingReference` | key | reference: `educationOrganizationId`, `evaluationDate`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `personId`, `schoolYear`, `sourceSystemDescriptor`, `termDescriptor` |  |
| `comments` |  | string max 1024 | Any comments about the performance evaluation to be captured. |
| `objectiveRatingLevelDescriptor` |  | descriptor URI | The rating level achieved based upon the rating or score. |
| `results` |  | array of tpdm_evaluationObjectiveRatingResult | An unordered collection of evaluationObjectiveRatingResults. |

## Endpoints

- `DELETE /tpdm/evaluationObjectiveRatings/{id}`
- `GET /tpdm/evaluationObjectiveRatings/deletes`
- `GET /tpdm/evaluationObjectiveRatings/keyChanges`
- `GET /tpdm/evaluationObjectiveRatings/partitions`
- `GET /tpdm/evaluationObjectiveRatings/{id}`
- `GET /tpdm/evaluationObjectiveRatings`
- `POST /tpdm/evaluationObjectiveRatings`
- `PUT /tpdm/evaluationObjectiveRatings/{id}`
