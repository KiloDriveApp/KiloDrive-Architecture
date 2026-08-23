# Valkey Architecture

## Role in KiloDrive

Valkey implements the Redis protocol and provides fast, bounded, distributed
coordination. It is not the source of truth for money, trips, memberships,
identity, or audit; those remain in MySQL. Losing Valkey may reduce realtime or
cache performance, but must not invent durable state.

Verified/configurable uses are:

- distributed tenant/settings/template cache;
- SignalR multi-node backplane;
- high-frequency driver telemetry and dirty-set batching;
- single-use cross-node passkey ceremony state;
- matching/dispatch deduplication and short-lived coordination; and
- bounded ephemeral state that must survive an IIS recycle/node switch.

The distinction between **fast state** and **durable truth** is the most useful
mental model for a new engineer. If deleting a key could lose money, complete a
trip, grant a role, approve a document, or erase audit evidence, that value does
not belong only in Valkey.

## Connection and trust boundary

Production connections use TLS, certificate and hostname validation, an
explicit endpoint, bounded connect/command timeouts, and a narrowly scoped ACL
identity. The connection string is protected configuration and never appears in
source, health output, or logs. Public network exposure is avoided; network
policy permits only the application and operations paths that need it.

Each workload identity receives the commands and key/channel patterns it needs.
Cache GET/SET does not imply pub/sub channel access, and SignalR pub/sub does not
imply administrative commands such as configuration, flush, or ACL mutation. A
successful `PING` proves connectivity—not authorization for the workload.

## Namespaces and data minimization

Logical uses have separate prefixes, TTLs, serializers, and ideally separate
credentials/databases or clusters according to risk. Keys include opaque tenant,
account, and entity scope. Phone numbers, emails, access tokens, routes, and
message bodies do not appear in readable keys.

Cached values have an explicit owner and invalidation path. A cache entry without
a TTL or invalidation rule becomes a second database and is rejected in review.

A namespace specification includes owner, purpose, key shape, data class,
serializer version, maximum value size, TTL, invalidation event, expected
cardinality, and failure behavior. Conceptual prefixes include
`cache:<tenant>:settings:<revision>`, `geo:<tenant>:drivers`, and
`ceremony:<opaque-id>`; production identifiers stay opaque and no personal data
is embedded in keys.

Serializer changes use a versioned prefix or value envelope. New code that
cannot read old bytes should create a miss, not a deserialization storm.
Tenant-setting writes invalidate or advance revision only after the durable
database transaction commits.

## Cache-aside and stampede control

Read caches use cache-aside: bounded read, authoritative lookup on miss, then a
TTL-limited fill. Authorization and money decisions revalidate authoritative
state at their transaction boundary. Negative caching is brief and limited to
cases where absence is safe to cache.

When a hot key expires, hundreds of callers must not all query MySQL or a maps
provider. Single-flight or a short lease plus jittered TTL spreads refresh. A
stale-while-revalidate path is allowed only for content that may safely be
briefly stale; security revocation, compliance, cashout limits, and wallet
balances do not use it.

## Security ceremonies

Passkey begin/complete state is single-use, short-lived, bound to ceremony and
account context, and atomically consumed. It fails closed if distributed state is
unavailable; process-local memory would break when requests cross nodes or the
process recycles.

Consumption is an atomic compare/delete or script-backed transition. Reading and
then deleting in separate commands permits two concurrent completions. The value
binds purpose, relying-party context, challenge, account/session context, issue
time, and expiry without logging the challenge.

Valkey does not store plaintext refresh tokens or local app-lock secrets. Secret
material uses purpose-specific protected storage, and security events are audited
without copying the secret.

## SignalR backplane

Before adding a second API node, SignalR uses a tested Valkey backplane. Its
runtime identity needs only the commands/channels required for the hub namespace.
`NOPERM` means connectivity/authentication succeeded but ACL channel permissions
do not cover publish/subscribe; the remedy is a narrowly scoped ACL, not an admin
credential.

ACL checks exercise the actual SignalR namespace and both publish and subscribe
from the deployed runtime identity. Testing with an administrator account can
hide a production `NOPERM` defect. Channel names and hub access tokens are
redacted from request and proxy telemetry.

