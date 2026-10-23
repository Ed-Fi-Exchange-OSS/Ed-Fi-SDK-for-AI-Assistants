# studentAcademicRecords

`/ed-fi/studentAcademicRecords`

This educational entity represents the cumulative record of academic achievement for a student.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `termDescriptor` | yes | descriptor URI | The term for the session during the school year. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `academicHonors` |  | array of edFi_studentAcademicRecordAcademicHonor | An unordered collection of studentAcademicRecordAcademicHonors. |
| `classRanking` |  | edFi_studentAcademicRecordClassRanking |  |
| `cumulativeAttemptedCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `cumulativeAttemptedCredits` |  | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `cumulativeAttemptedCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `cumulativeEarnedCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `cumulativeEarnedCredits` |  | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `cumulativeEarnedCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `diplomas` |  | array of edFi_studentAcademicRecordDiploma | An unordered collection of studentAcademicRecordDiplomas. |
| `gradePointAverages` |  | array of edFi_studentAcademicRecordGradePointAverage | An unordered collection of studentAcademicRecordGradePointAverages. |
| `projectedGraduationDate` |  | string (date) | The month and year the student is projected to graduate. |
| `recognitions` |  | array of edFi_studentAcademicRecordRecognition | An unordered collection of studentAcademicRecordRecognitions. |
| `reportCards` |  | array of edFi_studentAcademicRecordReportCard | An unordered collection of studentAcademicRecordReportCards. |
| `sessionAttemptedCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `sessionAttemptedCredits` |  | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `sessionAttemptedCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `sessionEarnedCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `sessionEarnedCredits` |  | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `sessionEarnedCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |

### Items in `academicHonors`

| Field | Required | Type | Description |
|---|---|---|---|
| `academicHonorCategoryDescriptor` | yes | descriptor URI | A designation of the type of academic distinctions earned by or awarded to the individual. |
| `honorDescription` | yes | string max 80 | A description of the type of academic distinctions earned by or awarded to the individual. |
| `achievementCategoryDescriptor` |  | descriptor URI | The category of achievement attributed to the individual. |
| `achievementCategorySystem` |  | string max 60 | The system that defines the categories by which an achievement is attributed to the individual. |
| `achievementTitle` |  | string max 60 | The title assigned to the achievement. |
| `criteria` |  | string max 150 | The criteria for competency-based completion of the achievement/award. |
| `criteriaURL` |  | string max 255 | The Uniform Resource Locator (URL) for the unique address of a web page describing the competency-based completion criteria for the achievement/award. |
| `evidenceStatement` |  | string max 150 | A statement or reference describing the evidence that the individual met the criteria for attainment of the achievement/award. |
| `honorAwardDate` |  | string (date) | The date the honor was awarded. |
| `honorAwardExpiresDate` |  | string (date) | Date on which the honor expires. |
| `imageURL` |  | string max 255 | The Uniform Resource Locator (URL) for the unique address of an image representing an award or badge associated with the achievement/award. |
| `issuerName` |  | string max 150 | The name of the agent, entity, or institution issuing the element. |
| `issuerOriginURL` |  | string max 255 | The Uniform Resource Locator (URL) from which the award was issued. |

### Items in `diplomas`

