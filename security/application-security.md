# Application and API Security

## Edge and HTTP hardening

Trusted proxy headers are accepted only from explicitly configured proxies. The
API and browser applications apply HSTS where appropriate, content-type
protection, frame denial, strict referrer policy, and a constrained CSP. The same
headers and correlation ID are re-applied after sanitized exception responses.

Request bodies and multipart uploads have bounded limits. Validation occurs
before handler mutation. Abuse-prone authentication, recovery, financial,
diagnostic, inquiry, and sharing endpoints have explicit rate-limit policies and
`Retry-After` behavior.

## Injection and content

EF Core/MySqlConnector parameterization is used for application queries. Reviewed
MySQL scripts are applied operationally rather than accepting user SQL. Public
HTML is limited to trusted administrator-managed content; user text is encoded.
Uploads are not executed from web roots.

## Mutation safety

Financial and high-impact mutations require idempotency. The server binds a key
to tenant, user, operation, and payload hash, returns a stable in-progress result
for concurrent duplicates, and replays completed responses. Payload mismatch is
rejected.

Entity versions and conditional transitions prevent stale acceptance,
cancellation, membership, document, and trip changes. Auditing and provider
side effects occur through durable records so an audit/provider outage does not
turn a committed mutation into a misleading client failure.

## Mobile protections

Secure storage, biometric APIs, platform keystore secrets, certificate/package
configuration, App Check, release signing, and store permission gates raise the
cost of attack. They do not move the security boundary out of the API.

Diagnostic proxy settings are compile-time gated and unavailable in production
builds. Sensitive wallet and account-security flows are disabled in approved
diagnostic builds that intercept traffic.
