# learningStandardEquivalenceAssociations

`/ed-fi/learningStandardEquivalenceAssociations`

Indicates a directional association of equivalence from a source to a target learning standard.

## Natural key

`namespace`, `sourceLearningStandardReference`, `targetLearningStandardReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `namespace` | key | string max 255 | The namespace of the organization that has created and owns the association. |
| `sourceLearningStandardReference` | key | reference: `learningStandardId` |  |
| `targetLearningStandardReference` | key | reference: `learningStandardId` |  |
| `effectiveDate` |  | string (date) | The date that the association is considered to be applicable or effective. |
| `learningStandardEquivalenceStrengthDescription` |  | string max 255 | Captures supplemental information on the relationship. |
| `learningStandardEquivalenceStrengthDescriptor` |  | descriptor URI | A measure that indicates the strength or quality of the equivalence relationship. |

## Endpoints

- `DELETE /ed-fi/learningStandardEquivalenceAssociations/{id}`
- `GET /ed-fi/learningStandardEquivalenceAssociations/deletes`
- `GET /ed-fi/learningStandardEquivalenceAssociations/keyChanges`
- `GET /ed-fi/learningStandardEquivalenceAssociations/partitions`
- `GET /ed-fi/learningStandardEquivalenceAssociations/{id}`
- `GET /ed-fi/learningStandardEquivalenceAssociations`
- `POST /ed-fi/learningStandardEquivalenceAssociations`
- `PUT /ed-fi/learningStandardEquivalenceAssociations/{id}`
