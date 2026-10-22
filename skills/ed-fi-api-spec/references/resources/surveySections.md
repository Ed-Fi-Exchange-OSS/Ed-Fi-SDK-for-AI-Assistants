# surveySections

`/ed-fi/surveySections`

The section of questions for the survey.

## Natural key

`surveySectionTitle`, `surveyReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `surveySectionTitle` | key | string max 255 | The title or label for the survey section. |
| `surveyReference` | key | reference: `namespace`, `surveyIdentifier` |  |

## Endpoints

- `DELETE /ed-fi/surveySections/{id}`
- `GET /ed-fi/surveySections/deletes`
- `GET /ed-fi/surveySections/keyChanges`
- `GET /ed-fi/surveySections/partitions`
- `GET /ed-fi/surveySections/{id}`
- `GET /ed-fi/surveySections`
- `POST /ed-fi/surveySections`
- `PUT /ed-fi/surveySections/{id}`
