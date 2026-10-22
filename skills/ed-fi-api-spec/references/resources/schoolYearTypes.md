# schoolYearTypes

`/ed-fi/schoolYearTypes`

Identifier for a school year.

## Natural key

`schoolYear`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `schoolYear` | key | integer (int32) | Key for School Year |
| `currentSchoolYear` | yes | boolean | The code for the current school year. |
| `schoolYearDescription` | yes | string max 50 | The description for the SchoolYear type. |

## Endpoints

- `DELETE /ed-fi/schoolYearTypes/{id}`
- `GET /ed-fi/schoolYearTypes/partitions`
- `GET /ed-fi/schoolYearTypes/{id}`
- `GET /ed-fi/schoolYearTypes`
- `POST /ed-fi/schoolYearTypes`
- `PUT /ed-fi/schoolYearTypes/{id}`
