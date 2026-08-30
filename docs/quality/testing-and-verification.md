# Testing and verification

- **Owner:** Quality engineering with domain, security, mobile, data, and
  operations owners
- **Status:** Engineering and release policy
- **Applies to:** API, mobile, portal, website, database, workers, providers,
  realtime, safety, and financial workflows
- **Related material:** [Capability status](../architecture/capability-status.md),
  [API deployment](../runbooks/api-deployment.md), and
  [mobile release](../runbooks/mobile-release.md)

## Why this guide exists

KiloDrive has a large automated test suite, but test count is not the same as
confidence. Ten tests that repeat one happy path may protect less than one
carefully designed race test. A controller test can return `200` while the
wallet journal is unbalanced. A widget can render perfectly while a copied
refresh token remains valid after logout.

This guide explains how KiloDrive decides that verification is proportionate
to risk. It describes the boundaries each test family protects, the invariants
that must remain true, and the evidence needed before a change is called
release-ready. It deliberately does not publish private test names, fixture
credentials, production identifiers, internal endpoints, or defensive
thresholds.

The central rule is straightforward:

> Test the business promise at the lowest useful level, then test the real
> boundaries that could invalidate that promise.

For example, a pure property test can prove that debits equal credits over many
generated amounts. It cannot prove MySQL row locks behave correctly when two
requests race. A real-database test covers that second boundary. A provider
sandbox test then covers signature, schema, and unknown-outcome behavior. All
three are necessary for a financial feature; none is a substitute for the
others.

## Test taxonomy

We use the following terms consistently.

| Test family | What it isolates | Typical purpose | What it must not pretend to prove |
| --- | --- | --- | --- |
| Unit test | One deterministic rule or small group of pure collaborators | Calculations, policies, validators, state transitions, formatting | Database, framework, network, or provider behavior |
| Property test | A rule over many generated inputs and operation sequences | Money conservation, idempotency, bounds, serialization round trips | Production traffic shape or provider correctness |
| Component test | One assembled subsystem with controlled external boundaries | Handler plus validation, a worker, notification rendering, cache policy | Full cross-process behavior |
| Repository test | Data access against the supported database or a faithful boundary fake | Query filters, indexes, locking, pagination, version merges | End-to-end authorization unless the HTTP boundary is included |
| Contract test | A producer/consumer or artifact agreement | OpenAPI, DTO shape, enum values, headers, store-product mapping | Business correctness behind the contract |
| Integration test | Multiple real application layers and selected real infrastructure | HTTP, authentication, MySQL transactions, outbox, object storage adapter | Physical-device or live-provider behavior unless explicitly included |
| Concurrency test | Deliberately overlapping operations | Single-winner acceptance, duplicate webhook/cashout, token rotation | Long-term capacity by itself |
| Failure-injection test | A known failure inserted at a specific boundary | Unknown result, rollback, retry, reconciliation, crash recovery | Random chaos without a hypothesis |
| Security regression test | A previously unsafe action reproduced and denied | IDOR, token replay, exported component abuse, step-up bypass | A complete penetration test |
| Flutter model/provider test | Mobile parsing and state behavior without a rendered screen | Cancellation, generations, version merge, offline state | Layout, accessibility, or native plugin behavior |
| Flutter widget/render test | A rendered interaction under controlled dimensions and state | Overflow, semantics, keyboard/inset, loading/error/empty states | Real device permissions, lifecycle, or provider SDK behavior |
| End-to-end test | A user journey across real application boundaries with controlled fixtures | Rider/driver lifecycle, rental booking, support case, settlement | Unbounded production load or every provider failure |
| Operational exercise | A controlled recovery procedure with monitors and owners present | Restore, provider outage, queue redrive, key rotation, failover | Continuous correctness after the exercise window |

Names matter because they stop evidence from being overstated. A test using an
in-memory database is not a MySQL concurrency test. A mocked payment response is
not provider certification. An emulator screenshot is not an iOS background
location test.

## What normally requires a unit test

Deterministic business logic should not depend solely on broad integration
tests. Unit or property coverage is normally required for:

- fare, fee, tax, toll, commission, refund, proration, exchange-rate, and
  withdrawal calculations;
- driver/rider/vehicle eligibility, membership limits, trust rules, duty
  windows, and country rules;
- ride, bid, trip, delivery, rental, support, verification, cashout, payment,
  SafetyCase, and deletion state transitions;
