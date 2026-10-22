# evaluationRatings

`/tpdm/evaluationRatings`

The summary weighting for the Evaluation instrument for an individual educator.

## Natural key

`evaluationDate`, `evaluationReference`, `performanceEvaluationRatingReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationDate` | key | string (date-time) | The date for the person's evaluation. |
| `evaluationReference` | key | reference: `educationOrganizationId`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` |  |
| `performanceEvaluationRatingReference` | key | reference: `educationOrganizationId`, `evaluationPeriodDescriptor`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `personId`, `schoolYear`, `sourceSystemDescriptor`, `termDescriptor` |  |
| `sectionReference` |  | reference: `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` |  |
| `actualDuration` |  | integer (int32) | The actual or estimated number of clock minutes during which the evaluation was conducted. |
| `comments` |  | string max 1024 | Any comments about the evaluation to be captured. |
| `evaluationRatingLevelDescriptor` |  | descriptor URI | The rating level achieved based upon the rating or score. |
| `evaluationRatingStatusDescriptor` |  | descriptor URI | The Status of the poerformance evaluation. |
| `results` |  | array of tpdm_evaluationRatingResult | An unordered collection of evaluationRatingResults. |
| `reviewers` |  | array of tpdm_evaluationRatingReviewer | An unordered collection of evaluationRatingReviewers. |

## Endpoints

- `DELETE /tpdm/evaluationRatings/{id}`
- `GET /tpdm/evaluationRatings/deletes`
- `GET /tpdm/evaluationRatings/keyChanges`
- `GET /tpdm/evaluationRatings/partitions`
- `GET /tpdm/evaluationRatings/{id}`
- `GET /tpdm/evaluationRatings`
- `POST /tpdm/evaluationRatings`
- `PUT /tpdm/evaluationRatings/{id}`
