# people

`/ed-fi/people`

This entity represents a human being.

## Natural key

`sourceSystemDescriptor`, `personId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `personId` | yes | string max 32 | A unique alphanumeric code assigned to a person. |
| `sourceSystemDescriptor` | yes | descriptor URI | This descriptor defines the originating record source system for the person. |

## Endpoints

- `GET /ed-fi/people`
- `POST /ed-fi/people`
- `GET /ed-fi/people/deletes`
- `GET /ed-fi/people/keyChanges`
- `GET /ed-fi/people/partitions`
- `GET /ed-fi/people/{id}`
- `PUT /ed-fi/people/{id}`
- `DELETE /ed-fi/people/{id}`
