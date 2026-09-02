# Runtime Boundaries and Certification

KiloDrive can be correct in source and still fail at a runtime boundary. A
controller may have an authorization attribute while a public compatibility
route bypasses normal tenant resolution. A mobile repository may parse a typed
model while a large screen still coordinates six unrelated requests. A ride
acceptance may commit correctly while SignalR loses the event that should make
it visible to the other phone.

This chapter connects those concerns. It describes the target architecture for
anonymous tenant selection, public endpoints, hardened responses, typed client
state, operational work queues, negotiated fares, realtime recovery, and
capacity evidence.

> **Status note:** this is architecture doctrine and a certification standard.
> It does not claim that every production deployment has completed every gate.
> The private release record must identify what is implemented, configured,
> runtime-certified, active, or blocked for each country and provider.

## Why these boundaries belong together

The following failures often appear unrelated:

- one tenant's public content appears under another brand;
- a `429` response becomes a Portal `500` because a view expected success JSON;
- a driver sees an older bid after reconnecting;
- a refresh hides a successful wallet card because an optional provider failed;
- a load test reports a healthy average while MySQL lock waits climb; and
- an exception path loses security headers after clearing the response.

They share one cause: an implicit boundary was allowed to carry more authority
than it should. The remedy is to make authority, ownership, version, failure
state, and certification evidence explicit.

## Anonymous tenant and brand resolution

An authenticated request derives its permitted tenant and country workspace
from signed identity claims plus authorized workspace selection. An anonymous
request does not have that proof. A caller-provided `X-Tenant` header is
therefore routing input, not authority.

The target production boundary uses either:

1. a canonical host-to-tenant mapping verified after the trusted proxy has
   normalized the request; or
2. a short-lived signed tenant/brand token bound to issuer, audience, tenant,
   purpose, issued time, expiry, key identifier, and policy version.

If host, token, authenticated identity, resource token, or provider-owned
mapping disagree, the request is rejected. The application must not silently
pick whichever value is most convenient.

### Transitional `X-Tenant` handling

Where compatibility still requires `X-Tenant`, it must be accepted only from a
trusted and authenticated proxy boundary. The edge strips the public header,
adds its verified internal routing value, and forwards the actual client IP
through the separately reviewed proxy contract. The API records a sanitized
deprecation event and an owner/date for removal.

This transition is deliberately narrow. New anonymous features do not copy the
header pattern.

### Tenant-less routes

Some routes genuinely begin without application tenant context. A payment or
messaging provider webhook is the clearest example. That does not make the
request untrusted by design; it changes the authentication substitute:

1. verify the provider signature over the exact raw request according to the
   provider contract;
2. enforce timestamp/replay rules;
3. locate the internal payment, delivery, or provider registration using a
   server-owned opaque reference;
4. restore tenant scope from that stored record; and
5. process the event idempotently.

A tenant value in the body, query string, or public header never substitutes
for these steps.

### Public sharing and tracking

Public share and tracking links use opaque or signed capabilities rather than
guessable database identifiers. A capability is bound to one resource, tenant,
purpose, audience where appropriate, privacy scope, expiry, and revocation
state. Tracking returns only the detail required by the approved product and
country policy. High-frequency polling is rate-limited and cache keys include
the verified authorization substitute and policy version.

Revocation and expiry fail closed. Errors remain coarse enough that an attacker
cannot enumerate whether a trip, person, document, or tenant exists.

## The anonymous-endpoint registry

`AllowAnonymous` is a source-code mechanism, not a security design. KiloDrive
maintains a machine-readable policy registry generated and checked against
runtime endpoint metadata.

Every anonymous route and HTTP method records:

| Field | Why it matters |
| --- | --- |
| Owner and feature | Someone must review and retire the exception |
| Business purpose | “Public” is not a purpose |
| Tenant rule | Verified host, signed context, restored provider mapping, or explicitly tenant-less |
| Authentication substitute | Signature, opaque token, public catalogue policy, or other reviewed proof |
| Resource binding | Prevents a valid token being moved to another object |
| Expiry, replay, and revocation | Limits stolen or repeated capabilities |
| Rate-limit partition | Defines whose activity consumes the budget |
| Body and content-type limits | Prevents anonymous resource exhaustion |
| Cache policy | Prevents cross-tenant or cross-token cache reuse |
| Privacy and logging policy | Defines what may be returned or recorded |
| Negative tests | Makes the policy executable |
| Review expiry | Prevents temporary exceptions becoming permanent folklore |

Continuous integration fails when endpoint metadata and this registry disagree.
A new anonymous route without a reviewed record is a build failure. So is a
route whose declared signature, tenant, rate-limit, or request-size control is
missing at runtime.

OpenAPI is checked independently: anonymous operations must not inherit bearer
security, and protected operations must not lose it.

## Hardened responses on every path

