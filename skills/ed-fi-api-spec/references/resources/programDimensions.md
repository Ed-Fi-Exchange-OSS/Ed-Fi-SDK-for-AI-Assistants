# programDimensions

`/ed-fi/programDimensions`

The NCES program accounting dimension. A program is defined by the NCES as a plan of activities and procedures designed to accomplish a predetermined objective or set of objectives. These are often categorized into broad program areas such as regular education, special education, vocational education, other PK-12 instructional, nonpublic school, adult and continuing education, community and junior college education, community services, and co-curricular or extracurricular activities.

## Natural key

`code`, `fiscalYear`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `code` | key | string max 16 | The code representation of the account program dimension. |
| `fiscalYear` | key | integer (int32) | The fiscal year for which the account program dimension is valid. |
| `codeName` |  | string max 100 | A description of the account program dimension. |
| `reportingTags` |  | array of edFi_programDimensionReportingTag | An unordered collection of programDimensionReportingTags. |

## Endpoints

- `DELETE /ed-fi/programDimensions/{id}`
- `GET /ed-fi/programDimensions/deletes`
- `GET /ed-fi/programDimensions/keyChanges`
- `GET /ed-fi/programDimensions/partitions`
- `GET /ed-fi/programDimensions/{id}`
- `GET /ed-fi/programDimensions`
- `POST /ed-fi/programDimensions`
- `PUT /ed-fi/programDimensions/{id}`
