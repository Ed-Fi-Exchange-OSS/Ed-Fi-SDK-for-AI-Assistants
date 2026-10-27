# surveySections

`/ed-fi/surveySections`

The section of questions for the survey.

## Natural key

`surveySectionTitle`, `namespace`, `surveyIdentifier`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `surveySectionTitle` | yes | string max 255 | The title or label for the survey section. |
| `surveyReference` | yes | reference; supply `namespace`, `surveyIdentifier` | A survey to identified or anonymous respondents. |

## Endpoints

- `GET /ed-fi/surveySections`
- `POST /ed-fi/surveySections`
- `GET /ed-fi/surveySections/deletes`
- `GET /ed-fi/surveySections/keyChanges`
- `GET /ed-fi/surveySections/partitions`
- `GET /ed-fi/surveySections/{id}`
- `PUT /ed-fi/surveySections/{id}`
- `DELETE /ed-fi/surveySections/{id}`
