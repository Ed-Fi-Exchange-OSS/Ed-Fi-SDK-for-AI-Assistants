# surveyProgramAssociations

`/ed-fi/surveyProgramAssociations`

The program associated with the survey.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

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
