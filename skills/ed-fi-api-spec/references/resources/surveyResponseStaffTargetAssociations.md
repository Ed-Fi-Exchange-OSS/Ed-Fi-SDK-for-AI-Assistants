# surveyResponseStaffTargetAssociations

`/ed-fi/surveyResponseStaffTargetAssociations`

The association provides information about the survey being taken and who the survey is about.

## Natural key

`staffUniqueId`, `namespace`, `surveyIdentifier`, `surveyResponseIdentifier`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `surveyResponseReference` | yes | reference; supply `namespace`, `surveyIdentifier`, `surveyResponseIdentifier` | Responses to a Survey for named or anonymous persons. |

## Endpoints

- `GET /ed-fi/surveyResponseStaffTargetAssociations`
- `POST /ed-fi/surveyResponseStaffTargetAssociations`
- `GET /ed-fi/surveyResponseStaffTargetAssociations/deletes`
- `GET /ed-fi/surveyResponseStaffTargetAssociations/keyChanges`
- `GET /ed-fi/surveyResponseStaffTargetAssociations/partitions`
- `GET /ed-fi/surveyResponseStaffTargetAssociations/{id}`
- `PUT /ed-fi/surveyResponseStaffTargetAssociations/{id}`
- `DELETE /ed-fi/surveyResponseStaffTargetAssociations/{id}`
