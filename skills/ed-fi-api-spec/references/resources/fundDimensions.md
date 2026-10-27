# fundDimensions

`/ed-fi/fundDimensions`

The NCES fund accounting dimension. A fund is a fiscal and accounting entity with a self-balancing set of
accounts recording cash and other financial resources, together with all related liabilities and residual
equities or balances, and changes therein, which are segregated for the purpose of carrying on specific
activities or attaining certain objectives in accordance with special regulations, restrictions, or
limitations.

## Natural key

`code`, `fiscalYear`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | yes | string max 16 | The code representation of the account fund dimension. |
| `fiscalYear` | yes | integer (int32) | The fiscal year for which the account fund dimension is valid. |
| `codeName` |  | string max 100 | A description of the account fund dimension. |
| `reportingTags` |  | array of edFi_fundDimensionReportingTag | An unordered collection of fundDimensionReportingTags. |

### Items in `reportingTags`

| Field | Required | Type | Description |
|---|---|---|---|
| `reportingTagDescriptor` | yes | descriptor URI | Optional tag for accountability reporting. |

## Endpoints

- `GET /ed-fi/fundDimensions`
- `POST /ed-fi/fundDimensions`
- `GET /ed-fi/fundDimensions/deletes`
- `GET /ed-fi/fundDimensions/keyChanges`
- `GET /ed-fi/fundDimensions/partitions`
- `GET /ed-fi/fundDimensions/{id}`
- `PUT /ed-fi/fundDimensions/{id}`
- `DELETE /ed-fi/fundDimensions/{id}`
