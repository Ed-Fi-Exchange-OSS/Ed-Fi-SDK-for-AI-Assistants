# schoolYearTypes

`/ed-fi/schoolYearTypes`

Identifier for a school year.

## Natural key

`schoolYear`

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
