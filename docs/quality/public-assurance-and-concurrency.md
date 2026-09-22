# Public quality assurance and concurrency guarantees

- **Owner:** Quality engineering, with API, mobile, data, security, and operations owners
- **Last verified:** 22 September 2026
- **Environment:** public architecture documentation; source-inventory snapshot, not production telemetry
- **Evidence boundary:** this page intentionally excludes test credentials, production identifiers, provider destinations, security findings, exact saturation thresholds, and unresolved weaknesses.

## What this page does and does not claim

KiloDrive publishes how it evaluates quality and the safety properties it
expects from concurrent operations. It does not equate a large test count, a
line-coverage percentage, or a single successful load run with production
readiness.

Each release still needs its own evidence: deterministic tests, current-schema
database tests, signed artifact checks, applicable provider sandbox exercises,
and production-readiness checks. A feature can be implemented and tested while
its provider, country, store, or operational configuration remains inactive.

This is not a penetration-test report. Security testing and independent
assessments are handled through controlled disclosure and responsible
remediation processes. Public documentation records the assurance approach,
not exploit paths or unremediated findings.

## Public test inventory snapshot

The following is a source inventory taken on 22 September 2026. It is useful
for showing the breadth of the verification estate, but it is not an execution
result and is not a quality score.

| Measure | Public snapshot | Interpretation |
| --- | ---: | --- |
| C# test source files | 760 | Server, architecture, contract, security, and integration test sources |
| C# `Fact` / `Theory` declarations | 3,554 | Potential xUnit test cases before theory expansion; not a pass count |
| API-focused C# test files | 469 | Domain/API policy, handlers, contracts, and boundary coverage |
| Integration test files | 65 | Cross-layer coverage, including supported-database cases |
| Architecture-rule test files | 57 | Dependency, contract, metadata, and boundary-growth rules |
| MySQL lifecycle-related source files | 53 | Disposable canonical-schema, locking, constraint, and lifecycle coverage |
| Concurrency/race/idempotency-related source files | 94 | Deliberate overlap, replay, recovery, and ordering scenarios |
| Flutter test source files | 516 | Mobile state, widget, accessibility, and workflow coverage |
| Dart `test` / `testWidgets` declarations | 2,949 | Potential mobile test cases; not a pass count |
| Flutter widget test declarations | 718 | Rendered interaction, semantics, layout, and state coverage |

The inventory is refreshed with reviewed release evidence. Exact executed test
counts, run hashes, duration, environment details, and any failed or flaky
case analysis stay in the restricted release record so they cannot be mistaken
for a permanent public claim.

## How KiloDrive measures meaningful coverage

Coverage is evaluated by business promise and boundary, rather than a single
repository-wide percentage.

| Critical area | Coverage expected | Examples of the promise being checked |
| --- | --- | --- |
| Identity and access | Policy/unit, HTTP authorization, session/replay, mobile recovery | A copied identifier grants no access; logout and account restrictions revoke the right sessions; sensitive changes require current proof. |
| Money and membership | Property, lifecycle, real-MySQL transaction, provider-contract, recovery | Journal entries balance; held funds do not become spendable; one purchase or payout request produces one economic effect. |
| Rides, bids, trips, deliveries, and rentals | Transition-table, API, concurrent-writer, realtime-recovery | A ride has one accepted driver; terminal states do not regress; reconnecting clients converge on durable truth. |
| Documents, vehicles, and safety | Validation, authorization, review lifecycle, media/quarantine, audit | Private evidence remains protected; reviewed decisions are attributable; expiry and rejection take effect safely. |
| Mobile workspaces | Provider/model, widget, semantics, localization, artifact and device evidence | The next safe action remains understandable through loading, offline, unknown-state, large-text, and resume paths. |
| Providers and asynchronous work | Contract, signature, duplicate/out-of-order, timeout, outbox, sandbox | A provider timeout is reconciled before another value-changing request; a durable command is not lost because a push or webhook is delayed. |
| Tenancy and country cells | Query-filter, cross-tenant denial, worker scope, current-schema integration | A tenant/country boundary cannot be crossed by a URL, cache item, worker, report, or replayed event. |

Line and branch coverage are tracked internally as change-detection signals.
They do not replace these outcome-oriented measures: generated code can inflate
them, while a high-risk race can remain untested behind a seemingly high
percentage. Reviewers require new code to name the business invariant and the
test families that prove it.

