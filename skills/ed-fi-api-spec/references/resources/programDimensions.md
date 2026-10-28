# programDimensions

`/ed-fi/programDimensions`

The NCES program accounting dimension. A program is defined by the NCES as a plan of activities and procedures
designed to accomplish a predetermined objective or set of objectives. These are often categorized into broad
program areas such as regular education, special education, vocational education, other PK-12 instructional,
nonpublic school, adult and continuing education, community and junior college education, community services,
and co-curricular or extracurricular activities.

## Natural key

`code`, `fiscalYear`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | yes | string max 16 | The code representation of the account program dimension. |
| `fiscalYear` | yes | integer (int32) | The fiscal year for which the account program dimension is valid. |
| `codeName` |  | string max 100 | A description of the account program dimension. |
| `reportingTags` |  | array of edFi_programDimensionReportingTag | An unordered collection of programDimensionReportingTags. |

### Items in `reportingTags`

| Field | Required | Type | Description |
|---|---|---|---|
| `reportingTagDescriptor` | yes | descriptor URI | Optional tag for accountability reporting. |

## Endpoints

- `GET /ed-fi/programDimensions`
- `POST /ed-fi/programDimensions`
- `GET /ed-fi/programDimensions/deletes`
- `GET /ed-fi/programDimensions/keyChanges`
- `GET /ed-fi/programDimensions/partitions`
- `GET /ed-fi/programDimensions/{id}`
- `PUT /ed-fi/programDimensions/{id}`
- `DELETE /ed-fi/programDimensions/{id}`
