# sourceDimensions

`/ed-fi/sourceDimensions`

The NCES source dimension. This dimension is used to segregate costs by school and operational unit such as
physical location, department, or other method.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | yes | string max 16 | The code representation of the account source dimension. |
| `fiscalYear` | yes | integer (int32) | The fiscal year for which the account source dimension is valid. |
| `codeName` |  | string max 100 | A description of the account source dimension. |
| `reportingTags` |  | array of edFi_sourceDimensionReportingTag | An unordered collection of sourceDimensionReportingTags. |

### Items in `reportingTags`

| Field | Required | Type | Description |
|---|---|---|---|
| `reportingTagDescriptor` | yes | descriptor URI | Optional tag for accountability reporting. |

## Endpoints

- `GET /ed-fi/sourceDimensions`
- `POST /ed-fi/sourceDimensions`
- `GET /ed-fi/sourceDimensions/deletes`
- `GET /ed-fi/sourceDimensions/keyChanges`
- `GET /ed-fi/sourceDimensions/partitions`
- `GET /ed-fi/sourceDimensions/{id}`
- `PUT /ed-fi/sourceDimensions/{id}`
- `DELETE /ed-fi/sourceDimensions/{id}`