- authorization and step-up policies that can be expressed without transport;
- retention, legal-hold, evidence-release, and data-minimization decisions;
- idempotency, replay, deduplication, monotonic-version, and retry decisions;
- route anomaly classification, telemetry freshness, GPS quality, and
  confidence thresholds;
- validation, normalization, Unicode, date/time, currency, and serialization
  rules; and
- notification routing and redaction decisions.

Keep the policy pure when possible. A state machine is easier to test and
review when the allowed transitions are not hidden among database writes,
provider calls, and UI code.

## Risk-based expectations

KiloDrive does not use one repository-wide percentage as the definition of
quality. Aggregate line and branch coverage can reveal an unexpected drop, but
it cannot show that the important assertions exist.

The strongest expectations apply to:

- money movement and accounting;
- authentication, authorization, identity, and account recovery;
- driver/rider safety and emergency handling;
- trip, delivery, and rental lifecycle transitions;
- private documents, call recordings, and deletion/retention;
- country/tenant isolation; and
- irreversible or externally visible provider operations.

For these areas, reviewers expect boundary values, forbidden transitions,
negative authorization, replay, concurrency, timeout, and recovery—not merely
the common success case. Generated DTOs, trivial property accessors, and
framework plumbing may justify less direct coverage when their behavior is
already protected by artifact or contract tests.

A change can have high line coverage and still fail review if it does not test
the critical invariant. Conversely, a narrowly scoped infrastructure adapter
may be acceptable with modest line coverage when its public contract, denial,
timeout, and provider-sandbox behavior are well proven.

## Architectural invariants and traceability

Every high-risk capability should name its invariants and point to the evidence
families that protect them. The identifiers below are stable public labels; the
private release record links them to exact test runs.

| ID | Invariant | Minimum evidence families |
| --- | --- | --- |
| `FIN-01` | Every posted journal balances: total debits equal total credits | Unit/property plus real-MySQL transaction tests |
| `FIN-02` | Available funds cannot spend held funds | Property, concurrency, lifecycle, reconciliation |
| `FIN-03` | One idempotency key/reference cannot create two economic effects | HTTP replay, concurrent duplicate, crash-point, provider reconciliation |
| `FIN-04` | Provider settlement and internal payable/clearing totals reconcile by currency | Provider sandbox, journal integration, daily reconciliation |
| `AUTH-01` | Possession of a UUID grants no access | Owner/other-user/tenant/country/role authorization matrix |
| `AUTH-02` | Logout and compromise revoke the relevant refresh-token family | Session integration, concurrent refresh, replay regression |
| `AUTH-03` | Sensitive boundary changes require recent approved step-up | Missing/expired/wrong-purpose proof tests |
| `TEN-01` | A request operates only in its proven tenant and country context | Query-filter, acting-context, cross-country, worker-scope tests |
| `LIFE-01` | Every lifecycle accepts only explicit transitions | Unit transition table plus HTTP/state persistence tests |
| `RT-01` | Realtime delivery never replaces durable truth | Disconnect/reconnect, missed-event, version convergence tests |
| `RT-02` | Persisted entity versions are monotonic and win over stale client events | Race, multi-node, clock-skew-independent merge tests |
| `SAFE-01` | Stale or low-quality telemetry is not presented as live truth | Freshness/accuracy, network gap, background/killed-device tests |
| `SAFE-02` | Safety evidence is private, auditable, retained, and deleted by policy | Authorization, quarantine, access audit, hold/expiry tests |
| `DATA-01` | Canonical schema, EF metadata, empty bootstrap, and every active cell agree | MySQL bootstrap/alignment/fingerprint/startup tests |
| `PRIV-01` | Logs and artifacts contain no credentials, message bodies, or private evidence | Static redaction, runtime telemetry, artifact inspection |
| `MOB-01` | A supported screen keeps its primary action reachable and understandable | Render matrix, semantics, keyboard/inset, real-device smoke |

When a design chapter introduces a new invariant, its pull request should add a
row or map it to an existing row. When an invariant changes, update its tests,
runbooks, and capability evidence together.

## Negative authorization matrix

Every sensitive resource is tested from more than the happy-path owner. The
matrix is tailored to the endpoint but normally includes:

