# certifications

`/ed-fi/certifications`

An offering by an official granting authority of a certification or license that qualifies persons to perform
specific job functions, such as fulfill a teaching assignment.

## Natural key

`certificationIdentifier`, `namespace`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `certificationIdentifier` | yes | string max 120 | Identifier or serial number assigned to the certification. |
| `namespace` | yes | string max 255 | The namespace for the certification, typically associated with the issuing authority. |
| `educationOrganizationReference` |  | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `certificationExams` |  | array of edFi_certificationCertificationExam | An unordered collection of certificationCertificationExams. |
| `certificationFieldDescriptor` |  | descriptor URI | The field of certification. |
| `certificationLevelDescriptor` |  | descriptor URI | The level or category of the certification. |
| `certificationStandardDescriptor` |  | descriptor URI | The standard, law, or policy defining the certification. |
| `certificationTitle` | yes | string max 64 | The title of the certification. |
| `educatorRoleDescriptor` |  | descriptor URI | The role authorized by the certification, typically associated with service and administrative certifications. |
| `effectiveDate` |  | string (date) | The month, day, and year on which the certification is offered. |
| `endDate` |  | string (date) | The month, day, and year on which the certification offering is expected to end. |
| `gradeLevels` |  | array of edFi_certificationGradeLevel | An unordered collection of certificationGradeLevels. |
| `instructionalSettingDescriptor` |  | descriptor URI | The setting authorized by the certification in which a person receives education and related services. |
| `minimumDegreeDescriptor` |  | descriptor URI | The minimum level of degree, if any, required for the certification. |
| `populationServedDescriptor` |  | descriptor URI | The type of students that the certification is offered and tailored to. |
| `routes` |  | array of edFi_certificationRoute | An unordered collection of certificationRoutes. |

### Items in `certificationExams`

| Field | Required | Type | Description |
|---|---|---|---|
| `certificationExamReference` | yes | reference; supply `certificationExamIdentifier`, `namespace` | An examination required by one or more certifications. |

### Items in `gradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade level(s) certified for teaching. |

### Items in `routes`

| Field | Required | Type | Description |
|---|---|---|---|
| `certificationRouteDescriptor` | yes | descriptor URI | The process, program, or pathway used to obtain the certification. |

## Endpoints

- `GET /ed-fi/certifications`
- `POST /ed-fi/certifications`
- `GET /ed-fi/certifications/deletes`
- `GET /ed-fi/certifications/keyChanges`
- `GET /ed-fi/certifications/partitions`
- `GET /ed-fi/certifications/{id}`
- `PUT /ed-fi/certifications/{id}`
- `DELETE /ed-fi/certifications/{id}`
