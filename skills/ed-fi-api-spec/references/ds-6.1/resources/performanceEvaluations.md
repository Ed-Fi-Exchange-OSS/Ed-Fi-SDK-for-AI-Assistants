# performanceEvaluations

`/ed-fi/performanceEvaluations`

A performance evaluation of an educator, typically regularly scheduled and uniformly applied, composed of one
or more evaluations.

## Natural key

`evaluationPeriodDescriptor`, `performanceEvaluationTypeDescriptor`, `termDescriptor`,
`performanceEvaluationTitle`, `educationOrganizationId`, `schoolYear`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationPeriodDescriptor` | yes | descriptor URI | The period for the evaluation. |
| `performanceEvaluationTitle` | yes | string max 50 | An assigned unique identifier for the performance evaluation. |
| `performanceEvaluationTypeDescriptor` | yes | descriptor URI | The type of performance evaluation conducted. |
| `termDescriptor` | yes | descriptor URI | The term for the session during the school year. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |
| `academicSubjectDescriptor` |  | descriptor URI | The description of the content or subject area of the performance evaluation. |
| `gradeLevels` |  | array of edFi_performanceEvaluationGradeLevel | An unordered collection of performanceEvaluationGradeLevels. |
| `performanceEvaluationDescription` |  | string max 255 | The long description of the performance evaluation. |
| `ratingLevels` |  | array of edFi_performanceEvaluationRatingLevel | An unordered collection of performanceEvaluationRatingLevels. |

### Items in `gradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade levels involved with the performance evaluation. |

### Items in `ratingLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationRatingLevelDescriptor` | yes | descriptor URI | The title for a level of rating or evaluation band. |
| `maxNumericRating` |  | number (double) | The maximum numerical rating or score to achieve the evaluation rating level. |
| `minNumericRating` |  | number (double) | The minimum numerical rating or score to achieve the evaluation rating level. |

## Endpoints

- `GET /ed-fi/performanceEvaluations`
- `POST /ed-fi/performanceEvaluations`
- `GET /ed-fi/performanceEvaluations/deletes`
- `GET /ed-fi/performanceEvaluations/keyChanges`
- `GET /ed-fi/performanceEvaluations/partitions`
- `GET /ed-fi/performanceEvaluations/{id}`
- `PUT /ed-fi/performanceEvaluations/{id}`
- `DELETE /ed-fi/performanceEvaluations/{id}`
