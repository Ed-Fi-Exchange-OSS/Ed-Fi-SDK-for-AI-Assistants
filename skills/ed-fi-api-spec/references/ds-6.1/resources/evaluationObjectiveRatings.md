# evaluationObjectiveRatings

`/ed-fi/evaluationObjectiveRatings`

The rating for the component evaluation objective for an individual educator.

## Natural key

`educationOrganizationId`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`,
`performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor`,
`evaluationDate`, `personId`, `sourceSystemDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationObjectiveReference` | yes | reference; supply `educationOrganizationId`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | A sub-component of an evaluation, a specific educator objective or domain of performance that is being evaluated. |
| `evaluationRatingReference` | yes | reference; supply `educationOrganizationId`, `evaluationDate`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `personId`, `schoolYear`, `sourceSystemDescriptor`, `termDescriptor` | The summary weighting for the evaluation instrument for an individual educator. |
| `comments` |  | string max 1024 | Any comments about the performance evaluation to be captured. |
| `objectiveRatingLevelDescriptor` |  | descriptor URI | The rating level achieved based upon the rating or score. |
| `results` |  | array of edFi_evaluationObjectiveRatingResult | An unordered collection of evaluationObjectiveRatingResults. |

### Items in `results`

| Field | Required | Type | Description |
|---|---|---|---|
| `numericRating` | yes | number (double) | The numerical summary rating or score for the evaluation. |
| `ratingResultTitle` | yes | string max 50 | The title of the rating result. |
| `resultDatatypeTypeDescriptor` | yes | descriptor URI | The datatype of the rating result. |

## Endpoints

- `GET /ed-fi/evaluationObjectiveRatings`
- `POST /ed-fi/evaluationObjectiveRatings`
- `GET /ed-fi/evaluationObjectiveRatings/deletes`
- `GET /ed-fi/evaluationObjectiveRatings/keyChanges`
- `GET /ed-fi/evaluationObjectiveRatings/partitions`
- `GET /ed-fi/evaluationObjectiveRatings/{id}`
- `PUT /ed-fi/evaluationObjectiveRatings/{id}`
- `DELETE /ed-fi/evaluationObjectiveRatings/{id}`
