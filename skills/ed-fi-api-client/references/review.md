# Reviewing existing Ed-Fi client code

Use this procedure when asked to review, audit, or check existing code that calls an Ed-Fi API. It applies
the same [rules](rules.md) used to build integrations, reporting each one by its level.

## 1. Scope the review

1. Find the code that talks to the Ed-Fi API: the token request, the HTTP client or SDK wrapper, and the
   loops that read or write resources. Ignore unrelated code.
2. Identify what kind of integration it is: **push** (writes), **pull** (reads), or both.
3. Note the target platform if visible (ODS/API 7.x or Ed-Fi API 8, from URLs or configuration). Some rules
   have **Versions** notes.

## 2. Load only the rules you need

Open [rules.md](rules.md) for the levels, then only the categories that apply:

| Code does | Load |
|---|---|
| Any Ed-Fi API call | [discovery](rules/discovery.md), [auth](rules/auth.md), [errors](rules/errors.md) |
| Writes (POST, PUT, DELETE) | [push](rules/push.md) |
| Reads (GET collections, change queries) | [pull](rules/pull.md) |

## 3. Check each rule

For each rule in the loaded categories, use its **Detect** notes to look for evidence in the code, and record
one of these outcomes:

| What you find | Rule level | Report as |
|---|---|---|
| The code violates the rule | Required | **Must fix** |
| The code does not follow the rule | Preferred | **Should fix** |
| The code uses the *Allowed but discouraged* pattern | Any rule that lists one | **Suggestion**: accept it, and propose the preferred alternative |
| The code follows the rule | Any | Not a finding (count it as passed) |
| Not enough code to tell | Any | Not a finding; mention it under "Not checked" |

Guidelines:

- **Cite evidence.** Every finding needs a file and line (or function) and a short quote or description of
  the code.
- **Keep the level from the table.** Report each finding in the section its rule level gives. Don't move a
  finding up or down because of its impact; if the impact is unusually high or low, say so in the finding's
  text.
- **One place per rule.** Don't list a rule as passed if you report a finding for it. If different parts of
  the code meet a rule at different levels (e.g. a hard-coded `verify=False` and a separate off-by-default
  setting), report each part once, at its own level.
- **Respect documented exceptions.** If the code explains a legitimate reason for a discouraged pattern (for
  example, deleting and reposting to change a natural key without cascading key updates, or disabling
  certificate validation only for local testing behind an explicit setting), report it as a suggestion at
  most, not a violation.
- **Don't guess at intent.** If a rule depends on runtime behavior you can't see (e.g. whether the host
  enables ETags or snapshots), list it under "Not checked" instead of reporting a violation.
- **Ask about ambiguous identifiers.** If it's unclear whether a variable holds the resource `id` or a
  natural key (e.g. `old_id` in an item URL), don't report a violation. List it under "Not checked" with the
  question to confirm, and state the fix that applies if it turns out to be a natural key.
- **Stay in the client's scope.** Claim sets, Profiles configuration and other host settings are out of scope
  for client code; mention them only if the code works around them incorrectly.

## 4. Report

Use this structure:

```markdown
## Ed-Fi client review: <repository or files>

**Integration:** push / pull / both · **Platform:** ODS/API 7.x / Ed-Fi API 8 / unknown
**Summary:** N must fix, N should fix, N suggestions · N rules passed · N not checked

### Must fix
- **PUSH-3** · `src/sync/students.py:88`: PUT to `/ed-fi/students/{studentUniqueId}` uses the natural key in
  the URL; this returns 404. Look up the resource `id` (from `Location` or a GET by `studentUniqueId`) and PUT
  to `/ed-fi/students/{id}`.

### Should fix
- **AUTH-1** · `src/edfi/client.py:42`: credentials are sent in the token request body. Use a Basic
  `Authorization` header (form-urlencode key and secret, join with `:`, base64-encode).

### Suggestions
- **PUSH-2** · `src/sync/sections.py:120`: deletes and reposts sections to apply changes. Sections support
  cascading key updates, so PUT by `id` would work and keep the resource `id` stable.

### Not checked
- **PUSH-7**: whether the host enables ETags is not visible from the code.
```

Order findings by level, then by file. Keep each finding to two or three lines: the rule ID, where, what is
wrong, and the fix. Link to the rule or guide only when the fix needs more explanation.

Before you send the report, check it:

1. **Re-read every cited line.** Open the file at the line you cite and confirm the code says what the finding
   claims. Drop or correct any finding you can't confirm.
2. **Check each rule ID appears in one section only**, except when separate parts of the code meet the rule at
   different levels. A rule with any finding is not "Passed".
3. **Check the levels against the table in step 3**, and that "Must fix" holds only *Required* rules.

## 5. After the review

If the developer asks for fixes, switch to building: apply the relevant guide ([push](push.md),
[pull](pull.md), [errors](errors.md), [authentication](authentication.md)) and the same rules.
