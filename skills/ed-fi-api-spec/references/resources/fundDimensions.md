# fundDimensions

`/ed-fi/fundDimensions`

The NCES fund accounting dimension. A fund is a fiscal and accounting entity with a self-balancing set of
accounts recording cash and other financial resources, together with all related liabilities and residual
equities or balances, and changes therein, which are segregated for the purpose of carrying on specific
activities or attaining certain objectives in accordance with special regulations, restrictions, or
limitations.

## Natural key

`code`, `fiscalYear`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | key | string max 16 | The code representation of the account fund dimension. |
| `fiscalYear` | key | integer (int32) | The fiscal year for which the account fund dimension is valid. |
| `codeName` |  | string max 100 | A description of the account fund dimension. |
| `reportingTags` |  | array of edFi_fundDimensionReportingTag | An unordered collection of fundDimensionReportingTags. |

## Endpoints

- `DELETE /ed-fi/fundDimensions/{id}`
- `GET /ed-fi/fundDimensions/deletes`
- `GET /ed-fi/fundDimensions/keyChanges`
- `GET /ed-fi/fundDimensions/partitions`
- `GET /ed-fi/fundDimensions/{id}`
- `GET /ed-fi/fundDimensions`
- `POST /ed-fi/fundDimensions`
- `PUT /ed-fi/fundDimensions/{id}`
