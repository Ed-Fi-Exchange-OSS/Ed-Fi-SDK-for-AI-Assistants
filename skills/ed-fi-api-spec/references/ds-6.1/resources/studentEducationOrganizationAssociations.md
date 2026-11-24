# studentEducationOrganizationAssociations

`/ed-fi/studentEducationOrganizationAssociations`

This association represents student information as reported in the context of the student's relationship to
the education organization. Enrollment relationship semantics are covered by StudentSchoolAssociation.

## Natural key

`educationOrganizationId`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `barrierToInternetAccessInResidenceDescriptor` |  | descriptor URI | An indication of the barrier to having internet access in the student s primary place of residence. |
| `cohortYears` |  | array of edFi_studentEducationOrganizationAssociationCohortYear | An unordered collection of studentEducationOrganizationAssociationCohortYears. |
| `displacedStudents` |  | array of edFi_studentEducationOrganizationAssociationDisplacedStudent | An unordered collection of studentEducationOrganizationAssociationDisplacedStudents. |
| `internetAccessInResidence` |  | boolean | An indication of whether the student is able to access the internet in their primary place of residence. |
| `internetAccessTypeInResidenceDescriptor` |  | descriptor URI | The primary type of internet service used in the student s primary place of residence. |
| `internetPerformanceInResidenceDescriptor` |  | descriptor URI | An indication of whether the student can complete the full range of learning activities, including video streaming and assignment upload, without interruptions… |
| `loginId` |  | string max 120 | The login ID for the user; used for security access control interface. |
| `primaryLearningDeviceAccessDescriptor` |  | descriptor URI | An indication of whether the primary learning device is shared or not shared with another individual. |
| `primaryLearningDeviceAwayFromSchoolDescriptor` |  | descriptor URI | The type of device the student uses most often to complete learning activities away from school. |
| `primaryLearningDeviceProviderDescriptor` |  | descriptor URI | The provider of the primary learning device. |
| `profileThumbnail` |  | string max 255 | Locator reference for the student photo. |
| `studentIndicators` |  | array of edFi_studentEducationOrganizationAssociationStudentIndicator | An unordered collection of studentEducationOrganizationAssociationStudentIndicators. |

### Items in `cohortYears`

| Field | Required | Type | Description |
|---|---|---|---|
| `cohortYearTypeDescriptor` | yes | descriptor URI | The type of cohort year (9th grade, graduation). |
| `termDescriptor` |  | descriptor URI | The term associated with the cohort year; for example, the intended term of graduation. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |

### Items in `displacedStudents`

| Field | Required | Type | Description |
|---|---|---|---|
| `displacedStudentStatusDescriptor` | yes | descriptor URI | Indicates whether a student has been displaced as a result of a crisis event. |
| `crisisHomelessnessIndicator` |  | boolean | Any student considered homeless (defined by the McKinney-Vento Homeless Education Assistance Act as lacking a fixed, regular, and adequate nighttime residence)… |
| `displacedStudentEndDate` |  | string (date) | The date marking the end of the period during which a student is considered displaced due to a crisis event. |
| `displacedStudentStartDate` |  | string (date) | The date on which a student is officially identified as displaced due to a crisis event. |
| `crisisEventReference` | yes | reference; supply `crisisEventName` | A natural or man-made event that causes the disruption of school-level activities and the temporary or permanent displacement of students. |

### Items in `studentIndicators`

| Field | Required | Type | Description |
|---|---|---|---|
| `indicatorName` | yes | string max 200 | The name of the indicator or metric. |
| `designatedBy` |  | string max 60 | The person, organization, or department that designated the program association. |
| `indicator` | yes | string max 60 | The value of the indicator or metric. |
| `indicatorGroup` |  | string max 200 | The name for a group of indicators. |
| `periods` |  | array of edFi_studentEducationOrganizationAssociationStudentIndicatorPeriod | An unordered collection of studentEducationOrganizationAssociationStudentIndicatorPeriods. |

## Endpoints

- `GET /ed-fi/studentEducationOrganizationAssociations`
- `POST /ed-fi/studentEducationOrganizationAssociations`
- `GET /ed-fi/studentEducationOrganizationAssociations/deletes`
- `GET /ed-fi/studentEducationOrganizationAssociations/keyChanges`
- `GET /ed-fi/studentEducationOrganizationAssociations/partitions`
- `GET /ed-fi/studentEducationOrganizationAssociations/{id}`
- `PUT /ed-fi/studentEducationOrganizationAssociations/{id}`
- `DELETE /ed-fi/studentEducationOrganizationAssociations/{id}`
