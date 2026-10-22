# localContractedStaffs

`/ed-fi/localContractedStaffs`

The set of local education agency or charter management organization contracted staff amounts.

## Natural key

`asOfDate`, `localAccountReference`, `staffReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `asOfDate` | key | string (date) | The date of the reported amount for the account. |
| `localAccountReference` | key | reference: `accountIdentifier`, `educationOrganizationId`, `fiscalYear` |  |
| `staffReference` | key | reference: `staffUniqueId` |  |
| `amount` | yes | number (double) | Current balance for the account. |
| `financialCollectionDescriptor` |  | descriptor URI | The accounting period or grouping for which the amount is collected. |

## Endpoints

- `DELETE /ed-fi/localContractedStaffs/{id}`
- `GET /ed-fi/localContractedStaffs/deletes`
- `GET /ed-fi/localContractedStaffs/keyChanges`
- `GET /ed-fi/localContractedStaffs/partitions`
- `GET /ed-fi/localContractedStaffs/{id}`
- `GET /ed-fi/localContractedStaffs`
- `POST /ed-fi/localContractedStaffs`
- `PUT /ed-fi/localContractedStaffs/{id}`
