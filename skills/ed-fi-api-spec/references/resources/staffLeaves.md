# staffLeaves

`/ed-fi/staffLeaves`

This entity represents the recording of the dates of staff leave (e.g., sick leave, personal time, vacation).

## Natural key

`staffLeaveEventCategoryDescriptor`, `beginDate`, `staffUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The begin date of the staff leave. |
| `staffLeaveEventCategoryDescriptor` | yes | descriptor URI | The code describing the type of leave taken. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `endDate` |  | string (date) | The end date of the staff leave. |
| `reason` |  | string max 40 | Expanded reason for the staff leave. |
| `substituteAssigned` |  | boolean | Indicator of whether a substitute was assigned during the period of staff leave. |

## Endpoints

- `GET /ed-fi/staffLeaves`
- `POST /ed-fi/staffLeaves`
- `GET /ed-fi/staffLeaves/deletes`
- `GET /ed-fi/staffLeaves/keyChanges`
- `GET /ed-fi/staffLeaves/partitions`
- `GET /ed-fi/staffLeaves/{id}`
- `PUT /ed-fi/staffLeaves/{id}`
- `DELETE /ed-fi/staffLeaves/{id}`
