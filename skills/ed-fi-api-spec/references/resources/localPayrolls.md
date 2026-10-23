# localPayrolls

`/ed-fi/localPayrolls`

The set of local education agency or charter management organization payroll amounts.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `asOfDate` | yes | string (date) | The date of the reported amount for the account. |
| `localAccountReference` | yes | reference; supply `accountIdentifier`, `educationOrganizationId`, `fiscalYear` | The set of account codes defined by an education organization for a fiscal year. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `amount` | yes | number (double) | Current balance for the account. |
| `financialCollectionDescriptor` |  | descriptor URI | The accounting period or grouping for which the amount is collected. |

## Endpoints

- `GET /ed-fi/localPayrolls`
- `POST /ed-fi/localPayrolls`
- `GET /ed-fi/localPayrolls/deletes`
- `GET /ed-fi/localPayrolls/keyChanges`
- `GET /ed-fi/localPayrolls/partitions`
- `GET /ed-fi/localPayrolls/{id}`
- `PUT /ed-fi/localPayrolls/{id}`
- `DELETE /ed-fi/localPayrolls/{id}`
