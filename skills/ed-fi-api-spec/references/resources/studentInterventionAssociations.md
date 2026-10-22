# studentInterventionAssociations

`/ed-fi/studentInterventionAssociations`

This association indicates the students participating in an intervention.

## Natural key

`interventionReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `cohortReference` |  | reference: `cohortIdentifier`, `educationOrganizationId` |  |
| `interventionReference` | key | reference: `educationOrganizationId`, `interventionIdentificationCode` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `diagnosticStatement` |  | string max 1024 | A statement provided by the assigner that provides information regarding why the student was assigned to this intervention. |
| `dosage` |  | integer (int32) | The duration of time in minutes for which the student was assigned to participate in the intervention. |
| `interventionEffectivenesses` |  | array of edFi_studentInterventionAssociationInterventionEffectiveness | An unordered collection of studentInterventionAssociationInterventionEffectivenesses. |

## Endpoints

- `DELETE /ed-fi/studentInterventionAssociations/{id}`
- `GET /ed-fi/studentInterventionAssociations/deletes`
- `GET /ed-fi/studentInterventionAssociations/keyChanges`
- `GET /ed-fi/studentInterventionAssociations/partitions`
- `GET /ed-fi/studentInterventionAssociations/{id}`
- `GET /ed-fi/studentInterventionAssociations`
- `POST /ed-fi/studentInterventionAssociations`
- `PUT /ed-fi/studentInterventionAssociations/{id}`
