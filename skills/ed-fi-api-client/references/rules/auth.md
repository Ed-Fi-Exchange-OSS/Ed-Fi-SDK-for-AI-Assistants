# Rules: Authentication and security

Part of the [Ed-Fi API client rules](../rules.md). See that file for what each level means for
building and reviewing code.

## AUTH-1: Send client credentials in a Basic `Authorization` header, urlencoded then base64-encoded

- **Level:** Preferred. Credentials in the form body are **Allowed but discouraged** on ODS/API 7.x.
- **Why:** request bodies are more likely to be logged by proxies, gateways and debugging tools. RFC 6749
  §2.3.1 requires form-urlencoding the key and secret before joining them with `:` and base64-encoding;
  Ed-Fi API 8 secrets always contain special characters, so skipping it causes `401` errors.
- **Detect:** `client_id` / `client_secret` sent as form fields in the token request body (discouraged on
  ODS/API 7.x; violation when the code targets Ed-Fi API 8); a Basic header built with a library's built-in
  basic-auth helper or from the raw secret without urlencoding (violation).
- **Versions:** Ed-Fi API 8 accepts only the Basic header and answers body credentials with `400`
  "Malformed Authorization header".
- **Details:** [authentication.md](../authentication.md#requesting-a-token)

## AUTH-2: Reuse the access token until it is about to expire

- **Level:** Required
- **Why:** a token request per API call is slow and can trip host rate limits. The lifetime is set by the
  host and returned in `expires_in`; there is no refresh token.
- **Detect:** a token request inside the per-record or per-request loop; a hard-coded token lifetime
  instead of `expires_in`; no early renewal margin; parallel workers each requesting their own token.
- **Details:** [authentication.md](../authentication.md#token-lifecycle-rules)

## AUTH-3: On `401`, re-authenticate once and retry once, then stop

- **Level:** Required
- **Why:** a single `401` usually means the token expired. A second `401` means the credentials are wrong,
  revoked, or for a different instance, and retrying in a loop hides the problem.
- **Detect:** no handling of `401`; unbounded retries on `401`; `401` treated like a `5xx`.
- **Details:** [authentication.md](../authentication.md#token-lifecycle-rules),
  [errors.md](../errors.md#401-unauthorized)

## AUTH-4: Never hard-code or log the client secret or access tokens

- **Level:** Required
- **Why:** leaked credentials give access to student data.
- **Detect:** secrets or tokens in source code, committed config files, logs, error messages or exception
  text; logging of full request headers or token request bodies.
- **Details:** [authentication.md](../authentication.md#what-the-client-needs)

## AUTH-5: Use HTTPS, and never permanently disable certificate validation

- **Level:** Required (HTTPS, and certificate validation on in shared and production environments).
  Turning validation off for local testing is **Allowed but discouraged**.
- **Why:** credentials and student data travel in every request. Testing against a local deployment with
  a self-signed certificate is a legitimate case, but code that skips validation tends to reach
  production.
- **Build:** prefer trusting the local certificate (add it to the trust store or the client's CA bundle).
  If validation must be switched off for local testing, gate it behind an explicit setting that is off by
  default, log a warning when it is on, and never hard-code it.
- **Detect:** `http://` API URLs outside local development (violation); options such as `verify=False`,
  `rejectUnauthorized: false`, or a certificate callback that always returns true, hard-coded or on by
  default (violation); the same behind an explicit, off-by-default local-testing setting (discouraged:
  add a cautionary note).
- **Details:** [authentication.md](../authentication.md#troubleshooting-authentication)
