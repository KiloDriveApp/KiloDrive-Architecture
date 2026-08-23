# Tutorial: Add a Durable Domain Event

Suppose a new workflow needs to announce that an entity changed. The tempting
implementation is to save the entity and immediately call SignalR. That works
until the process exits between those two lines.

This tutorial describes the safer design.

## Decide whether the event is actually durable

Use a durable event when another action must eventually happen after committed
business state. Examples include assignment changes, financial notifications,
document-review notices, and cross-cell orchestration checkpoints.

An ephemeral event is appropriate for replaceable hints such as typing state or
short-lived UI presence. Do not put every animation into the database. Do not
make a business promise depend only on an ephemeral publish.

## Define the event contract

Name the event after a business fact, not an implementation call. Prefer
`ride.cancelled` to `send_driver_message`.

The contract should include:

- entity identifier;
- persisted entity version;
- tenant/country scope required to restore context;
- event occurrence time from the injected clock;
- correlation/causation identifier; and
- the smallest payload the consumer needs.

Avoid names, phone numbers, raw chat text, access tokens, and document URLs in a
broad dispatch event. Consumers can perform an authorized query when they need
more detail.

## Write business state and outbox atomically

Inside one short country-cell transaction:

1. lock or conditionally update the aggregate;
2. validate the expected prior state/version;
3. apply the mutation and increment the version;
4. insert the outbox message with a UUIDv7 identifier and stable type; and
5. commit.

Do not enqueue after commit in controller code. Do not let an HTTP disconnect
cancel delivery of a committed promise.

## Register a handler before producing the event

A production lesson was learned the noisy way: an outbox event with no handler
retries until it becomes a permanent failure. Treat producer and handler
registration as one release unit.

Add a contract test that enumerates produced message types and proves each type
has a registered handler or an explicitly documented terminal policy.

## Make the handler replay-safe

Assume the same message can be delivered more than once. Depending on the side
effect, use:

- a provider idempotency key derived from the outbox ID;
- a unique local delivery/notification record;
- a conditional version check;
- a consumer inbox/deduplication record; or
- a read-before-write reconciliation when the provider result is unknown.

Blindly adding a transport retry to `POST` is not a substitute for this design.

## Decide how cloud dispatch and SQL recovery cooperate

KiloDrive can publish high-volume dispatch work to EventBridge and SQS while
retaining SQL recovery. The broker is useful for throughput and independent
consumer scaling. The SQL row remains the durable recovery evidence when IAM,
networking, queue policy, or a consumer is unavailable.

The broker failure path needs a metric and warning, but the request should not
claim the business transaction failed if SQL committed correctly.

## Add observability without payload leakage

Record bounded labels such as event type, sanitized status, attempt, latency,
and correlation ID. Avoid user IDs as metric labels; high-cardinality labels can
make a metrics backend expensive or unusable.

Useful signals include:

- oldest pending age;
- pending and failed count;
- handler duration by bounded type;
- last worker heartbeat;
- broker publish result;
- queue depth and age; and
- dead-letter count.

## Test the crash points

At minimum, test:

1. exception before commit — neither state nor outbox exists;
2. exception after commit but before worker claim — state and outbox recover;
3. worker crash after provider acceptance — replay reconciles, not duplicates;
4. duplicate broker delivery — consumer has one business effect;
5. unknown event type — readiness/alerts reveal it;
6. stale entity version — client ignores old event and refreshes safely; and
7. unavailable broker — SQL recovery remains effective.

## Update the operator story

Add the event type, owner, retry behavior, safe replay rule, and failure evidence
to the [outbox recovery runbook](../runbooks/outbox-recovery.md). A feature is not
finished if only its original author knows how to recover it.
