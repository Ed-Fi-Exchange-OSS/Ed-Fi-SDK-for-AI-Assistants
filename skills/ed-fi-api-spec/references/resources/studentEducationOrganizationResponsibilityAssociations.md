# studentEducationOrganizationResponsibilityAssociations

`/ed-fi/studentEducationOrganizationResponsibilityAssociations`

This association indicates a relationship between a student and an education organization other than an enrollment relationship, and generally indicating some kind of responsibility of the education organization for the student. Enrollment relationship semantics are covered by StudentSchoolAssociation.

## Natural key

`beginDate`, `responsibilityDescriptor`, `educationOrganizationReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | Month, day, and year of the start date of an education organization's responsibility for a student. |
| `responsibilityDescriptor` | key | descriptor URI | Indications of an education organization's responsibility for a student, such as accountability, attendance, funding, etc. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `endDate` |  | string (date) | Month, day, and year of the end date of an education organization's responsibility for a student. |

## Endpoints

- `DELETE /ed-fi/studentEducationOrganizationResponsibilityAssociations/{id}`
- `GET /ed-fi/studentEducationOrganizationResponsibilityAssociations/deletes`
- `GET /ed-fi/studentEducationOrganizationResponsibilityAssociations/keyChanges`
- `GET /ed-fi/studentEducationOrganizationResponsibilityAssociations/partitions`
- `GET /ed-fi/studentEducationOrganizationResponsibilityAssociations/{id}`
- `GET /ed-fi/studentEducationOrganizationResponsibilityAssociations`
- `POST /ed-fi/studentEducationOrganizationResponsibilityAssociations`
- `PUT /ed-fi/studentEducationOrganizationResponsibilityAssociations/{id}`
