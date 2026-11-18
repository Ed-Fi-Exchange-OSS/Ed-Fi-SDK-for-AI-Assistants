# evaluationRatings

`/tpdm/evaluationRatings`

The summary weighting for the Evaluation instrument for an individual educator.

## Natural key

`evaluationDate`, `educationOrganizationId`, `evaluationPeriodDescriptor`, `evaluationTitle`,
`performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor`,
`personId`, `sourceSystemDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationDate` | yes | string (date-time) | The date for the person's evaluation. |
| `evaluationReference` | yes | reference; supply `educationOrganizationId`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | An evaluation instrument appled to evaluate an educator. |
| `performanceEvaluationRatingReference` | yes | reference; supply `educationOrganizationId`, `evaluationPeriodDescriptor`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `personId`, `schoolYear`, `sourceSystemDescriptor`, `termDescriptor` | The summary rating for a Performance Evaluation across all Evaluation instruments for an individual educator. |
| `sectionReference` |  | reference; supply `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` | This entity represents a setting in which organized instruction of course content is provided, in-person or otherwise, to one or more students for a given peri… |
| `actualDuration` |  | integer (int32) | The actual or estimated number of clock minutes during which the evaluation was conducted. |
| `comments` |  | string max 1024 | Any comments about the evaluation to be captured. |
| `evaluationRatingLevelDescriptor` |  | descriptor URI | The rating level achieved based upon the rating or score. |
| `evaluationRatingStatusDescriptor` |  | descriptor URI | The Status of the poerformance evaluation. |
| `results` |  | array of tpdm_evaluationRatingResult | An unordered collection of evaluationRatingResults. |
| `reviewers` |  | array of tpdm_evaluationRatingReviewer | An unordered collection of evaluationRatingReviewers. |

### Items in `results`

| Field | Required | Type | Description |
|---|---|---|---|
| `rating` | yes | number (double) | The numerical summary rating or score for the evaluation. |
| `ratingResultTitle` | yes | string max 50 | The title of Rating Result. |
| `resultDatatypeTypeDescriptor` | yes | descriptor URI | The datatype of the result. |

### Items in `reviewers`

| Field | Required | Type | Description |
|---|---|---|---|
| `firstName` | yes | string max 75 | A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change. |
| `lastSurname` | yes | string max 75 | The name borne in common by members of a family. |
| `reviewerPersonReference` |  | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `receivedTraining` |  | tpdm_evaluationRatingReviewerReceivedTraining |  |

## Endpoints

- `GET /tpdm/evaluationRatings`
- `POST /tpdm/evaluationRatings`
- `GET /tpdm/evaluationRatings/deletes`
- `GET /tpdm/evaluationRatings/keyChanges`
- `GET /tpdm/evaluationRatings/partitions`
- `GET /tpdm/evaluationRatings/{id}`
- `PUT /tpdm/evaluationRatings/{id}`
- `DELETE /tpdm/evaluationRatings/{id}`
