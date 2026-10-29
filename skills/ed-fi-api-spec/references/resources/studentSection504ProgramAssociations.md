# studentSection504ProgramAssociations

`/ed-fi/studentSection504ProgramAssociations`

This association identifies student that qualifies for the Section 504 of the Rehabilitation Act of 1973.

## Natural key

`beginDate`, `educationOrganizationId`, `programEducationOrganizationId`, `programName`,
`programTypeDescriptor`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The earliest date the student is involved with the program. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `accommodationPlan` |  | boolean | Indicates whether student has a Section 504 accommodation plan. |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `section504DisabilityDescriptor` |  | descriptor URI | Defines one or more disabilities student has that qualifies them for a Section 504 plan. |
| `section504Eligibility` | yes | boolean | Indicates whether student has a disability, either temporary or permenant, that qualifies student for Section 504 consideration. |
| `section504EligibilityDecisionDate` |  | string (date) | The month, day, and year on which the Section 504 eligibility decision is made. |
| `section504MeetingDate` |  | string (date) | The month, day, and year on which the meeting with student's parent/guardian held to discuss the 504 eligibility of the student. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |

### Items in `programParticipationStatuses`

| Field | Required | Type | Description |
|---|---|---|---|
| `participationStatusDescriptor` | yes | descriptor URI | The student's program participation status. |
| `statusBeginDate` | yes | string (date) | The date the student's program participation status began. |
| `designatedBy` |  | string max 60 | The person, organization, or department that designated the participation status. |
| `statusEndDate` |  | string (date) | The date the student's program participation status ended. |

## Endpoints

- `GET /ed-fi/studentSection504ProgramAssociations`
- `POST /ed-fi/studentSection504ProgramAssociations`
- `GET /ed-fi/studentSection504ProgramAssociations/deletes`
- `GET /ed-fi/studentSection504ProgramAssociations/keyChanges`
- `GET /ed-fi/studentSection504ProgramAssociations/partitions`
- `GET /ed-fi/studentSection504ProgramAssociations/{id}`
- `PUT /ed-fi/studentSection504ProgramAssociations/{id}`
- `DELETE /ed-fi/studentSection504ProgramAssociations/{id}`
