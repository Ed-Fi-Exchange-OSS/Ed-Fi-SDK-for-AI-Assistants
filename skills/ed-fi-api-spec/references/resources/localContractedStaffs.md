# localContractedStaffs

`/ed-fi/localContractedStaffs`

The set of local education agency or charter management organization contracted staff amounts.

## Natural key

`asOfDate`, `accountIdentifier`, `educationOrganizationId`, `fiscalYear`, `staffUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `asOfDate` | yes | string (date) | The date of the reported amount for the account. |
| `localAccountReference` | yes | reference; supply `accountIdentifier`, `educationOrganizationId`, `fiscalYear` | The set of account codes defined by an education organization for a fiscal year. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `amount` | yes | number (double) | Current balance for the account. |
| `financialCollectionDescriptor` |  | descriptor URI | The accounting period or grouping for which the amount is collected. |

## Endpoints

- `GET /ed-fi/localContractedStaffs`
- `POST /ed-fi/localContractedStaffs`
- `GET /ed-fi/localContractedStaffs/deletes`
- `GET /ed-fi/localContractedStaffs/keyChanges`
- `GET /ed-fi/localContractedStaffs/partitions`
- `GET /ed-fi/localContractedStaffs/{id}`
- `PUT /ed-fi/localContractedStaffs/{id}`
- `DELETE /ed-fi/localContractedStaffs/{id}`
