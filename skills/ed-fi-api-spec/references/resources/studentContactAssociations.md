# studentContactAssociations

`/ed-fi/studentContactAssociations`

This association relates students to their parents, guardians, or caretakers.

Also searched as: parent, guardian.

## Natural key

`contactReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `contactReference` | key | reference: `contactUniqueId` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `contactPriority` |  | integer (int32) | The numeric order of the preferred sequence or priority of contact. |
| `contactRestrictions` |  | string max 250 | Restrictions for student and/or teacher contact with the individual (e.g., the student may not be picked up by the individual). |
| `emergencyContactStatus` |  | boolean | Indicator of whether the person is a designated emergency contact for the student. |
| `legalGuardian` |  | boolean | Indicator of whether the person is a legal guardian for the student. |
| `livesWith` |  | boolean | Indicator of whether the student lives with the associated contact. |
| `primaryContactStatus` |  | boolean | Indicator of whether the person is a primary contact for the student. |
| `relationDescriptor` |  | descriptor URI | The nature of an individual's relationship to a student, primarily used to capture family relationships. |

## Endpoints

- `DELETE /ed-fi/studentContactAssociations/{id}`
- `GET /ed-fi/studentContactAssociations/deletes`
- `GET /ed-fi/studentContactAssociations/keyChanges`
- `GET /ed-fi/studentContactAssociations/partitions`
- `GET /ed-fi/studentContactAssociations/{id}`
- `GET /ed-fi/studentContactAssociations`
- `POST /ed-fi/studentContactAssociations`
- `PUT /ed-fi/studentContactAssociations/{id}`