| Actor or context | Expected result |
| --- | --- |
| Correct owner with current session and required step-up | Allowed according to lifecycle and policy |
| Different user in the same tenant | Coarse denial, normally indistinguishable from not found |
| Correct user in the wrong tenant or country | Denied before data is disclosed or mutated |
| Correct role without the named permission | Forbidden without revealing resource details |
| Administrator without an authorized acting-country workspace | Denied |
| Anonymous, expired, revoked, or malformed session | Unauthorized |
| Valid bearer token without required recent step-up | Denied before mutation/provider work |
| Disabled, locked, restricted, or deleted account | Denied according to the account state |
| UUID copied from logs, links, or another account | No additional authority |

Apply this matrix to users, sessions, wallets, payout methods, documents,
vehicles, trips, chat, calls, recordings, deliveries, rentals, support cases,
SafetyCases, reports, and administrator operations. Return stable coarse errors
where a detailed distinction would help an attacker enumerate data.

## State-machine verification

Every meaningful lifecycle needs a transition table. Tests cover each allowed
edge and representative forbidden edges from every state. Terminal operations
are replayed to prove they do not happen twice.

Examples include:

- a completed trip cannot return to accepted or in-progress;
- two drivers cannot both win one ride request;
- a withdrawn bid cannot be accepted unless a new version is submitted;
- a cashout cannot be completed or refunded twice;
- a rejected document cannot become approved without a reviewed transition;
- a quarantined upload cannot be downloaded as clean;
- a settled rental cannot be checked in again;
- a resolved support or safety case cannot be changed by an ordinary reply; and
- deleting an account cannot bypass retention or legal hold.

Transition tests assert more than status. They inspect snapshots, ledger or
hold effects, immutable timeline/audit events, outbox intent, notification
eligibility, version increments, and any released resource such as vehicle
availability.

## Financial property and database testing

Financial correctness is tested at three levels:

1. **Pure invariants:** generated amounts and operation sequences prove balance,
   rounding, limits, held funds, and reference rules.
2. **Real MySQL behavior:** concurrent transactions prove row-lock order,
   isolation, unique constraints, rollback, and crash-point recovery using the
   supported MySQL major version.
3. **Provider and reconciliation behavior:** sandbox or signed fixture events
   prove duplicate, out-of-order, partial refund, chargeback, timeout after
   provider acceptance, currency mismatch, and settlement reconciliation.

A financial capability is not release-ready solely because its controller
integration test passes. Minimum useful properties include:

- debits equal credits for every journal;
- balances equal opening balance plus immutable posted effects;
- held balance never becomes spendable until an authorized release/refund;
- an idempotency key with the same request replays one result;
- the same key with a different request is rejected;
- duplicate/out-of-order provider events converge to the same final state;
- currency minor-unit exponents are respected for zero-, two-, and
  three-decimal currencies; and
- cashout remains fail-closed while reconciliation has an unexplained critical
  exception.

Generated values are bounded to realistic domain ranges and explicit overflow
boundaries. Tests never hide precision defects by using binary floating point
for stored money.

## Concurrency and race policy

Concurrency is ordinary marketplace behavior, not an exotic edge case. We
deliberately race:

- two drivers accepting the same ride or delivery;
- rider cancellation against driver acceptance;
- completion against cancellation;
- duplicate wallet transfer, voucher redemption, top-up, and cashout requests;
- two workers claiming the same outbox/broker message;
- duplicate and out-of-order payment/store webhooks;
- simultaneous refresh-token use and reuse detection;
- membership renewal against upgrade, downgrade, refund, or revocation;
- two administrators reviewing the same document, vehicle, case, or account;
- refresh against mutation and dispose against response in mobile providers;
  and
- realtime update against a slower HTTP response.

Tests synchronize at meaningful barriers rather than hoping thread timing
creates a race. The assertion checks one authoritative winner, deterministic
loser behavior, version/reference uniqueness, accounting effects, durable
events, and eventual client convergence.

## Failure-injection policy

For an operation with an external or asynchronous boundary, test failures at
specific points:

1. before validation or provider submission;
2. after validation but before database commit;
3. after provider acceptance but before its response reaches KiloDrive;
4. immediately after database commit but before HTTP response;
5. after durable outbox creation but before delivery;
6. during queue/broker delivery or handler execution;
7. during client disconnect, process recycle, or retry; and
8. during reconciliation or compensating action.

The expected outcome is documented for each point. A timeout is not interpreted
as provider failure when acceptance is unknown. The adapter reconciles by a
stable provider/idempotency reference before another mutation. Post-commit
notification or realtime failure must not turn a successful business operation
into an unsafe client retry.

