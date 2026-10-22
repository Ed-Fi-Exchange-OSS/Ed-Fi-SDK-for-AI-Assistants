# Example: Ed-Fi API client in JavaScript (Node.js)

An illustration of the client design in [authentication.md](../authentication.md#designing-the-client)
and the retry policy in [errors.md](../errors.md#retry-policy), using `axios`. Use it as a reference
for the logic, and write the client in the developer's own language and HTTP library.

## Client with discovery, token reuse and 401 handling

```javascript
import axios from 'axios';

export class EdFiClient {
  constructor(rootUrl, clientId, clientSecret) {
    this.rootUrl = rootUrl;
    this.clientId = clientId;
    this.clientSecret = clientSecret;
    this.urls = null;
    this.accessToken = null;
    this.tokenExpiresAt = 0;
    this.pendingAuth = null;
  }

  async discover() {
    if (this.urls) return this.urls;
    const { data } = await axios.get(this.rootUrl);
    if (!data?.urls?.oauth || !data?.urls?.dataManagementApi) {
      throw new Error('Discovery response is missing urls.oauth or urls.dataManagementApi');
    }
    this.urls = data.urls;
    return this.urls;
  }

  async authenticate() {
    // Collapse concurrent renewals into a single request.
    this.pendingAuth ??= (async () => {
      const { oauth } = await this.discover();
      // RFC 6749 §2.3.1: form-urlencode key and secret, join with ":", then base64.
      // (axios's built-in `auth` option skips the urlencoding step.)
      const formEncode = (value) => new URLSearchParams({ v: value }).toString().slice(2);
      const credentials = `${formEncode(this.clientId)}:${formEncode(this.clientSecret)}`;
      const basic = Buffer.from(credentials).toString('base64');
      try {
        const { data } = await axios.post(oauth, new URLSearchParams({ grant_type: 'client_credentials' }), {
          headers: {
            Authorization: `Basic ${basic}`,
            'Content-Type': 'application/x-www-form-urlencoded',
          },
        });
        this.accessToken = data.access_token;
        // Renew 60 seconds early.
        this.tokenExpiresAt = Date.now() + (data.expires_in - 60) * 1000;
      } catch (error) {
        const reason = error.response?.data?.error_description ?? error.message;
        throw new Error(`Authentication failed: ${reason}`);
      } finally {
        this.pendingAuth = null;
      }
    })();
    return this.pendingAuth;
  }

  async request(path, { method = 'GET', data, headers = {}, params } = {}) {
    const { dataManagementApi } = await this.discover();
    if (!this.accessToken || Date.now() >= this.tokenExpiresAt) await this.authenticate();

    const send = () =>
      axios({
        method,
        url: new URL(path.replace(/^\//, ''), dataManagementApi).toString(),
        params,
        data,
        headers: {
          Authorization: `Bearer ${this.accessToken}`,
          'Content-Type': 'application/json',
          ...headers,
        },
      });

    try {
      return await send();
    } catch (error) {
      if (error.response?.status !== 401) throw error;
      await this.authenticate(); // retry once with a fresh token
      return await send();
    }
  }
}

// Usage
const client = new EdFiClient(
  process.env.EDFI_API_ROOT_URL,
  process.env.EDFI_CLIENT_ID,
  process.env.EDFI_CLIENT_SECRET,
);
const response = await client.request('/ed-fi/schools', { params: { limit: 100, offset: 0 } });
```

## Retry wrapper

```javascript
const RETRYABLE = new Set([429, 500, 502, 503, 504]);

async function withRetry(send, { maxAttempts = 5, baseDelayMs = 500 } = {}) {
  for (let attempt = 1; ; attempt++) {
    try {
      return await send();
    } catch (error) {
      const status = error.response?.status;
      const retryable = status === undefined /* network error */ || RETRYABLE.has(status);
      if (!retryable || attempt >= maxAttempts) throw error;

      const retryAfterSeconds = Number(error.response?.headers?.['retry-after']);
      const delay = Number.isFinite(retryAfterSeconds)
        ? retryAfterSeconds * 1000
        : baseDelayMs * 2 ** (attempt - 1) * (0.5 + Math.random()); // exponential backoff with jitter
      await new Promise((resolve) => setTimeout(resolve, delay));
    }
  }
}
```

Usage: `await withRetry(() => client.request('/ed-fi/students', { method: 'POST', data: student }))`.

## Failure logging

```javascript
function describeFailure(resource, naturalKey, error) {
  const problem = error.response?.data ?? {};
  return {
    resource,                       // e.g. '/ed-fi/studentSchoolAssociations'
    naturalKey,                     // e.g. { studentUniqueId: '604822', schoolId: 255901001 }
    status: error.response?.status,
    type: problem.type,
    detail: problem.detail,
    validationErrors: problem.validationErrors ?? problem.errors,
    correlationId: problem.correlationId,
  };
}
```
