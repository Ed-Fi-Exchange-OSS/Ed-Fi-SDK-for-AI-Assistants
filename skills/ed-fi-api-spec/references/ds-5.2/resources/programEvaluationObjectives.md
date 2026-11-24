# programEvaluationObjectives

`/ed-fi/programEvaluationObjectives`

A subcomponent of a ProgramEvaluation, a specific student objective or domain of performance that is being
evaluated.

## Natural key

`programEvaluationObjectiveTitle`, `programEducationOrganizationId`, `programEvaluationPeriodDescriptor`,
`programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programEvaluationObjectiveTitle` | yes | string max 50 | The name or title of the program evaluation objective. |
| `programEvaluationReference` | yes | reference; supply `programEducationOrganizationId`, `programEvaluationPeriodDescriptor`, `programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor` | An evaluation instrument applied to evaluate a student in the context of a program. |
| `objectiveMaxNumericRating` |  | number (double) | The maximum summary numerical rating or score for the program evaluation objective. |
| `objectiveMinNumericRating` |  | number (double) | The minimum summary numerical rating or score for the program evaluation objective. |
| `objectiveSortOrder` |  | integer (int32) | The sort order of this program evaluation objective. |
| `programEvaluationLevels` |  | array of edFi_programEvaluationObjectiveProgramEvaluationLevel | An unordered collection of programEvaluationObjectiveProgramEvaluationLevels. |
| `programEvaluationObjectiveDescription` |  | string max 255 | The long description of the program evaluation objective. |

### Items in `programEvaluationLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `ratingLevelDescriptor` | yes | descriptor URI | The title for a level of rating or evaluation band (e.g., Excellent, Acceptable, Needs Improvement, Unacceptable). |
| `maxNumericRating` |  | number (double) | The maximum numerical rating or score to achieve the evaluation rating level. |
| `minNumericRating` |  | number (double) | The minimum numerical rating or score to achieve the evaluation rating level. |

## Endpoints

- `GET /ed-fi/programEvaluationObjectives`
- `POST /ed-fi/programEvaluationObjectives`
- `GET /ed-fi/programEvaluationObjectives/deletes`
- `GET /ed-fi/programEvaluationObjectives/keyChanges`
- `GET /ed-fi/programEvaluationObjectives/partitions`
- `GET /ed-fi/programEvaluationObjectives/{id}`
- `PUT /ed-fi/programEvaluationObjectives/{id}`
- `DELETE /ed-fi/programEvaluationObjectives/{id}`
