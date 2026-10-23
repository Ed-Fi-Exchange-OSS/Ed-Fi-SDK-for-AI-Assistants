# evaluationObjectives

`/tpdm/evaluationObjectives`

A subcomponent of an Evaluation, a specific educator Objective or domain of performance that is being
evaluated.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationObjectiveTitle` | yes | string max 50 | The name or title of the evaluation Objective. |
| `evaluationReference` | yes | reference; supply `educationOrganizationId`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | An evaluation instrument appled to evaluate an educator. |
| `evaluationObjectiveDescription` |  | string max 255 | The long description of the Evaluation Objective. |
| `evaluationTypeDescriptor` |  | descriptor URI | The type of the evaluation Objective (e.g., observation, principal, peer, student survey, student growth). |
| `maxRating` |  | number (double) | The maximum summary numerical rating or score for the evaluation Objective. |
| `minRating` |  | number (double) | The minimum summary numerical rating or score for the evaluation Objective. |
| `ratingLevels` |  | array of tpdm_evaluationObjectiveRatingLevel | An unordered collection of evaluationObjectiveRatingLevels. |
| `sortOrder` |  | integer (int32) | The sort order of this Evaluation Objective. |

### Items in `ratingLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationRatingLevelDescriptor` | yes | descriptor URI | The title for a level of rating or evaluation band (e.g., Excellent, Acceptable, Needs Improvement, Unacceptable). |
| `maxRating` |  | number (double) | The maximum numerical rating or score to achieve the evaluation rating level. |
| `minRating` |  | number (double) | The minimum numerical rating or score to achieve the evaluation rating level. |

## Endpoints

- `GET /tpdm/evaluationObjectives`
- `POST /tpdm/evaluationObjectives`
- `GET /tpdm/evaluationObjectives/deletes`
- `GET /tpdm/evaluationObjectives/keyChanges`
- `GET /tpdm/evaluationObjectives/partitions`
- `GET /tpdm/evaluationObjectives/{id}`
- `PUT /tpdm/evaluationObjectives/{id}`
- `DELETE /tpdm/evaluationObjectives/{id}`
