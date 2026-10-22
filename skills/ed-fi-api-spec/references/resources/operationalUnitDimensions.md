# operationalUnitDimensions

`/ed-fi/operationalUnitDimensions`

The NCES operational unit accounting dimension. This dimension is used to segregate costs by school and operational unit such as physical location, department, or other method.

## Natural key

`code`, `fiscalYear`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | key | string max 16 | The code representation of the account operational unit dimension. |
| `fiscalYear` | key | integer (int32) | The fiscal year for which the account operational unit dimension is valid. |
| `codeName` |  | string max 100 | A description of the account operational unit dimension. |
| `reportingTags` |  | array of edFi_operationalUnitDimensionReportingTag | An unordered collection of operationalUnitDimensionReportingTags. |

## Endpoints

- `DELETE /ed-fi/operationalUnitDimensions/{id}`
- `GET /ed-fi/operationalUnitDimensions/deletes`
- `GET /ed-fi/operationalUnitDimensions/keyChanges`
- `GET /ed-fi/operationalUnitDimensions/partitions`
- `GET /ed-fi/operationalUnitDimensions/{id}`
- `GET /ed-fi/operationalUnitDimensions`
- `POST /ed-fi/operationalUnitDimensions`
- `PUT /ed-fi/operationalUnitDimensions/{id}`
