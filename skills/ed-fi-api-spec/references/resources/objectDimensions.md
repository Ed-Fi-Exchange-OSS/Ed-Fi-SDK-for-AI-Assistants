# objectDimensions

`/ed-fi/objectDimensions`

The NCES object accounting dimension representing an expenditure. Per the NCES definition, this classification
is used to describe the service or commodity obtained as the result of a specific expenditure, such as
salaries, benefits, tuition reimbursement, and so forth.

## Natural key

`code`, `fiscalYear`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | key | string max 16 | The code representation of the account object dimension. |
| `fiscalYear` | key | integer (int32) | The fiscal year for which the account object dimension is valid. |
| `codeName` |  | string max 100 | A description of the account object dimension. |
| `reportingTags` |  | array of edFi_objectDimensionReportingTag | An unordered collection of objectDimensionReportingTags. |

## Endpoints

- `DELETE /ed-fi/objectDimensions/{id}`
- `GET /ed-fi/objectDimensions/deletes`
- `GET /ed-fi/objectDimensions/keyChanges`
- `GET /ed-fi/objectDimensions/partitions`
- `GET /ed-fi/objectDimensions/{id}`
- `GET /ed-fi/objectDimensions`
- `POST /ed-fi/objectDimensions`
- `PUT /ed-fi/objectDimensions/{id}`
