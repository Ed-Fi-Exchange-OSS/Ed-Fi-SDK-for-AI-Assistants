# studentCTEProgramAssociations

`/ed-fi/studentCTEProgramAssociations`

This association represents the career and technical education (CTE) program that a student participates in.
The association is a subclass of the GeneralStudentProgramAssociation specifically designed for CTE programs.

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
| `cteProgramServices` |  | array of edFi_studentCTEProgramAssociationCTEProgramService | An unordered collection of studentCTEProgramAssociationCTEProgramServices. |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `nonTraditionalGenderStatus` |  | boolean | Indicator that student is from a gender group that comprises less than 25% of the individuals employed in an occupation or field of work. |
| `privateCTEProgram` |  | boolean | Indicator that student participated in career and technical education at private agencies or institutions that are reported by the state for purposes of the El… |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |
| `technicalSkillsAssessmentDescriptor` |  | descriptor URI | Results of technical skills assessment aligned with industry recognized standards. |

## Endpoints

- `DELETE /ed-fi/studentCTEProgramAssociations/{id}`
- `GET /ed-fi/studentCTEProgramAssociations/deletes`
- `GET /ed-fi/studentCTEProgramAssociations/keyChanges`
- `GET /ed-fi/studentCTEProgramAssociations/partitions`
- `GET /ed-fi/studentCTEProgramAssociations/{id}`
- `GET /ed-fi/studentCTEProgramAssociations`
- `POST /ed-fi/studentCTEProgramAssociations`
- `PUT /ed-fi/studentCTEProgramAssociations/{id}`
