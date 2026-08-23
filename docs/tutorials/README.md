# Engineering Tutorials

The architecture chapters describe individual boundaries. These tutorials show
how those boundaries cooperate during real work.

- [Follow a request](follow-a-request.md) — trace one protected mobile command
  from tap to durable state, event delivery, and client reconciliation.
- [Add a durable domain event](add-a-durable-event.md) — design the database,
  outbox, handler, idempotency, telemetry, and recovery contract together.
- [Add a money movement](add-a-money-movement.md) — begin with invariants,
  choose locks, post a journal, and prove reconciliation.
- [Investigate a stale realtime screen](investigate-stale-realtime.md) — decide
  whether truth, delivery, subscription, cache, or client merge logic failed.

Examples are intentionally synthetic. They teach the method without exposing
production identifiers or access procedures.
