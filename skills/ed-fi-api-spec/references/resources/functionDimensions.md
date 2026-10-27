# functionDimensions

`/ed-fi/functionDimensions`

The NCES function accounting dimension representing an expenditure. The function describes the activity for
which a service or material object is acquired. The functions of a school district are generally classified
into five broad areas, including instruction, support services, operation of non-instructional services,
facilities acquisition and construction, and debt service.

## Natural key

`code`, `fiscalYear`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | yes | string max 16 | The code representation of the account function dimension. |
| `fiscalYear` | yes | integer (int32) | The fiscal year for which the account function dimension is valid. |
| `codeName` |  | string max 100 | A description of the account function dimension. |
| `reportingTags` |  | array of edFi_functionDimensionReportingTag | An unordered collection of functionDimensionReportingTags. |

### Items in `reportingTags`

| Field | Required | Type | Description |
|---|---|---|---|
| `reportingTagDescriptor` | yes | descriptor URI | Optional tag for accountability reporting. |

## Endpoints

- `GET /ed-fi/functionDimensions`
- `POST /ed-fi/functionDimensions`
- `GET /ed-fi/functionDimensions/deletes`
- `GET /ed-fi/functionDimensions/keyChanges`
- `GET /ed-fi/functionDimensions/partitions`
- `GET /ed-fi/functionDimensions/{id}`
- `PUT /ed-fi/functionDimensions/{id}`
- `DELETE /ed-fi/functionDimensions/{id}`
