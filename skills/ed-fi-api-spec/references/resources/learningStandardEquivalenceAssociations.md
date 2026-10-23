# learningStandardEquivalenceAssociations

`/ed-fi/learningStandardEquivalenceAssociations`

Indicates a directional association of equivalence from a source to a target learning standard.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `namespace` | yes | string max 255 | The namespace of the organization that has created and owns the association. |
| `sourceLearningStandardReference` | yes | reference; supply `learningStandardId` | A statement that describes a specific competency or academic standard. |
| `targetLearningStandardReference` | yes | reference; supply `learningStandardId` | A statement that describes a specific competency or academic standard. |
| `effectiveDate` |  | string (date) | The date that the association is considered to be applicable or effective. |
| `learningStandardEquivalenceStrengthDescription` |  | string max 255 | Captures supplemental information on the relationship. |
| `learningStandardEquivalenceStrengthDescriptor` |  | descriptor URI | A measure that indicates the strength or quality of the equivalence relationship. |

## Endpoints

- `GET /ed-fi/learningStandardEquivalenceAssociations`
- `POST /ed-fi/learningStandardEquivalenceAssociations`
- `GET /ed-fi/learningStandardEquivalenceAssociations/deletes`
- `GET /ed-fi/learningStandardEquivalenceAssociations/keyChanges`
- `GET /ed-fi/learningStandardEquivalenceAssociations/partitions`
- `GET /ed-fi/learningStandardEquivalenceAssociations/{id}`
- `PUT /ed-fi/learningStandardEquivalenceAssociations/{id}`
- `DELETE /ed-fi/learningStandardEquivalenceAssociations/{id}`
