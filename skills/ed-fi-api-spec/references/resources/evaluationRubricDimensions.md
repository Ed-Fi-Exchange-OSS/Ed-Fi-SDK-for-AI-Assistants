# evaluationRubricDimensions

`/ed-fi/evaluationRubricDimensions`

The cells of a rubric, consisting of a qualitative decription, definition, or exemplar with the associated
rubric evaluation level.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationRubricRating` | yes | integer (int32) | The numeric rating associated with the evaluation rubric dimension. |
| `programEvaluationElementReference` | yes | reference; supply `programEducationOrganizationId`, `programEvaluationElementTitle`, `programEvaluationPeriodDescriptor`, `programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor` | The lowest level elements or criterion of a students's performance that is being evaluated, typically by a rubric. |
| `evaluationCriterionDescription` | yes | string max 1024 | The evaluation criterion description for the evaluation rubric dimension. |
| `evaluationRubricRatingLevelDescriptor` |  | descriptor URI | The rating level achieved for the evaluation rubric dimension. |
| `rubricDimensionSortOrder` |  | integer (int32) | The sort order of the rubric dimension. |

## Endpoints

- `GET /ed-fi/evaluationRubricDimensions`
- `POST /ed-fi/evaluationRubricDimensions`
- `GET /ed-fi/evaluationRubricDimensions/deletes`
- `GET /ed-fi/evaluationRubricDimensions/keyChanges`
- `GET /ed-fi/evaluationRubricDimensions/partitions`
- `GET /ed-fi/evaluationRubricDimensions/{id}`
- `PUT /ed-fi/evaluationRubricDimensions/{id}`
- `DELETE /ed-fi/evaluationRubricDimensions/{id}`
