# OneRoster client skill: test prompts

Test prompts for the [`ed-fi-oneroster-client`](../../skills/ed-fi-oneroster-client/SKILL.md) skill (PRD
FR-REL-2). Expected outcomes come from the
[edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) source and the Ed-Fi OneRoster
documentation; outcomes marked **(key)** must be met for the prompt to pass.

Run each prompt in a fresh session, with the skill installed and without it, and record the results in
`oneroster-client-test-results.md`. Score each outcome ✅ met, ⚠️ partially met or ❌ not met.

The prompts cover the four topics of the skill: authentication (T1, T2, T6), what the service offers (T3,
T4), data freshness (T5) and mapping to Ed-Fi (T7, T8).

## T1 · Authentication: first request

**Prompt:**

> I have a key and secret for our district's Ed-Fi ODS/API 7.3, and the district also runs the Ed-Fi
> OneRoster API. Write a Python function that gets a token and lists the first page of classes from
> OneRoster. The ODS/API root URL and the OneRoster root URL come from environment variables.

**Expected outcomes:**

1. **(key)** Gets the token from the **ODS/API** token endpoint (from Discovery `urls.oauth`), with the same
   key and secret. Doesn't invent a separate OneRoster credential.
2. **(key)** Calls `/ims/oneroster/rostering/v1p2/classes` on the OneRoster service with
   `Authorization: Bearer`.
3. **(key)** Requests a OneRoster scope (`roster.readonly` or `roster-core.readonly`, as the full URI) in the
   token request's `scope` parameter. Without it the token carries no scopes and the request gets `403`.
4. Sends the credentials in a Basic header and reuses the token until it is about to expire.
5. Doesn't post credentials to the OneRoster service's `/oauth/token`, or explains that it only redirects to
   the ODS/API.
6. Notes that the host must issue JWT tokens that the OneRoster service accepts, and that GUID tokens fail
   with `401`.

## T2 · Authentication: demographics returns 403

**Prompt:**

> Our OneRoster sync works for users and enrollments, but `GET /ims/oneroster/rostering/v1p2/demographics`
> returns 403 with "Insufficient scope". We already have roster.readonly. Why?

**Expected outcomes:**

1. **(key)** Explains that demographics needs `roster-demographics.readonly`; `roster.readonly` excludes it by
   design in OneRoster 1.2.
2. **(key)** The fix: request `roster-demographics.readonly` in the token request's `scope` parameter, next to
   the scope already used. If the token's `scope` claim still lacks it, the host must allow it in the API
   client's claim set.
3. Doesn't suggest retrying, or getting a new token without changing the requested scopes, as the fix.

## T3 · Paging a full sync

**Prompt:**

> Write a JavaScript function that downloads all users from our Ed-Fi OneRoster API for a nightly sync. We
> have about 40,000 users.

**Expected outcomes:**

1. **(key)** Pages with `limit` and `offset` and doesn't rely on a total-count header, which the service
   doesn't send.
2. **(key)** Doesn't assume that a large `limit` (for example 10,000) is honored: the service clamps it to its
   maximum page size (500 by default) without an error. Stops on an empty page, or on a page shorter than a
   `limit` known to be within the maximum.
3. **(key)** Handles `429` with backoff (the default limit is 100 requests per minute).
4. Reuses one token for the whole run and gets a new one on `401`.
5. Parses errors from the `imsx_codeMajor` / `imsx_description` body, not Ed-Fi problem details.

## T4 · What the service doesn't offer

**Prompt:**

> Using the Ed-Fi OneRoster API, write code to post final grades from our LMS back to Ed-Fi as OneRoster
> results.

**Expected outcomes:**

1. **(key)** Says the Ed-Fi OneRoster API is read-only and serves only Rostering. It has no Gradebook service
   and accepts no POST or PUT.
2. **(key)** Points to the Ed-Fi ODS/API (for example the `grades` resource, with the `ed-fi-api-client`
   skill) to write grades.
3. Doesn't generate code against `/ims/oneroster/gradebook/v1p2/...` as if it existed.

## T5 · Data freshness and deletions

**Prompt:**

> We wrote a new student and their section association through the Ed-Fi ODS/API ten minutes ago, but the
> student doesn't show up in OneRoster users or enrollments. Also, our nightly OneRoster sync deletes local
> records that are missing from the feed. Is that safe?

**Expected outcomes:**

1. **(key)** Explains that the OneRoster data is refreshed on a schedule the host sets (often every 15 minutes
   on PostgreSQL, once a day as shipped on SQL Server), so recent ODS/API writes appear after the next refresh.
   Doesn't promise a fixed delay.
2. **(key)** Warns that a record can be missing without being deleted (resources refresh separately, a key
   change creates a new `sourcedId`, lost access to an education organization, an incomplete run), and
   recommends safeguards before deleting, such as a threshold or a soft delete.
3. Suggests asking the host about the refresh schedule instead of polling faster.

## T6 · Empty results with a valid token

**Prompt:**

> Our OneRoster API calls return 200 but every collection is empty: orgs, users, classes. The token works and
> the ODS/API has data. What's wrong?

**Expected outcomes:**

1. **(key)** Points to the token's education organizations: a client with none associated gets empty results,
   not an error.
2. **(key)** The fix is on the host side: associate the API client with the right education organizations in
   the ODS/API.
3. Mentions the data refresh as a second thing to check, for example right after a new deployment.

## T7 · Duplicate students

**Prompt:**

> In the OneRoster users feed we see the same student twice, with different sourcedIds. Is that a bug in the
> Ed-Fi OneRoster API?

**Expected outcomes:**

1. **(key)** Explains that users are school-scoped: a student associated with two schools gets one `users`
   record per school, each with its own `sourcedId`.
2. **(key)** Suggests grouping on `identifier` (the Ed-Fi `studentUniqueId`, also the first entry in
   `userIds`) when the client needs one record per person, instead of treating it as a bug.
3. Mentions that `demographics` follows the same records.

## T8 · Missing fields in classes

**Prompt:**

> Our LMS requires `subjects` and `grades` on every OneRoster class, but the Ed-Fi OneRoster API never
> returns them. How do we fix our Ed-Fi data so they're filled in?

**Expected outcomes:**

1. **(key)** Says the service doesn't fill `grades`, `subjects` or `subjectCodes` for classes, whatever the
   Ed-Fi data. It's a limitation of the service, not missing data.
2. Suggests a workaround in the client, such as reading the values from the ODS/API (the OneRoster course
   doesn't have them either), or raising it with the host or Ed-Fi.
3. Doesn't invent an Ed-Fi field or a configuration setting that would fill them.
