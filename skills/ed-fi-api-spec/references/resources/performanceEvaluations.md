# performanceEvaluations

`/tpdm/performanceEvaluations`

A performance evaluation of an educator, typically regularly scheduled and uniformly applied, composed of one
or more Evaluations.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationPeriodDescriptor` | yes | descriptor URI | The period for the evaluation. |
| `performanceEvaluationTitle` | yes | string max 50 | An assigned unique identifier for the performance evaluation. |
| `performanceEvaluationTypeDescriptor` | yes | descriptor URI | The type of performance evaluation conducted. |
| `termDescriptor` | yes | descriptor URI | The term for the session during the school year. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |
| `academicSubjectDescriptor` |  | descriptor URI | The description of the content or subject area of a performance evaluation. |
| `gradeLevels` |  | array of tpdm_performanceEvaluationGradeLevel | An unordered collection of performanceEvaluationGradeLevels. |
| `performanceEvaluationDescription` |  | string max 255 | The long description of the Performance Evaluation. |
| `ratingLevels` |  | array of tpdm_performanceEvaluationRatingLevel | An unordered collection of performanceEvaluationRatingLevels. |

### Items in `gradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade levels involved with the performance evaluation. |

### Items in `ratingLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationRatingLevelDescriptor` | yes | descriptor URI | The title for a level of rating or evaluation band (e.g., Excellent, Acceptable, Needs Improvement, Unacceptable). |
| `maxRating` |  | number (double) | The maximum numerical rating or score to achieve the evaluation rating level. |
| `minRating` |  | number (double) | The minimum numerical rating or score to achieve the evaluation rating level. |

## Endpoints

- `GET /tpdm/performanceEvaluations`
- `POST /tpdm/performanceEvaluations`
- `GET /tpdm/performanceEvaluations/deletes`
- `GET /tpdm/performanceEvaluations/keyChanges`
- `GET /tpdm/performanceEvaluations/partitions`
- `GET /tpdm/performanceEvaluations/{id}`
- `PUT /tpdm/performanceEvaluations/{id}`
- `DELETE /tpdm/performanceEvaluations/{id}`
