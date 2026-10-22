# API Client skill: test prompts

Test prompts with expected outcomes for the `ed-fi-api-client` skill (PRD FR-REL-1, FR-REL-2). Run each prompt
in a fresh session of each required harness (Claude Code, GitHub Copilot), **with and without** the skill
installed, and check the answer against the expected outcomes.

Scoring per expected outcome: ✅ met · ⚠️ partially met · ❌ not met. A prompt **passes** when every
outcome marked **(key)** is met and no answer contradicts a Required rule.

Prompts T1–T3 come from the problems Stephen listed as the most common for people (dependencies, token
caching and expiration, delete and repost instead of updating).

---

## T1 · Push: dependencies and the complete load (push guide)

**Prompt:**

> Write a Python script that reads students and their school enrollments from two CSV files (students.csv,
> enrollments.csv) and loads them into an Ed-Fi API. The API root URL, key and secret come from environment
> variables.

**Expected outcomes:**

1. **(key)** Loads students before student school associations, ideally using the `dependencies` endpoint
   (PUSH-1).
2. **(key)** Takes the token and resource URLs from the Discovery API, with no hard-coded `/data/v3/` or
   `/oauth/token` path (DISC-1).
3. **(key)** Sends the key and secret in a Basic header, form-urlencoded before base64 (AUTH-1).
4. **(key)** Reuses the token until it is about to expire (AUTH-2).
5. Uses POST for both creating and updating (upsert), with complete records (PUSH-2, PUSH-4).
6. Sends `entryGradeLevelDescriptor` as a full descriptor URI, with the mapping in configuration (PUSH-5).
7. Sends dates as `YYYY-MM-DD` (PUSH-6).
8. Retries only `5xx`, `429` and network errors; logs failures with the natural key and `correlationId`
   (ERR-2, ERR-3).

## T2 · Push: updating a record (delete and repost, natural key in URL)

**Prompt:**

> Using the Ed-Fi API, update the last name of the student with studentUniqueId 604822 to "Martinez".
> Show me the HTTP requests.

**Expected outcomes:**

1. **(key)** Does not PUT or DELETE to `/ed-fi/students/604822`; gets the resource `id` first (GET with
   `?studentUniqueId=604822`) or uses POST upsert (PUSH-3).
2. **(key)** Does not delete and repost the student (PUSH-2).
3. **(key)** Sends the complete student record, not only the changed field (PUSH-4).
4. Mentions `If-Match` with the ETag if the host enables it (PUSH-7). *(optional)*

## T3 · Auth: token caching (review interface)

**Prompt:**

> Review this code that calls our Ed-Fi API. Is anything wrong?
>
> ```python
> import os, requests
>
> def get_token():
>     r = requests.post(os.environ["EDFI_URL"] + "/oauth/token",
>                       data={"grant_type": "client_credentials",
>                             "client_id": os.environ["EDFI_KEY"],
>                             "client_secret": os.environ["EDFI_SECRET"]})
>     return r.json()["access_token"]
>
> def post_resource(path, body):
>     token = get_token()
>     r = requests.post(os.environ["EDFI_URL"] + "/data/v3" + path, json=body,
>                       headers={"Authorization": "Bearer " + token}, verify=False)
>     if r.status_code >= 400:
>         return post_resource(path, body)
>     return r
> ```

**Expected outcomes:**

1. **(key)** Flags requesting a new token on every call as **must fix** (AUTH-2).
2. **(key)** Flags retrying every error, including `4xx`, without limit or backoff as **must fix** (ERR-2).
3. **(key)** Flags `verify=False` hard-coded as **must fix** (AUTH-5).
4. Flags credentials in the request body as **should fix**, suggesting the Basic header (AUTH-1).
5. Flags hard-coded `/oauth/token` and `/data/v3` paths (DISC-1).
6. Uses the review format: findings grouped by level, with the rule ID and the fix.

## T4 · Errors: diagnosing a 409

**Prompt:**

> I got this response when posting a studentSchoolAssociation. What's wrong and how do I fix it?
>
> ```json
> {
>   "detail": "The referenced 'Student' resource does not exist.",
>   "type": "urn:ed-fi:api:data-conflict:unresolved-reference",
>   "title": "Unresolved Reference",
>   "status": 409,
>   "correlationId": "8a1f0c2e-7d1b-4c55-9b0e-2f6b1e3c9d10"
> }
> ```

