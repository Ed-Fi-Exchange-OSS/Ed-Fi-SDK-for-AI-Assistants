# performanceEvaluationRatings

`/ed-fi/performanceEvaluationRatings`

The summary rating for a performance evaluation across all evaluation instruments for an individual educator.

## Natural key

`educationOrganizationId`, `evaluationPeriodDescriptor`, `performanceEvaluationTitle`,
`performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor`, `personId`, `sourceSystemDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `performanceEvaluationReference` | yes | reference; supply `educationOrganizationId`, `evaluationPeriodDescriptor`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | A performance evaluation of an educator, typically regularly scheduled and uniformly applied, composed of one or more evaluations. |
| `personReference` | yes | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `actualDate` | yes | string (date) | The month, day, and year on which the performance evaluation was conducted. |
| `actualDuration` |  | integer (int32) | The actual or estimated number of minutes during which the performance evaluation was conducted. |
| `actualTime` |  | string | An indication of the time at which the performance evaluation was conducted. |
| `announced` |  | boolean | An indicator of whether the performance evaluation was announced or not. |
| `comments` |  | string max 1024 | Any comments about the performance evaluation to be captured. |
| `coteachingStyleObservedDescriptor` |  | descriptor URI | A type of co-teaching observed as part of the performance evaluation. |
| `performanceEvaluationRatingLevelDescriptor` |  | descriptor URI | The rating level achieved based upon the rating or score. |
| `results` |  | array of edFi_performanceEvaluationRatingResult | An unordered collection of performanceEvaluationRatingResults. |
| `reviewers` |  | array of edFi_performanceEvaluationRatingReviewer | An unordered collection of performanceEvaluationRatingReviewers. |
| `scheduleDate` |  | string (date) | The month, day, and year on which the performance evaluation was scheduled. |

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
| `receivedTraining` |  | edFi_performanceEvaluationRatingReviewerReceivedTraining |  |

## Endpoints

- `GET /ed-fi/performanceEvaluationRatings`
- `POST /ed-fi/performanceEvaluationRatings`
- `GET /ed-fi/performanceEvaluationRatings/deletes`
- `GET /ed-fi/performanceEvaluationRatings/keyChanges`
- `GET /ed-fi/performanceEvaluationRatings/partitions`
- `GET /ed-fi/performanceEvaluationRatings/{id}`
- `PUT /ed-fi/performanceEvaluationRatings/{id}`
- `DELETE /ed-fi/performanceEvaluationRatings/{id}`
