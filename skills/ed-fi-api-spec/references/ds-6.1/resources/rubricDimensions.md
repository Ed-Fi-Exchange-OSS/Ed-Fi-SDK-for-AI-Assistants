# rubricDimensions

`/ed-fi/rubricDimensions`

The cells of a rubric, consisting of a qualitative decription, definition, or exemplar with the associated
rubric rating and rating level.

## Natural key

`rubricRating`, `educationOrganizationId`, `evaluationElementTitle`, `evaluationObjectiveTitle`,
`evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`,
`performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `rubricRating` | yes | integer (int32) | The rating achieved for the rubric dimension. |
| `evaluationElementReference` | yes | reference; supply `educationOrganizationId`, `evaluationElementTitle`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | The lowest-level elements or criterion of performance being evaluated by rubric, quantitative measure, or aggregate survey response. |
| `criterionDescription` | yes | string max 1024 | The criterion description for the rubric dimension. |
| `dimensionOrder` |  | integer (int32) | The order for the rubric dimension. |
| `rubricRatingLevelDescriptor` |  | descriptor URI | The rating level achieved for the rubric dimension. |

## Endpoints

- `GET /ed-fi/rubricDimensions`
- `POST /ed-fi/rubricDimensions`
- `GET /ed-fi/rubricDimensions/deletes`
- `GET /ed-fi/rubricDimensions/keyChanges`
- `GET /ed-fi/rubricDimensions/partitions`
- `GET /ed-fi/rubricDimensions/{id}`
- `PUT /ed-fi/rubricDimensions/{id}`
- `DELETE /ed-fi/rubricDimensions/{id}`
