# programEvaluations

`/ed-fi/programEvaluations`

An evaluation instrument applied to evaluate a student in the context of a program. Student evaluations are
typically applied by a staff member based upon a rubric.

## Natural key

`programEvaluationPeriodDescriptor`, `programEvaluationTitle`, `programEvaluationTypeDescriptor`,
`programReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programEvaluationPeriodDescriptor` | key | descriptor URI | The name of the period for the program evaluation. |
| `programEvaluationTitle` | key | string max 50 | An assigned unique identifier for the student program evaluation. |
| `programEvaluationTypeDescriptor` | key | descriptor URI | The type of program evaluation conducted. |
| `programReference` | key | reference: `educationOrganizationId`, `programName`, `programTypeDescriptor` |  |
| `evaluationMaxNumericRating` |  | number (double) | The maximum summary numerical rating or score for the program evaluation. |
| `evaluationMinNumericRating` |  | number (double) | The minimum summary numerical rating or score for the program evaluation. |
| `levels` |  | array of edFi_programEvaluationLevel | An unordered collection of programEvaluationLevels. |
| `programEvaluationDescription` |  | string max 255 | The long description of the program evaluation. |

## Endpoints

- `DELETE /ed-fi/programEvaluations/{id}`
- `GET /ed-fi/programEvaluations/deletes`
- `GET /ed-fi/programEvaluations/keyChanges`
- `GET /ed-fi/programEvaluations/partitions`
- `GET /ed-fi/programEvaluations/{id}`
- `GET /ed-fi/programEvaluations`
- `POST /ed-fi/programEvaluations`
- `PUT /ed-fi/programEvaluations/{id}`
