# openStaffPositions

`/ed-fi/openStaffPositions`

This entity represents an open staff position that the education organization is seeking to fill.

## Natural key

`requisitionNumber`, `educationOrganizationId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `requisitionNumber` | yes | string max 20 | The number or identifier assigned to an open staff position, typically a requisition number assigned by Human Resources. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `schoolYearTypeReference` |  | reference; supply `schoolYear` | Identifier for a school year. |
| `academicSubjects` |  | array of edFi_openStaffPositionAcademicSubject | An unordered collection of openStaffPositionAcademicSubjects. |
| `datePosted` | yes | string (date) | Date the open staff position was posted. |
| `datePostingRemoved` |  | string (date) | The date the posting was removed or filled. |
| `employmentStatusDescriptor` | yes | descriptor URI | Reflects the type of employment or contract desired for the position. |
| `fullTimeEquivalency` |  | number (double) | The ratio between the hours of work expected in a position and the hours of work normally expected in a full-time position in the same setting. |
| `fundingSourceDescriptor` |  | descriptor URI | The funding source for the open staff position. |
| `highNeedAcademicSubject` |  | boolean | Indicator as to whether the open staff position is filling a high-need subject area designated as a teacher shortage that may be eligible for special grants, a… |
| `instructionalGradeLevels` |  | array of edFi_openStaffPositionInstructionalGradeLevel | An unordered collection of openStaffPositionInstructionalGradeLevels. |
| `isActive` |  | boolean | Indicator of whether the open staff position is currently active. |
| `maxSalary` |  | number (double) | The maximum salary or wage a person is paid before deductions (excluding differentials) but including annuities. |
| `minSalary` |  | number (double) | The minimum salary or wage a person is paid before deductions (excluding differentials) but including annuities. |
| `openStaffPositionReasonDescriptor` |  | descriptor URI | The reason for the open staff position. |
| `positionControlNumber` |  | string max 20 | Identifier assigned to the position to be filled. |
| `positionTitle` |  | string max 100 | The descriptive name of an individual's position. |
| `postingResultDescriptor` |  | descriptor URI | Indication of whether the OpenStaffPosition was filled or retired without filling. |
| `programAssignmentDescriptor` |  | descriptor URI | The name of the program for which the open staff position will be assigned. |
| `staffClassificationDescriptor` | yes | descriptor URI | The titles of employment, official status, or rank of education staff. |
| `termDescriptor` |  | descriptor URI | The first term for the session during the school year for which the open staff position is seeking to fill. |
| `totalBudgeted` |  | number (double) | The fully loaded cost budgeted for this teacher, including salary. |

### Items in `academicSubjects`

| Field | Required | Type | Description |
|---|---|---|---|
| `academicSubjectDescriptor` | yes | descriptor URI | The teaching field required for the open staff position. |

### Items in `instructionalGradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The set of grade levels for which the position's assignment is responsible. |

## Endpoints

- `GET /ed-fi/openStaffPositions`
- `POST /ed-fi/openStaffPositions`
- `GET /ed-fi/openStaffPositions/deletes`
- `GET /ed-fi/openStaffPositions/keyChanges`
- `GET /ed-fi/openStaffPositions/partitions`
- `GET /ed-fi/openStaffPositions/{id}`
- `PUT /ed-fi/openStaffPositions/{id}`
- `DELETE /ed-fi/openStaffPositions/{id}`
