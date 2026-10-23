# assessmentAdministrationParticipations

`/ed-fi/assessmentAdministrationParticipations`

Identifies the point of contact for the administration of an assessment under the purview of an education
organization.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentAdministrationReference` | yes | reference; supply `administrationIdentifier`, `assessmentIdentifier`, `assigningEducationOrganizationId`, `namespace` | The anticipated administration of an assessment under the purview of an education organization. |
| `participatingEducationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `administrationPointOfContacts` |  | array of edFi_assessmentAdministrationParticipationAdministrationPointOfContact | An unordered collection of assessmentAdministrationParticipationAdministrationPointOfContacts. |

### Items in `administrationPointOfContacts`

| Field | Required | Type | Description |
|---|---|---|---|
| `electronicMailAddress` | yes | string max 128 | The email address for the contact. |
| `firstName` | yes | string max 75 | The contact's first name. |
| `lastSurname` | yes | string max 75 | The contact's last name. |
| `loginId` |  | string max 60 | The login ID for the user; used for security access control interface. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |

## Endpoints

- `GET /ed-fi/assessmentAdministrationParticipations`
- `POST /ed-fi/assessmentAdministrationParticipations`
- `GET /ed-fi/assessmentAdministrationParticipations/deletes`
- `GET /ed-fi/assessmentAdministrationParticipations/keyChanges`
- `GET /ed-fi/assessmentAdministrationParticipations/partitions`
- `GET /ed-fi/assessmentAdministrationParticipations/{id}`
- `PUT /ed-fi/assessmentAdministrationParticipations/{id}`
- `DELETE /ed-fi/assessmentAdministrationParticipations/{id}`
