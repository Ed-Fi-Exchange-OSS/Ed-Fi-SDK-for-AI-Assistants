# openStaffPositions

`/ed-fi/openStaffPositions`

This entity represents an open staff position that the education organization is seeking to fill.

## Natural key

`requisitionNumber`, `educationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `requisitionNumber` | key | string max 20 | The number or identifier assigned to an open staff position, typically a requisition number assigned by Human Resources. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `academicSubjects` |  | array of edFi_openStaffPositionAcademicSubject | An unordered collection of openStaffPositionAcademicSubjects. |
| `datePosted` | yes | string (date) | Date the open staff position was posted. |
| `datePostingRemoved` |  | string (date) | The date the posting was removed or filled. |
| `employmentStatusDescriptor` | yes | descriptor URI | Reflects the type of employment or contract desired for the position. |
| `instructionalGradeLevels` |  | array of edFi_openStaffPositionInstructionalGradeLevel | An unordered collection of openStaffPositionInstructionalGradeLevels. |
| `positionTitle` |  | string max 100 | The descriptive name of an individual's position. |
| `postingResultDescriptor` |  | descriptor URI | Indication of whether the OpenStaffPosition was filled or retired without filling. |
| `programAssignmentDescriptor` |  | descriptor URI | The name of the program for which the open staff position will be assigned. |
| `staffClassificationDescriptor` | yes | descriptor URI | The titles of employment, official status, or rank of education staff. |

## Endpoints

- `DELETE /ed-fi/openStaffPositions/{id}`
- `GET /ed-fi/openStaffPositions/deletes`
- `GET /ed-fi/openStaffPositions/keyChanges`
- `GET /ed-fi/openStaffPositions/partitions`
- `GET /ed-fi/openStaffPositions/{id}`
- `GET /ed-fi/openStaffPositions`
- `POST /ed-fi/openStaffPositions`
- `PUT /ed-fi/openStaffPositions/{id}`
