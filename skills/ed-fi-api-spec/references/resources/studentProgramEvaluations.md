# studentProgramEvaluations

`/ed-fi/studentProgramEvaluations`

The evaluation results for a student as evaluated in the context of a program.

## Natural key

`evaluationDate`, `programEvaluationReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationDate` | key | string (date) | The month, day, and year on which the evaluation was conducted. |
| `educationOrganizationReference` |  | reference: `educationOrganizationId` |  |
| `programEvaluationReference` | key | reference: `programEducationOrganizationId`, `programEvaluationPeriodDescriptor`, `programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor` |  |
| `staffEvaluatorStaffReference` |  | reference: `staffUniqueId` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `evaluationDuration` |  | integer (int32) | The actual number of minutes to conduct the evaluation. |
| `externalEvaluators` |  | array of edFi_studentProgramEvaluationExternalEvaluator | An unordered collection of studentProgramEvaluationExternalEvaluators. |
| `studentEvaluationElements` |  | array of edFi_studentProgramEvaluationStudentEvaluationElement | An unordered collection of studentProgramEvaluationStudentEvaluationElements. |
| `studentEvaluationObjectives` |  | array of edFi_studentProgramEvaluationStudentEvaluationObjective | An unordered collection of studentProgramEvaluationStudentEvaluationObjectives. |
| `summaryEvaluationComment` |  | string max 1024 | Any comments about the summary evaluation to be captured. |
| `summaryEvaluationNumericRating` |  | number (double) | The numerical summary rating or score for the evaluation. |
| `summaryEvaluationRatingLevelDescriptor` |  | descriptor URI | The summary rating level achieved based upon the rating or score. |

## Endpoints

- `DELETE /ed-fi/studentProgramEvaluations/{id}`
- `GET /ed-fi/studentProgramEvaluations/deletes`
- `GET /ed-fi/studentProgramEvaluations/keyChanges`
- `GET /ed-fi/studentProgramEvaluations/partitions`
- `GET /ed-fi/studentProgramEvaluations/{id}`
- `GET /ed-fi/studentProgramEvaluations`
- `POST /ed-fi/studentProgramEvaluations`
- `PUT /ed-fi/studentProgramEvaluations/{id}`
