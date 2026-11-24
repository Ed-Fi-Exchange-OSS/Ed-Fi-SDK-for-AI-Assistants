# ideaEvents

`/ed-fi/ideaEvents`

EARLY ACCESS: An IDEA related student event describing status, dates and narrative.

## Natural key

`ideaEventTypeDescriptor`, `ideaEventIdentifier`, `educationOrganizationId`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `ideaEventIdentifier` | yes | string max 120 | A unique identifier for the event record as assigned by the provider of IEP services. |
| `ideaEventTypeDescriptor` | yes | descriptor URI | The specific legal step, procedure, or standard event milestone captured as part of IDEA compliance requirements. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `beginDate` | yes | string (date) | The date when the IDEA related event started. |
| `endDate` |  | string (date) | The date when the IDEA related event concluded. |
| `eventComplianceDescriptor` |  | descriptor URI | The type of compliance represented by this event. |
| `eventNarrative` |  | string max 2048 | Detailed and summary notes recorded during the event. |
| `eventReasonDescriptor` |  | descriptor URI | The reason why the IDEA event occurred. |

## Endpoints

- `GET /ed-fi/ideaEvents`
- `POST /ed-fi/ideaEvents`
- `GET /ed-fi/ideaEvents/deletes`
- `GET /ed-fi/ideaEvents/keyChanges`
- `GET /ed-fi/ideaEvents/partitions`
- `GET /ed-fi/ideaEvents/{id}`
- `PUT /ed-fi/ideaEvents/{id}`
- `DELETE /ed-fi/ideaEvents/{id}`
