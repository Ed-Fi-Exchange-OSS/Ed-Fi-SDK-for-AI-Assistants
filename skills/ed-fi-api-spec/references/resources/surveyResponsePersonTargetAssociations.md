# surveyResponsePersonTargetAssociations

`/tpdm/surveyResponsePersonTargetAssociations`

The association provides information about the survey being taken and who the survey is about.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

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
