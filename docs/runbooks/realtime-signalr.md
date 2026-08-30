# Runbook: realtime and SignalR degradation

- **Owner:** Realtime platform and marketplace operations
- **Status:** Operational degradation procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Realtime and events](../architecture/realtime-and-events.md), [EventBridge and SQS](../aws/eventbridge-sqs.md), and [observability](../architecture/observability.md)

**Use when:** bids/offers/chat arrive late, cancelled rides remain visible,
clients reconnect repeatedly, viewer counts lag, or different API nodes show
different behavior.

**Principle:** realtime delivery is an acceleration path. First prove whether the
domain state committed; then diagnose delivery. Never “fix” SignalR by bypassing
authorization.

## Impact assessment

Identify:

- feature (ride, bid, trip, chat, call, admin event);
- country/tenant and API release;
- one device/network or broad impact;
- single node versus cross-node pattern;
- event-to-UI delay and entity versions; and
- whether push/polling resync eventually converges.

Use dedicated test accounts and correlation IDs. Do not collect production hub
tokens or chat/location payloads.

## Diagnose from truth outward

### 1. Domain transaction

Confirm the expected ride/bid/trip/chat row and persisted monotonic entity version.
If the state did not commit, this is a domain/API issue, not SignalR. If the client
pressed Back and cancellation failed, it must remain/queue a durable cancellation
instead of simply leaving the screen.

### 2. Durable event

Confirm a dedicated lifecycle/outbox event exists and the handler is registered.
Do not use an unrelated event (for example `fare_updated`) as a cancellation
signal. Inspect outbox state/age and correlation without copying payload.

### 3. Hub authorization and groups

The hub accepts a dedicated sixty-second `discovery` or `trip` token; an ordinary
API bearer token is not a hub credential. Confirm user, role, tenant, country,
token version, token kind, trip/participant role where applicable, group naming,
and block/lifecycle policy. Broad driver discovery carries refresh cues only;
offer and bid contents are account-scoped. A System Administrator investigation
path is explicit and audited; admins do not silently join user chat groups.

### 4. Valkey backplane

- Is Valkey reachable over the expected protected connection?
- Does the account have the required pub/sub channel ACL?
- Does the channel prefix match on every API node?
- Are there connection, TLS, timeout, memory, or eviction warnings?
- Can a message sent from node A reach a test client connected to node B?

`NOPERM No permissions to access a channel` means authentication worked but the
ACL rejected pub/sub. Grant only the required channel commands/pattern. Do not
enable all commands or use an administrator account.

### 5. Client behavior

Check reconnect transitions, app lifecycle, subscription disposal, repository
merge by entity version, and bounded polling. A slow fallback interval can turn
a small realtime failure into a five- or thirty-second user-visible delay.

Do not mark every ride returned by the driver's feed as “viewed.” Explicit
per-ride visibility heartbeats are the source for viewer counts.

Bid mutation replay is encrypted and account-bound on supported mobile builds.
The bounded SQLite outbox retains the original idempotency key, request hash,
entity version, and authoritative offer expiry. Wrong-workspace or corrupt rows
are quarantined, malformed/missing expiry fails closed, and logout removes both
rows and the account key. This outbox authorizes no wallet, payout, security, or
arbitrary command replay.

### 6. Capacity

Inspect active connections, send rate, reconnect rate, API CPU/thread pool,
Valkey latency, network/socket limits, and load-balancer/WebSocket timeouts. A
reconnect storm may be the cause of saturation as well as a symptom.

## Containment

- Keep durable APIs available.
- Increase only bounded client refresh where safe; avoid a synchronized polling
  stampede.
- Route traffic away from a bad node if node-specific.
- Pause a noisy realtime producer if it threatens the backplane.
- If background telemetry is stale, expire driver online eligibility rather than
  showing a false live state.
- Preserve push fallback for committed high-value events.

## Recovery

1. Fix handler, token/group policy, backplane ACL/configuration, or client merge.
2. Test two devices connected to different API nodes.
3. Publish a new entity version or let clients resync authoritative state; do not
   replay arbitrary old UI events without version checks.
4. Restore normal polling intervals after realtime stability.
5. Watch reconnect and outbox/backplane latency for consecutive healthy windows.

## Deterministic verification scenario

With dedicated rider and driver accounts:

1. rider creates a ride;
2. rider adjusts fare;
3. driver opens that ride (viewer heartbeat);
4. driver bids, withdraws, and sends replacement counter;
5. rider rejects or accepts;
6. both exchange idempotent chat messages;
7. driver arrives, starts, and completes—or one party cancels;
8. repeat with disconnect after each commit, duplicate taps, node switch,
   background/resume, and out-of-order event delivery.

Assert both clients converge to server state quickly, no stale offer remains, no
message duplicates, closed trips cannot call/chat, and correlation/telemetry has
no token or payload.

## Rollback

If a new realtime release causes broad churn, restore the last compatible binary
or disable the narrow fan-out path while durable resync remains available. Do not
roll back domain data or remove entity versions. If a channel prefix changed,
ensure all nodes share one value before reintroducing traffic.
