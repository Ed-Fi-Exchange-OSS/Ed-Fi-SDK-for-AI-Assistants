# Data freshness

Why OneRoster data lags behind the ODS/API, and how to write sync jobs that stay correct. Part of the
[ed-fi-oneroster-client](../SKILL.md) skill.

## How the data is refreshed

The service doesn't query the ODS tables live. It reads OneRoster tables built from the ODS, which are
refreshed on a schedule **the host sets**. The schedule depends on the database:

| ODS database | How it refreshes | Schedule as shipped |
|---|---|---|
| PostgreSQL | The service refreshes one materialized view per resource, each on its own | A cron the host sets (`PGBOSS_CRON`); the shipped examples use every 15 minutes |
| SQL Server | A SQL Server Agent job refreshes the tables one after another | Once a day at 02:00, unless the host changes the job |

So a record written to the ODS/API can take minutes or **until the next day** to appear in OneRoster. Ask the
host for the actual schedule before designing a sync around it. Polling faster doesn't help.

What else to know:

- **There is no endpoint that reports when the last refresh ran** or whether it succeeded.
- **Resources can come from different refreshes.** On PostgreSQL each resource refreshes on its own, so
  `enrollments` can include a section association whose student hasn't reached `users` yet. On SQL Server, a
  failure partway through the job leaves the remaining tables from the previous run.
- **A failed refresh keeps the previous data**: the resource goes stale, it doesn't empty out.
- **Requests can slow down or fail during a refresh.** Reads wait while a table is being rebuilt, and a long
  wait can end in a `500`. Retry `500` responses with backoff.
- On PostgreSQL, after the service restarts, the first request to an ODS triggers an immediate refresh.

## Incremental sync

- `dateLastModified` comes from the Ed-Fi record behind each OneRoster record (for example the student),
  not from the OneRoster row. A change in related data, such as a new school association or role, may not
  change it. Filtering on `dateLastModified` alone can miss changes.
- Run a **full sync** periodically (for example nightly, after the host's refresh) even if you also run
  incremental syncs.
- Match records by `sourcedId`, and remember that it changes when the Ed-Fi data behind it changes
  ([mapping-to-ed-fi.md](mapping-to-ed-fi.md)).

## Deleting local records

A record can be missing from one run without having been deleted in Ed-Fi:

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
   Ed-Fi simply stop appearing.
