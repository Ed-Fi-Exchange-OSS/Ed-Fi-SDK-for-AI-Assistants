# evaluationObjectives

`/tpdm/evaluationObjectives`

A subcomponent of an Evaluation, a specific educator Objective or domain of performance that is being
evaluated.

## Natural key

`evaluationObjectiveTitle`, `evaluationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationObjectiveTitle` | key | string max 50 | The name or title of the evaluation Objective. |
| `evaluationReference` | key | reference: `educationOrganizationId`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` |  |
| `evaluationObjectiveDescription` |  | string max 255 | The long description of the Evaluation Objective. |
| `evaluationTypeDescriptor` |  | descriptor URI | The type of the evaluation Objective (e.g., observation, principal, peer, student survey, student growth). |
| `maxRating` |  | number (double) | The maximum summary numerical rating or score for the evaluation Objective. |
| `minRating` |  | number (double) | The minimum summary numerical rating or score for the evaluation Objective. |
| `ratingLevels` |  | array of tpdm_evaluationObjectiveRatingLevel | An unordered collection of evaluationObjectiveRatingLevels. |
| `sortOrder` |  | integer (int32) | The sort order of this Evaluation Objective. |

## Endpoints

- `DELETE /tpdm/evaluationObjectives/{id}`
- `GET /tpdm/evaluationObjectives/deletes`
- `GET /tpdm/evaluationObjectives/keyChanges`
- `GET /tpdm/evaluationObjectives/partitions`
- `GET /tpdm/evaluationObjectives/{id}`
- `GET /tpdm/evaluationObjectives`
- `POST /tpdm/evaluationObjectives`
- `PUT /tpdm/evaluationObjectives/{id}`
