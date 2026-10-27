# localActuals

`/ed-fi/localActuals`

The set of local education agency or charter management organization expense or revenue amounts.

## Natural key

`asOfDate`, `accountIdentifier`, `educationOrganizationId`, `fiscalYear`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

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
