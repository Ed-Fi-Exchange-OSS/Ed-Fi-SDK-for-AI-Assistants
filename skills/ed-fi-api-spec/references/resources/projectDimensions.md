# projectDimensions

`/ed-fi/projectDimensions`

The NCES project accounting dimension. The project dimension reporting code permits school districts to
accumulate expenditures to meet a variety of specialized reporting requirements at the local, state, and
federal levels.

## Natural key

`code`, `fiscalYear`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | yes | string max 16 | The code representation of the account project dimension. |
| `fiscalYear` | yes | integer (int32) | The fiscal year for which the account project dimension is valid. |
| `codeName` |  | string max 100 | A description of the account project dimension. |
| `reportingTags` |  | array of edFi_projectDimensionReportingTag | An unordered collection of projectDimensionReportingTags. |

### Items in `reportingTags`

| Field | Required | Type | Description |
|---|---|---|---|
| `reportingTagDescriptor` | yes | descriptor URI | Optional tag for accountability reporting. |

## Endpoints

- `GET /ed-fi/projectDimensions`
- `POST /ed-fi/projectDimensions`
- `GET /ed-fi/projectDimensions/deletes`
- `GET /ed-fi/projectDimensions/keyChanges`
- `GET /ed-fi/projectDimensions/partitions`
- `GET /ed-fi/projectDimensions/{id}`
- `PUT /ed-fi/projectDimensions/{id}`
- `DELETE /ed-fi/projectDimensions/{id}`
