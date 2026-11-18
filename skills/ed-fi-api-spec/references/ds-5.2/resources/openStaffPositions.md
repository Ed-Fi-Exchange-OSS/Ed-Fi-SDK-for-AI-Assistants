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
| `academicSubjects` |  | array of edFi_openStaffPositionAcademicSubject | An unordered collection of openStaffPositionAcademicSubjects. |
| `datePosted` | yes | string (date) | Date the open staff position was posted. |
| `datePostingRemoved` |  | string (date) | The date the posting was removed or filled. |
| `employmentStatusDescriptor` | yes | descriptor URI | Reflects the type of employment or contract desired for the position. |
| `instructionalGradeLevels` |  | array of edFi_openStaffPositionInstructionalGradeLevel | An unordered collection of openStaffPositionInstructionalGradeLevels. |
| `positionTitle` |  | string max 100 | The descriptive name of an individual's position. |
| `postingResultDescriptor` |  | descriptor URI | Indication of whether the OpenStaffPosition was filled or retired without filling. |
| `programAssignmentDescriptor` |  | descriptor URI | The name of the program for which the open staff position will be assigned. |
| `staffClassificationDescriptor` | yes | descriptor URI | The titles of employment, official status, or rank of education staff. |

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
