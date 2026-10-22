# studentSection504ProgramAssociations

`/ed-fi/studentSection504ProgramAssociations`

This association identifies student that qualifies for the Section 504 of the Rehabilitation Act of 1973.

## Natural key

`beginDate`, `educationOrganizationReference`, `programReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | The earliest date the student is involved with the program. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `programReference` | key | reference: `educationOrganizationId`, `programName`, `programTypeDescriptor` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `accommodationPlan` |  | boolean | Indicates whether student has a Section 504 accommodation plan. |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `section504DisabilityDescriptor` |  | descriptor URI | Defines one or more disabilities student has that qualifies them for a Section 504 plan. |
| `section504Eligibility` | yes | boolean | Indicates whether student has a disability, either temporary or permenant, that qualifies student for Section 504 consideration. |
| `section504EligibilityDecisionDate` |  | string (date) | The month, day, and year on which the Section 504 eligibility decision is made. |
| `section504MeetingDate` |  | string (date) | The month, day, and year on which the meeting with student's parent/guardian held to discuss the 504 eligibility of the student. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |

## Endpoints

- `DELETE /ed-fi/studentSection504ProgramAssociations/{id}`
- `GET /ed-fi/studentSection504ProgramAssociations/deletes`
- `GET /ed-fi/studentSection504ProgramAssociations/keyChanges`
- `GET /ed-fi/studentSection504ProgramAssociations/partitions`
- `GET /ed-fi/studentSection504ProgramAssociations/{id}`
- `GET /ed-fi/studentSection504ProgramAssociations`
- `POST /ed-fi/studentSection504ProgramAssociations`
- `PUT /ed-fi/studentSection504ProgramAssociations/{id}`
