# studentEducationOrganizationResponsibilityAssociations

`/ed-fi/studentEducationOrganizationResponsibilityAssociations`

This association indicates a relationship between a student and an education organization other than an
enrollment relationship, and generally indicating some kind of responsibility of the education organization
for the student. Enrollment relationship semantics are covered by StudentSchoolAssociation.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | Month, day, and year of the start date of an education organization's responsibility for a student. |
| `responsibilityDescriptor` | yes | descriptor URI | Indications of an education organization's responsibility for a student, such as accountability, attendance, funding, etc. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `endDate` |  | string (date) | Month, day, and year of the end date of an education organization's responsibility for a student. |

## Endpoints

- `GET /ed-fi/studentEducationOrganizationResponsibilityAssociations`
- `POST /ed-fi/studentEducationOrganizationResponsibilityAssociations`
- `GET /ed-fi/studentEducationOrganizationResponsibilityAssociations/deletes`
- `GET /ed-fi/studentEducationOrganizationResponsibilityAssociations/keyChanges`
- `GET /ed-fi/studentEducationOrganizationResponsibilityAssociations/partitions`
- `GET /ed-fi/studentEducationOrganizationResponsibilityAssociations/{id}`
- `PUT /ed-fi/studentEducationOrganizationResponsibilityAssociations/{id}`
- `DELETE /ed-fi/studentEducationOrganizationResponsibilityAssociations/{id}`
