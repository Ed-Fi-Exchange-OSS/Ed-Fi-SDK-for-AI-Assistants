# evaluations

`/tpdm/evaluations`

An evaluation instrument appled to evaluate an educator. The evaluation could be internally developed, or
could be an industry recognized instrument such as TTESS or Marzano.

## Natural key

`evaluationTitle`, `educationOrganizationId`, `evaluationPeriodDescriptor`, `performanceEvaluationTitle`,
`performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationTitle` | yes | string max 50 | The name or title of the evaluation. |
| `performanceEvaluationReference` | yes | reference; supply `educationOrganizationId`, `evaluationPeriodDescriptor`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | A performance evaluation of an educator, typically regularly scheduled and uniformly applied, composed of one or more Evaluations. |
| `evaluationDescription` |  | string max 255 | The long description of the Evaluation. |
| `evaluationTypeDescriptor` |  | descriptor URI | The type of the evaluation (e.g., observation, principal, peer, student survey, student growth). |
| `interRaterReliabilityScore` |  | integer (int32) | A score indicating how much homogeneity, or consensus, there is in the ratings given by judges. |
| `maxRating` |  | number (double) | The maximum summary numerical rating or score for the evaluation. |
| `minRating` |  | number (double) | The minimum summary numerical rating or score for the evaluation. |
| `ratingLevels` |  | array of tpdm_evaluationRatingLevel | An unordered collection of evaluationRatingLevels. |

### Items in `ratingLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationRatingLevelDescriptor` | yes | descriptor URI | The title for a level of rating or evaluation band (e.g., Excellent, Acceptable, Needs Improvement, Unacceptable). |
| `maxRating` |  | number (double) | The maximum numerical rating or score to achieve the evaluation rating level. |
| `minRating` |  | number (double) | The minimum numerical rating or score to achieve the evaluation rating level. |

## Endpoints

- `GET /tpdm/evaluations`
- `POST /tpdm/evaluations`
- `GET /tpdm/evaluations/deletes`
- `GET /tpdm/evaluations/keyChanges`
- `GET /tpdm/evaluations/partitions`
- `GET /tpdm/evaluations/{id}`
- `PUT /tpdm/evaluations/{id}`
- `DELETE /tpdm/evaluations/{id}`
