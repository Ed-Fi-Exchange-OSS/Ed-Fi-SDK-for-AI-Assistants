# surveyResponsePersonTargetAssociations

`/tpdm/surveyResponsePersonTargetAssociations`

The association provides information about the survey being taken and who the survey is about.

## Natural key

`personId`, `sourceSystemDescriptor`, `namespace`, `surveyIdentifier`, `surveyResponseIdentifier`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `personReference` | yes | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `surveyResponseReference` | yes | reference; supply `namespace`, `surveyIdentifier`, `surveyResponseIdentifier` | Responses to a Survey for named or anonymous persons. |

## Endpoints

- `GET /tpdm/surveyResponsePersonTargetAssociations`
- `POST /tpdm/surveyResponsePersonTargetAssociations`
- `GET /tpdm/surveyResponsePersonTargetAssociations/deletes`
- `GET /tpdm/surveyResponsePersonTargetAssociations/keyChanges`
- `GET /tpdm/surveyResponsePersonTargetAssociations/partitions`
- `GET /tpdm/surveyResponsePersonTargetAssociations/{id}`
- `PUT /tpdm/surveyResponsePersonTargetAssociations/{id}`
- `DELETE /tpdm/surveyResponsePersonTargetAssociations/{id}`
