# candidateRelationshipToStaffAssociations

`/ed-fi/candidateRelationshipToStaffAssociations`

Describes the relationship between a current candidate and a staff person, typically at a K12 partnering
district in the role of a mentor teacher, coordinating teacher, supervising principal, etc. It could also
describe the relationship between a current candidate and a university staff member. This is a relationship
between two different people

## Natural key

`candidateIdentifier`, `staffUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `candidateReference` | yes | reference; supply `candidateIdentifier` | A candidate is both a person enrolled in a educator preparation program and a candidate to become an educator. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `beginDate` | yes | string (date) | The month, day, and year on which the candidate is associated to the staff. |
| `endDate` |  | string (date) | The month, day, and year on which the candidate stops association with the staff. |
| `staffToCandidateRelationshipDescriptor` |  | descriptor URI | Defines the staff relationship to the candidate. |

## Endpoints

- `GET /ed-fi/candidateRelationshipToStaffAssociations`
- `POST /ed-fi/candidateRelationshipToStaffAssociations`
- `GET /ed-fi/candidateRelationshipToStaffAssociations/deletes`
- `GET /ed-fi/candidateRelationshipToStaffAssociations/keyChanges`
- `GET /ed-fi/candidateRelationshipToStaffAssociations/partitions`
- `GET /ed-fi/candidateRelationshipToStaffAssociations/{id}`
- `PUT /ed-fi/candidateRelationshipToStaffAssociations/{id}`
- `DELETE /ed-fi/candidateRelationshipToStaffAssociations/{id}`
