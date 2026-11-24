# operationalUnitDimensions

`/ed-fi/operationalUnitDimensions`

The NCES operational unit accounting dimension. This dimension is used to segregate costs by school and
operational unit such as physical location, department, or other method.

## Natural key

`code`, `fiscalYear`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | yes | string max 16 | The code representation of the account operational unit dimension. |
| `fiscalYear` | yes | integer (int32) | The fiscal year for which the account operational unit dimension is valid. |
| `codeName` |  | string max 100 | A description of the account operational unit dimension. |
| `reportingTags` |  | array of edFi_operationalUnitDimensionReportingTag | An unordered collection of operationalUnitDimensionReportingTags. |

### Items in `reportingTags`

| Field | Required | Type | Description |
|---|---|---|---|
| `reportingTagDescriptor` | yes | descriptor URI | Optional tag for accountability reporting. |

## Endpoints

- `GET /ed-fi/operationalUnitDimensions`
- `POST /ed-fi/operationalUnitDimensions`
- `GET /ed-fi/operationalUnitDimensions/deletes`
- `GET /ed-fi/operationalUnitDimensions/keyChanges`
- `GET /ed-fi/operationalUnitDimensions/partitions`
- `GET /ed-fi/operationalUnitDimensions/{id}`
- `PUT /ed-fi/operationalUnitDimensions/{id}`
- `DELETE /ed-fi/operationalUnitDimensions/{id}`
