# studentHealths

`/ed-fi/studentHealths`

This entity stores the student health records.

## Natural key

`educationOrganizationId`, `studentUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `additionalImmunizations` |  | array of edFi_studentHealthAdditionalImmunization | An unordered collection of studentHealthAdditionalImmunizations. |
| `asOfDate` | yes | string (date) | Date of last update of the student's health record. |
| `nonMedicalImmunizationExemptionDate` |  | string (date) | The year, month and day of the nonmedical exemption from vaccination claimed by the student's parent or guardian. |
| `nonMedicalImmunizationExemptionDescriptor` |  | descriptor URI | The type of nonmedical exemption from vaccination claimed by the student's parent or guardian. |
| `requiredImmunizations` |  | array of edFi_studentHealthRequiredImmunization | An unordered collection of studentHealthRequiredImmunizations. |

### Items in `additionalImmunizations`

| Field | Required | Type | Description |
|---|---|---|---|
| `immunizationName` | yes | string max 100 | The name of the immunization that the student has received. |
| `dates` |  | array of edFi_studentHealthAdditionalImmunizationDate | An unordered collection of studentHealthAdditionalImmunizationDates. |

### Items in `requiredImmunizations`

| Field | Required | Type | Description |
|---|---|---|---|
| `immunizationTypeDescriptor` | yes | descriptor URI | An indication of the type of immunization that the student has received. |
| `medicalExemption` |  | string max 1024 | The medical condition identified by a physician that contraindicates the vaccine. |
| `medicalExemptionDate` |  | string (date) | The year, month, and day of the medical exemption by a physician. |
| `dates` |  | array of edFi_studentHealthRequiredImmunizationDate | An unordered collection of studentHealthRequiredImmunizationDates. |

## Endpoints

- `GET /ed-fi/studentHealths`
- `POST /ed-fi/studentHealths`
- `GET /ed-fi/studentHealths/deletes`
- `GET /ed-fi/studentHealths/keyChanges`
- `GET /ed-fi/studentHealths/partitions`
- `GET /ed-fi/studentHealths/{id}`
- `PUT /ed-fi/studentHealths/{id}`
- `DELETE /ed-fi/studentHealths/{id}`
