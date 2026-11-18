# applicationEvents

`/ed-fi/applicationEvents`

The life cycle event associated with an application.

## Natural key

`applicationEventTypeDescriptor`, `eventDate`, `sequenceNumber`, `applicantProfileIdentifier`,
`applicationIdentifier`, `educationOrganizationId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `applicationEventTypeDescriptor` | yes | descriptor URI | Description of the application event. |
| `eventDate` | yes | string (date) | The date of the application event, or begin date if an interval. |
| `sequenceNumber` | yes | integer (int32) | The sequence number of the application events. |
| `applicationReference` | yes | reference; supply `applicantProfileIdentifier`, `applicationIdentifier`, `educationOrganizationId` | An application for employment or acceptance. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |
| `applicationEvaluationScore` |  | number (double) | The evaluation score for the application, if applicable. |
| `applicationEventResultDescriptor` |  | descriptor URI | The recommendation, result or conclusion of the application event. |
| `eventEndDate` |  | string (date) | The end date of the event, if an interval. |
| `termDescriptor` |  | descriptor URI | Defines the term of a session during the school year. |

## Endpoints

- `GET /ed-fi/applicationEvents`
- `POST /ed-fi/applicationEvents`
- `GET /ed-fi/applicationEvents/deletes`
- `GET /ed-fi/applicationEvents/keyChanges`
- `GET /ed-fi/applicationEvents/partitions`
- `GET /ed-fi/applicationEvents/{id}`
- `PUT /ed-fi/applicationEvents/{id}`
- `DELETE /ed-fi/applicationEvents/{id}`
