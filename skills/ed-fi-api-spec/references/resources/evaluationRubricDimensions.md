# evaluationRubricDimensions

`/ed-fi/evaluationRubricDimensions`

The cells of a rubric, consisting of a qualitative decription, definition, or exemplar with the associated
rubric evaluation level.

## Natural key

`evaluationRubricRating`, `programEvaluationElementReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationRubricRating` | key | integer (int32) | The numeric rating associated with the evaluation rubric dimension. |
| `programEvaluationElementReference` | key | reference: `programEducationOrganizationId`, `programEvaluationElementTitle`, `programEvaluationPeriodDescriptor`, `programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor` |  |
| `evaluationCriterionDescription` | yes | string max 1024 | The evaluation criterion description for the evaluation rubric dimension. |
| `evaluationRubricRatingLevelDescriptor` |  | descriptor URI | The rating level achieved for the evaluation rubric dimension. |
| `rubricDimensionSortOrder` |  | integer (int32) | The sort order of the rubric dimension. |

## Endpoints

- `DELETE /ed-fi/evaluationRubricDimensions/{id}`
- `GET /ed-fi/evaluationRubricDimensions/deletes`
- `GET /ed-fi/evaluationRubricDimensions/keyChanges`
- `GET /ed-fi/evaluationRubricDimensions/partitions`
- `GET /ed-fi/evaluationRubricDimensions/{id}`
- `GET /ed-fi/evaluationRubricDimensions`
- `POST /ed-fi/evaluationRubricDimensions`
- `PUT /ed-fi/evaluationRubricDimensions/{id}`
