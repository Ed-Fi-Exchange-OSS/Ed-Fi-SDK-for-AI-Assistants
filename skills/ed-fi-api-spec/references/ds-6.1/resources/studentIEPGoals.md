# studentIEPGoals

`/ed-fi/studentIEPGoals`

EARLY ACCESS: A goal prescribed to a student as part of their Individual Education Program (IEP).

## Natural key

`iepGoalIdentifier`, `educationOrganizationId`, `iepFinalizedDate`, `studentIEPIdentifier`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `iepGoalIdentifier` | yes | string max 120 | A unique identifier assigned by the provider of IEP services. |
| `studentIEPReference` | yes | reference; supply `educationOrganizationId`, `iepFinalizedDate`, `studentIEPIdentifier`, `studentUniqueId` | EARLY ACCESS: This entity represents an Individualized Education Program (IEP) for a student receiving special education services. |
| `achievementPeriod` |  | edFi_studentIEPGoalAchievementPeriod |  |
| `ideaEvents` |  | array of edFi_studentIEPGoalIDEAEvent | An unordered collection of studentIEPGoalIDEAEvents. |
| `iepGoalDetails` | yes | string max 2048 | Instructions or other details specific to the student and/or provider for achieving the stated goal. |
| `iepGoalTypeDescriptor` | yes | descriptor URI | A focused goal prescribed as part of the IEP. |

### Items in `ideaEvents`

| Field | Required | Type | Description |
|---|---|---|---|
| `ideaEventReference` | yes | reference; supply `educationOrganizationId`, `ideaEventIdentifier`, `ideaEventTypeDescriptor`, `studentUniqueId` | EARLY ACCESS: An IDEA related student event describing status, dates and narrative. |

## Endpoints

- `GET /ed-fi/studentIEPGoals`
- `POST /ed-fi/studentIEPGoals`
- `GET /ed-fi/studentIEPGoals/deletes`
- `GET /ed-fi/studentIEPGoals/keyChanges`
- `GET /ed-fi/studentIEPGoals/partitions`
- `GET /ed-fi/studentIEPGoals/{id}`
- `PUT /ed-fi/studentIEPGoals/{id}`
- `DELETE /ed-fi/studentIEPGoals/{id}`
