# educationOrganizationPeerAssociations

`/ed-fi/educationOrganizationPeerAssociations`

The association from an education organization to its peers.

## Natural key

`educationOrganizationReference`, `peerEducationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `peerEducationOrganizationReference` | key | reference: `educationOrganizationId` |  |

## Endpoints

- `DELETE /ed-fi/educationOrganizationPeerAssociations/{id}`
- `GET /ed-fi/educationOrganizationPeerAssociations/deletes`
- `GET /ed-fi/educationOrganizationPeerAssociations/keyChanges`
- `GET /ed-fi/educationOrganizationPeerAssociations/partitions`
- `GET /ed-fi/educationOrganizationPeerAssociations/{id}`
- `GET /ed-fi/educationOrganizationPeerAssociations`
- `POST /ed-fi/educationOrganizationPeerAssociations`
- `PUT /ed-fi/educationOrganizationPeerAssociations/{id}`