Backplane success does not make a hub message durable. The originating mutation
commits a lifecycle/outbox event first. A disconnected client recovers through
the durable API state and bounded polling/push, not Redis history.

## Driver telemetry and matching

Frequent location heartbeats can be stored and batched without making every GPS
point a heavy relational write. Entries include timestamp/accuracy and expire.
Matching rejects stale telemetry and applies online, assignment, vehicle,
compliance, trust, and duty gates at the authoritative transaction.

GEO proximity produces candidates; it is not the final eligibility decision.
The API validates country/tenant, freshness, accuracy, requested vehicle,
trust/compliance version, duty status, blocking, and active assignment before a
bid or acceptance. Candidate ranking can tolerate a cache miss; authorization
cannot.

Dirty-set batching persists only breadcrumb/audit detail required by trip,
safety, retention, and map-matching policy. High-frequency points have bounded
TTL and precision. General logs never receive raw coordinates.

Background behavior is explicit: either the approved platform service keeps a
perceptible heartbeat active, or online state expires when freshness is lost. A
stale cached location is not proof the driver is currently available.

## Failure behavior

| Use | Valkey unavailable behavior |
| --- | --- |
| Read cache | Query MySQL/provider if safe; bounded latency and cache refill |
| Template/settings cache | Load authoritative value; never use another tenant's entry |
| SignalR backplane | Single-node/local hub may continue; durable recovery remains |
| Driver telemetry | Mark location stale/offline; do not dispatch proximity work |
| Passkey ceremony | Fail closed with retryable safe error |
| Matching dedupe | Fall back only to an idempotent durable path |

Reconnect uses bounded exponential backoff with jitter. A retry storm should not
overload MySQL when cache returns. Circuit/health states are observable without
logging values.

### Degradation modes

- **Cache-only issue:** bypass affected cache with concurrency limits and watch
  MySQL/provider saturation.
- **Pub/sub issue:** preserve durable events and let clients reconcile by
  bounded polling/push; message loss is not state loss.
- **Telemetry issue:** expire online/proximity eligibility instead of reusing a
  stale point.
- **Security-ceremony issue:** fail closed and ask the user to retry; never fall
  back to process-local state on one API node.
- **Broad outage:** pause nonessential cache refill and matching work before a
  reconnect herd harms the authoritative database.

## Capacity and operations

Monitor p50/p95/p99 command latency, connected clients, memory, fragmentation,
eviction, key expirations, replication/persistence health where enabled,
failover, rejected connections, command/channel denials, cache hit rate, and hub
pub/sub errors. High-cardinality key names are sampled/aggregated safely, never
dumped to a general log.

Capacity planning separates cache, telemetry, and pub/sub workloads. A large
telemetry burst must not evict a security ceremony or saturate the SignalR
backplane. Scale thresholds are based on observed peak traffic plus recovery
headroom.

Keyspace cardinality is forecast from active tenants, concurrent drivers,
ceremonies, cached revisions, and TTL overlap. Memory planning includes
allocator overhead, failover headroom, and persistence behavior where enabled,
not only serialized bytes. Eviction policy is deliberate: losing a single-use
security ceremony has a different effect from evicting a place-details cache.

Benchmark the real command mix, not an isolated `GET`. GEO updates/queries,
pub/sub fanout, cache fills, atomic scripts, expiry churn, and reconnect all
compete for the event loop and network. Alarm thresholds come from legitimate
peaks plus recovery margin.

## Recovery exercise

1. Announce/record the test and confirm durable dependencies are healthy.
2. Capture baseline latency, hit rate, telemetry freshness, and hub delivery.
3. Remove Valkey connectivity in a controlled non-production environment.
4. Verify cache fallbacks, passkey fail-closed, online expiry, no cross-tenant
   leakage, and durable realtime recovery.
5. Restore service and observe bounded reconnect/refill without a thundering herd.
6. Reconcile no durable state was lost and archive sanitized evidence.

Never flush all keys in production as a diagnostic shortcut. Namespace-specific
eviction requires an owner, target proof, and recovery plan.

See the [Valkey degradation runbook](../runbooks/valkey-degradation.md) and
[realtime architecture](../architecture/realtime-and-events.md).
