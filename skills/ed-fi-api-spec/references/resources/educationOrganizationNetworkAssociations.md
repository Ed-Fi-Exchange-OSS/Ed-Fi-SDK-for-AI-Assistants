# educationOrganizationNetworkAssociations

`/ed-fi/educationOrganizationNetworkAssociations`

Properties of the association between the education organization and its network(s).

## Natural key

`educationOrganizationNetworkReference`, `memberEducationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationNetworkReference` | key | reference: `educationOrganizationNetworkId` |  |
| `memberEducationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `beginDate` |  | string (date) | The date on which the education organization joined this network. |
| `endDate` |  | string (date) | The date on which the education organization left this network. |

## Endpoints

- `DELETE /ed-fi/educationOrganizationNetworkAssociations/{id}`
- `GET /ed-fi/educationOrganizationNetworkAssociations/deletes`
- `GET /ed-fi/educationOrganizationNetworkAssociations/keyChanges`
- `GET /ed-fi/educationOrganizationNetworkAssociations/partitions`
- `GET /ed-fi/educationOrganizationNetworkAssociations/{id}`
- `GET /ed-fi/educationOrganizationNetworkAssociations`
- `POST /ed-fi/educationOrganizationNetworkAssociations`
- `PUT /ed-fi/educationOrganizationNetworkAssociations/{id}`
