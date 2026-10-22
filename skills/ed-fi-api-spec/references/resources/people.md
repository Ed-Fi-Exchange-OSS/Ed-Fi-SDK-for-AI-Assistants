# people

`/ed-fi/people`

This entity represents a human being.

## Natural key

`personId`, `sourceSystemDescriptor`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `personId` | key | string max 32 | A unique alphanumeric code assigned to a person. |
| `sourceSystemDescriptor` | key | descriptor URI | This descriptor defines the originating record source system for the person. |

## Endpoints

- `DELETE /ed-fi/people/{id}`
- `GET /ed-fi/people/deletes`
- `GET /ed-fi/people/keyChanges`
- `GET /ed-fi/people/partitions`
- `GET /ed-fi/people/{id}`
- `GET /ed-fi/people`
- `POST /ed-fi/people`
- `PUT /ed-fi/people/{id}`