**Expected outcomes:**

1. **(key)** Explains that the referenced student does not exist in the API (not a duplicate key).
2. **(key)** Fix: load the student first (dependency order), or correct the `studentReference` key values.
3. Recommends branching on `type`, not on `detail` text, and logging the `correlationId` (ERR-1, ERR-3).

## T5 · Auth: 401 on the token request

**Prompt:**

> Our client gets 401 invalid_client from the Ed-Fi token endpoint. The key and secret are correct; we use
> the HTTP library's built-in basic-auth option. The secret contains characters like ":" and "#". What could
> be wrong?

**Expected outcomes:**

1. **(key)** Points to the missing form-urlencoding of key and secret before base64 (RFC 6749 §2.3.1) in
   built-in basic-auth helpers (AUTH-1).
2. Shows how to build the header correctly (urlencode, join with `:`, base64).
3. Mentions checking that the request goes to the instance or tenant that issued the credentials.

## T6 · Pull: incremental sync (change queries)

**Prompt:**

> Design a nightly job that copies Ed-Fi sections and student section associations into our data warehouse,
> reading only what changed since the last run.

**Expected outcomes:**

1. **(key)** Uses change queries with both `minChangeVersion` and `maxChangeVersion`, from
   `availableChangeVersions` (PULL-3).
2. **(key)** Processes `/deletes` and `/keyChanges`, not only changed records (PULL-3).
3. **(key)** Saves the new change version only after the whole run succeeds (PULL-3).
4. Order: key changes, then changes, then deletes in reverse dependency order.
5. Pages through every request (PULL-1).
6. Mentions snapshots on ODS/API 7.x (`Use-Snapshot`), and that Ed-Fi API 8.0 has none (PULL-4).

## T7 · Pull: large extract (paging)

**Prompt:**

> We need to extract all studentSectionAttendanceEvents (several million records) from an ODS/API 7.3
> instance as fast as possible. How should we page through them?

**Expected outcomes:**

1. **(key)** Recommends cursor paging (`pageSize`, `pageToken`, `Next-Page-Token`) over deep offset paging
   (PULL-2).
2. **(key)** Recommends `/partitions` for parallel extraction, with the same filters on every request.
3. Notes that cursor paging cannot be combined with `limit`/`offset` or `totalCount`.
4. Stops on an empty page, not on a computed total (PULL-1).

## T8 · Platform: moving to Ed-Fi API 8

**Prompt:**

> We're moving our Ed-Fi client from ODS/API 7.3 to Ed-Fi API 8. What do we need to change?

**Expected outcomes:**

1. **(key)** Resource URLs lose the `v3` segment; build URLs from the Discovery API.
2. **(key)** Property names are case-sensitive.
3. **(key)** The token endpoint moved to `/connect/token` (with an `/oauth/token` compatibility proxy); take it
   from the Discovery API.
4. No snapshot support in 8.0.
5. Does not claim other breaking changes that aren't documented.

## T9 · Push: descriptors

**Prompt:**

> Our SIS stores grade level as codes like "05" and "KG". How do I send them to the Ed-Fi API on a
> studentSchoolAssociation?

**Expected outcomes:**

1. **(key)** Sends a full descriptor URI (e.g. `uri://ed-fi.org/GradeLevelDescriptor#Fifth grade`), not the
   bare code (PUSH-5).
2. **(key)** Reads the available values from the target API (`gradeLevelDescriptors`); namespaces can differ
   by state or district.
3. Keeps the source-to-descriptor mapping in configuration, not in code.

## T10 · Review: documented exception

**Prompt:**

> Review this function. It is used only to change a section's identifier when the SIS renumbers it.
>
> ```python
> # Sections are renumbered by the SIS. We delete and repost because the old
> # host did not support key changes for this resource.
> def renumber_section(client, old_id, new_section):
>     client.delete(f"ed-fi/sections/{old_id}")
>     client.post("ed-fi/sections", new_section)
> ```

**Expected outcomes:**

1. **(key)** Treats delete and repost as a **suggestion**, not a violation, because the code documents a
   reason (PUSH-2, *Allowed but discouraged*).
2. **(key)** Points out that `sections` supports cascading key updates in ODS/API 7.x, so a PUT changing the
   key would keep the `id` stable.
3. Mentions dependent records (`409 dependent-item-exists` on delete) if the delete is kept.
