# staffEducationOrganizationContactAssociations

`/ed-fi/staffEducationOrganizationContactAssociations`

This association provides the contact information of the staff associated with the education organization.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `contactTitle` | yes | string max 75 | The title of the contact in the context of the education organization. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `address` |  | edFi_staffEducationOrganizationContactAssociationAddress |  |
| `contactTypeDescriptor` |  | descriptor URI | Indicates the type for the contact information. |
| `electronicMailAddress` | yes | string max 128 | The email for the contact associated with the education organization. |
| `telephones` |  | array of edFi_staffEducationOrganizationContactAssociationTelephone | An unordered collection of staffEducationOrganizationContactAssociationTelephones. |

### Items in `telephones`

| Field | Required | Type | Description |
|---|---|---|---|
| `telephoneNumberTypeDescriptor` | yes | descriptor URI | The type of communication number listed for an individual or organization. |
| `telephoneNumber` | yes | string max 24 | The telephone number including the area code, and extension, if applicable. |
| `doNotPublishIndicator` |  | boolean | An indication that the telephone number should not be published. |
| `orderOfPriority` |  | integer (int32) | The order of priority assigned to telephone numbers to define which number to attempt first, second, etc. |
| `textMessageCapabilityIndicator` |  | boolean | An indication that the telephone number is technically capable of sending and receiving Short Message Service (SMS) text messages. |

## Endpoints

- `GET /ed-fi/staffEducationOrganizationContactAssociations`
- `POST /ed-fi/staffEducationOrganizationContactAssociations`
- `GET /ed-fi/staffEducationOrganizationContactAssociations/deletes`
- `GET /ed-fi/staffEducationOrganizationContactAssociations/keyChanges`
- `GET /ed-fi/staffEducationOrganizationContactAssociations/partitions`
- `GET /ed-fi/staffEducationOrganizationContactAssociations/{id}`
- `PUT /ed-fi/staffEducationOrganizationContactAssociations/{id}`
- `DELETE /ed-fi/staffEducationOrganizationContactAssociations/{id}`
