# educationOrganizationInterventionPrescriptionAssociations

`/ed-fi/educationOrganizationInterventionPrescriptionAssociations`

This association indicates interventions made available by an education organization. Often, a district-level
education organization purchases a set of intervention prescriptions and makes them available to its schools
for use on demand.

## Natural key

`educationOrganizationId`, `interventionPrescriptionEducationOrganizationId`,
`interventionPrescriptionIdentificationCode`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `interventionPrescriptionReference` | yes | reference; supply `educationOrganizationId`, `interventionPrescriptionIdentificationCode` | This entity represents a formal prescription of an instructional approach focusing on the specific techniques and materials used to teach a given subject. |
| `beginDate` |  | string (date) | The begin date of the period during which the intervention prescription is available. |
| `endDate` |  | string (date) | The end date of the period during which the intervention prescription is available. |

## Endpoints

- `GET /ed-fi/educationOrganizationInterventionPrescriptionAssociations`
- `POST /ed-fi/educationOrganizationInterventionPrescriptionAssociations`
- `GET /ed-fi/educationOrganizationInterventionPrescriptionAssociations/deletes`
- `GET /ed-fi/educationOrganizationInterventionPrescriptionAssociations/keyChanges`
- `GET /ed-fi/educationOrganizationInterventionPrescriptionAssociations/partitions`
- `GET /ed-fi/educationOrganizationInterventionPrescriptionAssociations/{id}`
- `PUT /ed-fi/educationOrganizationInterventionPrescriptionAssociations/{id}`
- `DELETE /ed-fi/educationOrganizationInterventionPrescriptionAssociations/{id}`