## Concurrency and race-condition guarantees

Marketplace activity is inherently concurrent: phones retry, workers restart,
webhooks arrive more than once, and multiple people may act on the same trip
or account. KiloDrive designs the following guarantees into value-changing and
state-machine operations.

| Guarantee | Design approach | Observable safe result |
| --- | --- | --- |
| At-most-once economic effect | Stable KiloDrive idempotency keys, provider references, unique constraints, and reconciliation | A repeated request returns or reconciles the original outcome; it does not create a second debit, credit, hold, or entitlement. |
| One authoritative state transition | Persisted revisions, conditional writes, transition policies, and short transactions | A stale client or second writer receives a safe conflict/recovery outcome rather than overwriting the winner. |
| Financial conservation | Immutable ledger/journal entries, holds, reference uniqueness, and read-only reconciliation | Balances, holds, settlements, refunds, and compensating postings remain explainable by evidence rather than background edits. |
| Durable post-commit work | SQL outbox, leased claims, deduplication, bounded retry, and dead-letter investigation | A committed command is not forgotten if delivery, a worker, or a network connection fails. |
| Provider ordering tolerance | Provider event identity, idempotent handlers, causal status rules, and reconciliation | Duplicate, delayed, or out-of-order webhooks converge safely without state regression. |
| Tenant and country isolation | Proven tenant/country context, query filters, scoped workers, and negative authorization tests | A concurrent request or worker cannot use another tenant or country cell's data as authority. |
| Client convergence | Versioned DTOs, checkpoint replay, push/realtime invalidation, and HTTP refresh | Realtime is fast delivery, not truth; a disconnected or stale client recovers from durable state. |

## Race scenarios exercised by the test strategy

The test program deliberately coordinates overlap at meaningful barriers rather
than relying on timing luck. Public examples include:

- two drivers attempting to accept the same ride or delivery;
- rider cancellation racing with driver acceptance, start, or completion;
- duplicate wallet transfer, top-up, voucher redemption, cash-out, refund, or
  membership command;
- duplicate and out-of-order payment, store, and messaging-provider events;
- two workers attempting to claim the same outbox or broker delivery;
- renewal racing with upgrade, downgrade, refund, revocation, or restoration;
- two reviewers deciding the same document, vehicle, account, or case;
- session refresh/reuse, device revalidation, and security-boundary changes
  occurring in parallel; and
- realtime delivery racing with a slower HTTP read or client process restart.

For each scenario, the required assertion is broader than an HTTP status code:
the test checks the authoritative winner, stable loser/recovery result,
revision behavior, unique references, financial postings or holds where
applicable, audit/outbox intent, and eventual client-visible convergence.

## Database, provider, and device boundaries

Concurrency tests are not treated as complete until the right boundary is
included.

- Pure tests establish state-machine, money, validation, and retry rules.
- Disposable MySQL tests establish locking, constraints, isolation, deadlock
  handling, rollback, and canonical-schema compatibility.
- Provider fixtures or sandboxes establish signed payload shape, duplicate and
  delayed delivery, unknown outcomes, and reconciliation behavior.
- Signed mobile artifacts and physical-device exercises establish native
  lifecycle, permissions, background behavior, accessibility, and client
  recovery.

No in-memory database, mock provider, or emulator screenshot is represented as
proof for a boundary it does not actually exercise.

## Capacity statements

KiloDrive is designed for horizontal API scaling, independently operated
country cells, replaceable short-lived distributed state, durable outbox
processing, and asynchronous provider work. That design is not a public claim
of a fixed number of simultaneous rides.

Capacity is established per release and deployment environment with a declared
workload shape and measured service objectives. The controlled exercise records
API latency, database time and lock waits, pool saturation, cache/realtime
pressure, queue age, provider latency, error rate, and recovery behavior. Exact
thresholds, test traffic, and bottlenecks remain internal until they are
reviewed and remediated. See [scaling and capacity planning](../architecture/scaling-and-capacity.md).

## Related documents

- [Testing and verification](testing-and-verification.md)
- [Capability status and evidence](../architecture/capability-status.md)
- [Scaling and capacity planning](../architecture/scaling-and-capacity.md)
- [Security and responsible disclosure](../security/README.md)
- [Release evidence and operational runbooks](../runbooks/README.md)
