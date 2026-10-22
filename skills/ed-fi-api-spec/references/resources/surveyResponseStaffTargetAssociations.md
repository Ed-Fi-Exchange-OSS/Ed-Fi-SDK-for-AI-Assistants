# surveyResponseStaffTargetAssociations

`/ed-fi/surveyResponseStaffTargetAssociations`

The association provides information about the survey being taken and who the survey is about.

## Natural key

`staffReference`, `surveyResponseReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `staffReference` | key | reference: `staffUniqueId` |  |
| `surveyResponseReference` | key | reference: `namespace`, `surveyIdentifier`, `surveyResponseIdentifier` |  |

## Endpoints

- `DELETE /ed-fi/surveyResponseStaffTargetAssociations/{id}`
- `GET /ed-fi/surveyResponseStaffTargetAssociations/deletes`
- `GET /ed-fi/surveyResponseStaffTargetAssociations/keyChanges`
- `GET /ed-fi/surveyResponseStaffTargetAssociations/partitions`
- `GET /ed-fi/surveyResponseStaffTargetAssociations/{id}`
- `GET /ed-fi/surveyResponseStaffTargetAssociations`
- `POST /ed-fi/surveyResponseStaffTargetAssociations`
- `PUT /ed-fi/surveyResponseStaffTargetAssociations/{id}`
