# chartOfAccounts

`/ed-fi/chartOfAccounts`

A valid combination of account dimensions under which financials are reported. This financial entity
represents a funding source combined with its purpose and type of transaction. It provides a formal record of
the debits and credits relating to the specific account.

## Natural key

`accountIdentifier`, `fiscalYear`, `educationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `accountIdentifier` | key | string max 50 | SEA populated code value for the valid combination of account dimensions under which financials are reported. |
| `fiscalYear` | key | integer (int32) | The fiscal year for the account |
| `balanceSheetDimensionReference` |  | reference: `code`, `fiscalYear` |  |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `functionDimensionReference` |  | reference: `code`, `fiscalYear` |  |
| `fundDimensionReference` |  | reference: `code`, `fiscalYear` |  |
| `objectDimensionReference` |  | reference: `code`, `fiscalYear` |  |
| `operationalUnitDimensionReference` |  | reference: `code`, `fiscalYear` |  |
| `programDimensionReference` |  | reference: `code`, `fiscalYear` |  |
| `projectDimensionReference` |  | reference: `code`, `fiscalYear` |  |
| `sourceDimensionReference` |  | reference: `code`, `fiscalYear` |  |
| `accountName` |  | string max 100 | A descriptive name for the account. |
| `accountTypeDescriptor` | yes | descriptor URI | The type of account used in accounting such as revenue, expenditure, or balance sheet. |
| `reportingTags` |  | array of edFi_chartOfAccountReportingTag | An unordered collection of chartOfAccountReportingTags. |

## Endpoints

- `DELETE /ed-fi/chartOfAccounts/{id}`
- `GET /ed-fi/chartOfAccounts/deletes`
- `GET /ed-fi/chartOfAccounts/keyChanges`
- `GET /ed-fi/chartOfAccounts/partitions`
- `GET /ed-fi/chartOfAccounts/{id}`
- `GET /ed-fi/chartOfAccounts`
- `POST /ed-fi/chartOfAccounts`
- `PUT /ed-fi/chartOfAccounts/{id}`
