# academicWeeks

`/ed-fi/academicWeeks`

This entity represents the academic weeks for a school year, optionally captured to support analyses.

## Natural key

`weekIdentifier`, `schoolReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `weekIdentifier` | key | string max 80 | The school label for the week. |
| `schoolReference` | key | reference: `schoolId` |  |
| `beginDate` | yes | string (date) | The start date for the academic week. |
| `endDate` | yes | string (date) | The end date for the academic week. |
| `totalInstructionalDays` | yes | integer (int32) | The total instructional days during the academic week. |

## Endpoints

- `DELETE /ed-fi/academicWeeks/{id}`
- `GET /ed-fi/academicWeeks/deletes`
- `GET /ed-fi/academicWeeks/keyChanges`
- `GET /ed-fi/academicWeeks/partitions`
- `GET /ed-fi/academicWeeks/{id}`
- `GET /ed-fi/academicWeeks`
- `POST /ed-fi/academicWeeks`
- `PUT /ed-fi/academicWeeks/{id}`
