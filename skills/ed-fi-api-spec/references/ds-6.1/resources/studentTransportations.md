# studentTransportations

`/ed-fi/studentTransportations`

This entity captures a student's specific transportation arrangement.

## Natural key

`transportationEducationOrganizationId`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `transportationEducationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `specialAccomodationRequirements` |  | string max 1024 | Specific requirements needed to accommodate a student's physical needs which may include special equipment installed in a vehicle or a special arrangement for… |
| `studentBusDetails` |  | edFi_studentTransportationStudentBusDetails |  |
| `transportationPublicExpenseEligibilityTypeDescriptor` |  | descriptor URI | The primary type of eligibility for transporting a student at public expense. |
| `transportationTypeDescriptor` |  | descriptor URI | The mode or type of transportation utilized by a student to commute to and from school |

## Endpoints

- `GET /ed-fi/studentTransportations`
- `POST /ed-fi/studentTransportations`
- `GET /ed-fi/studentTransportations/deletes`
- `GET /ed-fi/studentTransportations/keyChanges`
- `GET /ed-fi/studentTransportations/partitions`
- `GET /ed-fi/studentTransportations/{id}`
- `PUT /ed-fi/studentTransportations/{id}`
- `DELETE /ed-fi/studentTransportations/{id}`
