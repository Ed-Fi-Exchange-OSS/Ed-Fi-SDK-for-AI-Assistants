# locations

`/ed-fi/locations`

This entity represents the physical space where students gather for a particular class/section. The location
may be an indoor or outdoor area designated for the purpose of meeting the educational needs of students.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `classroomIdentificationCode` | yes | string max 60 | A unique number or alphanumeric code assigned to a room by a school, school system, state, or other agency or entity. |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `maximumNumberOfSeats` |  | integer (int32) | The most number of seats the class can maintain. |
| `optimalNumberOfSeats` |  | integer (int32) | The number of seats that is most favorable to the class. |

## Endpoints

- `GET /ed-fi/locations`
- `POST /ed-fi/locations`
- `GET /ed-fi/locations/deletes`
- `GET /ed-fi/locations/keyChanges`
- `GET /ed-fi/locations/partitions`
- `GET /ed-fi/locations/{id}`
- `PUT /ed-fi/locations/{id}`
- `DELETE /ed-fi/locations/{id}`
