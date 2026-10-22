# programEvaluationElements

`/ed-fi/programEvaluationElements`

The lowest level elements or criterion of a students's performance that is being evaluated, typically by a
rubric.

## Natural key

`programEvaluationElementTitle`, `programEvaluationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programEvaluationElementTitle` | key | string max 50 | The name or title of the program evaluation element. |
| `programEvaluationObjectiveReference` |  | reference: `programEducationOrganizationId`, `programEvaluationObjectiveTitle`, `programEvaluationPeriodDescriptor`, `programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor` |  |
| `programEvaluationReference` | key | reference: `programEducationOrganizationId`, `programEvaluationPeriodDescriptor`, `programEvaluationTitle`, `programEvaluationTypeDescriptor`, `programName`, `programTypeDescriptor` |  |
| `elementMaxNumericRating` |  | number (double) | The maximum summary numerical rating or score for the program evaluation element. |
| `elementMinNumericRating` |  | number (double) | The minimum summary numerical rating or score for the program evaluation element. |
| `elementSortOrder` |  | integer (int32) | The sort order of this program evaluation element. |
| `programEvaluationElementDescription` |  | string max 255 | The long description of the program evaluation element. |
| `programEvaluationLevels` |  | array of edFi_programEvaluationElementProgramEvaluationLevel | An unordered collection of programEvaluationElementProgramEvaluationLevels. |

## Endpoints

- `DELETE /ed-fi/programEvaluationElements/{id}`
- `GET /ed-fi/programEvaluationElements/deletes`
- `GET /ed-fi/programEvaluationElements/keyChanges`
- `GET /ed-fi/programEvaluationElements/partitions`
- `GET /ed-fi/programEvaluationElements/{id}`
- `GET /ed-fi/programEvaluationElements`
- `POST /ed-fi/programEvaluationElements`
- `PUT /ed-fi/programEvaluationElements/{id}`
