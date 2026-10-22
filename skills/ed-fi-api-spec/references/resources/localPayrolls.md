# localPayrolls

`/ed-fi/localPayrolls`

The set of local education agency or charter management organization payroll amounts.

## Natural key

`asOfDate`, `localAccountReference`, `staffReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

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

- `DELETE /ed-fi/localPayrolls/{id}`
- `GET /ed-fi/localPayrolls/deletes`
- `GET /ed-fi/localPayrolls/keyChanges`
- `GET /ed-fi/localPayrolls/partitions`
- `GET /ed-fi/localPayrolls/{id}`
- `GET /ed-fi/localPayrolls`
- `POST /ed-fi/localPayrolls`
- `PUT /ed-fi/localPayrolls/{id}`
