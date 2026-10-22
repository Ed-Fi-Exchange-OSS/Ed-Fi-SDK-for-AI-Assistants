# localEncumbrances

`/ed-fi/localEncumbrances`

The set of local education agency or charter management organization encumbrance amounts.

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

- `DELETE /ed-fi/localEncumbrances/{id}`
- `GET /ed-fi/localEncumbrances/deletes`
- `GET /ed-fi/localEncumbrances/keyChanges`
- `GET /ed-fi/localEncumbrances/partitions`
- `GET /ed-fi/localEncumbrances/{id}`
- `GET /ed-fi/localEncumbrances`
- `POST /ed-fi/localEncumbrances`
- `PUT /ed-fi/localEncumbrances/{id}`
