# certificationExams

`/ed-fi/certificationExams`

An examination required by one or more certifications.

## Natural key

`certificationExamIdentifier`, `namespace`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `certificationExamIdentifier` | yes | string max 120 | Identifier or serial number assigned to the certification exam. |
| `namespace` | yes | string max 255 | The namespace for the certification exam. |
| `educationOrganizationReference` |  | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `certificationExamTitle` | yes | string max 60 | The title of the certification exam. |
| `certificationExamTypeDescriptor` |  | descriptor URI | The type or category of the certification exam. |
| `effectiveDate` |  | string (date) | The month, day, and year on which the certification exam is offered. |
| `endDate` |  | string (date) | The month, day, and year on which the certification exam offering is expected to end. |

## Endpoints

- `GET /ed-fi/certificationExams`
- `POST /ed-fi/certificationExams`
- `GET /ed-fi/certificationExams/deletes`
- `GET /ed-fi/certificationExams/keyChanges`
- `GET /ed-fi/certificationExams/partitions`
- `GET /ed-fi/certificationExams/{id}`
- `PUT /ed-fi/certificationExams/{id}`
- `DELETE /ed-fi/certificationExams/{id}`
