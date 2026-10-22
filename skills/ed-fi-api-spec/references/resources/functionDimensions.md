# functionDimensions

`/ed-fi/functionDimensions`

The NCES function accounting dimension representing an expenditure. The function describes the activity for
which a service or material object is acquired. The functions of a school district are generally classified
into five broad areas, including instruction, support services, operation of non-instructional services,
facilities acquisition and construction, and debt service.

## Natural key

`code`, `fiscalYear`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | key | string max 16 | The code representation of the account function dimension. |
| `fiscalYear` | key | integer (int32) | The fiscal year for which the account function dimension is valid. |
| `codeName` |  | string max 100 | A description of the account function dimension. |
| `reportingTags` |  | array of edFi_functionDimensionReportingTag | An unordered collection of functionDimensionReportingTags. |

## Endpoints

- `DELETE /ed-fi/functionDimensions/{id}`
- `GET /ed-fi/functionDimensions/deletes`
- `GET /ed-fi/functionDimensions/keyChanges`
- `GET /ed-fi/functionDimensions/partitions`
- `GET /ed-fi/functionDimensions/{id}`
- `GET /ed-fi/functionDimensions`
- `POST /ed-fi/functionDimensions`
- `PUT /ed-fi/functionDimensions/{id}`
