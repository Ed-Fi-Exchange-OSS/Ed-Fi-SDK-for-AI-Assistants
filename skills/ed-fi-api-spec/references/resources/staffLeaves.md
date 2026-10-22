# staffLeaves

`/ed-fi/staffLeaves`

This entity represents the recording of the dates of staff leave (e.g., sick leave, personal time, vacation).

## Natural key

`beginDate`, `staffLeaveEventCategoryDescriptor`, `staffReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | The begin date of the staff leave. |
| `staffLeaveEventCategoryDescriptor` | key | descriptor URI | The code describing the type of leave taken. |
| `staffReference` | key | reference: `staffUniqueId` |  |
| `endDate` |  | string (date) | The end date of the staff leave. |
| `reason` |  | string max 40 | Expanded reason for the staff leave. |
| `substituteAssigned` |  | boolean | Indicator of whether a substitute was assigned during the period of staff leave. |

## Endpoints

- `DELETE /ed-fi/staffLeaves/{id}`
- `GET /ed-fi/staffLeaves/deletes`
- `GET /ed-fi/staffLeaves/keyChanges`
- `GET /ed-fi/staffLeaves/partitions`
- `GET /ed-fi/staffLeaves/{id}`
- `GET /ed-fi/staffLeaves`
- `POST /ed-fi/staffLeaves`
- `PUT /ed-fi/staffLeaves/{id}`
