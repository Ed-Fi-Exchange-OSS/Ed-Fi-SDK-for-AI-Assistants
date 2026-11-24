# quantitativeMeasureScores

`/ed-fi/quantitativeMeasureScores`

The score or value for a quantitative measure achieved by an individual educator.

## Natural key

`educationOrganizationId`, `evaluationDate`, `evaluationElementTitle`, `evaluationObjectiveTitle`,
`evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`,
`performanceEvaluationTypeDescriptor`, `personId`, `schoolYear`, `sourceSystemDescriptor`, `termDescriptor`,
`quantitativeMeasureIdentifier`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationElementRatingReference` | yes | reference; supply `educationOrganizationId`, `evaluationDate`, `evaluationElementTitle`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `personId`, `schoolYear`, `sourceSystemDescriptor`, `termDescriptor` | The lowest-level rating for an evaluation element for an individual educator. |
| `quantitativeMeasureReference` | yes | reference; supply `educationOrganizationId`, `evaluationElementTitle`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `quantitativeMeasureIdentifier`, `schoolYear`, `termDescriptor` | A quantitative measure of the educator performance associated with an evaluation element. |
| `scoreValue` | yes | number (double) | The score value for the quantitive measure. |
| `standardError` |  | number (double) | The standard error for the quantitative measure. |

## Endpoints

- `GET /ed-fi/quantitativeMeasureScores`
- `POST /ed-fi/quantitativeMeasureScores`
- `GET /ed-fi/quantitativeMeasureScores/deletes`
- `GET /ed-fi/quantitativeMeasureScores/keyChanges`
- `GET /ed-fi/quantitativeMeasureScores/partitions`
- `GET /ed-fi/quantitativeMeasureScores/{id}`
- `PUT /ed-fi/quantitativeMeasureScores/{id}`
- `DELETE /ed-fi/quantitativeMeasureScores/{id}`
