# localBudgets

`/ed-fi/localBudgets`

The set of local education agency or charter management organization budget amounts.

## Natural key

`asOfDate`, `localAccountReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `asOfDate` | key | string (date) | The date of the reported amount for the account. |
| `localAccountReference` | key | reference: `accountIdentifier`, `educationOrganizationId`, `fiscalYear` |  |
| `amount` | yes | number (double) | Current balance for the account. |
| `financialCollectionDescriptor` |  | descriptor URI | The accounting period or grouping for which the amount is collected. |

## Endpoints

- `DELETE /ed-fi/localBudgets/{id}`
- `GET /ed-fi/localBudgets/deletes`
- `GET /ed-fi/localBudgets/keyChanges`
- `GET /ed-fi/localBudgets/partitions`
- `GET /ed-fi/localBudgets/{id}`
- `GET /ed-fi/localBudgets`
- `POST /ed-fi/localBudgets`
- `PUT /ed-fi/localBudgets/{id}`
