# quantitativeMeasures

`/ed-fi/quantitativeMeasures`

A quantitative measure of the educator performance associated with an evaluation element.

## Natural key

`quantitativeMeasureIdentifier`, `educationOrganizationId`, `evaluationElementTitle`,
`evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`,
`performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `quantitativeMeasureIdentifier` | yes | string max 64 | An assigned unique identifier for the quantitative measure. |
| `evaluationElementReference` | yes | reference; supply `educationOrganizationId`, `evaluationElementTitle`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `schoolYear`, `termDescriptor` | The lowest-level elements or criterion of performance being evaluated by rubric, quantitative measure, or aggregate survey response. |
| `quantitativeMeasureDatatypeDescriptor` |  | descriptor URI | The datatype of the result. |
| `quantitativeMeasureTypeDescriptor` |  | descriptor URI | The type of the quantitative measure. |

## Endpoints

- `GET /ed-fi/quantitativeMeasures`
- `POST /ed-fi/quantitativeMeasures`
- `GET /ed-fi/quantitativeMeasures/deletes`
- `GET /ed-fi/quantitativeMeasures/keyChanges`
- `GET /ed-fi/quantitativeMeasures/partitions`
- `GET /ed-fi/quantitativeMeasures/{id}`
- `PUT /ed-fi/quantitativeMeasures/{id}`
- `DELETE /ed-fi/quantitativeMeasures/{id}`
