# feederSchoolAssociations

`/ed-fi/feederSchoolAssociations`

The association from feeder school to the receiving school.

## Natural key

`beginDate`, `feederSchoolReference`, `schoolReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | The month, day, and year of the first day of the feeder school association. |
| `feederSchoolReference` | key | reference: `schoolId` |  |
| `schoolReference` | key | reference: `schoolId` |  |
| `endDate` |  | string (date) | The month, day, and year of the last day of the feeder school association. |
| `feederRelationshipDescription` |  | string max 1024 | Describes the relationship from the feeder school to the receiving school, for example by program emphasis, such as special education, language immersion, scie… |

## Endpoints

- `DELETE /ed-fi/feederSchoolAssociations/{id}`
- `GET /ed-fi/feederSchoolAssociations/deletes`
- `GET /ed-fi/feederSchoolAssociations/keyChanges`
- `GET /ed-fi/feederSchoolAssociations/partitions`
- `GET /ed-fi/feederSchoolAssociations/{id}`
- `GET /ed-fi/feederSchoolAssociations`
- `POST /ed-fi/feederSchoolAssociations`
- `PUT /ed-fi/feederSchoolAssociations/{id}`
