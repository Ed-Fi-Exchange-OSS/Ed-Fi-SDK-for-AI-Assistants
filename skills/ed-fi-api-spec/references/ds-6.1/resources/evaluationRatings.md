# evaluationRatings

`/ed-fi/evaluationRatings`

The summary weighting for the evaluation instrument for an individual educator.

## Natural key

`evaluationDate`, `educationOrganizationId`, `evaluationPeriodDescriptor`, `evaluationTitle`,
`performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor`,
`personId`, `sourceSystemDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationDate` | yes | string (date-time) | The date for the person's evaluation. |
| `evaluationReference` | yes | reference; supply `educationOrganizationId`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | An evaluation instrument applied to evaluate an educator. |
| `performanceEvaluationRatingReference` | yes | reference; supply `educationOrganizationId`, `evaluationPeriodDescriptor`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `personId`, `schoolYear`, `sourceSystemDescriptor`, `termDescriptor` | The summary rating for a performance evaluation across all evaluation instruments for an individual educator. |
| `sectionReference` |  | reference; supply `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` | This entity represents a setting in which organized instruction of course content is provided, in-person or otherwise, to one or more students for a given peri… |
| `actualDuration` |  | integer (int32) | The actual or estimated number of clock minutes during which the evaluation was conducted. |
| `comments` |  | string max 1024 | Any comments about the evaluation to be captured. |
| `evaluationRatingLevelDescriptor` |  | descriptor URI | The rating level achieved based upon the rating or score. |
| `evaluationRatingStatusDescriptor` |  | descriptor URI | The status of the performance evaluation. |
| `results` |  | array of edFi_evaluationRatingResult | An unordered collection of evaluationRatingResults. |
| `reviewers` |  | array of edFi_evaluationRatingReviewer | An unordered collection of evaluationRatingReviewers. |

### Items in `results`

| Field | Required | Type | Description |
|---|---|---|---|
| `numericRating` | yes | number (double) | The numerical summary rating or score for the evaluation. |
| `ratingResultTitle` | yes | string max 50 | The title of the rating result. |
| `resultDatatypeTypeDescriptor` | yes | descriptor URI | The datatype of the rating result. |

### Items in `reviewers`

| Field | Required | Type | Description |
|---|---|---|---|
| `firstName` | yes | string max 75 | A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change. |
| `lastSurname` | yes | string max 75 | The name borne in common by members of a family. |
| `reviewerPersonReference` |  | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `receivedTraining` |  | edFi_evaluationRatingReviewerReceivedTraining |  |

## Endpoints

- `GET /ed-fi/evaluationRatings`
- `POST /ed-fi/evaluationRatings`
- `GET /ed-fi/evaluationRatings/deletes`
- `GET /ed-fi/evaluationRatings/keyChanges`
- `GET /ed-fi/evaluationRatings/partitions`
- `GET /ed-fi/evaluationRatings/{id}`
- `PUT /ed-fi/evaluationRatings/{id}`
- `DELETE /ed-fi/evaluationRatings/{id}`
