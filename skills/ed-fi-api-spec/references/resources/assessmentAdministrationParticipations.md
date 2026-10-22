# assessmentAdministrationParticipations

`/ed-fi/assessmentAdministrationParticipations`

Identifies the point of contact for the administration of an assessment under the purview of an education organization.

## Natural key

`assessmentAdministrationReference`, `participatingEducationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentAdministrationReference` | key | reference: `administrationIdentifier`, `assessmentIdentifier`, `assigningEducationOrganizationId`, `namespace` |  |
| `participatingEducationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `administrationPointOfContacts` |  | array of edFi_assessmentAdministrationParticipationAdministrationPointOfContact | An unordered collection of assessmentAdministrationParticipationAdministrationPointOfContacts. |

## Endpoints

- `DELETE /ed-fi/assessmentAdministrationParticipations/{id}`
- `GET /ed-fi/assessmentAdministrationParticipations/deletes`
- `GET /ed-fi/assessmentAdministrationParticipations/keyChanges`
- `GET /ed-fi/assessmentAdministrationParticipations/partitions`
- `GET /ed-fi/assessmentAdministrationParticipations/{id}`
- `GET /ed-fi/assessmentAdministrationParticipations`
- `POST /ed-fi/assessmentAdministrationParticipations`
- `PUT /ed-fi/assessmentAdministrationParticipations/{id}`