| Field | Required | Type | Description |
|---|---|---|---|
| `diplomaTypeDescriptor` | yes | descriptor URI | The type of diploma/credential that is awarded to a student in recognition of his/her completion of the curricular requirements. |
| `diplomaAwardDate` | yes | string (date) | The month, day, and year on which the student met graduation requirements and was awarded a diploma. |
| `achievementCategoryDescriptor` |  | descriptor URI | The category of achievement attributed to the individual. |
| `diplomaLevelDescriptor` |  | descriptor URI | The level of diploma/credential that is awarded to a student in recognition of completion of the curricular requirements. |
| `achievementCategorySystem` |  | string max 60 | The system that defines the categories by which an achievement is attributed to the individual. |
| `achievementTitle` |  | string max 60 | The title assigned to the achievement. |
| `criteria` |  | string max 150 | The criteria for competency-based completion of the achievement/award. |
| `criteriaURL` |  | string max 255 | The Uniform Resource Locator (URL) for the unique address of a web page describing the competency-based completion criteria for the achievement/award. |
| `cteCompleter` |  | boolean | Indicated a student who reached a state-defined threshold of vocational education and who attained a high school diploma or its recognized state equivalent or… |
| `diplomaAwardExpiresDate` |  | string (date) | Date on which the diploma expires. |
| `diplomaDescription` |  | string max 80 | The description of the diploma given to the student for accomplishments. |
| `evidenceStatement` |  | string max 150 | A statement or reference describing the evidence that the individual met the criteria for attainment of the achievement/award. |
| `imageURL` |  | string max 255 | The Uniform Resource Locator (URL) for the unique address of an image representing an award or badge associated with the achievement/award. |
| `issuerName` |  | string max 150 | The name of the agent, entity, or institution issuing the element. |
| `issuerOriginURL` |  | string max 255 | The Uniform Resource Locator (URL) from which the award was issued. |

### Items in `gradePointAverages`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradePointAverageTypeDescriptor` | yes | descriptor URI | The system used for calculating the grade point average for an individual. |
| `gradePointAverageValue` | yes | number (double) | The value of the grade points earned divided by the number of credits attempted. |
| `isCumulative` |  | boolean | Indicator of whether or not the Grade Point Average value is cumulative. |
| `maxGradePointAverageValue` |  | number (double) | The maximum value for the grade point average. |

### Items in `recognitions`

| Field | Required | Type | Description |
|---|---|---|---|
| `recognitionTypeDescriptor` | yes | descriptor URI | The nature of recognition given to the individual for accomplishments in a co-curricular, or extra-curricular activity. |
| `achievementCategoryDescriptor` |  | descriptor URI | The category of achievement attributed to the individual. |
| `achievementCategorySystem` |  | string max 60 | The system that defines the categories by which an achievement is attributed to the individual. |
| `achievementTitle` |  | string max 60 | The title assigned to the achievement. |
| `criteria` |  | string max 150 | The criteria for competency-based completion of the achievement/award. |
| `criteriaURL` |  | string max 255 | The Uniform Resource Locator (URL) for the unique address of a web page describing the competency-based completion criteria for the achievement/award. |
| `evidenceStatement` |  | string max 150 | A statement or reference describing the evidence that the individual met the criteria for attainment of the achievement/award. |
| `imageURL` |  | string max 255 | The Uniform Resource Locator (URL) for the unique address of an image representing an award or badge associated with the achievement/award. |
| `issuerName` |  | string max 150 | The name of the agent, entity, or institution issuing the element. |
| `issuerOriginURL` |  | string max 255 | The Uniform Resource Locator (URL) from which the award was issued. |
| `recognitionAwardDate` |  | string (date) | The date the recognition was awarded or earned. |
| `recognitionAwardExpiresDate` |  | string (date) | Date on which the recognition expires. |
| `recognitionDescription` |  | string max 80 | A description of the type of recognition earned by or awarded to the individual. |

### Items in `reportCards`

| Field | Required | Type | Description |
|---|---|---|---|
| `reportCardReference` | yes | reference; supply `educationOrganizationId`, `gradingPeriodDescriptor`, `gradingPeriodName`, `gradingPeriodSchoolId`, `gradingPeriodSchoolYear`, `studentUniqueId` | This educational entity represents the collection of student grades for courses taken during a grading period. |

## Endpoints

- `GET /ed-fi/studentAcademicRecords`
- `POST /ed-fi/studentAcademicRecords`
- `GET /ed-fi/studentAcademicRecords/deletes`
- `GET /ed-fi/studentAcademicRecords/keyChanges`
- `GET /ed-fi/studentAcademicRecords/partitions`
- `GET /ed-fi/studentAcademicRecords/{id}`
- `PUT /ed-fi/studentAcademicRecords/{id}`
- `DELETE /ed-fi/studentAcademicRecords/{id}`
