# localAccounts

`/ed-fi/localAccounts`

The set of account codes defined by an education organization for a fiscal year. It provides a formal record
of the debits and credits relating to the specific account.

## Natural key

`accountIdentifier`, `fiscalYear`, `educationOrganizationId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `accountIdentifier` | yes | string max 50 | Code value for the valid combination of account dimensions by LEA under which financials are reported. |
| `fiscalYear` | yes | integer (int32) | The fiscal year for the account. |
| `chartOfAccountReference` | yes | reference; supply `accountIdentifier`, `educationOrganizationId`, `fiscalYear` | A valid combination of account dimensions under which financials are reported. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `accountName` |  | string max 100 | A descriptive name for the account. |
| `reportingTags` |  | array of edFi_localAccountReportingTag | An unordered collection of localAccountReportingTags. |

### Items in `reportingTags`

| Field | Required | Type | Description |
|---|---|---|---|
| `reportingTagDescriptor` | yes | descriptor URI | A descriptor used at the dimension and/or chart of account levels to demote specific state needs for reporting. |
| `tagValue` |  | string max 100 | The value associated with the reporting tag. |

## Endpoints

- `GET /ed-fi/localAccounts`
- `POST /ed-fi/localAccounts`
- `GET /ed-fi/localAccounts/deletes`
- `GET /ed-fi/localAccounts/keyChanges`
- `GET /ed-fi/localAccounts/partitions`
- `GET /ed-fi/localAccounts/{id}`
- `PUT /ed-fi/localAccounts/{id}`
- `DELETE /ed-fi/localAccounts/{id}`
