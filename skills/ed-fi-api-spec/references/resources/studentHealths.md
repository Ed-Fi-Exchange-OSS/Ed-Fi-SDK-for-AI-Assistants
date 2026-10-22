# studentHealths

`/ed-fi/studentHealths`

This entity stores the student health records.

## Natural key

`educationOrganizationReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `additionalImmunizations` |  | array of edFi_studentHealthAdditionalImmunization | An unordered collection of studentHealthAdditionalImmunizations. |
| `asOfDate` | yes | string (date) | Date of last update of the student's health record. |
| `nonMedicalImmunizationExemptionDate` |  | string (date) | The year, month and day of the nonmedical exemption from vaccination claimed by the student's parent or guardian. |
| `nonMedicalImmunizationExemptionDescriptor` |  | descriptor URI | The type of nonmedical exemption from vaccination claimed by the student's parent or guardian. |
| `requiredImmunizations` |  | array of edFi_studentHealthRequiredImmunization | An unordered collection of studentHealthRequiredImmunizations. |

## Endpoints

- `DELETE /ed-fi/studentHealths/{id}`
- `GET /ed-fi/studentHealths/deletes`
- `GET /ed-fi/studentHealths/keyChanges`
- `GET /ed-fi/studentHealths/partitions`
- `GET /ed-fi/studentHealths/{id}`
- `GET /ed-fi/studentHealths`
- `POST /ed-fi/studentHealths`
- `PUT /ed-fi/studentHealths/{id}`
