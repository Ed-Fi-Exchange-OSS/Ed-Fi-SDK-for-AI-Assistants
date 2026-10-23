# localActuals

`/ed-fi/localActuals`

The set of local education agency or charter management organization expense or revenue amounts.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `asOfDate` | yes | string (date) | The date of the reported amount for the account. |
| `localAccountReference` | yes | reference; supply `accountIdentifier`, `educationOrganizationId`, `fiscalYear` | The set of account codes defined by an education organization for a fiscal year. |
| `amount` | yes | number (double) | Current balance for the account. |
| `financialCollectionDescriptor` |  | descriptor URI | The accounting period or grouping for which the amount is collected. |

## Endpoints

- `GET /ed-fi/localActuals`
- `POST /ed-fi/localActuals`
- `GET /ed-fi/localActuals/deletes`
- `GET /ed-fi/localActuals/keyChanges`
- `GET /ed-fi/localActuals/partitions`
- `GET /ed-fi/localActuals/{id}`
- `PUT /ed-fi/localActuals/{id}`
- `DELETE /ed-fi/localActuals/{id}`
