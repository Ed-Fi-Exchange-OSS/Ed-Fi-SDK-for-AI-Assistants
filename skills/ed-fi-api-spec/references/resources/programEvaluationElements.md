# programEvaluationElements

`/ed-fi/programEvaluationElements`

The lowest level elements or criterion of a students's performance that is being evaluated, typically by a
rubric.

## Natural key

`programEvaluationElementTitle`, `programEducationOrganizationId`, `programEvaluationPeriodDescriptor`,
`programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programEvaluationElementTitle` | yes | string max 50 | The name or title of the program evaluation element. |
| `programEvaluationObjectiveReference` |  | reference; supply `programEducationOrganizationId`, `programEvaluationObjectiveTitle`, `programEvaluationPeriodDescriptor`, `programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor` | A subcomponent of a ProgramEvaluation, a specific student objective or domain of performance that is being evaluated. |
| `programEvaluationReference` | yes | reference; supply `programEducationOrganizationId`, `programEvaluationPeriodDescriptor`, `programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor` | An evaluation instrument applied to evaluate a student in the context of a program. |
| `elementMaxNumericRating` |  | number (double) | The maximum summary numerical rating or score for the program evaluation element. |
| `elementMinNumericRating` |  | number (double) | The minimum summary numerical rating or score for the program evaluation element. |
| `elementSortOrder` |  | integer (int32) | The sort order of this program evaluation element. |
| `programEvaluationElementDescription` |  | string max 255 | The long description of the program evaluation element. |
| `programEvaluationLevels` |  | array of edFi_programEvaluationElementProgramEvaluationLevel | An unordered collection of programEvaluationElementProgramEvaluationLevels. |

### Items in `programEvaluationLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `ratingLevelDescriptor` | yes | descriptor URI | The title for a level of rating or evaluation band (e.g., Excellent, Acceptable, Needs Improvement, Unacceptable). |
| `maxNumericRating` |  | number (double) | The maximum numerical rating or score to achieve the evaluation rating level. |
| `minNumericRating` |  | number (double) | The minimum numerical rating or score to achieve the evaluation rating level. |

## Endpoints

- `GET /ed-fi/programEvaluationElements`
- `POST /ed-fi/programEvaluationElements`
- `GET /ed-fi/programEvaluationElements/deletes`
- `GET /ed-fi/programEvaluationElements/keyChanges`
- `GET /ed-fi/programEvaluationElements/partitions`
- `GET /ed-fi/programEvaluationElements/{id}`
- `PUT /ed-fi/programEvaluationElements/{id}`
- `DELETE /ed-fi/programEvaluationElements/{id}`
