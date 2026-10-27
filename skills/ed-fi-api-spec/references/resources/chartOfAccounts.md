# chartOfAccounts

`/ed-fi/chartOfAccounts`

A valid combination of account dimensions under which financials are reported. This financial entity
represents a funding source combined with its purpose and type of transaction. It provides a formal record of
the debits and credits relating to the specific account.

## Natural key

`accountIdentifier`, `fiscalYear`, `educationOrganizationId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `accountIdentifier` | yes | string max 50 | SEA populated code value for the valid combination of account dimensions under which financials are reported. |
| `fiscalYear` | yes | integer (int32) | The fiscal year for the account |
| `balanceSheetDimensionReference` |  | reference; supply `code`, `fiscalYear` | The NCES balance sheet accounting dimension, used to track financial transactions for each fund. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `functionDimensionReference` |  | reference; supply `code`, `fiscalYear` | The NCES function accounting dimension representing an expenditure. |
| `fundDimensionReference` |  | reference; supply `code`, `fiscalYear` | The NCES fund accounting dimension. |
| `objectDimensionReference` |  | reference; supply `code`, `fiscalYear` | The NCES object accounting dimension representing an expenditure. |
| `operationalUnitDimensionReference` |  | reference; supply `code`, `fiscalYear` | The NCES operational unit accounting dimension. |
| `programDimensionReference` |  | reference; supply `code`, `fiscalYear` | The NCES program accounting dimension. |
| `projectDimensionReference` |  | reference; supply `code`, `fiscalYear` | The NCES project accounting dimension. |
| `sourceDimensionReference` |  | reference; supply `code`, `fiscalYear` | The NCES source dimension. |
| `accountName` |  | string max 100 | A descriptive name for the account. |
| `accountTypeDescriptor` | yes | descriptor URI | The type of account used in accounting such as revenue, expenditure, or balance sheet. |
| `reportingTags` |  | array of edFi_chartOfAccountReportingTag | An unordered collection of chartOfAccountReportingTags. |

### Items in `reportingTags`

| Field | Required | Type | Description |
|---|---|---|---|
| `reportingTagDescriptor` | yes | descriptor URI | A descriptor used at the dimension and/or chart of account levels to demote specific state needs for reporting. |
| `tagValue` |  | string max 100 | The value associated with the reporting tag. |

## Endpoints

- `GET /ed-fi/chartOfAccounts`
- `POST /ed-fi/chartOfAccounts`
- `GET /ed-fi/chartOfAccounts/deletes`
- `GET /ed-fi/chartOfAccounts/keyChanges`
- `GET /ed-fi/chartOfAccounts/partitions`
- `GET /ed-fi/chartOfAccounts/{id}`
- `PUT /ed-fi/chartOfAccounts/{id}`
- `DELETE /ed-fi/chartOfAccounts/{id}`
