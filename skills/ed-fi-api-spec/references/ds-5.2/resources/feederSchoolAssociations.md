# feederSchoolAssociations

`/ed-fi/feederSchoolAssociations`

The association from feeder school to the receiving school.

## Natural key

`beginDate`, `feederSchoolId`, `schoolId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The month, day, and year of the first day of the feeder school association. |
| `feederSchoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `endDate` |  | string (date) | The month, day, and year of the last day of the feeder school association. |
| `feederRelationshipDescription` |  | string max 1024 | Describes the relationship from the feeder school to the receiving school, for example by program emphasis, such as special education, language immersion, scie… |

## Endpoints

- `GET /ed-fi/feederSchoolAssociations`
- `POST /ed-fi/feederSchoolAssociations`
- `GET /ed-fi/feederSchoolAssociations/deletes`
- `GET /ed-fi/feederSchoolAssociations/keyChanges`
- `GET /ed-fi/feederSchoolAssociations/partitions`
- `GET /ed-fi/feederSchoolAssociations/{id}`
- `PUT /ed-fi/feederSchoolAssociations/{id}`
- `DELETE /ed-fi/feederSchoolAssociations/{id}`
