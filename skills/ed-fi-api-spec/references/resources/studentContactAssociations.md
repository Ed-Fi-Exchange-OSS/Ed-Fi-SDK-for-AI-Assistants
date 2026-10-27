# studentContactAssociations

`/ed-fi/studentContactAssociations`

This association relates students to their parents, guardians, or caretakers.

Also searched as: parent, guardian.

## Natural key

`contactUniqueId`, `studentUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `contactReference` | yes | reference; supply `contactUniqueId` | This entity represents a contact of a student, such as a parent, guardian or caretaker. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `contactPriority` |  | integer (int32) | The numeric order of the preferred sequence or priority of contact. |
| `contactRestrictions` |  | string max 250 | Restrictions for student and/or teacher contact with the individual (e.g., the student may not be picked up by the individual). |
| `emergencyContactStatus` |  | boolean | Indicator of whether the person is a designated emergency contact for the student. |
| `legalGuardian` |  | boolean | Indicator of whether the person is a legal guardian for the student. |
| `livesWith` |  | boolean | Indicator of whether the student lives with the associated contact. |
| `primaryContactStatus` |  | boolean | Indicator of whether the person is a primary contact for the student. |
| `relationDescriptor` |  | descriptor URI | The nature of an individual's relationship to a student, primarily used to capture family relationships. |

## Endpoints

- `GET /ed-fi/studentContactAssociations`
- `POST /ed-fi/studentContactAssociations`
- `GET /ed-fi/studentContactAssociations/deletes`
- `GET /ed-fi/studentContactAssociations/keyChanges`
- `GET /ed-fi/studentContactAssociations/partitions`
- `GET /ed-fi/studentContactAssociations/{id}`
- `PUT /ed-fi/studentContactAssociations/{id}`
- `DELETE /ed-fi/studentContactAssociations/{id}`
