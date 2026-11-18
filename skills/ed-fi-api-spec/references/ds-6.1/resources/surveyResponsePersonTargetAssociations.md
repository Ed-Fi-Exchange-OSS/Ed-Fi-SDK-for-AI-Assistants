# surveyResponsePersonTargetAssociations

`/ed-fi/surveyResponsePersonTargetAssociations`

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

- `GET /ed-fi/surveyResponsePersonTargetAssociations`
- `POST /ed-fi/surveyResponsePersonTargetAssociations`
- `GET /ed-fi/surveyResponsePersonTargetAssociations/deletes`
- `GET /ed-fi/surveyResponsePersonTargetAssociations/keyChanges`
- `GET /ed-fi/surveyResponsePersonTargetAssociations/partitions`
- `GET /ed-fi/surveyResponsePersonTargetAssociations/{id}`
- `PUT /ed-fi/surveyResponsePersonTargetAssociations/{id}`
- `DELETE /ed-fi/surveyResponsePersonTargetAssociations/{id}`
