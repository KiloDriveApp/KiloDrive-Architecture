# ADR 003: Valkey for fresh distributed geospatial state

- **Status:** Accepted
- **Date:** 2026-08-23
- **Decision owners:** Architecture, Realtime, and Operations
- **Related systems:** Driver telemetry, matching, SignalR, MySQL persistence

## Context

Active drivers can publish location more frequently than ordinary business
records change. Writing every ping synchronously to MySQL would create hot
indexes, lock/IO pressure, and unnecessary history. Keeping location only in API
process memory would fail as soon as a request reaches another node or a process
restarts.

Matching needs a fast answer to “which current driver points are near this
pickup?” It then needs durable MySQL data to decide which of those drivers are
actually eligible.

Some location samples also need to become durable trip replay and safety
evidence. The live cache and historical record therefore have different jobs.

## Decision drivers

- Multi-node visibility of current driver location.
- Efficient radius prefilter for dispatch.
- Short-lived state that expires when a device disappears.
- Bounded MySQL write rate and replay storage.
- Safe degradation when cache is unavailable.
- No stale location as sole proof of eligibility.
- Privacy-aware retention and no coordinates in ordinary logs.

## Decision

Production uses TLS-protected Valkey (Redis protocol) for current driver
geospatial state.

For each accepted sample, the realtime service keeps:

- a short-lived latest-value record containing coordinates and bounded telemetry
  metadata;
- a tenant-scoped GEO member for nearby lookup; and
- a dirty/latest marker for asynchronous persistence.

The application also holds a latest-value process buffer to coalesce writes. A
background worker reads dirty entries, updates the driver profile's durable last
location, and, for an active trip, inserts a deduplicated trip location sample
and evaluates route anomalies. It acknowledges a dirty member only if the value
has not changed since it was read.

Matching uses Valkey GEO only as a candidate prefilter. It rechecks in MySQL:
tenant, active/online state, durable freshness, active assignment, vehicle
compatibility/compliance, blocks, trust, and feature limits. It prunes candidates
again before road-matrix work.

When Valkey is absent, a process-local path exists for development and tests.
Production multi-node deployment requires distributed state. A bounded MySQL
bounding-box fallback may support degraded matching, but stale/uncertain drivers
are excluded rather than guessed online.

## Alternatives considered

### Write every sample directly to MySQL

Simple and durable, but expensive at high frequency. It couples client ping rate
to the primary operational database and increases contention. MySQL remains the
batched evidence store, not the synchronous live bus.

### API process memory only

Very fast and inexpensive. Rejected for production because nodes diverge,
restart loses presence, and matching depends on load-balancer routing. Retained
only as an explicit development fallback.

### Kafka compacted topic as latest state

Excellent streaming durability and replay, but radius query is not native and
the operational footprint is larger. A stream may complement telemetry later;
it does not replace the current GEO candidate index by itself.

### MySQL spatial index only

Useful for durable spatial projections and low/medium-frequency queries, but it
still receives the high-frequency write load and needs freshness cleanup. It is
used selectively for durable route/toll projections, not as the primary live
driver-presence store.

### H3 cell index

Good for hierarchical aggregation and coarse partitioning, but it does not
provide road identity and is not implemented in the reviewed baseline. It may
be evaluated as an additional prefilter with a separate ADR.

## Consequences

### Benefits

- Fast tenant-scoped nearby candidate lookup.
- Shared location state across API nodes.
- TTL naturally limits stale presence and privacy exposure.
- Latest-value coalescing bounds MySQL writes.
- Durable trip samples remain available for replay/safety after cache loss.
- SignalR and other distributed cache needs can use the same operated Valkey
  platform with separated namespaces/ACLs.

### Costs and risks

- Valkey becomes an important production dependency with TLS, ACL, capacity,
  backup/configuration, and alerting duties.
- GEO membership and latest-value TTL can drift if updates partially fail.
- A stale online boolean can disagree with expired telemetry.
- Dirty-set accumulation can create persistence lag.
- One shared Valkey without namespace ACLs or capacity isolation can let one
  workload harm another.
- Cache failover may temporarily reduce nearby dispatch while fresh heartbeats
  rebuild the index.

## Invariants

1. Valkey location is ephemeral and never a wallet/trip lifecycle authority.
2. Matching requires freshness and durable eligibility, not only GEO proximity.
3. Location keys/members are tenant-scoped and contain no contact data.
4. A persistence worker records only the latest coalesced sample per flush unit
   and deduplicates trip samples.
5. A dirty marker is removed only after proving no newer value replaced it.
6. Process memory is not a production multi-node substitute.
7. Stale presence expires or is forced offline honestly.

## Security, privacy, and compliance

- Valkey connections use protected credentials, TLS, and least-privilege ACLs
  for the required command/channel namespaces.
- Exact keys, credentials, coordinates, and customer identifiers are not logged.
- Location TTL and durable replay retention are purpose- and jurisdiction-aware.
- Background location requires visible user purpose and platform-compliant
  permission behavior.
- Live location is disclosed only to authorized trip/workspace participants and
  expires after the purpose closes.
- Incident tooling reports counts, lag, status, and latency—not member payloads.

## Reliability and operations

Monitor:

- connectivity and command latency;
- memory use, eviction, fragmentation, and connection count;
- dirty/latest backlog and persistence lag;
- driver freshness and forced-offline rate;
- GEO candidate count and fallback use; and
- SignalR/backplane ACL failures if the platform is shared.

On Valkey loss, stop treating cached presence as current, use the reviewed
degraded path, and let fresh device heartbeats rebuild state after recovery.
Do not repopulate current location from old trip history.

Before adding an API node, verify the same protected Valkey endpoint, ACL,
serialization contract, and clock/freshness policy across nodes.

## Validation

- Multi-node publish/read and GEO candidate tests.
- TTL expiry and stale-online cleanup tests.
- Out-of-order and duplicate sample tests.
- Worker crash before acknowledgement and retry tests.
- Race where a newer value arrives while the old one is persisted.
- Valkey loss, reconnect, empty-index rebuild, and memory fallback tests.
- Matching tests proving a nearby but offline/assigned/noncompliant driver is
  excluded.
- Privacy tests confirming coordinates and serialized samples do not enter
  ordinary logs or telemetry labels.

## Follow-up

- Keep [geospatial processing](../architecture/geospatial.md) aligned with the
  telemetry implementation.
- Maintain the Valkey degradation and realtime runbooks.
- Revisit stream/H3 augmentation only after measured candidate, history, or
  analytics requirements justify it.
