# Mapping to the Ed-Fi ODS/API

Where each OneRoster record comes from in the Ed-Fi ODS/API, to explain records that are duplicated, missing
or have empty fields. Part of the [ed-fi-oneroster-client](../SKILL.md) skill. The full mapping is in the
[OneRoster data model](https://docs.ed-fi.org/reference/oneroster/data-model/) pages.

## `sourcedId`

Every `sourcedId` is an **MD5 hash of a string built from Ed-Fi Data Standard's natural key (identity)
fields**. For most records that is the Ed-Fi natural key; for users it is a role prefix, the unique ID and the
school ID.

- It is deterministic and stable across refreshes, so it is safe to store as the external ID.
- It **changes when any of those fields changes** in the Ed-Fi ODS/API database. The old record disappears and
  a new one appears; there is no link between them in OneRoster.
- It can't be reversed. To find the ODS/API record, use `metadata.edfi` or `identifier` (below), not the hash.

## Finding the ODS/API record

Every record carries the ODS/API resource and natural key it comes from in `metadata.edfi`:

```json
"metadata": {
  "edfi": {
    "resource": "sections",
    "naturalKey": { "localCourseCode": "ALG-1", "schoolid": 255901001, "sectionIdentifier": "ALG-1-01",
                    "sessionName": "2025-2026 Fall Semester" }
  }
}
```

- Use it to join OneRoster records to ODS/API data, for example a class to its ODS/API section, or to write
  back to the ODS/API.
- Read the key names as they come; their casing doesn't always match the ODS/API (`schoolid`), and some keys
  leave out parts of the Data Standard natural key (the section key has no `schoolYear`). Match
  case-insensitively and add the missing parts from the related records (such as the class's term).
- `identifier` also holds an ODS/API identifier: the student, staff or contact unique ID on users, and the
  education organization ID on orgs. On classes, `classCode` is the `localCourseCode`, which several sections
  share; on courses, `courseCode` is the ODS/API course code.

## Records by resource

| OneRoster | ODS/API source | What to know |
|---|---|---|
| `orgs` | Schools, local education agencies, state education agency | `type` is `school`, `district` or `state`; `parent` and `children` follow the education organization hierarchy in the ODS/API |
| `academicSessions` (`schoolYear`) | Calendar dates | One synthesized school year per district, from the most common first and last instructional days of its schools. Missing when the host hasn't mapped the calendar events that mark instructional days |
| `academicSessions` (terms, grading periods) | Sessions | `type` comes from the host's `TermDescriptor` mapping; sessions with an unmapped term type are left out |
| `courses` | Courses | One record per course, across all years it is offered. `grades`, `subjects` and `subjectCodes` are never filled |
| `classes` | Sections | One per section. `grades`, `subjects` and `subjectCodes` are never filled; `classType` is always `scheduled` |
| `users` | Students, staff, contacts | **One record per person per school** (see below) |
| `enrollments` | Student and staff section associations | The key includes `beginDate`, so a re-enrollment is a new record. Staff enrollments always have `role` `teacher`; `primary` is `"true"` for a "Teacher of Record" |
| `demographics` | Student demographics | Same rows and `sourcedId`s as the student records in `users` |

## Users are school-scoped

A student or staff member associated with two schools gets **two `users` records**, each with its own
`sourcedId`. This is intended, not a bug: enrollments at each school reference the matching record.

- To get one record per person, group by `identifier`. It holds the ODS/API `studentUniqueId`,
  `staffUniqueId` or `contactUniqueId` (`parentUniqueId` on Data Standard 4.0), which is also the first entry
  in `userIds`.
- A student who changes schools gets a new `sourcedId` at the new school.
- Contacts (parents and guardians) get one record each, keyed to the school of their linked students' most
  recent enrollment. When that changes, the contact gets a new `sourcedId`.
- The `roles` array lists each organization the person is associated with. For students and staff each one is
  marked `primary` or `secondary`; for contacts every entry is `primary`.
- `/teachers` returns staff whose role is `teacher`. A staff member gets one role, taken from their staff
  classifications through the host's mapping, so staff with several classifications may not appear there.

## Missing or empty fields

- Top-level fields with no value are left out of the response, not sent as `null`.
- Some fields are never filled by this service, whatever the ODS/API data: `grades`, `subjects` and
  `subjectCodes` on classes and courses. Changing the ODS/API data won't change the OneRoster output. If the
  client needs them, read the values from the ODS/API (for example the course's academic subject and offered
  grade levels, found through `metadata.edfi`) or another source, or raise it with the host.
- Values that come from descriptors (session type, role, sex, race, teacher of record) depend on the host's
  descriptor mapping to OneRoster values. An unmapped descriptor value can leave the field empty or the record
  out; for example, staff with no mapped role and no section assignment don't appear to school-scoped
  clients. Ask the host to check the mapping.
- Staff who work at several schools can get an inaccurate role in some versions of the service. Report
  surprising roles to the host with the staff member's `identifier`.

## Data Standard versions

The service supports Data Standard versions 4.0, 5.1, and 5.2. Support for Data Standard 6.1 is in recent
pre-release versions of the service; check the host's version. The OneRoster resources are the same, but some
details follow the Data Standard: on 4.0, contacts are parents (`parentUniqueId`, `metadata.edfi.resource`
`parents`), and on 6.1 demographics come from student demographics.
