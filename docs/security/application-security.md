# Application and API security

This document follows a request from the public edge to the domain handler and
back. It highlights controls that are easy to place in the wrong order and bugs
that look harmless until an attacker automates them.

The [security control model](security-control-model.md) supplies current source
evidence and configuration qualifications. The
[OWASP API Top 10 mapping](owasp-api-top-10-2023.md) organizes review by risk,
including object, property and function authorization as separate concerns.

## Edge and trusted proxy boundary

Cloudflare or another approved edge may terminate public TLS and add the original
client address. The API trusts `CF-Connecting-IP` or forwarded headers only when
the immediate proxy belongs to an explicitly configured trusted set. Otherwise,
an attacker can choose their own apparent IP and evade rate limits or poison
audits.

The resolved client IP feeds rate-limit partitions, session evidence, and audit
stamps. Application code should use the shared resolver rather than reading the
socket peer directly.

WAF rules can block or challenge common WordPress/PHP probes and suspicious path
scans before they reach IIS. WAF is noise reduction, not authorization; a valid-
looking API request still passes every application check.

## Middleware order

Ordering changes meaning. In the reviewed API source, after the early response,
correlation, exception and applicable mobile-version boundaries, the protected
request pipeline registers:

1. authentication;
2. device access for the public API runtime profile;
3. endpoint authorization;
4. tenant resolution and the authenticated cell-session check;
5. rate limiting;
6. applicable App Check and public-form admission;
7. idempotency and mutation-audit middleware; and
8. endpoint filters, validation and handler execution.

This order comes from `Program.cs` at the
[reviewed baseline](../current-baseline.md). It corrects the older illustrative
ordering that placed rate limiting before authentication and authorization.
Protected endpoints reject unauthenticated callers before tenant resolution,
model validation or notification staging. The hosting/edge layer still needs
its own traffic controls; a later application limiter does not bound all work
performed before it. Tests should assert ordering and absence of unauthorized
side effects, not merely the final status code.

## Response hardening

API, portal, and website responses preserve:

- a validated/generated correlation ID;
- HSTS where HTTPS policy applies;
- `X-Content-Type-Options: nosniff`;
- frame protection;
- a strict referrer policy; and
- the application-specific Content Security Policy.

Exception middleware often calls `Response.Clear()`. That can erase headers set
earlier. KiloDrive uses a shared hardening helper to reapply them before writing
sanitized Problem Details. Integration tests cover validation, domain,
concurrency, rate-limit, and unhandled error paths.

CSP is not fixed by adding `unsafe-inline` whenever a widget fails. Remove inline
styles/scripts, use self-hosted pinned assets and nonces/hashes where truly
needed, and keep Swagger's documented policy separate from corporate/portal
pages.

Production CSP changes use parsed directives and allow-listed sources, not a
raw textbox followed by immediate activation. A candidate is versioned, diffed,
validated for syntax and security regressions, staged, independently approved,
and checked by a no-redirect synthetic health probe before activation. Rollback
selects a previously activated, probe-passed version. The control plane is
implemented; browser resource-load and rollback exercises remain release/
operational evidence rather than a source-code claim.

## Validation, injection, and content handling

DTO validation gives each missing/invalid field a stable error instead of a vague
“complete everything.” EF Core/MySqlConnector parameterization handles normal
queries. Operational SQL is reviewed and idempotent; user-provided SQL is never
executed.

User text is encoded. Administrator-managed website HTML is a trusted-content
boundary with restricted roles and audit. Uploads are kept outside public web
roots and follow quarantine rules.

Request body and multipart limits are set at the hosting layer as well as the
application where possible. A warning that the server's request-size feature is
read-only means the limit was attempted too late; correct the IIS/Kestrel hosting
configuration rather than ignoring it.

## Rate limiting

Use route-specific budgets for login, 2FA, reset, OTP, top-up, diagnostics, share
links, and other abuse-prone endpoints. Partition by authenticated user when
available and trusted client IP where appropriate. Return `429` with a useful
`Retry-After` and stable error code.

Do not disable the limiter globally to fix a legitimate burst. Measure normal
peak behavior and tune the narrow policy. Keep business usage limits—such as bid
or membership limits—separate from transport abuse limits.

The reviewed ASP.NET limiter instances hold process-local counters. Multiple
API nodes require an assessed aggregate budget; using Redis elsewhere does not
make these counters distributed. Configurable endpoint budgets can also observe
without enforcing. Effective modes, provider spending controls and multi-node
capacity evidence remain operational verification requirements.

