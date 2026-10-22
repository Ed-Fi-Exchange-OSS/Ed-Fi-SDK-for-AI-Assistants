# rubricDimensions

`/tpdm/rubricDimensions`

The cells of a rubric, consisting of a qualitative decription, definition, or exemplar with the associated
rubric rating and rating level.

## Natural key

`rubricRating`, `evaluationElementReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `rubricRating` | key | integer (int32) | The rating achieved for the rubric dimension. |
| `evaluationElementReference` | key | reference: `educationOrganizationId`, `evaluationElementTitle`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` |  |
| `criterionDescription` | yes | string max 1024 | The criterion description for the rubric dimension. |
| `dimensionOrder` |  | integer (int32) | The order for the rubric dimension. |
| `rubricRatingLevelDescriptor` |  | descriptor URI | The rating level achieved for the rubric dimension. |

## Endpoints

- `DELETE /tpdm/rubricDimensions/{id}`
- `GET /tpdm/rubricDimensions/deletes`
- `GET /tpdm/rubricDimensions/keyChanges`
- `GET /tpdm/rubricDimensions/partitions`
- `GET /tpdm/rubricDimensions/{id}`
- `GET /tpdm/rubricDimensions`
- `POST /tpdm/rubricDimensions`
- `PUT /tpdm/rubricDimensions/{id}`
