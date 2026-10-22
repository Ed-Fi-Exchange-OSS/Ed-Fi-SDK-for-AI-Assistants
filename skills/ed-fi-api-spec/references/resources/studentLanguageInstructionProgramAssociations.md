# studentLanguageInstructionProgramAssociations

`/ed-fi/studentLanguageInstructionProgramAssociations`

This association represents the Title III Language Instruction for Limited English Proficient and Immigrant
Students program(s) that a student participates in or from which the student receives services. The
association is a subclass of the GeneralStudentProgramAssociation specifically designed for language
instruction programs.

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
| `dosage` |  | integer (int32) | The duration of time in minutes for which the student was assigned to participate in the program. |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `englishLanguageProficiencyAssessments` |  | array of edFi_studentLanguageInstructionProgramAssociationEnglishLanguageProficiencyAssessment | An unordered collection of studentLanguageInstructionProgramAssociationEnglishLanguageProficiencyAssessments. |
| `englishLearnerParticipation` |  | boolean | An indication that an English learner student is served by an English language instruction educational program supported with Title III of ESEA funds. |
| `languageInstructionProgramServices` |  | array of edFi_studentLanguageInstructionProgramAssociationLanguageInstructionProgramService | An unordered collection of studentLanguageInstructionProgramAssociationLanguageInstructionProgramServices. |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |

## Endpoints

- `DELETE /ed-fi/studentLanguageInstructionProgramAssociations/{id}`
- `GET /ed-fi/studentLanguageInstructionProgramAssociations/deletes`
- `GET /ed-fi/studentLanguageInstructionProgramAssociations/keyChanges`
- `GET /ed-fi/studentLanguageInstructionProgramAssociations/partitions`
- `GET /ed-fi/studentLanguageInstructionProgramAssociations/{id}`
- `GET /ed-fi/studentLanguageInstructionProgramAssociations`
- `POST /ed-fi/studentLanguageInstructionProgramAssociations`
- `PUT /ed-fi/studentLanguageInstructionProgramAssociations/{id}`
