# studentLanguageInstructionProgramAssociations

`/ed-fi/studentLanguageInstructionProgramAssociations`

This association represents the Title III Language Instruction for Limited English Proficient and Immigrant
Students program(s) that a student participates in or from which the student receives services. The
association is a subclass of the GeneralStudentProgramAssociation specifically designed for language
instruction programs.

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
| `dosage` |  | integer (int32) | The duration of time in minutes for which the student was assigned to participate in the program. |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `englishLanguageProficiencyAssessments` |  | array of edFi_studentLanguageInstructionProgramAssociationEnglishLanguageProficiencyAssessment | An unordered collection of studentLanguageInstructionProgramAssociationEnglishLanguageProficiencyAssessments. |
| `englishLearnerParticipation` |  | boolean | An indication that an English learner student is served by an English language instruction educational program supported with Title III of ESEA funds. |
| `languageInstructionProgramServices` |  | array of edFi_studentLanguageInstructionProgramAssociationLanguageInstructionProgramService | An unordered collection of studentLanguageInstructionProgramAssociationLanguageInstructionProgramServices. |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |

### Items in `englishLanguageProficiencyAssessments`

| Field | Required | Type | Description |
|---|---|---|---|
| `monitoredDescriptor` |  | descriptor URI | Student is monitored on content achievement who are no longer receiving services. |
| `participationDescriptor` |  | descriptor URI | Field indicating the participation in the yearly English language assessment. |
| `proficiencyDescriptor` |  | descriptor URI | The proficiency level for the yearly English language assessment. |
| `progressDescriptor` |  | descriptor URI | The yearly progress or growth from last year's assessment. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |

### Items in `languageInstructionProgramServices`

| Field | Required | Type | Description |
|---|---|---|---|
| `languageInstructionProgramServiceDescriptor` | yes | descriptor URI | Indicates the service being provided to the student by the language instruction program. |
| `primaryIndicator` |  | boolean | True if service is a primary service. |
| `serviceBeginDate` |  | string (date) | First date the student was in this option for the current school year. |
| `serviceEndDate` |  | string (date) | Last date the student was in this option for the current school year. |

### Items in `programParticipationStatuses`

| Field | Required | Type | Description |
|---|---|---|---|
| `participationStatusDescriptor` | yes | descriptor URI | The student's program participation status. |
| `statusBeginDate` | yes | string (date) | The date the student's program participation status began. |
| `designatedBy` |  | string max 60 | The person, organization, or department that designated the participation status. |
| `statusEndDate` |  | string (date) | The date the student's program participation status ended. |

## Endpoints

- `GET /ed-fi/studentLanguageInstructionProgramAssociations`
- `POST /ed-fi/studentLanguageInstructionProgramAssociations`
- `GET /ed-fi/studentLanguageInstructionProgramAssociations/deletes`
- `GET /ed-fi/studentLanguageInstructionProgramAssociations/keyChanges`
- `GET /ed-fi/studentLanguageInstructionProgramAssociations/partitions`
- `GET /ed-fi/studentLanguageInstructionProgramAssociations/{id}`
- `PUT /ed-fi/studentLanguageInstructionProgramAssociations/{id}`
- `DELETE /ed-fi/studentLanguageInstructionProgramAssociations/{id}`