Failure injection is controlled and hypothesis-driven. It is not permission to
crash production randomly, flood a provider, or delete infrastructure.

## Mocking and real-boundary policy

Mocks are useful when they make a rule fast and deterministic. They become
dangerous when they erase the behavior being tested.

May normally be mocked or faked:

- maps, payment, messaging, storage, media, and identity provider interfaces in
  pure/component tests;
- clocks, randomness, UUID generation, and network reachability;
- repositories in widget/render tests; and
- provider outcomes for deterministic failure sequences.

Must eventually be tested at the real or faithful boundary:

- MySQL locking, constraints, collation, spatial functions, transaction
  isolation, and foreign keys;
- Valkey TLS/ACL, GEO, cache, rate coordination, and SignalR backplane;
- signed webhook/token/attestation schemas and provider error shapes;
- S3-style private object, encryption, quarantine, and presigned access policy;
- Android/iOS permissions, lifecycle, background execution, biometrics, push,
  deep links, and native calling; and
- store purchase acknowledgement, restore, revocation, and product mappings.

SQLite or an in-memory provider is not accepted as proof of MySQL concurrency
or collation behavior. A provider mock is not accepted as proof of a real
signature parser or sandbox contract.

## Database verification policy

Database tests use disposable schemas and the supported MySQL major version.
They cover:

- canonical empty bootstrap;
- reviewed idempotent alignment from supported prior states;
- EF relational metadata parity with tables, columns, indexes, foreign keys,
  collations, generated/spatial definitions, and nullability;
- normalized control and country-cell fingerprints;
- startup/readiness refusal when expected metadata drifts;
- unique and foreign-key enforcement;
- row-lock order, isolation, deadlock retry policy, and rollback;
- Unicode round trips and country-specific reference data;
- spatial query correctness and index-aware candidate narrowing; and
- parallel-safe fixtures with independent ownership and cleanup.

An empty table is not evidence that a table is unused. No test or cleanup
process drops production structures merely because they contain no rows.
Production metadata inspection uses read-only credentials from a controlled
bastion; reviewed DDL is applied separately.

## Contract and backward-compatibility tests

The reviewed OpenAPI artifact is executable release evidence. Tests compare
endpoint metadata and generated schema so authorization, anonymous access,
required parameters, enums, idempotency headers, rate-limit guidance,
ProblemDetails responses, and canonical routes remain truthful.

Compatibility tests prove:

- the current mobile/portal builds work against the proposed API;
- supported older client versions retain their existing wire shape and routes;
- additive fields do not become accidentally required;
- enum and money/time representations remain stable;
- deprecated aliases follow their published sunset policy;
- doubled or unversioned routes are not introduced accidentally; and
- a rollback to the previous binary remains compatible with expand-first
  schema changes.

Mobile rollback relies heavily on server backward compatibility because an
installed app cannot be remotely removed. A breaking API change therefore
requires an explicit major-version and client migration plan.

## Mobile security and artifact regression tests

The shipped APK/AAB/IPA—not only source declarations—is inspected. Automated
assertions cover:

- no new exported Android component without explicit review;
- privileged IPC does not rely on a `normal` custom permission;
- internal receiver/activity/service components are not exported when external
  IPC is unnecessary;
- debuggable, cleartext, backup, network security, foreground-service,
  microphone, camera, location, call, and media permissions match the product;
- release Dart AOT uses approved obfuscation/split-debug-info controls and does
  not expose developer workstation paths;
- debug symbols remain protected and tied to the artifact hash;
- native libraries meet supported ABI and Android page-alignment requirements;
- iOS entitlements, background modes, privacy manifests, and executable private
  selectors match the reviewed feature set; and
- release artifacts exclude credentials, fixtures, private documents, build
  junk, and diagnostic proxy capability.

A security finding is not complete when the source looks fixed. The test must
inspect the final merged/re-signed artifact where plugin manifests and embedded
frameworks can change behavior.

## Deep-link and session abuse tests

Deep links are tested while anonymous, authenticated as the wrong user,
authenticated in the wrong country, expired, malformed, replayed, and pointed
at a deleted or unauthorized entity. A link may navigate; it cannot grant
authorization or skip required step-up.

Authentication/session regression coverage includes:

