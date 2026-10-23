# performanceEvaluationRatings

`/tpdm/performanceEvaluationRatings`

The summary rating for a Performance Evaluation across all Evaluation instruments for an individual educator.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `performanceEvaluationReference` | yes | reference; supply `educationOrganizationId`, `evaluationPeriodDescriptor`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | A performance evaluation of an educator, typically regularly scheduled and uniformly applied, composed of one or more Evaluations. |
| `personReference` | yes | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
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
| `receivedTraining` |  | tpdm_performanceEvaluationRatingReviewerReceivedTraining |  |

## Endpoints

- `GET /tpdm/performanceEvaluationRatings`
- `POST /tpdm/performanceEvaluationRatings`
- `GET /tpdm/performanceEvaluationRatings/deletes`
- `GET /tpdm/performanceEvaluationRatings/keyChanges`
- `GET /tpdm/performanceEvaluationRatings/partitions`
- `GET /tpdm/performanceEvaluationRatings/{id}`
- `PUT /tpdm/performanceEvaluationRatings/{id}`
- `DELETE /tpdm/performanceEvaluationRatings/{id}`
