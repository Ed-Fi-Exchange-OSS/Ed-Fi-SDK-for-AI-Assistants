# localAccounts

`/ed-fi/localAccounts`

The set of account codes defined by an education organization for a fiscal year. It provides a formal record of the debits and credits relating to the specific account.

## Natural key

`accountIdentifier`, `fiscalYear`, `chartOfAccountReference`, `educationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `accountIdentifier` | key | string max 50 | Code value for the valid combination of account dimensions by LEA under which financials are reported. |
| `fiscalYear` | key | integer (int32) | The fiscal year for the account. |
| `chartOfAccountReference` | key | reference: `accountIdentifier`, `educationOrganizationId`, `fiscalYear` |  |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `accountName` |  | string max 100 | A descriptive name for the account. |
| `reportingTags` |  | array of edFi_localAccountReportingTag | An unordered collection of localAccountReportingTags. |

## Endpoints

- `DELETE /ed-fi/localAccounts/{id}`
- `GET /ed-fi/localAccounts/deletes`
- `GET /ed-fi/localAccounts/keyChanges`
- `GET /ed-fi/localAccounts/partitions`
- `GET /ed-fi/localAccounts/{id}`
- `GET /ed-fi/localAccounts`
- `POST /ed-fi/localAccounts`
- `PUT /ed-fi/localAccounts/{id}`
