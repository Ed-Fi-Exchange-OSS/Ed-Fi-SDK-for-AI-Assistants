# educationOrganizationInterventionPrescriptionAssociations

`/ed-fi/educationOrganizationInterventionPrescriptionAssociations`

This association indicates interventions made available by an education organization. Often, a district-level education organization purchases a set of intervention prescriptions and makes them available to its schools for use on demand.

## Natural key

`educationOrganizationReference`, `interventionPrescriptionReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `interventionPrescriptionReference` | key | reference: `educationOrganizationId`, `interventionPrescriptionIdentificationCode` |  |
| `beginDate` |  | string (date) | The begin date of the period during which the intervention prescription is available. |
| `endDate` |  | string (date) | The end date of the period during which the intervention prescription is available. |

## Endpoints

- `DELETE /ed-fi/educationOrganizationInterventionPrescriptionAssociations/{id}`
- `GET /ed-fi/educationOrganizationInterventionPrescriptionAssociations/deletes`
- `GET /ed-fi/educationOrganizationInterventionPrescriptionAssociations/keyChanges`
- `GET /ed-fi/educationOrganizationInterventionPrescriptionAssociations/partitions`
- `GET /ed-fi/educationOrganizationInterventionPrescriptionAssociations/{id}`
- `GET /ed-fi/educationOrganizationInterventionPrescriptionAssociations`
- `POST /ed-fi/educationOrganizationInterventionPrescriptionAssociations`
- `PUT /ed-fi/educationOrganizationInterventionPrescriptionAssociations/{id}`
