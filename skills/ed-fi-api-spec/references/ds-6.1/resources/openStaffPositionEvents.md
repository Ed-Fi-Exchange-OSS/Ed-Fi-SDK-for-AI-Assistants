# openStaffPositionEvents

`/ed-fi/openStaffPositionEvents`

Represents significant milestones related to an open staff position.

## Natural key

`openStaffPositionEventTypeDescriptor`, `eventDate`, `educationOrganizationId`, `requisitionNumber`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `eventDate` | yes | string (date) | The date when the open staff position event occurred. |
| `openStaffPositionEventTypeDescriptor` | yes | descriptor URI | Specifies the type of milestone event. |
| `openStaffPositionReference` | yes | reference; supply `educationOrganizationId`, `requisitionNumber` | This entity represents an open staff position that the education organization is seeking to fill. |
| `openStaffPositionEventStatusDescriptor` |  | descriptor URI | Reflects the status of the milestone event. |

## Endpoints

- `GET /ed-fi/openStaffPositionEvents`
- `POST /ed-fi/openStaffPositionEvents`
- `GET /ed-fi/openStaffPositionEvents/deletes`
- `GET /ed-fi/openStaffPositionEvents/keyChanges`
- `GET /ed-fi/openStaffPositionEvents/partitions`
- `GET /ed-fi/openStaffPositionEvents/{id}`
- `PUT /ed-fi/openStaffPositionEvents/{id}`
- `DELETE /ed-fi/openStaffPositionEvents/{id}`
