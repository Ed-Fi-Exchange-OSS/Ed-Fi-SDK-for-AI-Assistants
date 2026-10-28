# balanceSheetDimensions

`/ed-fi/balanceSheetDimensions`

The NCES balance sheet accounting dimension, used to track financial transactions for each fund. These
financial statements only report assets, deferred outflows of resources, liabilities, deferred inflows of
resources, and equity accounts. The statements are considered snapshots of how these accounts stand as of a
certain point in time.

## Natural key

`code`, `fiscalYear`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | yes | string max 16 | The code representation of the account balance sheet dimension. |
| `fiscalYear` | yes | integer (int32) | The fiscal year for which the account balance sheet dimension is valid. |
| `codeName` |  | string max 100 | A description of the account balance sheet dimension. |
| `reportingTags` |  | array of edFi_balanceSheetDimensionReportingTag | An unordered collection of balanceSheetDimensionReportingTags. |

### Items in `reportingTags`

| Field | Required | Type | Description |
|---|---|---|---|
| `reportingTagDescriptor` | yes | descriptor URI | Optional tag for accountability reporting. |

## Endpoints

- `GET /ed-fi/balanceSheetDimensions`
- `POST /ed-fi/balanceSheetDimensions`
- `GET /ed-fi/balanceSheetDimensions/deletes`
- `GET /ed-fi/balanceSheetDimensions/keyChanges`
- `GET /ed-fi/balanceSheetDimensions/partitions`
- `GET /ed-fi/balanceSheetDimensions/{id}`
- `PUT /ed-fi/balanceSheetDimensions/{id}`
- `DELETE /ed-fi/balanceSheetDimensions/{id}`
