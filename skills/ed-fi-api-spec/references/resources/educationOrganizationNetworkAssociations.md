# educationOrganizationNetworkAssociations

`/ed-fi/educationOrganizationNetworkAssociations`

Properties of the association between the education organization and its network(s).

## Natural key

`memberEducationOrganizationId`, `educationOrganizationNetworkId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationNetworkReference` | yes | reference; supply `educationOrganizationNetworkId` | This entity is a self-organized membership network of peer-level education organizations intended to provide shared services or collective procurement. |
| `memberEducationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `beginDate` |  | string (date) | The date on which the education organization joined this network. |
| `endDate` |  | string (date) | The date on which the education organization left this network. |

## Endpoints

- `GET /ed-fi/educationOrganizationNetworkAssociations`
- `POST /ed-fi/educationOrganizationNetworkAssociations`
- `GET /ed-fi/educationOrganizationNetworkAssociations/deletes`
- `GET /ed-fi/educationOrganizationNetworkAssociations/keyChanges`
- `GET /ed-fi/educationOrganizationNetworkAssociations/partitions`
- `GET /ed-fi/educationOrganizationNetworkAssociations/{id}`
- `PUT /ed-fi/educationOrganizationNetworkAssociations/{id}`
- `DELETE /ed-fi/educationOrganizationNetworkAssociations/{id}`
