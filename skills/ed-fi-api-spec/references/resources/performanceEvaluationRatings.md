# performanceEvaluationRatings

`/tpdm/performanceEvaluationRatings`

The summary rating for a Performance Evaluation across all Evaluation instruments for an individual educator.

## Natural key

`performanceEvaluationReference`, `personReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `performanceEvaluationReference` | key | reference: `educationOrganizationId`, `evaluationPeriodDescriptor`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` |  |
| `personReference` | key | reference: `personId`, `sourceSystemDescriptor` |  |
| `actualDate` | yes | string (date) | The month, day, and year on which the performance evaluation was conducted. |
| `actualDuration` |  | integer (int32) | The actual or estimated number of clock minutes during which the performance evaluation was conducted. |
| `actualTime` |  | string | An indication of the the time at which the performance evaluation was conducted. |
| `announced` |  | boolean | An indicator of whether the performance evaluation was announced or not. |
| `comments` |  | string max 1024 | Any comments about the performance evaluation to be captured. |
| `coteachingStyleObservedDescriptor` |  | descriptor URI | A type of co-teaching observed as part of the performance evaluation. |
| `performanceEvaluationRatingLevelDescriptor` |  | descriptor URI | The rating level achieved based upon the rating or score. |
| `results` |  | array of tpdm_performanceEvaluationRatingResult | An unordered collection of performanceEvaluationRatingResults. |
| `reviewers` |  | array of tpdm_performanceEvaluationRatingReviewer | An unordered collection of performanceEvaluationRatingReviewers. |
| `scheduleDate` |  | string (date) | The month, day, and year on which the performance evaluation was scheduled. |

## Endpoints

- `DELETE /tpdm/performanceEvaluationRatings/{id}`
- `GET /tpdm/performanceEvaluationRatings/deletes`
- `GET /tpdm/performanceEvaluationRatings/keyChanges`
- `GET /tpdm/performanceEvaluationRatings/partitions`
- `GET /tpdm/performanceEvaluationRatings/{id}`
- `GET /tpdm/performanceEvaluationRatings`
- `POST /tpdm/performanceEvaluationRatings`
- `PUT /tpdm/performanceEvaluationRatings/{id}`
