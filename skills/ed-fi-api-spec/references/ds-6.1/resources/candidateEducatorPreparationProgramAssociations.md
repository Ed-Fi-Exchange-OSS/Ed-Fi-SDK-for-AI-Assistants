# candidateEducatorPreparationProgramAssociations

`/ed-fi/candidateEducatorPreparationProgramAssociations`

Information about the association between the educator candidate and the educator preparation program.

## Natural key

`beginDate`, `candidateIdentifier`, `educationOrganizationId`, `programName`, `programTypeDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The begin date for the association. |
| `applicationReference` |  | reference; supply `applicantProfileIdentifier`, `applicationIdentifier`, `educationOrganizationId` | An application for employment or acceptance. |
| `candidateReference` | yes | reference; supply `candidateIdentifier` | A candidate is both a person enrolled in a educator preparation program and a candidate to become an educator. |
| `educatorPreparationProgramReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | The educator preparation program designed to prepare students to become licensed educators. |
| `candidateIndicators` |  | array of edFi_candidateEducatorPreparationProgramAssociationCandidateIndicator | An unordered collection of candidateEducatorPreparationProgramAssociationCandidateIndicators. |
| `cohortYears` |  | array of edFi_candidateEducatorPreparationProgramAssociationCohortYear | An unordered collection of candidateEducatorPreparationProgramAssociationCohortYears. |
| `degreeSpecializations` |  | array of edFi_candidateEducatorPreparationProgramAssociationDegreeSpecialization | An unordered collection of candidateEducatorPreparationProgramAssociationDegreeSpecializations. |
| `endDate` |  | string (date) | The end date for the association. |
| `eppProgramPathwayDescriptor` |  | descriptor URI | The program pathway the candidate is following. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason exited for the association. |

### Items in `candidateIndicators`

| Field | Required | Type | Description |
|---|---|---|---|
| `indicatorBeginDate` | yes | string (date) | The month, day, and year when the indicator value is valid. |
| `indicatorName` | yes | string max 200 | The name of the indicator or metric. |
| `designatedBy` |  | string max 60 | The person, organization, or department that designated the program association. |
| `endDate` |  | string (date) | The month, day, and year when the indicator value is no longer valid. |
| `indicator` | yes | string max 60 | The value of the indicator or metric. |
| `indicatorGroup` |  | string max 200 | The name for a group of indicators. |

### Items in `cohortYears`

| Field | Required | Type | Description |
|---|---|---|---|
| `cohortYearTypeDescriptor` | yes | descriptor URI | The type of cohort year (9th grade, graduation). |
| `termDescriptor` |  | descriptor URI | The term associated with the cohort year; for example, the intended term of graduation. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |

### Items in `degreeSpecializations`

| Field | Required | Type | Description |
|---|---|---|---|
| `majorSpecialization` | yes | string max 255 | The major area for a degree or area of specialization for a certificate. |
| `specializationBeginDate` | yes | string (date) | The month, day, and year on which the teacher candidate first declared specialization. |
| `endDate` |  | string (date) | The month, day, and year on which the teacher candidate exited the declared specialization. |
| `minorSpecialization` |  | string max 255 | The minor area for a degree or area of specialization for a certificate. |

## Endpoints

- `GET /ed-fi/candidateEducatorPreparationProgramAssociations`
- `POST /ed-fi/candidateEducatorPreparationProgramAssociations`
- `GET /ed-fi/candidateEducatorPreparationProgramAssociations/deletes`
- `GET /ed-fi/candidateEducatorPreparationProgramAssociations/keyChanges`
- `GET /ed-fi/candidateEducatorPreparationProgramAssociations/partitions`
- `GET /ed-fi/candidateEducatorPreparationProgramAssociations/{id}`
- `PUT /ed-fi/candidateEducatorPreparationProgramAssociations/{id}`
- `DELETE /ed-fi/candidateEducatorPreparationProgramAssociations/{id}`