Security headers and correlation evidence are response invariants, not happy-
path decoration. A shared response-hardening component applies the relevant
policy to successful responses and to failures produced by validation,
authentication, authorization, tenant resolution, rate limiting, concurrency,
domain exceptions, and unexpected exceptions.

The correlation identifier is validated or generated early and retained before
any middleware clears a partial response. After `Response.Clear()`, the helper
reapplies the identifier and required headers before writing sanitized Problem
Details.

The policy includes, where appropriate:

- `X-Correlation-ID`;
- HTTP Strict Transport Security;
- `X-Content-Type-Options: nosniff`;
- frame protection;
- `Referrer-Policy`;
- the reviewed Content Security Policy;
- safe cache controls; and
- `Retry-After` for bounded retry responses.

An error response never includes an exception message, stack trace, SQL,
authorization header, cookie, token, request body, provider payload, object
storage path, or unnecessary personal data. The correlation identifier joins
restricted evidence without turning the public response into a diagnostic dump.

Streaming and attachment routes need special care: headers must be established
before the body begins, and middleware must not attempt to clear an already
committed stream.

## Typed mobile slices and small composition surfaces

The mobile architecture separates four responsibilities:

```text
private transport adapter -> public repository interface
                          -> immutable view model
                          -> AutoDisposeAsyncNotifier
                          -> focused feature widget
```

Dynamic maps may exist inside a private decoder because JSON is dynamic on the
wire. They do not cross into public repositories, state notifiers, or widgets.
Transport errors become typed application failures with safe operation and
correlation context.

Each independently useful card or tab owns its state. It distinguishes initial
loading, successful empty, successful data, refresh with last-good data,
partial failure, whole-slice failure, mutation progress, conflict, and unknown
mutation outcome.

Cancellation stops genuinely superseded reads. Where a network stack cannot
cancel delivery, a request generation prevents a disposed or older response
from publishing. Realtime data merges only when its persisted server revision
is newer than the current model.

### Composition-file limits

A route shell may own layout, navigation, and coordination between feature
widgets. It must not become the repository, state machine, form controller, and
realtime client for the whole workflow.

The repository uses a reviewable composition-size and complexity gate. An
exception records an owner, rationale, expiry date, extraction plan, and test
evidence. The limit is a warning about ownership—not an invitation to split one
giant class into arbitrary partial files.

An extraction is useful only when the new widget has:

- a narrow state dependency;
- one clear behavior boundary;
- isolated rendered and interaction tests;
- stable route and deep-link behavior; and
- measured rebuild and frame-cost evidence.

## Typed Portal contracts

The Portal is server-rendered, but it is still an API client. Razor views do not
walk `JsonElement`, assume optional properties exist, or interpret arbitrary
dictionaries.

A reviewed or generated client owns serialization, optional fields, enum
mapping, Problem Details, correlation IDs, timestamps, ISO currency, and
revision/ETag metadata. Controllers map typed application results to typed view
models. Views render those models and submit anti-forgery-protected forms.

This prevents a predictable failure pattern: the API correctly returns a
`401`, `409`, `429`, or sanitized `500`, then the Portal throws because it tries
to read a property from a success payload that is not there.

Critical route tests cover successful data, successful empty results, missing
optional fields, authentication expiry, authorization denial, validation,
conflict, rate limiting with `Retry-After`, and sanitized server failures. They
also assert that raw payloads, internal identifiers, secrets, and bare numeric
enums do not appear in rendered HTML.

## Operational work queues

Entity directories answer “what records exist?” Operators usually need a
different answer: “what needs attention next?”

The System Administrator dashboard therefore presents country- and capability-
scoped work queues for verification, safety SLA breaches, financial mismatch,
cashout approval, provider health, outbox failure, scheduled-ride risk, rental
disputes, compliance expiry, and overdue support work.

Each queue item provides:

- a safe case/reference number;
- country and authorized workspace;
- owner or assignee;
- age, severity, SLA, and breach state;
- the next action;
- required capability and recent step-up state;
- persisted revision; and
- an audited navigation target.

Counts and list queries share the same tenant, country, retention, and
eligibility predicates. If policy intentionally hides an older record, the
summary says so instead of falsely reporting an empty archive.

Queues load independently. One failed provider query cannot erase successful
verification or finance queues. Background refresh advertises new items and
does not reorder the row an operator is investigating. Visual merging pauses
while an editor or confirmation is active.

## Negotiated-fare truth

KiloDrive's negotiation model needs more evidence than a conventional fixed-
fare accept button. The system distinguishes:

1. the immutable system quote and pricing-policy version;
2. the rider's current offer and revision;
3. each driver's proposed or accepted amount and revision;
4. the accepted fare and vehicle/compliance snapshot; and
5. the final payment, receipt, distance, duration, and provenance.