- refresh-token rotation, concurrent refresh, replay, and family revocation;
- logout revocation and account disablement;
- password reset and credential changes invalidating appropriate sessions;
- OTP expiry, attempt isolation, reuse, purpose confusion, and provisional
  registration cleanup;
- TOTP/passkey enrollment, confirmation, recovery, deletion, and recent-auth
  requirements;
- multi-node single-use ceremonies; and
- stolen, expired, wrong-audience, wrong-country, and malformed tokens.

Login UI assertions use stable error codes, not localized English text.

## App Check and Play Integrity

Where app attestation is enabled, server tests cover valid, missing, expired,
malformed, replayed, wrong-package, and wrong-signature credentials. Each
endpoint family documents whether attestation:

- fails closed because the action crosses a high-risk boundary;
- contributes to a risk decision or additional step-up; or
- is observed during a rollout without blocking legitimate users.

The policy is server-enforced. A client-side check or bundled SDK is not proof
that the API validates attestation. Test fixtures use provider-approved test
tokens or an explicit non-production verifier and never weaken the production
verifier globally.

## Security finding to permanent regression

Once a vulnerability is confirmed, its correction is not complete until a
test reproduces the old unsafe behavior and proves the new denial or safe
result. The test should live at the lowest level that captures the root cause,
plus an artifact/integration layer when packaging or middleware contributed.

Examples include:

- a foreign payout-method UUID cannot be deleted;
- logout makes the prior refresh token unusable;
- OTP guesses do not lock the victim's password login;
- a forged local incoming-call intent cannot reach a privileged component;
- support/document attachment quarantine returns a friendly unavailable state
  without leaking storage details; and
- security/correlation headers survive sanitized exception responses.

The incident or finding record links to the invariant and test evidence without
publishing an exploit recipe or sensitive internal detail.

## Flaky-test policy

“Rerun until green” is not a release strategy. A flaky test can be a real race,
clock defect, shared fixture, or leaked dependency.

When a test is flaky:

1. record the failure and retain sanitized evidence;
2. assign an owner and severity;
3. investigate timing, fixture isolation, environment, and product behavior;
4. quarantine only through an explicit reviewed mechanism;
5. set a deadline and tracking reference for removal; and
6. publish the quarantine count in release evidence.

A quarantined test does not count as passed. Critical financial, security,
safety, schema, or authorization gates cannot be silently quarantined to ship a
release.

## Determinism, clocks, and identifiers

Tests use injected clocks, deterministic randomness, and controlled UUID
factories where the rule depends on them. OTP/JWT expiry, trip scheduling,
retention, membership periods, retries, SLA, and settlement are advanced by the
test clock rather than by long sleeps.

Realtime and concurrency tests may wait for bounded synchronization, but they
must not depend on “sleep and hope.” Each wait has a reason, timeout, and useful
failure message. Dates are asserted in UTC at the API/storage boundary and in
the selected local timezone at the presentation boundary.

## Hermetic boundaries and seeded fuzzing

An ordinary unit, component, repository, widget, or application test is
hermetic: it cannot reach production, a public API, a real notification
destination, or a payment/provider account just because credentials or a URL
exist on the developer machine. The test process validates requested origins
and provider modes before network work begins. An unexpected external boundary
is a failed test, not a warning.

Certification is a separate, explicit job. It requires a reviewed environment
allowlist, non-user destinations/accounts, a unique run ID, automatic cleanup,
sanitized evidence, and a narrow reason for crossing the boundary. A live test
flag does not weaken the production application or ordinary test runner.

Form and calculation fuzzing uses deterministic seeds and bounded generated
values. It covers whitespace, paste, locale decimal separators, negative and
exponent input, large/overflow values, malformed dates, future enum values, and
operation sequences. When a generated case finds a defect:

1. record the seed and smallest reproducing input without PII;
2. add it to the reviewed regression corpus;
3. fix the product rule or parser rather than filtering the seed out; and
4. keep randomized exploration plus the deterministic regression.

Fuzzing complements explicit boundary examples. It does not prove usable error
copy, layout, accessibility, database locks, or provider behavior.

## Synthetic fixtures and cleanup

Tests use deterministic, clearly non-user fixtures:

- synthetic names, phone numbers, emails, documents, payment references, GPS
  traces, and images;
- approved driver/vehicle evidence and memberships created through supported
  fixture/admin APIs;
