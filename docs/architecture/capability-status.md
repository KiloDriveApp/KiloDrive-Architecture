# Capability Status and Evidence

## Why this page exists

A source file can prove that an adapter was written. It cannot prove that a
provider approved the account, credentials were deployed, the network path is
open, a canary succeeds, or an operator can recover the service. This page keeps
architecture claims honest by separating code capability from active operation.

The status is a reviewed source baseline, not a live production dashboard.
Operators use restricted deployment evidence and health systems for the latter.

## Review baseline and evidence anchors

- **Reviewed:** 2026-08-24
- **Public product baseline:** mobile `1.0.0+70`, Flutter `3.41.7` / Dart
  `3.11.5`, .NET `9`, MySQL `8`, schema-contract version `2026.08.24.10`
- **Evidence owners:** Architecture plus the named domain, Security, Quality,
  and Operations owners
- **Private source revision and raw results:** retained in restricted release
  evidence rather than publishing an inaccessible private-repository identifier

“Implemented” rows were reviewed against these public-safe evidence families:

| Evidence key | Reviewed family |
| --- | --- |
| `SCHEMA` | Canonical empty bootstrap, EF relational metadata comparison, normalized control/cell fingerprint tests, startup/readiness contract |
| `IDENTITY` | Login/OTP/refresh/passkey/2FA/logout integration and cross-user authorization tests |
| `REALTIME` | Durable outbox contract/crash tests, entity-version merge races, two-client disconnect/reconnect lifecycle tests |
| `GEO` | Synthetic coordinate, freshness, GEO eligibility, OSRM match, frontage-road/toll, and RideCheck trace tests |
| `MONEY` | Ledger property/concurrency/crash tests, provider webhook matrix, cashout/membership and daily reconciliation tests |
| `UPLOAD` | Magic-byte, size, scanner timeout/reject/retry, quarantine authorization, re-encode, retention tests |
| `MOBILE` | Format/analyze/unit/widget/integration, localization parity, responsive render matrix, signed native artifact gates |
| `SAFETY` | Driver trust/eligibility, trip-share expiry/privacy, route-anomaly policy, SafetyCase state-machine, emergency-context and retention-metadata tests |
| `COMPLIANCE` | Country provision/activation, rule validation, schema drift block, privacy checkpoint and jurisdiction/financial operating-model review evidence |
| `OPERATIONS` | Health/canary, controlled failure/recovery, alert delivery, restore, and runbook exercise evidence |

The matrix's final column says what must be present for a deployment claim. The
evidence keys above say what supported the source-level status. A new review
updates this date, version baseline, status row, and affected ADR; changing the
word without new evidence is not acceptable.

The evidence families are governed by
[Testing and verification](../quality/testing-and-verification.md). That guide
defines what each category means, which high-risk invariants require direct
evidence, and why a test count or one coverage percentage cannot change a
capability claim by itself.

## Status terms

- **Implemented** — the core behavior is represented in code/schema and has
  focused verification.
- **Configurable** — an implemented adapter or path needs approved deployment
  configuration, credentials, infrastructure, provider status, or policy.
- **Operational policy** — the control depends on a human/automated procedure
  and retained evidence, not only code.
- **Incremental** — the chosen direction is active in named slices while a
  compatibility path remains.
- **Planned** — design option only; do not present it as a shipped capability.

## Reviewed capability matrix

