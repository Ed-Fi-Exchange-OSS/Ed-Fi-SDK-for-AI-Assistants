# objectDimensions

`/ed-fi/objectDimensions`

The NCES object accounting dimension representing an expenditure. Per the NCES definition, this classification
is used to describe the service or commodity obtained as the result of a specific expenditure, such as
salaries, benefits, tuition reimbursement, and so forth.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | yes | string max 16 | The code representation of the account object dimension. |
| `fiscalYear` | yes | integer (int32) | The fiscal year for which the account object dimension is valid. |
| `codeName` |  | string max 100 | A description of the account object dimension. |
| `reportingTags` |  | array of edFi_objectDimensionReportingTag | An unordered collection of objectDimensionReportingTags. |

### Items in `reportingTags`

| Field | Required | Type | Description |
|---|---|---|---|
| `reportingTagDescriptor` | yes | descriptor URI | Optional tag for accountability reporting. |

## Endpoints

- `GET /ed-fi/objectDimensions`
- `POST /ed-fi/objectDimensions`
- `GET /ed-fi/objectDimensions/deletes`
- `GET /ed-fi/objectDimensions/keyChanges`
- `GET /ed-fi/objectDimensions/partitions`
- `GET /ed-fi/objectDimensions/{id}`
- `PUT /ed-fi/objectDimensions/{id}`
- `DELETE /ed-fi/objectDimensions/{id}`
