# What's new: Data Standard 5.0 to 5.1

Scope: v5.0 to v5.1. No breaking changes; all additions are optional. Names are as in the API.

## New resources

- `crisisEvents` (Enrollment domain)
  - Key: `crisisEventName` (must be unique; Ed-Fi suggested convention: Location+CrisisType+Year).
  - Required: `crisisTypeDescriptor`.
  - Optional: `crisisDescription`, `crisisStartDate`, `crisisEndDate`.
- `studentHealths` (new Student Health domain; separate claimset access control intended)
  - Key: student reference (`studentUniqueId`), `educationOrganizationReference`.
  - The referenced education organization is the level (SEA, LEA, School) responsible for securing the data.
  - Required: `asOfDate` (not a key; date the record was last updated).
  - Optional: `nonMedicalImmunizationExemptionDescriptor`, `nonMedicalImmunizationExemptionDate`
    (blanket exemption for all immunizations).
  - Optional collection `requiredImmunizations`:
    - `immunizationTypeDescriptor`
    - `immunizationDates` (optional collection; one per dose)
    - `medicalExemption` (string, optional)
    - `medicalExemptionDate` (optional; date granted by doctor)
  - Optional collection `additionalImmunizations`:
    - `immunizationName` (string)
    - `immunizationDates` (optional collection; one per dose)
- `studentTransportations` (Enrollment domain; separate claimset access control intended)
  - Key: student reference, `transportationEducationOrganizationReference` (org managing the transportation).
    (The source misspells it `TransporationEducationOrganization`.)
  - Optional: `transportationPublicExpenseEligibilityTypeDescriptor`, `transportationTypeDescriptor`,
    `specialAccomodationRequirements` (string).
  - Optional collection `studentBusDetails`: `busNumber` (string), `busRouteDescriptor`,
    `travelDayofWeekDescriptor`, `travelDirectionDescriptor`, `mileage` (decimal).

## New descriptor types

- `crisisTypeDescriptors`
- `displacedStudentStatusDescriptors`
- `immunizationTypeDescriptors`
- `nonMedicalImmunizationExemptionDescriptors`
- `transportationPublicExpenseEligibilityTypeDescriptors`
- `transportationTypeDescriptors`
- `travelDayofWeekDescriptors`
- `travelDirectionDescriptors`
- `busRouteDescriptors` (values must be loaded)

## Changed resources

- `studentEducationOrganizationAssociations`: new optional collection `displacedStudents`:
  - `crisisEventReference` (required; supply `crisisEventName`).
  - `displacedStudentStatusDescriptor` (required).
  - `displacedStudentStartDate`, `displacedStudentEndDate`, `crisisHomelessnessIndicator` (optional).
  - Added when a displaced student is enrolled, typically when the association is written.
  - A student displaced from another state gets a new student ID; store the original state's ID in
    `studentIdentificationCodes`.
  - The source also calls the dates `DisplacedStudentBeginDate`/`DisplacedStudentEndDate`; the first form
    matches the API.
- `studentEducationOrganizationAssociations.hispanicLatinoEthnicity` (boolean): deprecated, to be removed in
  2029 (not yet removed). Not breaking in 5.1.
- `raceDescriptors`: recommended sample values now include "Hispanic or Latino" and
  "Middle Eastern or North African". Values are data, not part of the spec.

## Validation relaxed

- Unnecessary `minLength` = 1 removed from optional string properties, to avoid ODS/API 7+ validation
  failures. Not breaking.

## Other

- TPDM namespace changed from 5.0.0 to 5.1; XSD and sample data namespaces are now 5.1.0.
- No renamed or removed resources, properties or descriptors; no key (identity) changes.
