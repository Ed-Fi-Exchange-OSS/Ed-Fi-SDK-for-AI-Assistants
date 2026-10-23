# surveySectionResponsePersonTargetAssociations

`/tpdm/surveySectionResponsePersonTargetAssociations`

This association provides information about the survey section and the person the survey section is about.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

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
