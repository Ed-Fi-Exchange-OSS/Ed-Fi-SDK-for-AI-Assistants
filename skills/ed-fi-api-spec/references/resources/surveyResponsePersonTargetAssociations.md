# surveyResponsePersonTargetAssociations

`/tpdm/surveyResponsePersonTargetAssociations`

The association provides information about the survey being taken and who the survey is about.

## Natural key

`personReference`, `surveyResponseReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `personReference` | key | reference: `personId`, `sourceSystemDescriptor` |  |
| `surveyResponseReference` | key | reference: `namespace`, `surveyIdentifier`, `surveyResponseIdentifier` |  |

## Endpoints

- `DELETE /tpdm/surveyResponsePersonTargetAssociations/{id}`
- `GET /tpdm/surveyResponsePersonTargetAssociations/deletes`
- `GET /tpdm/surveyResponsePersonTargetAssociations/keyChanges`
- `GET /tpdm/surveyResponsePersonTargetAssociations/partitions`
- `GET /tpdm/surveyResponsePersonTargetAssociations/{id}`
- `GET /tpdm/surveyResponsePersonTargetAssociations`
- `POST /tpdm/surveyResponsePersonTargetAssociations`
- `PUT /tpdm/surveyResponsePersonTargetAssociations/{id}`
