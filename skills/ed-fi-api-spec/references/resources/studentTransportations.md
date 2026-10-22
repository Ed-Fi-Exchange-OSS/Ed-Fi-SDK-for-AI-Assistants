# studentTransportations

`/ed-fi/studentTransportations`

This entity captures a student's specific transportation arrangement.

## Natural key

`studentReference`, `transportationEducationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `studentReference` | key | reference: `studentUniqueId` |  |
| `transportationEducationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `specialAccomodationRequirements` |  | string max 1024 | Specific requirements needed to accommodate a student's physical needs which may include special equipment installed in a vehicle or a special arrangement for… |
| `studentBusDetails` |  | edFi_studentTransportationStudentBusDetails |  |
| `transportationPublicExpenseEligibilityTypeDescriptor` |  | descriptor URI | The primary type of eligibility for transporting a student at public expense. |
| `transportationTypeDescriptor` |  | descriptor URI | The mode or type of transportation utilized by a student to commute to and from school |

## Endpoints

- `DELETE /ed-fi/studentTransportations/{id}`
- `GET /ed-fi/studentTransportations/deletes`
- `GET /ed-fi/studentTransportations/keyChanges`
- `GET /ed-fi/studentTransportations/partitions`
- `GET /ed-fi/studentTransportations/{id}`
- `GET /ed-fi/studentTransportations`
- `POST /ed-fi/studentTransportations`
- `PUT /ed-fi/studentTransportations/{id}`
