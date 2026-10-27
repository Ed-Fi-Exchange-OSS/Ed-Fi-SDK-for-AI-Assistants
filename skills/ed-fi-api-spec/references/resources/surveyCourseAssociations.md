# surveyCourseAssociations

`/ed-fi/surveyCourseAssociations`

The course associated with the survey.

## Natural key

`courseCode`, `educationOrganizationId`, `namespace`, `surveyIdentifier`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

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
