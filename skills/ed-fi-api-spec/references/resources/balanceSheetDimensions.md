# balanceSheetDimensions

`/ed-fi/balanceSheetDimensions`

The NCES balance sheet accounting dimension, used to track financial transactions for each fund. These
financial statements only report assets, deferred outflows of resources, liabilities, deferred inflows of
resources, and equity accounts. The statements are considered snapshots of how these accounts stand as of a
certain point in time.

## Natural key

`code`, `fiscalYear`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | key | string max 16 | The code representation of the account balance sheet dimension. |
| `fiscalYear` | key | integer (int32) | The fiscal year for which the account balance sheet dimension is valid. |
| `codeName` |  | string max 100 | A description of the account balance sheet dimension. |
| `reportingTags` |  | array of edFi_balanceSheetDimensionReportingTag | An unordered collection of balanceSheetDimensionReportingTags. |

## Endpoints

- `DELETE /ed-fi/balanceSheetDimensions/{id}`
- `GET /ed-fi/balanceSheetDimensions/deletes`
- `GET /ed-fi/balanceSheetDimensions/keyChanges`
- `GET /ed-fi/balanceSheetDimensions/partitions`
- `GET /ed-fi/balanceSheetDimensions/{id}`
- `GET /ed-fi/balanceSheetDimensions`
- `POST /ed-fi/balanceSheetDimensions`
- `PUT /ed-fi/balanceSheetDimensions/{id}`