| Capability | Status | What the status means | Evidence required before saying “active” |
| --- | --- | --- | --- |
| Global identity control plane and country operational cells | Implemented | Authentication and global directory data are separated from country-local operational/financial graphs | Compiled model, canonical schema, cell/control fingerprints, startup/readiness and cross-cell tests |
| Country activation and jurisdiction controls | Implemented gates plus operational/legal approval | A country cannot become active until its shard and schema contract are ready; legal scope, provider approval, rules, owners, and evidence remain an accountable launch decision | Provision/fingerprint tests, signed country compliance register, rule versions, provider/counsel approvals, rollback and periodic review |
| Rider and driver safety foundations | Implemented/incremental and configurable operations | Trust preferences, eligibility checks, bounded trip sharing, route-deviation events, emergency context, and the SafetyCase state model exist; complete case participant authorization, attachment lifecycle, retention enforcement, detection evidence, and human response remain deployment or maturity boundaries | Two-client/device tests, noisy/offline trace fixtures, case authorization/evidence tests, emergency and escalation tabletop, access/retention review, responder SLA evidence |
| UUIDv7 transactional identifiers | Implemented/incremental | New exposed/security-sensitive transactional creation paths use the common RFC 9562 generator; stable catalogues retain business codes | Static creation-site policy and database/API round-trip tests |
| MySQL metadata contract | Implemented | Startup/readiness compares normalized table, column, index, and foreign-key expectations rather than trusting a version label alone | Empty bootstrap parity, clone alignment, all-cell fingerprints, exact binary version |
| Valkey cache, GEO, and SignalR backplane | Configurable production dependency | The distributed implementation exists; process-memory fallback is development-only | TLS/ACL command canaries, multi-node tests, latency/memory alarms, degradation exercise |
| SQL outbox | Implemented | Side-effect intent is committed with country business state and processed after HTTP completion | Producer/handler coverage, crash-point tests, lag/failure alarm and recovery runbook |
| EventBridge/SQS dispatch acceleration | Configurable | Hybrid broker path can scale fan-out while SQL remains recovery authority | Least-privilege publish/consume proof, queue/DLQ alarms, fallback and redrive exercise |
| SignalR realtime delivery | Implemented/configurable scale-out | Clients receive low-latency hints and reconcile authoritative state; multi-node operation depends on the backplane | Entity-version merge tests, disconnect/reconnect suite, backplane canary |
| Google route/geocode provider adapters | Configurable | Server-side proxies support route/place operations without putting server keys in Flutter | Approved credentials, quota dashboard, warm/provider-stage metrics, synthetic route tests |
| OSRM table and map matching | Configurable/incremental | Road-network adapters support bounded matrix and trace matching; weak/unavailable results remain unverified | Regional data version, capacity, confidence fixtures, degradation/recovery proof |
| MySQL spatial route/toll projections | Incremental | Guarded services can use SRID 4326 bounding-box and precise distance queries; rollout is cell/schema dependent | Reviewed idempotent schema, spatial indexes, fingerprints, clone tests, certified routes |
| H3 geospatial indexing | Planned | H3 is documented as a possible coarse partition/aggregation tool, not current route proof | Separate ADR, library/resolution choice, comparison fixtures, privacy/retention review |
| Wallet subledger and double-entry journals | Implemented | Customer balance history and balanced accounting evidence are linked by canonical references | Property/crash/concurrency tests and zero unexplained daily reconciliation |
| External payment/store billing | Configurable | Signed verification, idempotent webhooks, entitlement and reconciliation paths exist by provider | Protected credentials, exact product mappings, sandbox matrix, notifications, settlement reconciliation |
| Private object storage and quarantine | Implemented/configurable scanner | Objects remain private and untrusted uploads remain quarantined until a trusted clean disposition | Block-public-access/KMS/IAM proof, scanner timeout/reject/retry tests, authorized download audit |
| LiveKit/TURN voice | Configurable | Scoped token, call lifecycle, and mobile integration exist; network/media capacity is deployment-specific | TLS/UDP/TCP/TURN tests, two-device background/killed/handoff suite, capacity and cleanup evidence |
| LiveKit egress recording | Configurable and consent-gated | Recording can be requested only under explicit consent and jurisdiction/retention policy | Egress health, least-privilege encrypted object output, visible state, deletion/hold and audit exercise |
| FCM/APNs, SMS, WhatsApp, SES canaries | Configurable | Probe framework exists but must use dedicated non-user destinations and protected credentials | Scheduled success/failure/maintenance tests, confirmed human alert destination, sanitized storage review |
| OpenTelemetry/ADOT and CloudWatch | Configurable | Instrumentation and collector/alarm assets exist; deployment determines active export | Collector health, known-test trace/metric, dashboard freshness, alarm notification and rollback |
| Passkeys and TOTP step-up | Implemented/configurable platform support | Server ceremonies and sensitive-boundary policy exist; clients/authenticators vary | Cross-node single-use ceremony tests, protected secret/key-ring proof, recent-auth boundary tests |
| Password hashing and migration | Implemented with a deployment profile | Argon2id is the normal password-storage profile; an explicit PBKDF2-HMAC-SHA256 profile exists only for an approved FIPS boundary, and successful verification can upgrade an older supported hash | Algorithm/config validation, bounded-parser and RFC-vector tests, capacity gate, legacy rehash test, protected configuration review |
| Scheduled-ride reservation and guarantee | Implemented with country-configured timing | A future request is not called guaranteed until a reserved eligible driver reconfirms before the cutoff; cancellation or ineligibility starts replacement search without creating a second ride | Cutoff/reconfirmation/replacement races, two-client lifecycle, delayed outbox recovery, country policy and notification evidence |
| Multi-stop, round-trip, and hourly rides | Implemented/incremental client coverage | Stops are ordered lifecycle records, round trips retain the return leg, and hourly work snapshots the booked period/rate; exact country availability remains configurable | Quote/create parity, stop state/version races, wait-time and hourly settlement tests, current client render evidence |
| Driver professional toolkit | Implemented/incremental | Destination mode, service areas, availability, managed queues, goals, mileage, expenses, forecasts and projections have server and mobile foundations; forecasts remain non-authoritative | Country/timezone tests, queue expiry and active-assignment races, privacy-preserving forecast tests, statement/accounting reconciliation |
| Family and business travel profiles | Implemented/incremental | Delegated booking, policy, notification and tracking permissions are capability-scoped; country and billing activation remain explicit | Invitation/revocation, cost-centre/policy, cross-member IDOR, billing and trip-share expiry tests |
| Marketplace intelligence | Implemented as advisory projections | Fare ranges, response windows, pickup probability and coarse demand cells are estimates; they never assign a driver or expose an individual rider location | Sparse-data confidence, cell suppression, stale-cache, no-provider and ordinary-feed independence tests |
| Courier chain of custody | Implemented/incremental and policy-gated | Declared parcels, pickup/recipient proof, custody events, failed delivery and return-to-sender are durable; optional protection and business shipping require country/provider approval | OTP/QR replay, evidence authorization, custody concurrency, failed/return lifecycle, escrow and reconciliation tests |
| Rental booking lifecycle | Implemented/incremental and provider-gated | Availability, quote, authorization, confirmation, check-in/out, evidence, extension, settlement and dispute foundations exist; deposit capture, insurance and adjudication depend on approved country/provider operations | Overlap and extension races, payment unknown outcomes, evidence scan/access, deposit/refund and dispute reconciliation |
| Two-sided reputation and imported history | Implemented/incremental | Verified-trip category feedback and reviewed third-party starting evidence are distinct; moderation, anti-retaliation and appeal controls remain operational responsibilities | One-review-per-party, delayed publication, manipulation/authorization, import evidence and appeal tests |
| Structured support and disputes | Implemented/incremental operations | Cases have human references, typed subjects, private evidence, messages, owner/SLA and conditional status; staffing and jurisdictional retention determine active service levels | Participant/admin authorization, attachment quarantine, reply/status races, SLA escalation and closure evidence |
| Promotional voucher batch issuance | Implemented | Administrative batches require request-hash-bound idempotency and a deterministic operation reference so an uncertain response cannot mint a second batch | Concurrent/replay/mismatch tests, protected replay body, HMAC lookup, batch/value/journal reconciliation |
| Release AOT privacy gates | Implemented release control | Release builds use reviewed Dart obfuscation/split-debug-info and scan archives for developer paths while symbols remain protected for crash diagnosis | Exact APK/AAB/IPA scan, symbol custody, negative fixture and clean-checkout CI evidence |
| Corporate website information architecture and SEO | Implemented/incremental localized content | Database-backed audience/safety/pricing/resource pages publish canonical, alternate, social and structured metadata; only reviewed English/Spanish/French content is claimed | Route/content/locale tests, sitemap/robots validation, structured-data and link checks, narrow/desktop rendered browser suite |
| Flutter repository/AsyncNotifier slices | Incremental | Network state is moving feature by feature behind public repositories with cancellation/version handling | Static dependency gate, race/disposal tests, no route/DTO drift, rendered state tests |
| Horizontal API scale-out | Architecturally supported, operationally gated | Stateless request handling can scale after every shared-state prerequisite is proven | Shared Data Protection, distributed ceremonies/cache/backplane, consistent config/JWKS, crash/failover exercise |

