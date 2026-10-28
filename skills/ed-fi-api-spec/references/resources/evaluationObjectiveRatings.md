# evaluationObjectiveRatings

`/tpdm/evaluationObjectiveRatings`

The rating for the component Evaluation Objective for an individual educator.

## Natural key

`educationOrganizationId`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`,
`performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor`,
`evaluationDate`, `personId`, `sourceSystemDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationObjectiveReference` | yes | reference; supply `educationOrganizationId`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | A subcomponent of an Evaluation, a specific educator Objective or domain of performance that is being evaluated. |
| `evaluationRatingReference` | yes | reference; supply `educationOrganizationId`, `evaluationDate`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `personId`, `schoolYear`, `sourceSystemDescriptor`, `termDescriptor` | The summary weighting for the Evaluation instrument for an individual educator. |
| `comments` |  | string max 1024 | Any comments about the performance evaluation to be captured. |
| `objectiveRatingLevelDescriptor` |  | descriptor URI | The rating level achieved based upon the rating or score. |
| `results` |  | array of tpdm_evaluationObjectiveRatingResult | An unordered collection of evaluationObjectiveRatingResults. |

### Items in `results`

| Field | Required | Type | Description |
|---|---|---|---|
| `rating` | yes | number (double) | The numerical summary rating or score for the evaluation. |
| `ratingResultTitle` | yes | string max 50 | The title of Rating Result. |
| `resultDatatypeTypeDescriptor` | yes | descriptor URI | The datatype of the result. |

## Endpoints

- `GET /tpdm/evaluationObjectiveRatings`
- `POST /tpdm/evaluationObjectiveRatings`
- `GET /tpdm/evaluationObjectiveRatings/deletes`
- `GET /tpdm/evaluationObjectiveRatings/keyChanges`
- `GET /tpdm/evaluationObjectiveRatings/partitions`
- `GET /tpdm/evaluationObjectiveRatings/{id}`
- `PUT /tpdm/evaluationObjectiveRatings/{id}`
- `DELETE /tpdm/evaluationObjectiveRatings/{id}`
