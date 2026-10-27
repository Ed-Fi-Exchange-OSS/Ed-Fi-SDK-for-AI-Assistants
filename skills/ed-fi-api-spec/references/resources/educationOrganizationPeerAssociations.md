# educationOrganizationPeerAssociations

`/ed-fi/educationOrganizationPeerAssociations`

The association from an education organization to its peers.

## Natural key

`educationOrganizationId`, `peerEducationOrganizationId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `peerEducationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |

## Endpoints

- `GET /ed-fi/educationOrganizationPeerAssociations`
- `POST /ed-fi/educationOrganizationPeerAssociations`
- `GET /ed-fi/educationOrganizationPeerAssociations/deletes`
- `GET /ed-fi/educationOrganizationPeerAssociations/keyChanges`
- `GET /ed-fi/educationOrganizationPeerAssociations/partitions`
- `GET /ed-fi/educationOrganizationPeerAssociations/{id}`
- `PUT /ed-fi/educationOrganizationPeerAssociations/{id}`
- `DELETE /ed-fi/educationOrganizationPeerAssociations/{id}`
