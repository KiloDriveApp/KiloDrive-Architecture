# Capability Status and Evidence

## Why this page exists

A source file can prove that an adapter was written. It cannot prove that a
provider approved the account, credentials were deployed, the network path is
open, a canary succeeds, or an operator can recover the service. This page keeps
architecture claims honest by separating code capability from active operation.

The status is a reviewed source baseline, not a live production dashboard.
Operators use restricted deployment evidence and health systems for the latter.

## Review baseline and evidence anchors

- **Reviewed:** 2026-08-30
- **Public product baseline:** mobile `1.0.0+82`, Flutter `3.41.7` / Dart
  `3.11.5`, .NET `9`, MySQL `8`, schema-contract version `2026.08.30.1`
- **Evidence owners:** Architecture plus the named domain, Security, Quality,
  and Operations owners
- **Reviewed source revision and raw results:** retained in restricted release
  evidence; this public chapter records only the release-safe baseline above

“Implemented” rows were reviewed against these public-safe evidence families:

| Evidence key | Reviewed family |
| --- | --- |
| `SCHEMA` | Canonical empty bootstrap, EF relational metadata comparison, normalized control/cell fingerprint tests, startup/readiness contract |
| `IDENTITY` | Login/OTP/refresh/passkey/2FA/logout integration and cross-user authorization tests |
| `REALTIME` | Durable outbox contract/crash tests, entity-version merge races, and deterministic two-logical-client disconnect/reconnect tests; physical-device evidence is tracked separately |
| `GEO` | Synthetic coordinate, freshness, GEO eligibility, OSRM match, frontage-road/toll, and RideCheck trace tests |
| `MONEY` | Ledger property/concurrency/crash tests, fake-provider/disposable-MySQL webhook matrices, cashout/membership and daily reconciliation tests; live provider certification is separate |
| `UPLOAD` | Magic-byte, size, scanner timeout/reject/retry, quarantine authorization, re-encode, retention tests |
| `MOBILE` | Format/analyze/unit/widget/integration, localization parity, responsive render matrix, signed native artifact gates |
| `UX_STATE` | Typed loading/empty/error/partial state, interrupted-flow restoration, accessibility, cache-revision and lifecycle tests |
| `TEST_BOUNDARY` | Hermetic network/provider guards, deterministic fuzz seeds, non-user fixture manifests, allowlist and cleanup verification |
| `SAFETY` | Driver trust/eligibility, trip-share expiry/privacy, route-anomaly policy, SafetyCase state-machine, emergency-context and retention-metadata tests |
| `COMPLIANCE` | Country provision/activation, rule validation, schema drift block, privacy checkpoint and jurisdiction/financial operating-model review evidence |
| `OPERATIONS` | Implemented health/canary and recovery harnesses plus separately retained evidence for each actually executed alert, restore, or runbook exercise |

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

The matrix follows the doctrine's two axes:

- **Source maturity:** Implemented, Incremental, or Planned.
- **Deployment state:** Configurable, Uncertified, Certified, Active, or
  Unavailable.

Operational policy is named separately. A status cell may list both axes. When
it lists only source maturity, it makes no claim that a production deployment is
active or certified; when it lists a deployment condition, the evidence column
still governs the named release and country.

## Reviewed capability matrix

