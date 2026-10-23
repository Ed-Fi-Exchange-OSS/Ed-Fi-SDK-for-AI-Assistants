# studentSchoolFoodServiceProgramAssociations

`/ed-fi/studentSchoolFoodServiceProgramAssociations`

This association represents the school food services program(s), such as the Free or Reduced Lunch program,
that a student participates in or from which the student receives services. The association is a subclass of
the GeneralStudentProgramAssociation specifically designed for school food service programs.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The earliest date the student is involved with the program. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `directCertification` |  | boolean | Indicates that the student's National School Lunch Program (NSLP) eligibility has been determined through direct certification. |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `schoolFoodServiceProgramServices` |  | array of edFi_studentSchoolFoodServiceProgramAssociationSchoolFoodServiceProgramService | An unordered collection of studentSchoolFoodServiceProgramAssociationSchoolFoodServiceProgramServices. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |

### Items in `programParticipationStatuses`

| Field | Required | Type | Description |
|---|---|---|---|
| `participationStatusDescriptor` | yes | descriptor URI | The student's program participation status. |
| `statusBeginDate` | yes | string (date) | The date the student's program participation status began. |
| `designatedBy` |  | string max 60 | The person, organization, or department that designated the participation status. |
| `statusEndDate` |  | string (date) | The date the student's program participation status ended. |

### Items in `schoolFoodServiceProgramServices`

| Field | Required | Type | Description |
|---|---|---|---|
| `schoolFoodServiceProgramServiceDescriptor` | yes | descriptor URI | Indicates the service being provided to the student by the school food service program. |
| `primaryIndicator` |  | boolean | True if service is a primary service. |
| `serviceBeginDate` |  | string (date) | First date the student was in this option for the current school year. |
| `serviceEndDate` |  | string (date) | Last date the student was in this option for the current school year. |

## Endpoints

- `GET /ed-fi/studentSchoolFoodServiceProgramAssociations`
- `POST /ed-fi/studentSchoolFoodServiceProgramAssociations`
- `GET /ed-fi/studentSchoolFoodServiceProgramAssociations/deletes`
- `GET /ed-fi/studentSchoolFoodServiceProgramAssociations/keyChanges`
- `GET /ed-fi/studentSchoolFoodServiceProgramAssociations/partitions`
- `GET /ed-fi/studentSchoolFoodServiceProgramAssociations/{id}`
- `PUT /ed-fi/studentSchoolFoodServiceProgramAssociations/{id}`
- `DELETE /ed-fi/studentSchoolFoodServiceProgramAssociations/{id}`
