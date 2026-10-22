# surveySectionResponsePersonTargetAssociations

`/tpdm/surveySectionResponsePersonTargetAssociations`

This association provides information about the survey section and the person the survey section is about.

## Natural key

`personReference`, `surveySectionResponseReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `personReference` | key | reference: `personId`, `sourceSystemDescriptor` |  |
| `surveySectionResponseReference` | key | reference: `namespace`, `surveyIdentifier`, `surveyResponseIdentifier`, `surveySectionTitle` |  |

## Endpoints

- `DELETE /tpdm/surveySectionResponsePersonTargetAssociations/{id}`
- `GET /tpdm/surveySectionResponsePersonTargetAssociations/deletes`
- `GET /tpdm/surveySectionResponsePersonTargetAssociations/keyChanges`
- `GET /tpdm/surveySectionResponsePersonTargetAssociations/partitions`
- `GET /tpdm/surveySectionResponsePersonTargetAssociations/{id}`
- `GET /tpdm/surveySectionResponsePersonTargetAssociations`
- `POST /tpdm/surveySectionResponsePersonTargetAssociations`
- `PUT /tpdm/surveySectionResponsePersonTargetAssociations/{id}`