| Capability | Source maturity; deployment state | What the status means | Evidence required before saying “active” |
| --- | --- | --- | --- |
| Global identity control plane and country operational cells | Implemented | Authentication and global directory data are separated from country-local operational/financial graphs | Compiled model, canonical schema, cell/control fingerprints, startup/readiness and cross-cell tests |
| Typed registration intent and interrupted signup | Implemented | Role, country, contact method, driver account type and rental-organization choice travel as one immutable reviewed intent; API validation rejects contradictory combinations | Role/country/contact/social matrix, restart restoration, payload consistency and partial-projection reconciliation tests |
| Recent authentication and recoverable social linking | Implemented/configurable providers | Sensitive account changes require a short-lived proof of current account control; social collisions use a protected pending-link ceremony rather than email-only linking or a dead end | Password/linked-provider proof tests, replay/expiry/account-mismatch denial, Apple relay/nonce coverage and configured-provider device tests |
| Account-bound profile/contact/avatar state | Implemented/incremental | Profile/contact changes preserve typed state and revision-aware images invalidate account caches; older presentation slices remain under migration | Upload/revision/logout tests, contact partial states, relaunch and cross-account cache isolation |
| Country activation and jurisdiction controls | Implemented gates plus operational/legal approval | A country cannot become active until its shard and schema contract are ready; legal scope, provider approval, rules, owners, and evidence remain an accountable launch decision | Provision/fingerprint tests, signed country compliance register, rule versions, provider/counsel approvals, rollback and periodic review |
| Rider and driver safety foundations | Implemented/incremental and configurable operations | Trust preferences, eligibility checks, bounded trip sharing, route-deviation events, emergency context, and the SafetyCase state model exist; complete case participant authorization, attachment lifecycle, retention enforcement, detection evidence, and human response remain deployment or maturity boundaries | Two-client/device tests, noisy/offline trace fixtures, case authorization/evidence tests, emergency and escalation tabletop, access/retention review, responder SLA evidence |
| UUIDv7 transactional identifiers | Implemented/incremental | New exposed/security-sensitive transactional creation paths use the common RFC 9562 generator; stable catalogues retain business codes | Static creation-site policy and database/API round-trip tests |
| MySQL metadata contract | Implemented | Startup/readiness compares normalized table, column, index, and foreign-key expectations rather than trusting a version label alone | Empty bootstrap parity, clone alignment, all-cell fingerprints, exact binary version |
| Valkey cache, GEO, and SignalR backplane | Configurable production dependency | The distributed implementation exists; process-memory fallback is development-only | TLS/ACL command canaries, multi-node tests, latency/memory alarms, degradation exercise |
| SQL outbox | Implemented | Side-effect intent is committed with country business state and processed after HTTP completion | Producer/handler coverage, crash-point tests, lag/failure alarm and recovery runbook |
| EventBridge/SQS dispatch acceleration | Configurable | Hybrid broker path can scale fan-out while SQL remains recovery authority | Least-privilege publish/consume proof, queue/DLQ alarms, fallback and redrive exercise |
| SignalR realtime delivery | Implemented/configurable scale-out | Clients receive low-latency hints and reconcile authoritative state; multi-node operation depends on the backplane | Entity-version merge tests, disconnect/reconnect suite, backplane canary |
| Driver bidding-location readiness and active telemetry | Implemented/incremental and platform-configurable | The driver is not presented as ready for offers without permission and fresh telemetry; active-trip background behavior remains visible and lifecycle-scoped | Permission denial/recovery, stale lease, background/killed-state, notification/service-stop and two-device matching tests |
| Twelve-page driver onboarding and consolidated review | Implemented source; Uncertified end-to-end deployment | Server-derived progress restores the current page, an existing compliant vehicle satisfies vehicle setup, deferred background/address evidence has a deadline, and final submission creates one consolidated review case rather than per-upload onboarding tickets | Fresh/existing-driver, interruption/relaunch, 21-day lock, document quarantine/rejection, single-ticket, admin review, notification, deletion and two-device tests |
| Account-bound push installation ownership | Implemented source; Configurable FCM/APNs delivery | One provider token belongs to its latest authenticated user; atomic MySQL/SQLite upsert transfers a shared device without duplicate-key failure, logout deactivates the current binding, and token values stay out of logs | Concurrent login/switch/logout, token rotation, stale-owner delivery denial, reinstall/restore, FCM/APNs receipt and leak tests |
| Route alteration and telemetry-gap safety | Implemented/configurable operations | A requested route change is a versioned accept/reject lifecycle with durable distribution; prolonged missing telemetry creates a bounded safety signal rather than a fabricated date or location | Duplicate/stale version, disconnect/recycle, alert suppression/recovery, route/fare recomputation and noisy-telemetry tests |
| Google route/geocode provider adapters | Configurable | Server-side proxies support route/place operations without putting server keys in Flutter | Approved credentials, quota dashboard, warm/provider-stage metrics, synthetic route tests |
| OSRM table and map matching | Configurable/incremental | Road-network adapters support bounded matrix and trace matching; weak/unavailable results remain unverified | Regional data version, capacity, confidence fixtures, degradation/recovery proof |
| MySQL spatial route/toll projections | Incremental | Guarded services can use SRID 4326 bounding-box and precise distance queries; rollout is cell/schema dependent | Reviewed idempotent schema, spatial indexes, fingerprints, clone tests, certified routes |
| H3 geospatial indexing | Planned | H3 is documented as a possible coarse partition/aggregation tool, not current route proof | Separate ADR, library/resolution choice, comparison fixtures, privacy/retention review |
| Wallet subledger and double-entry journals | Implemented | Customer balance history and balanced accounting evidence are linked by canonical references | Property/crash/concurrency tests and zero unexplained daily reconciliation |
| External payment/store billing | Configurable | Signed verification, idempotent webhooks, entitlement and reconciliation paths exist by provider | Protected credentials, exact product mappings, sandbox matrix, notifications, settlement reconciliation |
| Live store/PSP/payout certification | Implemented testable boundaries; Uncertified per provider/release unless evidence says otherwise | Fake/disposable-provider tests prove application invariants but do not prove Apple, Google, a PSP, or payout provider accepted and reconciled the named release | Licensed store devices, sandbox/test-provider purchase/capture/refund/chargeback/return/reversal, crash points, signed webhook, settlement and zero-unreconciled-money evidence |
| Private object storage and quarantine | Implemented/configurable scanner | Objects remain private and untrusted uploads remain quarantined until a trusted clean disposition | Block-public-access/KMS/IAM proof, scanner timeout/reject/retry tests, authorized download audit |
| LiveKit/TURN voice | Configurable | Scoped token, call lifecycle, and mobile integration exist; network/media capacity is deployment-specific | TLS/UDP/TCP/TURN tests, two-device background/killed/handoff suite, capacity and cleanup evidence |
| LiveKit egress recording | Configurable and consent-gated | Recording can be requested only under explicit consent and jurisdiction/retention policy | Egress health, least-privilege encrypted object output, visible state, deletion/hold and audit exercise |
| FCM/APNs, SMS, WhatsApp, SES, AWS voice and LiveKit canaries | Configurable framework; certification provider-specific | Probe transports and sanitized status exist; AWS voice is opt-in, maintenance is deployment configuration, and provider acceptance is not delivery | Dedicated non-user destinations, authenticated delivery/inbound evidence producers, scheduled success/failure/maintenance, human alert and leak review |
| OpenTelemetry/ADOT and CloudWatch | Configurable | Instrumentation and collector/alarm assets exist; deployment determines active export | Collector health, known-test trace/metric, dashboard freshness, alarm notification and rollback |
| Passkeys and TOTP step-up | Implemented/configurable platform support | Server ceremonies and sensitive-boundary policy exist; clients/authenticators vary | Cross-node single-use ceremony tests, protected secret/key-ring proof, recent-auth boundary tests |
| Password hashing and migration | Implemented with a deployment profile | Argon2id is the normal password-storage profile; an explicit PBKDF2-HMAC-SHA256 profile exists only for an approved FIPS boundary, and successful verification can upgrade an older supported hash | Algorithm/config validation, bounded-parser and RFC-vector tests, capacity gate, legacy rehash test, protected configuration review |
| Scheduled-ride reservation and guarantee | Incremental source implementation; country activation/runtime certification required | A future request is not called guaranteed until a reserved eligible driver reconfirms before the cutoff; cancellation or ineligibility starts replacement search without creating a second ride | Accelerated-clock cutoff/reconfirmation/replacement/no-driver tests, delayed outbox recovery, country support/compensation policy, notification and time-driven runtime evidence |
| Multi-stop, round-trip, and hourly rides | Implemented/incremental client coverage | Stops are ordered lifecycle records, round trips retain the return leg, and hourly work snapshots the booked period/rate; exact country availability remains configurable | Quote/create parity, stop state/version races, wait-time and hourly settlement tests, current client render evidence |
| Driver professional toolkit | Implemented/incremental | Destination mode, service areas, availability, managed queues, goals, mileage, expenses, forecasts and projections have server and mobile foundations; forecasts remain non-authoritative | Country/timezone tests, queue expiry and active-assignment races, privacy-preserving forecast tests, statement/accounting reconciliation |
| Native managed queue leases | Implemented/incremental and country-policy-gated | An explicitly joined airport/venue queue is renewed by a short zone/lease-bound native location session, not screen lifetime; offline, assignment, zone exit or expiry closes it | Android/iOS background, killed-state, reboot, zone-exit, duplicate-join, clock-skew and privacy/store-policy certification |
| Family and business travel profiles | Implemented/incremental | Delegated booking, policy, notification and tracking permissions are capability-scoped; country and billing activation remain explicit | Invitation/revocation, cost-centre/policy, cross-member IDOR, billing and trip-share expiry tests |
| Supervised family communication and teen policy foundations | API/Flutter implemented incrementally and country/legal-gated; Portal planned | Guardian authority, consent evidence, scoped tracking/notifications and a distinct supervised conversation are modeled separately from the private rider-driver channel; Portal activation is not claimed | Age-boundary, consent/revocation, three-client authorization, Portal parity, safeguarding, retention and jurisdiction approval |
| Assisted-rider profile and matching | Implemented backend foundation; partial Flutter; Unavailable/Uncertified by default | Profile, protected caregiver contact, driver attestation, bounded backend snapshot and matching checks exist; offer/assigned-trip presentation, caregiver delivery, Portal and fail-closed client policy are incomplete | Signed-policy/kill-switch denial, offer/assigned-trip presentation, positive/negative two-device matching, caregiver delivery, accessibility, retention, Portal, privacy/legal/fairness and country activation |
| Marketplace intelligence | Implemented as advisory projections | Fare ranges, response windows, pickup probability and coarse demand cells are estimates; they never assign a driver or expose an individual rider location | Sparse-data confidence, cell suppression, stale-cache, no-provider and ordinary-feed independence tests |
| Typed trip distance provenance | Implemented/incremental presentation | Trip summaries carry validated-route, validated-telemetry, or unavailable provenance; unit conversion never invents legacy distance from fare | Completed/cancelled/legacy, telemetry-gap, km/miles, paging/backfill and API/Flutter/Portal parity tests |
| Courier chain of custody | Implemented/incremental and policy-gated | Declared parcels, pickup/recipient proof, custody events, failed delivery and return-to-sender are durable; optional protection and business shipping require country/provider approval | OTP/QR replay, evidence authorization, custody concurrency, failed/return lifecycle, escrow and reconciliation tests |
| Rental booking lifecycle | Implemented/incremental and provider-gated | Availability, quote, authorization, confirmation, check-in/out, evidence, extension, settlement and dispute foundations exist; deposit capture, insurance and adjudication depend on approved country/provider operations | Overlap and extension races, payment unknown outcomes, evidence scan/access, deposit/refund and dispute reconciliation |
| Two-sided reputation and imported history | Implemented/incremental | Verified-trip category feedback and reviewed third-party starting evidence are distinct; moderation, anti-retaliation and appeal controls remain operational responsibilities | One-review-per-party, delayed publication, manipulation/authorization, import evidence and appeal tests |
| Structured support and disputes | Incremental source; Configurable operations | Domain cases have human references, typed subjects, private evidence, messages, owner/SLA and conditional status; staffing and jurisdictional retention determine active service levels | Participant/admin authorization, attachment quarantine, reply/status races, SLA escalation and closure evidence |
| Canonical support client contract | Incremental source | API, Flutter and Portal presenters share Received, Reviewing, Waiting for information and Resolved semantics; legacy values map deterministically and unknown values remain neutral | Contract-version, migration, pagination, lifecycle, authorization, timezone and future-enum rendering tests |
| Allow-listed lifecycle webhooks | Implemented named-event source coverage; Configurable subscribers | Reviewed ride, bid, trip, rental, membership/store, safety and support event names stage durable minimal envelopes; this is not a claim that every internal transition is public, and support crosses control/cell through an idempotent relay | Versioned event catalogue, subscription authorization/signature, duplicate/out-of-order, destination outage, cleanup and deployment delivery evidence |
| Rider-controlled pickup confirmation | Implemented/configurable country override | When enabled, a random short-lived single-use PIN/signed-QR challenge is participant/trip/purpose-bound and digest-protected; emergency override is explicit and audited | Replay/cross-trip/brute-force/expiry/accessibility tests plus production-safe two-device and country-policy evidence |
| Durable wallet top-up status | Implemented/incremental | Payment ID plus idempotency key restore Pending, Completed, Failed or Needs attention across process death without implying that every payment product has equivalent recovery | Timeout-after-capture, delayed/duplicate/out-of-order webhook, account-switch, receipt/support and reconciliation tests |
| Multi-payer trip fare splitting | Implemented source candidate; Unavailable/Uncertified deployment | Immediate wallet code covers invitations, exact allocation, holds, settlement and cancellation release, but canonical `schema.sql` lacks the objects and client/server lifecycle gaps prevent a production claim | Bootstrap/alignment parity, mandatory version/stable retry, renewed consent after fare change, payer-insufficient-funds policy, expiry/audit/reconciliation, owner/Portal UI, reversal integration, country/PSP and two-client tests |
| Automated or instant payout | Implemented backend foundation; Dormant/Uncertified | Protected destinations, outbox initiation/reconciliation, callback outcomes and return/reversal accounting exist, but there is no supported certification activation and tenant-safe multi-country callback operation is not certified; **instant** is unavailable | Dual-controlled certification path, provider-owned destination proof, named least-privilege provider, tenant/country callback restoration, duplicate/out-of-order/unknown/crash tests, reconciliation, measured SLA and country activation |
| Typed System Admin trip investigation | Implemented/incremental | Investigation data is separated into safe typed sections with local-time/ISO-money presentation and independent partial states instead of raw payload traversal | Completed/cancelled/no-chat/no-call/no-replay, cross-country permission, step-up, partial API and rendered tests |
| System Administrator operational workspace | Implemented/incremental | Capability/country-scoped navigation, work queues, account security, audit search, restricted documents, investigation and outbox operations replace raw entity/payload handling slice by slice | Limited-admin menu parity, recent-auth/2FA boundaries, delta-refresh races, cross-country IDOR, retention and mobile/Portal parity tests |
| Promotional voucher batch issuance | Implemented | Administrative batches require request-hash-bound idempotency and a deterministic operation reference so an uncertain response cannot mint a second batch | Concurrent/replay/mismatch tests, protected replay body, HMAC lookup, batch/value/journal reconciliation |
| Release AOT privacy gates | Implemented release control | Release builds use reviewed Dart obfuscation/split-debug-info and scan archives for developer paths while symbols remain protected for crash diagnosis | Exact APK/AAB/IPA scan, symbol custody, negative fixture and clean-checkout CI evidence |
| Corporate website information architecture and SEO | Implemented/incremental localized content | Database-backed audience/safety/pricing/resource pages publish canonical, alternate, social and structured metadata; only reviewed English/Spanish/French content is claimed | Route/content/locale tests, sitemap/robots validation, structured-data and link checks, narrow/desktop rendered browser suite |
| Authenticated Portal role traversal | Incremental source; Uncertified until a named run supplies evidence | Typed clients, capability navigation, forms, anti-forgery and Playwright foundations exist; a reachable login page is not authenticated role/workflow certification | CI-secret-backed Rider/Driver/Rental/TenantAdmin/Limited System Administrator/System Administrator route, authorization, validation, CSP/console/network and cleanup evidence |
| iOS simulator and physical-device runtime | Implemented source; Uncertified until signed-device evidence exists | iOS code, entitlements and artifact gates exist, but source review or Android execution does not prove APNs, active-trip background location, CallKit/LiveKit, StoreKit, biometrics/passkeys, killed-state or network-handoff behavior | Approved simulator plus physical-device matrix, permission denial, background/killed recovery, signed IPA entitlement/privacy/private-selector scan and redacted artifacts |
| Tenant/country feature-readiness policy | Implemented/incremental registry and gates | Versioned rollout, kill, maintenance and dependency state controls routes and capable clients; schema/UI presence alone is not availability | Route/UI/docs parity, signed TTL cache, expiry/unknown fail-closed, percentage rollout, rollback and country launch evidence |
| Flutter repository/AsyncNotifier slices | Incremental | Network state is moving feature by feature behind public repositories with cancellation/version handling | Static dependency gate, race/disposal tests, no route/DTO drift, rendered state tests |
| Hermetic and fuzz regression boundaries | Implemented quality control | Ordinary tests fail closed against real external origins/providers; seeded form/property failures become stable regression fixtures | Clean-environment CI, explicit certification opt-in, seed replay, leak scan and cleanup evidence |
| Deterministic fixture coordinator | Implemented for disposable/local certification; Configurable CI execution | Role manifests, run-ID tagging, mutation allowlists and cleanup/reconciliation exist without making a logical two-client pass equal physical-device or production certification | CI-secret-backed full role matrix, allowlist ledger, positive/negative/IDOR/concurrency run, finally cleanup, offline drivers, reconciled money and sanitized evidence |
| Horizontal API scale-out | Architecturally supported, operationally gated | Stateless request handling can scale after every shared-state prerequisite is proven | Shared Data Protection, distributed ceremonies/cache/backplane, consistent config/JWKS, crash/failover exercise |
| Production-shaped capacity and disaster recovery | Implemented harnesses; Uncertified operating envelope | Low-rate health or one logical load run is not a capacity, failover, RPO or RTO claim | Production-shaped staging ramps/soak, per-stage warm/provider metrics, reconnect storm, database/Valkey/backplane loss, PITR/restore/key recovery, reconciliation and cleanup evidence |

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
- [System Administration](system-administration.md)
- [Scaling and capacity](scaling-and-capacity.md)
- [Public documentation policy](../governance/public-documentation-policy.md)
- [Third-party and SBOM policy](../third-party/README.md)
- [Runbook index](../runbooks/README.md)
