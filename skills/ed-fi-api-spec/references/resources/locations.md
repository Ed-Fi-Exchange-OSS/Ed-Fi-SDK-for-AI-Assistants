# locations

`/ed-fi/locations`

This entity represents the physical space where students gather for a particular class/section. The location
may be an indoor or outdoor area designated for the purpose of meeting the educational needs of students.

## Natural key

`classroomIdentificationCode`, `schoolReference`. The natural key can be changed with PUT (cascading key
updates).

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `classroomIdentificationCode` | key | string max 60 | A unique number or alphanumeric code assigned to a room by a school, school system, state, or other agency or entity. |
| `schoolReference` | key | reference: `schoolId` |  |
| `maximumNumberOfSeats` |  | integer (int32) | The most number of seats the class can maintain. |
| `optimalNumberOfSeats` |  | integer (int32) | The number of seats that is most favorable to the class. |

## Endpoints

- `DELETE /ed-fi/locations/{id}`
- `GET /ed-fi/locations/deletes`
- `GET /ed-fi/locations/keyChanges`
- `GET /ed-fi/locations/partitions`
- `GET /ed-fi/locations/{id}`
- `GET /ed-fi/locations`
- `POST /ed-fi/locations`
- `PUT /ed-fi/locations/{id}`
