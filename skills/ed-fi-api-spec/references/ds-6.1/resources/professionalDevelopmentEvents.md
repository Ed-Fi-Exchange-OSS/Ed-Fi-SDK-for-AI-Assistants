# professionalDevelopmentEvents

`/ed-fi/professionalDevelopmentEvents`

Information about a professional development event.

## Natural key

`namespace`, `professionalDevelopmentTitle`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `namespace` | yes | string max 255 | Namespace for the event, typically associated with the issuing authority. |
| `professionalDevelopmentTitle` | yes | string max 60 | The title or name for a professional development. |
| `multipleSession` |  | boolean | An indication of whether a professional development event is comprised of multiple sessions. |
| `professionalDevelopmentOfferedByDescriptor` | yes | descriptor URI | A code describing an organization that is offering a specific professional development. |
| `professionalDevelopmentReason` |  | string max 60 | The reported reason for a teacher candidate's professional development. |
| `required` |  | boolean | An indication of whether a teacher candidate is active in a professional development. |
| `totalHours` |  | integer (int32) | The number of total hours the professional development contains. |

## Endpoints

- `GET /ed-fi/professionalDevelopmentEvents`
- `POST /ed-fi/professionalDevelopmentEvents`
- `GET /ed-fi/professionalDevelopmentEvents/deletes`
- `GET /ed-fi/professionalDevelopmentEvents/keyChanges`
- `GET /ed-fi/professionalDevelopmentEvents/partitions`
- `GET /ed-fi/professionalDevelopmentEvents/{id}`
- `PUT /ed-fi/professionalDevelopmentEvents/{id}`
- `DELETE /ed-fi/professionalDevelopmentEvents/{id}`
