# studentSchoolFoodServiceProgramAssociations

`/ed-fi/studentSchoolFoodServiceProgramAssociations`

This association represents the school food services program(s), such as the Free or Reduced Lunch program,
that a student participates in or from which the student receives services. The association is a subclass of
the GeneralStudentProgramAssociation specifically designed for school food service programs.

## Natural key

`beginDate`, `educationOrganizationReference`, `programReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | The earliest date the student is involved with the program. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `programReference` | key | reference: `educationOrganizationId`, `programName`, `programTypeDescriptor` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `directCertification` |  | boolean | Indicates that the student's National School Lunch Program (NSLP) eligibility has been determined through direct certification. |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `schoolFoodServiceProgramServices` |  | array of edFi_studentSchoolFoodServiceProgramAssociationSchoolFoodServiceProgramService | An unordered collection of studentSchoolFoodServiceProgramAssociationSchoolFoodServiceProgramServices. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |

## Endpoints

- `DELETE /ed-fi/studentSchoolFoodServiceProgramAssociations/{id}`
- `GET /ed-fi/studentSchoolFoodServiceProgramAssociations/deletes`
- `GET /ed-fi/studentSchoolFoodServiceProgramAssociations/keyChanges`
- `GET /ed-fi/studentSchoolFoodServiceProgramAssociations/partitions`
- `GET /ed-fi/studentSchoolFoodServiceProgramAssociations/{id}`
- `GET /ed-fi/studentSchoolFoodServiceProgramAssociations`
- `POST /ed-fi/studentSchoolFoodServiceProgramAssociations`
- `PUT /ed-fi/studentSchoolFoodServiceProgramAssociations/{id}`
