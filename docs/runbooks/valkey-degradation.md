# Runbook: Valkey degradation, ACL failure, or loss

- **Owner:** Platform operations and realtime services
- **Status:** Operational policy
- **Last exercised:** Record the most recent cache/backplane/location failover date here
- **Related architecture:** [Realtime and events](../architecture/realtime-and-events.md), [hosting](../architecture/hosting.md), [threat boundaries](../security/threat-boundaries.md)

## Purpose and safety boundary

Valkey accelerates several different KiloDrive capabilities: distributed cache,
SignalR pub/sub, live driver location, short-lived coordination, and—where
configured—single-use authentication ceremonies. An outage therefore has more
than one failure mode.

This runbook protects correctness first. Durable rides, money, documents, and
audit stay in MySQL/object storage. Replaceable cache and location state may be
rebuilt. Single-use security state must fail closed; it must not fall back to a
process-local cache in a multi-node production environment.

## Trigger and customer symptoms

- readiness reports unreachable/high-latency Valkey;
- `NOAUTH`, `WRONGPASS`, TLS, timeout, connection-pool, or DNS errors;
- `NOPERM No permissions to access a channel` from SignalR;
- cross-node realtime events disappear while same-node events work;
- driver locations stop refreshing or eligibility expires;
- cache misses drive MySQL load sharply upward;
- passkey/challenge ceremonies fail after node switching;
- memory pressure, evictions, rejected connections, or replication lag; or
- reconnect storms after a brief outage.

Record the affected capability/namespace. “Redis is down” is too coarse to guide
safe behavior: a GET/SET cache path, GEO update, pub/sub channel, and one-time
challenge have different risk.

## Preconditions

- Use a restricted operational account; never reuse the application credential
  for administration.
- Know the last healthy topology/configuration and whether replicas/failover are
  part of the deployed design.
- Confirm MySQL health before allowing cache-miss traffic to increase.
- Identify which features fail open, degrade, or fail closed.
- Do not paste connection strings, credentials, private endpoints, channel names
  containing identifiers, or key contents into incident systems.

## Diagnose in order

### 1. Determine blast radius

Compare all API nodes and capabilities:

- Can a bounded cache key be read/written?
- Can node A publish a synthetic event received through node B?
- Can a synthetic driver GEO update and lookup complete?
- Can distributed single-use state be created, consumed once, and rejected on
  replay?
- Are failures isolated to one node, command family, key prefix, or pub/sub
  namespace?

This separates a service outage from an ACL/prefix/configuration mismatch.

### 2. Verify network and identity

Check DNS, protected transport/certificate, endpoint/port, connection limit,
runtime credential source, and server reachability. `NOPERM` means the server
authenticated the client but denied the command or channel pattern. It is not a
network failure and should not be fixed by granting every command.

For SignalR, compare the channel prefix on every API node and confirm the
application account has only the needed pub/sub commands and patterns. For
location/cache, verify their distinct command/key permissions.

### 3. Check resource pressure

Inspect latency, CPU, memory, fragmentation, eviction policy/count, keyspace,
connections, blocked clients, network throughput, command rate, slow operations,
replication/failover state, and reconnect attempts. A client reconnect storm can
worsen a short outage; use bounded exponential reconnect with jitter.

Never run broad key scans or administrative commands on a busy production node.
Use bounded server metrics and safe sampling.

### 4. Check the client side

Confirm connection multiplexer reuse, timeouts, retry bounds, cancellation,
circuit state, pool/socket pressure, and deployed configuration consistency.
Creating one connection per request is an application defect, not a Valkey
capacity problem.

## Contain by capability

### Distributed cache

Allow safe misses, but cap concurrent refills and use jittered TTLs to avoid a
database stampede. Preserve last-known non-sensitive data only within its policy
TTL. Never use stale cached authorization, country activation, or entitlement
as permission to mutate.

### SignalR backplane

Keep durable APIs and outbox events available. Clients use bounded resync/polling
and entity versions. Do not claim realtime delivery is healthy. If one node is
misconfigured, drain it rather than disabling backplane authorization globally.

### Driver location

Expire online eligibility when telemetry becomes stale. Do not keep matching a
driver from an old coordinate. Explain the offline/degraded state to the driver
and require a fresh permitted heartbeat before bidding resumes.

### Security ceremonies

Fail closed for passkey challenges, nonce/replay state, or other single-use
security material. Offer a separately approved authentication method. Do not
fall back to process memory across multiple nodes.

## Recover

1. Fix the narrow cause: service health, network/TLS, capacity, credentials,
   command/channel ACL, prefix mismatch, or client connection behavior.
2. Restore one application node/capability and run synthetic tests.
3. Reintroduce nodes gradually and watch connections/reconnects/latency.
4. Warm only high-value cache keys with bounded concurrency; let the rest refill
   naturally.
5. Require fresh driver telemetry before restoring online eligibility.
6. Let clients reconnect and re-fetch authoritative entity state; do not replay
   unversioned UI messages blindly.
7. Discard expired single-use challenges. Users start a fresh ceremony.

If failover may have lost acknowledged cache writes, remember that only
replaceable state belongs here. Investigate any feature whose correctness
depended on those writes and move its authority to durable storage.

## Verification

- Cache operations succeed and MySQL query/load returns to baseline.
- Two API nodes exchange a synthetic SignalR event through the backplane.
- A client connected to each node converges after out-of-order/duplicate events.
- Driver GEO update/search works; stale locations remain ineligible until fresh.
- A distributed challenge can be consumed exactly once across different nodes.
- Latency, memory, evictions, connections, and reconnects remain healthy through
  consecutive windows.
- Readiness and dashboards accurately report recovery.
- Logs/traces contain no connection secret, key value, channel payload, token,
  location coordinate, or user identifier.

## Rollback or abort criteria

Abort a configuration rollout if cross-node pub/sub still fails, evictions
threaten required state, reconnects saturate the service, or security ceremonies
can replay/fail open. Restore the last known configuration and reduce traffic to
the affected optional paths. Do not remove schema/domain safeguards to make the
readiness check green.

## Evidence and follow-up

Keep deployment/config revision, safe node/capability labels, metric snapshots,
sanitized error category, test correlations, alarm transitions, and recovery
time. Add regression tests for the exact ACL, failover, reconnect, cache-stampede,
or multi-node ceremony fault. Review whether key TTLs, memory budget, client
timeouts, and alert thresholds match observed peak behavior.
