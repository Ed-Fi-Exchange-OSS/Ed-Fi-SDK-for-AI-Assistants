# rubricDimensions

`/tpdm/rubricDimensions`

The cells of a rubric, consisting of a qualitative decription, definition, or exemplar with the associated
rubric rating and rating level.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `rubricRating` | yes | integer (int32) | The rating achieved for the rubric dimension. |
| `evaluationElementReference` | yes | reference; supply `educationOrganizationId`, `evaluationElementTitle`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | The lowest-level Elements or criterion of performance being evaluated by rubric, quantitative measure, or aggregate survey response. |
| `criterionDescription` | yes | string max 1024 | The criterion description for the rubric dimension. |
| `dimensionOrder` |  | integer (int32) | The order for the rubric dimension. |
| `rubricRatingLevelDescriptor` |  | descriptor URI | The rating level achieved for the rubric dimension. |

## Endpoints

- `GET /tpdm/rubricDimensions`
- `POST /tpdm/rubricDimensions`
- `GET /tpdm/rubricDimensions/deletes`
- `GET /tpdm/rubricDimensions/keyChanges`
- `GET /tpdm/rubricDimensions/partitions`
- `GET /tpdm/rubricDimensions/{id}`
- `PUT /tpdm/rubricDimensions/{id}`
- `DELETE /tpdm/rubricDimensions/{id}`
