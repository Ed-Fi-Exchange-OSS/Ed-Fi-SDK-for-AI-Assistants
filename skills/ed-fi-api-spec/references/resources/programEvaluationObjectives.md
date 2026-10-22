# programEvaluationObjectives

`/ed-fi/programEvaluationObjectives`

A subcomponent of a ProgramEvaluation, a specific student objective or domain of performance that is being evaluated.

## Natural key

`programEvaluationObjectiveTitle`, `programEvaluationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programEvaluationObjectiveTitle` | key | string max 50 | The name or title of the program evaluation objective. |
| `programEvaluationReference` | key | reference: `programEducationOrganizationId`, `programEvaluationPeriodDescriptor`, `programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor` |  |
| `objectiveMaxNumericRating` |  | number (double) | The maximum summary numerical rating or score for the program evaluation objective. |
| `objectiveMinNumericRating` |  | number (double) | The minimum summary numerical rating or score for the program evaluation objective. |
| `objectiveSortOrder` |  | integer (int32) | The sort order of this program evaluation objective. |
| `programEvaluationLevels` |  | array of edFi_programEvaluationObjectiveProgramEvaluationLevel | An unordered collection of programEvaluationObjectiveProgramEvaluationLevels. |
| `programEvaluationObjectiveDescription` |  | string max 255 | The long description of the program evaluation objective. |

## Endpoints

- `DELETE /ed-fi/programEvaluationObjectives/{id}`
- `GET /ed-fi/programEvaluationObjectives/deletes`
- `GET /ed-fi/programEvaluationObjectives/keyChanges`
- `GET /ed-fi/programEvaluationObjectives/partitions`
- `GET /ed-fi/programEvaluationObjectives/{id}`
- `GET /ed-fi/programEvaluationObjectives`
- `POST /ed-fi/programEvaluationObjectives`
- `PUT /ed-fi/programEvaluationObjectives/{id}`
