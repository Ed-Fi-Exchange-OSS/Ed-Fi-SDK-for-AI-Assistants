# studentProgramEvaluations

`/ed-fi/studentProgramEvaluations`

The evaluation results for a student as evaluated in the context of a program.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationDate` | yes | string (date) | The month, day, and year on which the evaluation was conducted. |
| `educationOrganizationReference` |  | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `programEvaluationReference` | yes | reference; supply `programEducationOrganizationId`, `programEvaluationPeriodDescriptor`, `programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor` | An evaluation instrument applied to evaluate a student in the context of a program. |
| `staffEvaluatorStaffReference` |  | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `evaluationDuration` |  | integer (int32) | The actual number of minutes to conduct the evaluation. |
| `externalEvaluators` |  | array of edFi_studentProgramEvaluationExternalEvaluator | An unordered collection of studentProgramEvaluationExternalEvaluators. |
| `studentEvaluationElements` |  | array of edFi_studentProgramEvaluationStudentEvaluationElement | An unordered collection of studentProgramEvaluationStudentEvaluationElements. |
| `studentEvaluationObjectives` |  | array of edFi_studentProgramEvaluationStudentEvaluationObjective | An unordered collection of studentProgramEvaluationStudentEvaluationObjectives. |
| `summaryEvaluationComment` |  | string max 1024 | Any comments about the summary evaluation to be captured. |
| `summaryEvaluationNumericRating` |  | number (double) | The numerical summary rating or score for the evaluation. |
| `summaryEvaluationRatingLevelDescriptor` |  | descriptor URI | The summary rating level achieved based upon the rating or score. |

### Items in `externalEvaluators`

| Field | Required | Type | Description |
|---|---|---|---|
| `externalEvaluator` | yes | string max 150 | The external person(s) - not staff - that conducted the evaluation. |

### Items in `studentEvaluationElements`

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationElementRatingLevelDescriptor` |  | descriptor URI | The rating level achieved based upon the rating or score for the evaluation element. |
| `evaluationElementNumericRating` |  | number (double) | The numerical rating or score for the evaluation element. |
| `programEvaluationElementReference` | yes | reference; supply `programEducationOrganizationId`, `programEvaluationElementTitle`, `programEvaluationPeriodDescriptor`, `programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor` | The lowest level elements or criterion of a students's performance that is being evaluated, typically by a rubric. |

### Items in `studentEvaluationObjectives`

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationObjectiveRatingLevelDescriptor` |  | descriptor URI | The rating level achieved based upon the rating or score for the evaluation objective. |
| `evaluationObjectiveNumericRating` |  | number (double) | The numerical rating or score for the evaluation objective. |
| `programEvaluationObjectiveReference` | yes | reference; supply `programEducationOrganizationId`, `programEvaluationObjectiveTitle`, `programEvaluationPeriodDescriptor`, `programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor` | A subcomponent of a ProgramEvaluation, a specific student objective or domain of performance that is being evaluated. |

## Endpoints

- `GET /ed-fi/studentProgramEvaluations`
- `POST /ed-fi/studentProgramEvaluations`
- `GET /ed-fi/studentProgramEvaluations/deletes`
- `GET /ed-fi/studentProgramEvaluations/keyChanges`
- `GET /ed-fi/studentProgramEvaluations/partitions`
- `GET /ed-fi/studentProgramEvaluations/{id}`
- `PUT /ed-fi/studentProgramEvaluations/{id}`
- `DELETE /ed-fi/studentProgramEvaluations/{id}`
