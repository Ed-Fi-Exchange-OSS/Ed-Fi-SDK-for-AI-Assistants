# academicWeeks

`/ed-fi/academicWeeks`

This entity represents the academic weeks for a school year, optionally captured to support analyses.

## Natural key

`weekIdentifier`, `schoolId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `weekIdentifier` | yes | string max 80 | The school label for the week. |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `beginDate` | yes | string (date) | The start date for the academic week. |
| `endDate` | yes | string (date) | The end date for the academic week. |
| `totalInstructionalDays` | yes | integer (int32) | The total instructional days during the academic week. |

## Endpoints

- `GET /ed-fi/academicWeeks`
- `POST /ed-fi/academicWeeks`
- `GET /ed-fi/academicWeeks/deletes`
- `GET /ed-fi/academicWeeks/keyChanges`
- `GET /ed-fi/academicWeeks/partitions`
- `GET /ed-fi/academicWeeks/{id}`
- `PUT /ed-fi/academicWeeks/{id}`
- `DELETE /ed-fi/academicWeeks/{id}`
