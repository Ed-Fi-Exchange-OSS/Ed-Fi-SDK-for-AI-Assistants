# staffEducationOrganizationContactAssociations

`/ed-fi/staffEducationOrganizationContactAssociations`

This association provides the contact information of the staff associated with the education organization.

## Natural key

`contactTitle`, `educationOrganizationReference`, `staffReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `contactTitle` | key | string max 75 | The title of the contact in the context of the education organization. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `staffReference` | key | reference: `staffUniqueId` |  |
| `address` |  | edFi_staffEducationOrganizationContactAssociationAddress |  |
| `contactTypeDescriptor` |  | descriptor URI | Indicates the type for the contact information. |
| `electronicMailAddress` | yes | string max 128 | The email for the contact associated with the education organization. |
| `telephones` |  | array of edFi_staffEducationOrganizationContactAssociationTelephone | An unordered collection of staffEducationOrganizationContactAssociationTelephones. |

## Endpoints

- `DELETE /ed-fi/staffEducationOrganizationContactAssociations/{id}`
- `GET /ed-fi/staffEducationOrganizationContactAssociations/deletes`
- `GET /ed-fi/staffEducationOrganizationContactAssociations/keyChanges`
- `GET /ed-fi/staffEducationOrganizationContactAssociations/partitions`
- `GET /ed-fi/staffEducationOrganizationContactAssociations/{id}`
- `GET /ed-fi/staffEducationOrganizationContactAssociations`
- `POST /ed-fi/staffEducationOrganizationContactAssociations`
- `PUT /ed-fi/staffEducationOrganizationContactAssociations/{id}`
