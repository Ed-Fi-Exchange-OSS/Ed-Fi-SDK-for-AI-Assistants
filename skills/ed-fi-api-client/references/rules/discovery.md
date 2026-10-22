# Rules: Discovery

Part of the [Ed-Fi API client rules](../rules.md). See that file for what each level means for
building and reviewing code.

## DISC-1: Configure only the API root URL; take every other URL from the Discovery API

- **Level:** Required
- **Why:** hosts add tenant and context segments, and Ed-Fi API 8 removed the `v3` segment from resource
  URLs. URLs built by hand break when the host or version changes.
- **Detect:** hard-coded `/oauth/token`, `/connect/token`, `/data/v3/`, `/metadata/` or
  `/changeQueries/` paths; more than one configured base URL; no GET on the root URL.
- **Versions:** ODS/API 7.x uses `.../data/v3/{schema}/{resource}`; Ed-Fi API 8 uses
  `.../data/{schema}/{resource}` and its token endpoint moved to `/connect/token`.
- **Details:** [SKILL.md](../../SKILL.md#step-1-start-every-integration-from-the-discovery-api)
