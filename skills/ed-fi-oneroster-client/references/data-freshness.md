# Data freshness

Why OneRoster data lags behind the ODS/API, and how to write sync jobs that stay correct. Part of the
[ed-fi-oneroster-client](../SKILL.md) skill.

## How the data is refreshed

The service doesn't read the ODS/API data live. It serves a copy that the host refreshes on a schedule, from
every few minutes to once a day. Between refreshes, a direct ODS/API `GET` and a OneRoster `GET` can
disagree: a record written to the ODS/API appears in OneRoster only after the next refresh, and a change or
delete shows up in OneRoster late too.

- When OneRoster data doesn't match the ODS/API, check whether the change is newer than the last refresh
  before looking for another cause. Ask the host for the refresh schedule; polling faster doesn't help.
- If OneRoster data never catches up with the ODS/API, ask the host whether the scheduled refresh is set up
  and running.
- **There is no endpoint that reports when the last refresh ran** or whether it succeeded.
- **Resources can come from different refreshes.** For example, `enrollments` can include a section
  association whose student hasn't reached `users` yet.
- **A failed refresh keeps the previous data**: the resource goes stale, it doesn't empty out.
- **Requests can slow down or fail during a refresh.** A long wait can end in a `500`. Retry `500` responses
  with backoff.

## Incremental sync

- `dateLastModified` comes from the ODS/API record behind each OneRoster record (for example the student),
  not from the OneRoster row. A change in related data, such as a new school association or role, may not
  change it. Filtering on `dateLastModified` alone can miss changes.
- Run a **full sync** periodically (for example nightly, after the host's refresh) even if you also run
  incremental syncs.
- Match records by `sourcedId`, and remember that it changes when the ODS/API data behind it changes
  ([mapping-to-ed-fi.md](mapping-to-ed-fi.md)).

## Deleting local records

A record can be missing from one run without having been deleted in the ODS/API:

- the resource it depends on hasn't refreshed yet (see above);
- its `sourcedId` changed: a student or staff member moving schools, a re-enrollment, or a contact whose
  linked student enrolled at another school;
- the API client lost access to an education organization, so a whole school's records disappear;
- the run itself was cut short (an error in the middle of paging, or a refresh between pages).

Before deleting local records that are missing from the feed:

1. Delete only after a run that paged every resource to the end without errors.
2. Set a threshold: if more than a small share of records (for example 5%) would be deleted in one run, stop
   and alert instead.
3. Prefer a soft delete (mark inactive) and purge only after the record has been missing for several runs.
4. Don't wait for `status: tobedeleted`. This service returns every record as `active`; records deleted in
   the ODS/API simply stop appearing.
