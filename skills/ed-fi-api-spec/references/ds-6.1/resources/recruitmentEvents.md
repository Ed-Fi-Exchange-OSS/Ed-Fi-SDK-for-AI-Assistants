# recruitmentEvents

`/ed-fi/recruitmentEvents`

Events associated with the recruitment process.

## Natural key

`eventDate`, `eventTitle`, `educationOrganizationId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `eventDate` | yes | string (date) | The date of the event. |
| `eventTitle` | yes | string max 50 | The title of the event. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `eventDescription` |  | string max 255 | The long description of the event. |
| `eventLocation` |  | string max 255 | The location of the event. |
| `recruitmentEventTypeDescriptor` | yes | descriptor URI | The type of event. |

## Endpoints

- `GET /ed-fi/recruitmentEvents`
- `POST /ed-fi/recruitmentEvents`
- `GET /ed-fi/recruitmentEvents/deletes`
- `GET /ed-fi/recruitmentEvents/keyChanges`
- `GET /ed-fi/recruitmentEvents/partitions`
- `GET /ed-fi/recruitmentEvents/{id}`
- `PUT /ed-fi/recruitmentEvents/{id}`
- `DELETE /ed-fi/recruitmentEvents/{id}`
