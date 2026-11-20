# Extension review: test with planted defects

Test of the review guidance in `ed-fi-extension-builder` ([review.md](../../skills/ed-fi-extension-builder/references/review.md)),
against an extension with 13 planted defects. Run on 2026-11-20 in Claude Code (headless, default model), one
run with the skill installed and one without, from the same prompt. GitHub Copilot runs are part of the full
test prompt set.

## The extension

`SampleBusRoutes` 1.0.0, a bus route extension for Data Standard 5.2. The MetaEd build tools (MetaEd 4.9.0)
were set up next to it.

`DomainEntity/BusRoutes.metaed`:

```metaed
Domain Entity BusRoutes
    documentation "BusRoutes"
    string RouteNumber
        documentation "Teh number of the route."
        is part of identity
        max length 20
    domain entity EdFi.School
        documentation "The school the route serves."
        is part of identity
    descriptor BusTypeDescriptor
        documentation "The type of bus."
        is required
    integer SeatCount
        documentation "The number of seats on the bus."
        is required
        is queryable field
```

`Association/StudentBusRouteAssociation.metaed`:

```metaed
Association StudentBusRouteAssociation
    documentation "This association links a student record to a bus route."
    domain entity BusRoutes
        documentation "The bus route."
    domain entity EdFi.Student
        documentation "The student who rides the route."
    descriptor GradeLevel
        documentation "The grade level of the student when assigned to the route."
        is required
```

`DomainEntity/Staff.metaed`:

```metaed
Domain Entity Staff
    documentation "A staff record for a bus driver."
    string StaffUniqueId
        documentation "The identifier of the staff member."
        is part of identity
        max length 32
    string DriverLicenseNumber
        documentation "The driver's license number."
        is required
        max length 20
```

`DomainEntity/StudentExtension.metaed`:

```metaed
Domain Entity EdFi.Student additions
    descriptor BusEligibility
        documentation "Whether the student is eligible for bus transportation."
        is required
    date LanguageBeginDate
        documentation "The date the student began speaking the home language."
        is optional
    date LanguageEndDate
        documentation "The date the student stopped speaking the home language."
        is optional
```

`Descriptor/BusTypeDescriptor.metaed` (`documentation "The type of bus. Examples include: Value1, Value2."`) and
`Descriptor/GradeLevel.metaed` (`documentation "The grade level."`).

The build fails with 3 errors (the `Descriptor` suffix, twice, and the undeclared `BusEligibility`). With those
fixed, it succeeds with two `already exists in project Ed-Fi` warnings, for `Staff` and `GradeLevel`.

## Prompt

> Please review the MetaEd extension in ./BusRoutes before we deploy it to our Ed-Fi API 8.1 host. The MetaEd
> build tools are already set up in ./metaed-build, and I accept the Ed-Fi license agreement. Don't change the
> files; just give me the review.

## Results

| # | Planted defect | Rule | With skill | Without skill |
|---|---|---|---|---|
| 1 | Descriptor named `BusTypeDescriptor` (build error) | BUILD-1, NAME-2 | ✅ | ✅ |
| 2 | Undeclared descriptor `BusEligibility` (build error) | BUILD-1 | ✅ | ✅ |
| 3 | Core `Staff` redeclared in the extension | CORE-1 | ✅ | ✅ |
| 4 | Core `GradeLevel` descriptor duplicated; the association binds to the copy | CORE-1 to CORE-3 | ✅ | ✅ |
| 5 | Required property added to core `Student` | CORE-5 | ✅ | ❌ |
| 6 | Begin and end dates on student language data | HYG-1 | ✅ | ⚠️ Questioned, not as a history problem |
| 7 | Typo "Teh" | DOC-1 | ✅ | ✅ |
| 8 | Documentation that repeats the name | DOC-2 | ✅ | ✅ |
| 9 | "student record", "staff record" | DOC-3 | ✅ | ❌ |
| 10 | Placeholder descriptor examples | DOC-4 | ✅ | ✅ |
| 11 | Plural entity name `BusRoutes` | NAME-1 | ✅ | ✅ |
| 12 | `Student` not first in the association | KEY-2 | ✅ | ❌ |
| 13 | Deprecated `is queryable field` | HYG-2 | ✅ | ❌ |
| | **Total** | | **13 / 13** | **8 / 13** (one partial) |

Other findings:

- **With the skill:** one false positive, fixed in the rules afterwards: it flagged `StudentExtension.metaed`
  for not being named after its entity, although the how-to guides name `additions` files this way (NAME-3
  now says so). It also reported the missing date note (DOC-5), which is valid. No files changed.
- **Without the skill:** two incorrect claims. It said `Domain Entity EdFi.Student additions` is not how to
  extend a core entity (it is the syntax of the how-to guides), and that building with tech version `7.3.0`
  would produce an extension that won't load on Ed-Fi API 8.1 (the generated `ApiSchema-EXTENSION.json` is the
  same with `7.3.0` and `8.1.0`). No files changed.

## Not tested yet

- GitHub Copilot.
- Repeated runs; each condition ran once.
- Extensions larger than this one, and review of a pull request diff.