## Idempotency and optimistic concurrency

Mobile networks lose responses and users tap twice. Protected mutations bind an
idempotency key to tenant, user, operation, and payload hash. Concurrent claims
receive an in-progress result; completed retries replay the stored response; a
different payload under the same key is rejected.

Idempotency answers “did this logical command already run?” Entity versions and
conditional state answer “is this transition still legal?” A ride acceptance,
wallet transfer, document decision, and membership change often need both.

Do not blindly retry POST/PUT/PATCH/DELETE in a generic HTTP resilience handler.
A provider may have accepted the first call before timing out. Retry only with a
stable provider idempotency key or after reconciliation.

Administrative issuance of redeemable value follows the same rule. A voucher
batch binds tenant, administrator, route, idempotency key, quantity, face value,
credit currency, and request hash to one durable operation reference. If the
database commits and the response is lost, the same request replays the same
batch; it never mints another set of codes. An in-flight duplicate conflicts and
a changed payload under the same key is rejected.

Because the replay response contains one-time voucher material, it is encrypted
with the persistent Data Protection key ring rather than stored as readable
idempotency JSON. Lookup uses a keyed HMAC digest and bounded display suffix,
not plaintext or a fast unkeyed hash. Losing the key ring or HMAC key is an
incident affecting recovery or redemption; neither secret belongs in logs,
source, metrics, or the public documentation repository.

## Tenant and object authorization

Global EF query filters reduce accidental tenant leakage but are not magic. Code
using `IgnoreQueryFilters` must manually prove and document the boundary. Every
lookup by externally supplied UUID also checks ownership, participant membership,
or explicit administrator permission.

A past payout-method defect demonstrated the danger of loading by ID and then
deleting without checking `UserId`. The secure query includes both identifiers
and returns the same coarse result for foreign and missing records.

System Administrator APIs need explicit permissions, country workspace, and
auditing. A role name alone should not silently grant every future operation.

## Financial and lifecycle safety

Wallet changes use deterministic lock ordering and immutable journal references.
Held funds are unavailable for another spend. Reconciliation blocks unsafe
cashout, but its equations and status sets must be correct—an overly broad false
positive can become a platform-wide denial of service.

Ride/bid/trip transitions revalidate eligibility within the locked transaction:
online state, fresh location, active assignment, duty, compliance version,
vehicle, trust level, and membership. A bid made earlier is not permanent proof
that the driver is still eligible.

Durable audit/outbox records are staged in the business transaction. Awaiting a
separate audit write or provider send after commit can make the client receive an
error for a mutation that actually succeeded.

## Realtime security

Hub tokens live for sixty seconds and are explicitly `discovery`- or
`trip`-scoped. They are bound to user, role, tenant, country, token version and,
for trip tokens, participant role. An ordinary API bearer token is rejected as a
hub credential. The server checks participant authorization when joining groups
and when handling messages. Broad driver fan-out carries refresh cues rather
than another user's offer/bid content.
Realtime is only an acceleration path; durable state and bounded resync recover
lost frames.

WebSocket negotiation may carry `access_token` in the query. Application request
logging, reverse proxy, OTel tags, and exception sanitization must remove it. An
automated test searches telemetry and error text for both the key and test token.

Chat sends use a client message ID/idempotency key so a lost response does not
duplicate a message. After persistence, SignalR fan-out should use durable work
or a service-lifetime token—not the HTTP request cancellation token.

## Mobile security is complementary

The app uses secure storage, platform biometrics/keystore, release signing,
bounded caches, and production permission gates. These controls protect a normal
device user and raise attacker cost. They do not authorize an API command.

The ordinary customer app exposes no proxy/server configuration UI and contains
no hidden trust-all-certificate switch. Network inspection belongs in managed
test infrastructure or a separately reviewed support build with a documented
scope. It must not be reachable through production user settings or silently
weaken certificate validation, wallet, or account-security traffic.

## Review checklist for a new mutation

- Stable versioned route and documented auth policy.
- Tenant/country and resource-owner checks in the query.
- Specific validator and field-level errors.
- Step-up if it changes security, contact, payout, or destructive state.
- Idempotency and expected entity version where retries/races matter.
- One local transaction with ledger/journal invariants where money moves.
- Durable outbox/audit side effects.
- Coarse Problem Details with correlation and security headers.
- No payload/token in logs, traces, metrics, or alerts.
- Positive, cross-user, cross-tenant, stale-state, duplicate, timeout, and
  malformed-input tests.
