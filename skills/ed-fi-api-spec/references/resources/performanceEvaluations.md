# performanceEvaluations

`/tpdm/performanceEvaluations`

A performance evaluation of an educator, typically regularly scheduled and uniformly applied, composed of one or more Evaluations.

## Natural key

`evaluationPeriodDescriptor`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `termDescriptor`, `educationOrganizationReference`, `schoolYearTypeReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationPeriodDescriptor` | key | descriptor URI | The period for the evaluation. |
| `performanceEvaluationTitle` | key | string max 50 | An assigned unique identifier for the performance evaluation. |
| `performanceEvaluationTypeDescriptor` | key | descriptor URI | The type of performance evaluation conducted. |
| `termDescriptor` | key | descriptor URI | The term for the session during the school year. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `schoolYearTypeReference` | key | reference: `schoolYear` |  |
| `academicSubjectDescriptor` |  | descriptor URI | The description of the content or subject area of a performance evaluation. |
| `gradeLevels` |  | array of tpdm_performanceEvaluationGradeLevel | An unordered collection of performanceEvaluationGradeLevels. |
| `performanceEvaluationDescription` |  | string max 255 | The long description of the Performance Evaluation. |
| `ratingLevels` |  | array of tpdm_performanceEvaluationRatingLevel | An unordered collection of performanceEvaluationRatingLevels. |

## Endpoints

- `DELETE /tpdm/performanceEvaluations/{id}`
- `GET /tpdm/performanceEvaluations/deletes`
- `GET /tpdm/performanceEvaluations/keyChanges`
- `GET /tpdm/performanceEvaluations/partitions`
- `GET /tpdm/performanceEvaluations/{id}`
- `GET /tpdm/performanceEvaluations`
- `POST /tpdm/performanceEvaluations`
- `PUT /tpdm/performanceEvaluations/{id}`
