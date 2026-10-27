# surveys

`/ed-fi/surveys`

A survey to identified or anonymous respondents.

## Natural key

`namespace`, `surveyIdentifier`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `namespace` | yes | string max 255 | Namespace for the survey. |
| `surveyIdentifier` | yes | string max 60 | The unique survey identifier from the survey tool. |
| `educationOrganizationReference` |  | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |
| `sessionReference` |  | reference; supply `schoolId`, `schoolYear`, `sessionName` | A specific designated unit of time during which instruction is provided, grades are reported and academic credits are awarded to students (whenever applicable). |
| `numberAdministered` |  | integer (int32) | Number of persons to whom this survey was administered. |
| `surveyCategoryDescriptor` |  | descriptor URI | The category or type of survey. |
| `surveyTitle` | yes | string max 255 | The title of the survey. |

## Endpoints

- `GET /ed-fi/surveys`
- `POST /ed-fi/surveys`
- `GET /ed-fi/surveys/deletes`
- `GET /ed-fi/surveys/keyChanges`
- `GET /ed-fi/surveys/partitions`
- `GET /ed-fi/surveys/{id}`
- `PUT /ed-fi/surveys/{id}`
- `DELETE /ed-fi/surveys/{id}`
