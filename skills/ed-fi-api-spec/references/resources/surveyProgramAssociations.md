# surveyProgramAssociations

`/ed-fi/surveyProgramAssociations`

The program associated with the survey.

## Natural key

`programReference`, `surveyReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programReference` | key | reference: `educationOrganizationId`, `programName`, `programTypeDescriptor` |  |
| `surveyReference` | key | reference: `namespace`, `surveyIdentifier` |  |

## Endpoints

- `DELETE /ed-fi/surveyProgramAssociations/{id}`
- `GET /ed-fi/surveyProgramAssociations/deletes`
- `GET /ed-fi/surveyProgramAssociations/keyChanges`
- `GET /ed-fi/surveyProgramAssociations/partitions`
- `GET /ed-fi/surveyProgramAssociations/{id}`
- `GET /ed-fi/surveyProgramAssociations`
- `POST /ed-fi/surveyProgramAssociations`
- `PUT /ed-fi/surveyProgramAssociations/{id}`
