# localEncumbrances

`/ed-fi/localEncumbrances`

The set of local education agency or charter management organization encumbrance amounts.

## Natural key

`asOfDate`, `accountIdentifier`, `educationOrganizationId`, `fiscalYear`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `asOfDate` | yes | string (date) | The date of the reported amount for the account. |
| `localAccountReference` | yes | reference; supply `accountIdentifier`, `educationOrganizationId`, `fiscalYear` | The set of account codes defined by an education organization for a fiscal year. |
| `amount` | yes | number (double) | Current balance for the account. |
| `financialCollectionDescriptor` |  | descriptor URI | The accounting period or grouping for which the amount is collected. |

## Endpoints

- `GET /ed-fi/localEncumbrances`
- `POST /ed-fi/localEncumbrances`
- `GET /ed-fi/localEncumbrances/deletes`
- `GET /ed-fi/localEncumbrances/keyChanges`
- `GET /ed-fi/localEncumbrances/partitions`
- `GET /ed-fi/localEncumbrances/{id}`
- `PUT /ed-fi/localEncumbrances/{id}`
- `DELETE /ed-fi/localEncumbrances/{id}`
