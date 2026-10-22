# evaluations

`/tpdm/evaluations`

An evaluation instrument appled to evaluate an educator. The evaluation could be internally developed, or
could be an industry recognized instrument such as TTESS or Marzano.

## Natural key

`evaluationTitle`, `performanceEvaluationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationTitle` | key | string max 50 | The name or title of the evaluation. |
| `performanceEvaluationReference` | key | reference: `educationOrganizationId`, `evaluationPeriodDescriptor`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` |  |
| `evaluationDescription` |  | string max 255 | The long description of the Evaluation. |
| `evaluationTypeDescriptor` |  | descriptor URI | The type of the evaluation (e.g., observation, principal, peer, student survey, student growth). |
| `interRaterReliabilityScore` |  | integer (int32) | A score indicating how much homogeneity, or consensus, there is in the ratings given by judges. |
| `maxRating` |  | number (double) | The maximum summary numerical rating or score for the evaluation. |
| `minRating` |  | number (double) | The minimum summary numerical rating or score for the evaluation. |
| `ratingLevels` |  | array of tpdm_evaluationRatingLevel | An unordered collection of evaluationRatingLevels. |

## Endpoints

- `DELETE /tpdm/evaluations/{id}`
- `GET /tpdm/evaluations/deletes`
- `GET /tpdm/evaluations/keyChanges`
- `GET /tpdm/evaluations/partitions`
- `GET /tpdm/evaluations/{id}`
- `GET /tpdm/evaluations`
- `POST /tpdm/evaluations`
- `PUT /tpdm/evaluations/{id}`
