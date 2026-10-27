# surveyProgramAssociations

`/ed-fi/surveyProgramAssociations`

The program associated with the survey.

## Natural key

`educationOrganizationId`, `programName`, `programTypeDescriptor`, `namespace`, `surveyIdentifier`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |
| `surveyReference` | yes | reference; supply `namespace`, `surveyIdentifier` | A survey to identified or anonymous respondents. |

## Endpoints

- `GET /ed-fi/surveyProgramAssociations`
- `POST /ed-fi/surveyProgramAssociations`
- `GET /ed-fi/surveyProgramAssociations/deletes`
- `GET /ed-fi/surveyProgramAssociations/keyChanges`
- `GET /ed-fi/surveyProgramAssociations/partitions`
- `GET /ed-fi/surveyProgramAssociations/{id}`
- `PUT /ed-fi/surveyProgramAssociations/{id}`
- `DELETE /ed-fi/surveyProgramAssociations/{id}`
