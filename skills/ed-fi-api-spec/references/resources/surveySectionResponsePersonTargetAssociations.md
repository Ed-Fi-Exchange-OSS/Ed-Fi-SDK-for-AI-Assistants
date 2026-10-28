# surveySectionResponsePersonTargetAssociations

`/tpdm/surveySectionResponsePersonTargetAssociations`

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

- `GET /tpdm/surveySectionResponsePersonTargetAssociations`
- `POST /tpdm/surveySectionResponsePersonTargetAssociations`
- `GET /tpdm/surveySectionResponsePersonTargetAssociations/deletes`
- `GET /tpdm/surveySectionResponsePersonTargetAssociations/keyChanges`
- `GET /tpdm/surveySectionResponsePersonTargetAssociations/partitions`
- `GET /tpdm/surveySectionResponsePersonTargetAssociations/{id}`
- `PUT /tpdm/surveySectionResponsePersonTargetAssociations/{id}`
- `DELETE /tpdm/surveySectionResponsePersonTargetAssociations/{id}`
