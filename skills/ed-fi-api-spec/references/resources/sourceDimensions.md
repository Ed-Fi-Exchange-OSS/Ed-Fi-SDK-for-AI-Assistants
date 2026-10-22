# sourceDimensions

`/ed-fi/sourceDimensions`

The NCES source dimension. This dimension is used to segregate costs by school and operational unit such as physical location, department, or other method.

## Natural key

`code`, `fiscalYear`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | key | string max 16 | The code representation of the account source dimension. |
| `fiscalYear` | key | integer (int32) | The fiscal year for which the account source dimension is valid. |
| `codeName` |  | string max 100 | A description of the account source dimension. |
| `reportingTags` |  | array of edFi_sourceDimensionReportingTag | An unordered collection of sourceDimensionReportingTags. |

## Endpoints

- `DELETE /ed-fi/sourceDimensions/{id}`
- `GET /ed-fi/sourceDimensions/deletes`
- `GET /ed-fi/sourceDimensions/keyChanges`
- `GET /ed-fi/sourceDimensions/partitions`
- `GET /ed-fi/sourceDimensions/{id}`
- `GET /ed-fi/sourceDimensions`
- `POST /ed-fi/sourceDimensions`
- `PUT /ed-fi/sourceDimensions/{id}`
