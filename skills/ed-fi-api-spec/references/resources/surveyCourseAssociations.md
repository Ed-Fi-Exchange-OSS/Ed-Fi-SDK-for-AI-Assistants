# surveyCourseAssociations

`/ed-fi/surveyCourseAssociations`

The course associated with the survey.

## Natural key

`courseReference`, `surveyReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `courseReference` | key | reference: `courseCode`, `educationOrganizationId` |  |
| `surveyReference` | key | reference: `namespace`, `surveyIdentifier` |  |

## Endpoints

- `DELETE /ed-fi/surveyCourseAssociations/{id}`
- `GET /ed-fi/surveyCourseAssociations/deletes`
- `GET /ed-fi/surveyCourseAssociations/keyChanges`
- `GET /ed-fi/surveyCourseAssociations/partitions`
- `GET /ed-fi/surveyCourseAssociations/{id}`
- `GET /ed-fi/surveyCourseAssociations`
- `POST /ed-fi/surveyCourseAssociations`
- `PUT /ed-fi/surveyCourseAssociations/{id}`
