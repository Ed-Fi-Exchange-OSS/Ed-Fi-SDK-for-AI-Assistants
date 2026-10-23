# surveySectionResponseStaffTargetAssociations

`/ed-fi/surveySectionResponseStaffTargetAssociations`

This association provides information about the survey section and the staff the survey section is about.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `surveySectionResponseReference` | yes | reference; supply `namespace`, `surveyIdentifier`, `surveyResponseIdentifier`, `surveySectionTitle` | Optional information about the responses provided for a section of a survey. |

## Endpoints

- `GET /ed-fi/surveySectionResponseStaffTargetAssociations`
- `POST /ed-fi/surveySectionResponseStaffTargetAssociations`
- `GET /ed-fi/surveySectionResponseStaffTargetAssociations/deletes`
- `GET /ed-fi/surveySectionResponseStaffTargetAssociations/keyChanges`
- `GET /ed-fi/surveySectionResponseStaffTargetAssociations/partitions`
- `GET /ed-fi/surveySectionResponseStaffTargetAssociations/{id}`
- `PUT /ed-fi/surveySectionResponseStaffTargetAssociations/{id}`
- `DELETE /ed-fi/surveySectionResponseStaffTargetAssociations/{id}`