Availability probability and response time are advisory. Their typed contract
includes a range, confidence, sample sufficiency, freshness, expiry, source or
model version, and an honest non-guarantee label. Sparse data produces wider
uncertainty, not false precision.

The server owns offer expiry. Clients may animate a countdown, but they
revalidate current state and revision before a mutation. Create, fare change,
bid, withdraw, replacement, reject, accept, cancel, and chat commands are
idempotent and conditional where their contract exposes mutable state.

A rider's fare change never silently rewrites a driver's earlier consent. The
bid expires or requires explicit reconfirmation according to policy.

Acceptance rechecks online lease freshness, duty, active assignments,
membership, trust level, identity, selected vehicle, and full compliance inside
the locked transaction. The trip snapshots the accepted vehicle and compliance
version so a later vehicle edit cannot rewrite history.

Completion distance and duration come from retained, validated route or
telemetry evidence with quality/provenance metadata. A bounded manual override
requires authority, reason, and audit. Fare is never reverse-engineered into a
distance.

## Two-client recovery certification

A useful ride test has two independently stateful clients. The certification
flow covers quote, create, fare change, bid, withdraw, replacement, reject or
accept, chat, arrive, start, active telemetry, complete or cancel, and review.

After every transition, the Rider UI, Driver UI, REST resource, SignalR stream,
MySQL aggregate, audit, outbox, and financial records must agree.

Failure injection includes:

- duplicate taps and a lost response after commit;
- stale, duplicate, delayed, and out-of-order versions;
- SignalR disconnect and group rejoin;
- Valkey/backplane loss and restoration;
- API process recycle;
- mobile background, process death, and cold restoration;
- offline chat and telemetry replay;
- token refresh during an active trip; and
- stale location leading to an explicit telemetry-gap safety state.

In-process tests make the races deterministic. They are not enough to certify a
multi-node backplane, Android foreground location, iOS background behavior, or
OS process restoration. Those boundaries require emulator/simulator and
approved physical-device evidence in a production-shaped environment.

## Capacity, soak, memory, and query plans

Capacity is a measured operating envelope for a deployment, dataset, and
workload. It is not a permanent marketing number.

Production-shaped staging includes multiple stateless API nodes,
production-equivalent MySQL cells, Valkey and SignalR scale-out, routing
dependencies or faithful simulators, durable workers, provider fakes, and the
same proxy/readiness/telemetry behavior used in production.

Controlled ramps begin at one pair, then 10, 25, 50, and 100. Larger stages such
as 500 and 2,000 pairs proceed only after smaller integrity gates pass and the
load generators themselves have proven headroom. A multi-hour soak crosses
token refresh, cache expiry, connection recycling, outbox lease, and worker
schedule boundaries.

Measurements separate warm application time from database, serialization,
maps/routing, provider, and queue time. The record includes p50/p95/p99,
throughput, classified 4xx, 5xx, CPU, memory, garbage collection, connection
pools, MySQL waits/locks, Valkey latency/evictions, SignalR reconnects, and
outbox age.

Release-mode mobile memory testing repeatedly traverses maps, image lists,
document previews, chat, rentals, administrative lists, and account switching.
It records process PSS, Dart/native heaps, graphics, image caches, platform
views, and live controllers/subscriptions before, during, and after collection.
The gate detects statistically significant retained growth across cycles rather
than failing on one noisy reading.

Representative database queries use bounded `EXPLAIN ANALYZE` on disposable
clones or approved staging data. Index decisions record actual and estimated
rows, chosen access path, sort/temp-table behavior, latency, write cost, and
rollback DDL. No index, foreign key, unique constraint, or financial invariant
is removed simply because a development table is empty.

## Release evidence and stop conditions

A release record for these boundaries includes:

- the anonymous-route registry comparison;
- response-header/error-path assertions;
- typed dependency and composition-gate results;
- Portal contract/render tests;
- two-client version and recovery timeline;
- Android/iOS runtime evidence;
- capacity and soak charts;
- memory-retention analysis;
- database query-plan decisions;
- fixture cleanup and financial reconciliation; and
- sanitized correlation identifiers for failures and recovery.

Stop the release for cross-tenant confusion, an undocumented anonymous route,
missing security headers on an error path, sensitive response leakage, stale or
cross-account client state, a state regression after reconnect, duplicate
business effects, unreconciled money, unbounded retained memory, schema drift,
or an unclassified server error.

## Related reading

- [API architecture](api.md)
- [Tenancy and country cells](tenancy-and-country-cells.md)
- [Mobile architecture](mobile.md)
- [Portal and website architecture](portal-and-website.md)
- [System Administration architecture](system-administration.md)
- [Marketplace product lifecycles](marketplace-product-lifecycles.md)
- [Scaling and capacity](scaling-and-capacity.md)
- [Threat boundaries](../security/threat-boundaries.md)
- [Testing and verification](../quality/testing-and-verification.md)
