# ADR 005: EventBridge and SQS acceleration with SQL outbox recovery

- **Status:** Accepted
- **Date:** 2026-08-23
- **Decision owners:** Dispatch, Platform Operations, and Architecture
- **Related systems:** Country-cell outbox, AWS EventBridge, SQS, matching workers, SignalR, push notifications

## Context

Ride dispatch is bursty. One request can fan out to many eligible drivers, and
responses arrive while the rider is changing fare, cancelling, or accepting an
offer. Running all fan-out work in the HTTP request makes latency and correctness
depend on every downstream provider. Polling a MySQL outbox alone is durable but
can add contention and delay during a dispatch surge.

Moving all truth into a cloud bus would create a different problem. EventBridge
and SQS provide at-least-once delivery, not an atomic transaction with the
country MySQL cell. Publishing before commit risks dispatching a ride that rolls
back. Publishing after commit leaves a crash window in which no cloud event is
sent. Provider/IAM/network failures can also prevent publication.

The platform needs low-latency fan-out without making AWS the only evidence that
dispatch work exists.

## Decision drivers

- Ride/bid/trip state and event intent must commit atomically.
- Dispatch must survive API process loss and AWS publication failure.
- Workers must handle duplicates, delayed messages, and out-of-order delivery.
- A cloud backlog should absorb bursts instead of moving contention back to the
  request thread or country database.
- Recovery must not require copying route, contact, or message payloads into
  cloud event logs.
- The team needs observable lag, dead-letter handling, and a safe rollback to
  SQL recovery.
- The normal and fallback paths must execute the same business handler.

## Decision

KiloDrive uses a hybrid dispatch pattern:

1. The country-cell transaction commits the domain mutation and a compact,
   immutable outbox/dispatch intent.
2. After commit, the publisher submits a minimal envelope to a dedicated
   EventBridge bus.
3. A narrowly matched rule sends the event to an SQS queue.
4. An SQS consumer claims the stable event ID, re-reads authoritative country
   state, validates the persisted monotonic entity version, and performs the
   current eligible fan-out.
5. The message is deleted only after successful idempotent handling.
6. If cloud publication or consumption does not acknowledge the SQL intent
   within a configured recovery age, the SQL worker invokes the same handler.
7. Repeated permanent failures go to a dead-letter path with safe diagnostic
   metadata and an operator runbook.

The bus envelope contains identifiers, bounded event type/version, country and
tenant routing surrogate, availability time, and correlation ID. It excludes
precise location, contact data, message bodies, tokens, payment details, and
documents.

Correctness remains in conditional domain transitions and idempotent handlers.
The broker is an acceleration and back-pressure mechanism, not the source of
truth.

## Delivery contract

- Delivery is at least once.
- Global ordering is not promised.
- A stable event ID is the logical deduplication key.
- Entity state uses a persisted monotonic version; wall-clock ticks are not an
  ordering authority.
- A consumer revalidates current state and ignores superseded work.
- Downstream mutations use their own stable idempotency/provider reference.
- Unknown provider results are reconciled before retry.
- Handler registration for every published event type is a release contract.

## Alternatives considered

### SQL outbox polling only

This is the simplest durable design and remains the fallback. It was not chosen
as the sole high-throughput path because frequent polling/claiming can add lock,
connection, and query pressure to the same country database serving rides and
wallets. It remains suitable for low-volume domains and emergency recovery.

### EventBridge without SQL intent

This removes database polling but creates a post-commit loss window and makes
cloud audit history the only evidence of an unsent event. It was rejected for
ride lifecycle and financial/customer notification work.

### Publish before database commit

This avoids the post-commit publish gap but lets consumers observe state that
can still roll back. Retrying that race is harder than recovering a committed
outbox intent. It was rejected.

### RabbitMQ or Kafka as the only broker

Both can support high-throughput architectures. They were not chosen for this
stage because EventBridge/SQS fit the managed AWS operating model and do not
require running another stateful cluster. Kafka may become attractive for high
volume ordered streams and replay analytics, but it would not remove the need
for transactional outbox/idempotency.

### Distributed transaction across MySQL and broker

Two-phase commit would increase coupling and operational fragility and is not a
practical contract across these services. It was rejected.

## Consequences

### Benefits

- HTTP latency is decoupled from dispatch fan-out.
- SQS absorbs temporary bursts and exposes backlog age.
- A committed SQL recovery ledger survives cloud/IAM/process failure.
- The broker consumer can scale independently.
- At-least-once behavior is explicit and testable.
- Event content remains small and privacy bounded.

### Costs and risks

- Two delivery paths increase reasoning and testing requirements.
- Duplicates are expected; a non-idempotent handler will notify twice.
- The recovery delay trades duplicate probability against delayed fallback.
- EventBridge rule, SQS policy, IAM, visibility, redrive, and alarms are more
  infrastructure to own.
- A missing handler can poison the queue/outbox until release contract tests
  catch it.
- Queue success does not prove the mobile client rendered the state; client
  reconciliation remains required.

## Security, privacy, and compliance

The publisher role can put events only on the designated bus. The rule can send
only to the designated queue. The consumer can receive/change visibility/delete
only there. Dead-letter inspection/redrive uses a separate audited operator role.

Event payloads follow data minimization. Provider IDs, status, latency, attempts,
event type, and correlation ID may be observed. Routes, contact details, tokens,
message bodies, and documents are prohibited. Encryption, retention, audit, and
access policies apply to bus/queue telemetry and dead-letter storage.

## Reliability and operations

Operators watch failed EventBridge entries, publish errors, queue visible and
in-flight counts, oldest age, receive count, dead-letter count, consumer
heartbeat, handler duration, SQL fallback age, and duplicate/no-op rate.

The SQS visibility timeout exceeds the normal handler duration. Long handlers
extend visibility only while proving ownership. Scale uses sustained oldest age
and saturation rather than queue depth alone.

When cloud dispatch is impaired, SQL recovery stays enabled. When a consumer is
poisoning work, pause the narrow consumer and preserve rows/messages. Recovery
never deletes failure evidence merely to clear an alarm.

See [EventBridge and SQS dispatch](../aws/eventbridge-sqs.md), [dispatching](../runbooks/dispatching.md),
and [outbox recovery](../runbooks/outbox-recovery.md).

## Validation

- Commit an event and kill the API before publish; SQL recovery executes once.
- Deliver the same SQS event concurrently; one logical outcome occurs.
- Deliver versions out of order; current entity state wins.
- Deny `PutEvents`; readiness/metrics show failure and fallback drains.
- Stop the consumer; age alarm fires, then backlog drains within quotas.
- Force handler timeout and lost delete response; duplicate remains harmless.
- Publish an unsupported type; it enters the bounded failure/DLQ workflow.
- Search logs/traces/event archives for seeded fake PII/token values; none appear.
- Run the two-client ride/bid lifecycle with node loss after each commit.

## Follow-up

- Keep event schemas/version compatibility and handler registration under CI.
- Capacity-test recovery to prevent a SQL stampede after a long broker outage.
- Exercise DLQ diagnosis and redrive at least twice a year.
- Revisit broker choice only with measured throughput, ordering, replay, cost,
  and team-operability evidence.
