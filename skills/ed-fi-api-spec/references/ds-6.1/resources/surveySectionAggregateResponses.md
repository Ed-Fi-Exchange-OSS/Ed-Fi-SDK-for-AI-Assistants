# surveySectionAggregateResponses

`/ed-fi/surveySectionAggregateResponses`

The aggregate or average score across the surveying population for a survey section being used for performance
evaluation.

## Natural key

`educationOrganizationId`, `evaluationDate`, `evaluationElementTitle`, `evaluationObjectiveTitle`,
`evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`,
`performanceEvaluationTypeDescriptor`, `personId`, `schoolYear`, `sourceSystemDescriptor`, `termDescriptor`,
`namespace`, `surveyIdentifier`, `surveySectionTitle`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `evaluationElementRatingReference` | yes | reference; supply `educationOrganizationId`, `evaluationDate`, `evaluationElementTitle`, `evaluationObjectiveTitle`, `evaluationPeriodDescriptor`, `evaluationTitle`, `performanceEvaluationTitle`, `performanceEvaluationTypeDescriptor`, `personId`, `schoolYear`, `sourceSystemDescriptor`, `termDescriptor` | The lowest-level rating for an evaluation element for an individual educator. |
| `surveySectionReference` | yes | reference; supply `namespace`, `surveyIdentifier`, `surveySectionTitle` | The section of questions for the survey. |
| `scoreValue` | yes | number (double) | The score value for the aggregate survey section response. |

## Endpoints

- `GET /ed-fi/surveySectionAggregateResponses`
- `POST /ed-fi/surveySectionAggregateResponses`
- `GET /ed-fi/surveySectionAggregateResponses/deletes`
- `GET /ed-fi/surveySectionAggregateResponses/keyChanges`
- `GET /ed-fi/surveySectionAggregateResponses/partitions`
- `GET /ed-fi/surveySectionAggregateResponses/{id}`
- `PUT /ed-fi/surveySectionAggregateResponses/{id}`
- `DELETE /ed-fi/surveySectionAggregateResponses/{id}`
