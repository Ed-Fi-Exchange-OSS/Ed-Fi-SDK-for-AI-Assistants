# surveySectionResponsePersonTargetAssociations

`/ed-fi/surveySectionResponsePersonTargetAssociations`

This association provides information about the survey section and the person the survey section is about.

## Natural key

`personId`, `sourceSystemDescriptor`, `namespace`, `surveyIdentifier`, `surveyResponseIdentifier`,
`surveySectionTitle`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `personReference` | yes | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `surveySectionResponseReference` | yes | reference; supply `namespace`, `surveyIdentifier`, `surveyResponseIdentifier`, `surveySectionTitle` | Optional information about the responses provided for a section of a survey. |

## Endpoints

- `GET /ed-fi/surveySectionResponsePersonTargetAssociations`
- `POST /ed-fi/surveySectionResponsePersonTargetAssociations`
- `GET /ed-fi/surveySectionResponsePersonTargetAssociations/deletes`
- `GET /ed-fi/surveySectionResponsePersonTargetAssociations/keyChanges`
- `GET /ed-fi/surveySectionResponsePersonTargetAssociations/partitions`
- `GET /ed-fi/surveySectionResponsePersonTargetAssociations/{id}`
- `PUT /ed-fi/surveySectionResponsePersonTargetAssociations/{id}`
- `DELETE /ed-fi/surveySectionResponsePersonTargetAssociations/{id}`
