# projectDimensions

`/ed-fi/projectDimensions`

The NCES project accounting dimension. The project dimension reporting code permits school districts to
accumulate expenditures to meet a variety of specialized reporting requirements at the local, state, and
federal levels.

## Natural key

`code`, `fiscalYear`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | key | string max 16 | The code representation of the account project dimension. |
| `fiscalYear` | key | integer (int32) | The fiscal year for which the account project dimension is valid. |
| `codeName` |  | string max 100 | A description of the account project dimension. |
| `reportingTags` |  | array of edFi_projectDimensionReportingTag | An unordered collection of projectDimensionReportingTags. |

## Endpoints

- `DELETE /ed-fi/projectDimensions/{id}`
- `GET /ed-fi/projectDimensions/deletes`
- `GET /ed-fi/projectDimensions/keyChanges`
- `GET /ed-fi/projectDimensions/partitions`
- `GET /ed-fi/projectDimensions/{id}`
- `GET /ed-fi/projectDimensions`
- `POST /ed-fi/projectDimensions`
- `PUT /ed-fi/projectDimensions/{id}`
