# surveySectionResponseStaffTargetAssociations

`/ed-fi/surveySectionResponseStaffTargetAssociations`

This association provides information about the survey section and the staff the survey section is about.

## Natural key

`staffReference`, `surveySectionResponseReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `staffReference` | key | reference: `staffUniqueId` |  |
| `surveySectionResponseReference` | key | reference: `namespace`, `surveyIdentifier`, `surveyResponseIdentifier`, `surveySectionTitle` |  |

## Endpoints

- `DELETE /ed-fi/surveySectionResponseStaffTargetAssociations/{id}`
- `GET /ed-fi/surveySectionResponseStaffTargetAssociations/deletes`
- `GET /ed-fi/surveySectionResponseStaffTargetAssociations/keyChanges`
- `GET /ed-fi/surveySectionResponseStaffTargetAssociations/partitions`
- `GET /ed-fi/surveySectionResponseStaffTargetAssociations/{id}`
- `GET /ed-fi/surveySectionResponseStaffTargetAssociations`
- `POST /ed-fi/surveySectionResponseStaffTargetAssociations`
- `PUT /ed-fi/surveySectionResponseStaffTargetAssociations/{id}`
