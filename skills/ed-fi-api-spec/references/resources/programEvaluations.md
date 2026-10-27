# programEvaluations

`/ed-fi/programEvaluations`

An evaluation instrument applied to evaluate a student in the context of a program. Student evaluations are
typically applied by a staff member based upon a rubric.

## Natural key

`programEvaluationPeriodDescriptor`, `programEvaluationTypeDescriptor`, `programEvaluationTitle`,
`programEducationOrganizationId`, `programName`, `programTypeDescriptor`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programEvaluationPeriodDescriptor` | yes | descriptor URI | The name of the period for the program evaluation. |
| `programEvaluationTitle` | yes | string max 50 | An assigned unique identifier for the student program evaluation. |
| `programEvaluationTypeDescriptor` | yes | descriptor URI | The type of program evaluation conducted. |
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |
| `evaluationMaxNumericRating` |  | number (double) | The maximum summary numerical rating or score for the program evaluation. |
| `evaluationMinNumericRating` |  | number (double) | The minimum summary numerical rating or score for the program evaluation. |
| `levels` |  | array of edFi_programEvaluationLevel | An unordered collection of programEvaluationLevels. |
| `programEvaluationDescription` |  | string max 255 | The long description of the program evaluation. |

### Items in `levels`

| Field | Required | Type | Description |
|---|---|---|---|
| `ratingLevelDescriptor` | yes | descriptor URI | The title for a level of rating or evaluation band (e.g., Excellent, Acceptable, Needs Improvement, Unacceptable). |
| `maxNumericRating` |  | number (double) | The maximum numerical rating or score to achieve the evaluation rating level. |
| `minNumericRating` |  | number (double) | The minimum numerical rating or score to achieve the evaluation rating level. |

## Endpoints

- `GET /ed-fi/programEvaluations`
- `POST /ed-fi/programEvaluations`
- `GET /ed-fi/programEvaluations/deletes`
- `GET /ed-fi/programEvaluations/keyChanges`
- `GET /ed-fi/programEvaluations/partitions`
- `GET /ed-fi/programEvaluations/{id}`
- `PUT /ed-fi/programEvaluations/{id}`
- `DELETE /ed-fi/programEvaluations/{id}`
