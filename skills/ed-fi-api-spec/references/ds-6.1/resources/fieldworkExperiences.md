# fieldworkExperiences

`/ed-fi/fieldworkExperiences`

The information regarding a post-secondary instructional course in a particular field of study that typically
involves a prescribed number, instruction periods, or meetings for enrolled students.

## Natural key

`beginDate`, `fieldworkIdentifier`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The month, day, and year on which the staff first starts fieldwork. |
| `fieldworkIdentifier` | yes | string max 64 | The unique identifier for the fieldwork experience. |
| `educatorPreparationProgramReference` |  | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | The educator preparation program designed to prepare students to become licensed educators. |
| `schoolReference` |  | reference; supply `schoolId` | This entity represents an educational organization that includes staff, students and candidates who participate in classes and educational activity groups, inc… |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `coteaching` |  | edFi_fieldworkExperienceCoteaching |  |
| `endDate` |  | string (date) | The month, day, and year on which the staff ends fieldwork. |
| `fieldworkTypeDescriptor` | yes | descriptor URI | The type of fieldwork being executed by a staff. |
| `hoursCompleted` |  | number (double) | The number of hours completed during the fieldwork experience. |

## Endpoints

- `GET /ed-fi/fieldworkExperiences`
- `POST /ed-fi/fieldworkExperiences`
- `GET /ed-fi/fieldworkExperiences/deletes`
- `GET /ed-fi/fieldworkExperiences/keyChanges`
- `GET /ed-fi/fieldworkExperiences/partitions`
- `GET /ed-fi/fieldworkExperiences/{id}`
- `PUT /ed-fi/fieldworkExperiences/{id}`
- `DELETE /ed-fi/fieldworkExperiences/{id}`
