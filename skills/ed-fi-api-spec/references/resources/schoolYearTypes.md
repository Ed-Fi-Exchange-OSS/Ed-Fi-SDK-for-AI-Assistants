# schoolYearTypes

`/ed-fi/schoolYearTypes`

Identifier for a school year.

## Natural key

`schoolYear`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `schoolYear` | yes | integer (int32) | Key for School Year |
| `currentSchoolYear` | yes | boolean | The code for the current school year. |
| `schoolYearDescription` | yes | string max 50 | The description for the SchoolYear type. |

## Endpoints

- `GET /ed-fi/schoolYearTypes`
- `POST /ed-fi/schoolYearTypes`
- `GET /ed-fi/schoolYearTypes/partitions`
- `GET /ed-fi/schoolYearTypes/{id}`
- `PUT /ed-fi/schoolYearTypes/{id}`
- `DELETE /ed-fi/schoolYearTypes/{id}`
