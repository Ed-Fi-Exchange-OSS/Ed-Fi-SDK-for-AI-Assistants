# goals

`/ed-fi/goals`

The goal for performance improvement assigned to an educator associated with an evaluation element.

## Natural key

`assignmentDate`, `goalTitle`, `personId`, `sourceSystemDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `assignmentDate` | yes | string (date) | The month, day, and year on which the goal was assigned. |
| `goalTitle` | yes | string max 255 | The name or title of the goal. |
| `evaluationElementReference` |  | reference; supply `educationOrganizationId`, `evaluationElementTitle`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | The lowest-level elements or criterion of performance being evaluated by rubric, quantitative measure, or aggregate survey response. |
| `evaluationObjectiveReference` |  | reference; supply `educationOrganizationId`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | A sub-component of an evaluation, a specific educator objective or domain of performance that is being evaluated. |
| `parentGoalReference` |  | reference; supply `assignmentDate`, `goalTitle`, `personId`, `sourceSystemDescriptor` | The goal for performance improvement assigned to an educator associated with an evaluation element. |
| `personReference` | yes | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `comments` |  | string max 1024 | Any comments about the goal or its completion to be captured. |
| `completedDate` |  | string (date) | The month, day, and year on which the goal was completed. |
| `completedIndicator` |  | boolean | Indicator that the goal was completed. |
| `dueDate` |  | string (date) | The month, day, and year on which the goal is due or expected to be completed. |
| `goalDescription` |  | string max 1024 | The description of the goal. |
| `goalTypeDescriptor` |  | descriptor URI | The type of the goal. |

## Endpoints

- `GET /ed-fi/goals`
- `POST /ed-fi/goals`
- `GET /ed-fi/goals/deletes`
- `GET /ed-fi/goals/keyChanges`
- `GET /ed-fi/goals/partitions`
- `GET /ed-fi/goals/{id}`
- `PUT /ed-fi/goals/{id}`
- `DELETE /ed-fi/goals/{id}`