- funded test wallets and fake providers, never customer balances;
- separate tenant/country ownership for isolation checks; and
- unique fixture-run identifiers for parallel execution.

No production database subset is copied into ordinary tests. Any exceptional
use of production-derived data requires formal governance and irreversible
anonymization before it enters a test environment.

Cleanup runs in a `finally` path. When financial, safety, audit, or legal records
cannot be deleted, the fixture is closed and anonymized through supported
lifecycle operations. Evidence retains only sanitized correlation IDs and
fixture-run references.

Before a ride/bid test, fixture readiness is asserted explicitly: verified
driver's license, compliant active primary vehicle, valid membership, fresh permitted
location, no active assignment, and `canBid=true`. A partially constructed
fixture is a failed precondition, not an application defect.

## Mobile test pyramid

The mobile pipeline uses different speeds for different confidence:

1. **Every pull request:** fast model, formatter, repository/provider, widget,
   localization, static architecture, and contract tests.
2. **Merge/build:** emulator smoke for tools-only, rider, driver, rental, and
   System Admin workspaces using Flutter semantics rather than raw coordinate
   taps or ADB text injection.
3. **Nightly/release:** physical Android/iOS coverage for permissions, system
   insets, background/killed active-trip location, push, biometrics, offline
   queue, SignalR reconnect, voice, map handoff, and store billing.

The render matrix includes narrow phone, phone/tablet portrait and landscape,
split screen, 1.3x and 2.0x text, light/dark/high contrast, keyboard open/closed,
and Android gesture/three-button navigation. It asserts no overflow, reachable
primary actions, minimum touch targets, semantics order, and safe top/bottom
bounds.

Screenshots and recordings never contain credentials, tokens, personal
messages, real notifications, or customer data.

## Release evidence

Each release retains private evidence tied to the exact artifact and source
revision. A public-safe summary may publish:

- product version and build number;
- UTC test timestamp and approved toolchain family;
- test families executed;
- pass, fail, skipped, and quarantined counts;
- artifact and reviewed contract hashes;
- schema contract version/fingerprint family; and
- known limitations or deferred device/provider exercises.

Do not publish private test names, credentials, account/host identifiers,
customer data, defensive thresholds, raw logs, stack traces, document paths, or
provider payloads. “All tests passed” is never used when required suites were
skipped or quarantined.

## Release gate

A capability is not release-ready until:

- its high-risk invariants have direct tests;
- allowed and forbidden lifecycle transitions pass;
- the negative authorization matrix passes;
- idempotency, race, timeout, and recovery behavior pass where applicable;
- real MySQL/provider/native boundaries have the required evidence;
- current and supported older clients remain contract-compatible;
- no critical test is quarantined;
- fixtures are ready, isolated, and cleaned/anonymized;
- the exact signed artifacts pass their security and behavior gates; and
- the capability-status page and runbooks accurately describe what is active,
  configurable, or still planned.

The release owner may accept a documented lower-risk exception only through the
restricted risk process, with owner, scope, expiry, rollback, and monitoring.
No exception may redefine a failed financial, authorization, privacy, or safety
invariant as a pass.

## Common mistakes

- Counting tests instead of identifying the invariant they protect.
- Treating high line coverage as proof of correct authorization or accounting.
- Using SQLite/in-memory behavior to claim MySQL locking correctness.
- Mocking a provider signature parser and calling the provider certified.
- Testing only allowed state transitions and never forbidden ones.
- Letting a retry hide a flaky realtime or concurrency defect.
- Sleeping for real expiry windows instead of controlling time.
- Running destructive or unbounded load against production.
- Using a half-built driver/rider/rental fixture and blaming the application.
- Testing a debug APK and submitting a different release AAB.
- Fixing a vulnerability without adding a permanent regression test.
- Publishing raw logs or test names that expose private architecture or data.

## Related reading

- [Capability status and evidence](../architecture/capability-status.md)
- [API architecture](../architecture/api.md)
- [Mobile architecture](../architecture/mobile.md)
- [Financial systems](../architecture/financial-systems.md)
- [Rider and driver safety](../architecture/rider-driver-safety.md)
- [Database schema lifecycle](../database/schema-lifecycle.md)
- [Security posture](../security/README.md)
- [API deployment runbook](../runbooks/api-deployment.md)
- [Mobile release runbook](../runbooks/mobile-release.md)
- [Capacity baseline runbook](../runbooks/capacity-baseline.md)
