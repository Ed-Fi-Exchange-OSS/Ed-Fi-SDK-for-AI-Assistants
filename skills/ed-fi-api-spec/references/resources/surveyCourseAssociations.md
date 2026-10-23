# surveyCourseAssociations

`/ed-fi/surveyCourseAssociations`

The course associated with the survey.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `courseReference` | yes | reference; supply `courseCode`, `educationOrganizationId` | This educational entity represents the organization of subject matter and related learning experiences provided for the instruction of students on a regular or… |
| `surveyReference` | yes | reference; supply `namespace`, `surveyIdentifier` | A survey to identified or anonymous respondents. |

## Endpoints

- `GET /ed-fi/surveyCourseAssociations`
- `POST /ed-fi/surveyCourseAssociations`
- `GET /ed-fi/surveyCourseAssociations/deletes`
- `GET /ed-fi/surveyCourseAssociations/keyChanges`
- `GET /ed-fi/surveyCourseAssociations/partitions`
- `GET /ed-fi/surveyCourseAssociations/{id}`
- `PUT /ed-fi/surveyCourseAssociations/{id}`
- `DELETE /ed-fi/surveyCourseAssociations/{id}`