## How to change a status

A pull request does not change **Configurable** to **active** merely by adding a
setting. The capability owner gathers deployment evidence:

1. identify the exact binary, schema, configuration revision, and country;
2. prove the protected credential and least-privilege policy without printing
   either;
3. exercise success, timeout, denial, duplicate, and recovery paths with a
   dedicated fixture;
4. prove health, metrics, alarms, human notification, and runbook accuracy;
5. confirm privacy, retention, provider terms, and country policy; and
6. record owner, review date, rollback, and evidence index in the restricted
   operational system.

The public page may then say the capability is available in the reviewed
release family. It still should not publish account, host, destination, or
defensive details.

## Claims that should trigger review

Be suspicious when documentation says:

- “enabled everywhere” for a country- or provider-gated feature;
- “real time” without a durable recovery path;
- “encrypted” without naming the boundary and key owner;
- “exactly once” for a distributed provider delivery;
- “fully compliant” without jurisdiction and evidence scope;
- “supports unlimited scale” without a measured operating envelope; or
- “the latest version” without an exact reviewed baseline.

Replace the claim with a control, limitation, and verification method.

## Related reading

- [Testing and verification](../quality/testing-and-verification.md)
- [System context](system-context.md)
- [Rider and driver safety](rider-driver-safety.md)
- [Jurisdictional compliance](jurisdictional-compliance.md)
- [Scaling and capacity](scaling-and-capacity.md)
- [Public documentation policy](../governance/public-documentation-policy.md)
- [Third-party and SBOM policy](../third-party/README.md)
- [Runbook index](../runbooks/README.md)
