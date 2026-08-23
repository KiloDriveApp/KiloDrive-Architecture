# Scaling and Capacity Planning

## Capacity is a chain, not one number

“How many users can KiloDrive handle?” sounds like a single-number question. It
is not. Ten thousand registered users who open the app once a week are easier
than five hundred drivers publishing location at the same moment that riders
create trips and a messaging provider slows down.

Capacity is the smallest safe limit in a chain:

```text
edge -> API -> connection pools -> country cell -> Valkey -> queues/workers
     -> maps/messaging/payments -> device networks
```

If the database can process a thousand writes per second but the API pool
permits only thirty concurrent connections, the pool may become visible first.
If local processing is fast but a map provider takes two seconds, quote latency
is provider-bound. If API and database are healthy while one outbox worker is
stuck, riders can complete trips but receive late receipts.

This chapter explains how KiloDrive reasons about those limits without
publishing live infrastructure sizes or pretending a laboratory benchmark is a
guarantee.

## Start with workload shapes

Registered-account count is useful for business planning, but it is a weak
capacity input. Model actions that consume resources.

| Workload | Typical shape | Main pressure |
| --- | --- | --- |
| Authentication burst | Short request, password/OTP/provider work, control-plane write | CPU for password hashing, control DB, messaging quota |
| Place autocomplete | Several reads while a rider types | Provider latency/quota and cache hit rate |
| Fare quote | Route/geocode plus local pricing | Map provider, route cache, CPU/serialization |
| Ride creation | Short transactional write plus outbox | Country DB locks and dispatch fan-out |
| Driver telemetry | Frequent small updates per online driver | Network, Valkey commands, persistence batching |
| Available rides | Repeated filtered reads | Valkey GEO, country indexes, eligibility joins |
| Bid burst | Contended mutations on popular requests | Row locks, idempotency, entity version conflicts |
| SignalR presence | Long-lived connections with small messages | Sockets, memory, backplane bandwidth |
| Trip completion | State, wallet, payment, journal, outbox in one transaction | Database locks and ledger indexes |
| Report generation | Infrequent but CPU/memory/IO heavy | Query range, renderer memory, artifact storage |
| Voice call | Sustained bidirectional media | LiveKit/TURN CPU and network bandwidth |

The same daily-active-user count can produce very different combinations of
these workloads. Build a scenario such as “weekday commute peak with many
online drivers, concurrent ride searches, and a messaging slowdown,” then test
the parts under controlled conditions.

## A little queueing theory without the fear

Little's Law is a helpful approximation:

```text
concurrency = throughput × average time in system
```

If an endpoint receives 100 requests per second and each occupies a database
connection for 100 milliseconds on average, it needs roughly ten concurrent
connections just for that endpoint. At 500 milliseconds, it needs roughly
fifty. Tail latency matters: a slow provider or lock wait can consume the pool
even when request rate does not change.

The lesson is not to calculate one perfect number. It is to measure service
time at each stage, keep transactions short, and leave headroom for bursts and
failure recovery.

## Customer-facing latency budgets

KiloDrive treats performance as a budget split across stages rather than an
undifferentiated endpoint stopwatch. A warm quote might include:

```text
request and authorization
  + cache lookup
  + route/geocode provider time when not cached
  + database/reference lookup
  + fare/traffic/toll calculation
  + serialization and network
```

The warm-cache p95 objective is measured separately from provider time. An
alert fires only when the warm p95 exceeds its approved threshold for two
consecutive windows; one cold request should not page an operator. Provider
latency still receives its own span, metric, quota, and alert.

Track p50, p95, and p99:

- **p50** describes the ordinary experience.
- **p95** reveals broad degradation and is useful for service objectives.
- **p99** reveals queueing, lock contention, cold paths, and rare provider
  stalls that averages hide.

Always pair latency with throughput, error rate, saturation, and queue lag. A
fast endpoint that rejects half its requests is not healthy.

## Scaling each layer

### Edge and IIS/API nodes

The edge absorbs common probes, terminates or forwards TLS according to policy,
applies WAF and rate limits, and caches only content declared safe. Application
authorization still happens in the API.

API nodes are stateless with deliberate exceptions moved to shared systems.
Before adding a second node, verify:

- SignalR uses the Valkey backplane and its ACL permits the channel namespace;
- passkey ceremonies and other single-use challenges use distributed storage;
- Data Protection keys are shared and durably protected where the framework
  needs them;
- idempotency records live in the owning database, not process memory;
- every node resolves the same country/tenant configuration and JWT public-key
  set; and
- local filesystem writes are not treated as shared storage.

Scale out when CPU, request concurrency, or long-lived connection handling is
the first limit and the shared-state checklist is green. Scale up when one
process or native dependency benefits from faster cores and operational
simplicity matters more than node redundancy. Usually the safe plan includes
both a tested vertical ceiling and a horizontal path.

### MySQL control plane and country cells

The control database receives authentication and global-directory work. Each
country cell contains local operational and financial contention. This split
lets a busy country be tuned independently.

Measure:

- active and waiting connections versus configured pools;
- query and transaction p95/p99;
- lock waits, deadlocks, and transaction retries;
- buffer-pool hit rate and disk latency;
- replication/backup lag where applicable;
- rows examined versus returned for critical queries; and
- outbox claim and completion rate.

Useful improvements usually arrive in this order:

1. remove an unbounded or non-sargable query;
2. add the correct composite index after verifying the access pattern;
3. shorten transactions and move provider work out of them;
4. eliminate chatty round trips and N+1 queries;
5. tune pool/server limits together, with measured headroom;
6. scale instance resources; and
7. add carefully scoped read replicas or further partitioning only when the
   consistency model permits it.

Increasing the connection pool alone can make matters worse by allowing more
concurrent work to fight for the same locks and IO.

### Valkey

Valkey serves short-lived distributed state, current geospatial position,
cache, and SignalR scale-out. Monitor memory, eviction, fragmentation,
connections, command latency, network, hot keys, GEO candidate size, and pub/sub
failures.

Use separate prefixes, TTL policies, and ACL permissions for workloads. A
credential that can read cache keys may not need to publish SignalR channels.
The platform once encountered an authenticated account that returned `NOPERM`
for the backplane channel: reachability was healthy, authorization was not.
Canary the command families the application actually uses.

Do not solve memory pressure by deleting unknown keys. Identify ownership,
expiry policy, and rebuild behavior first. Wallet or trip truth never belongs
only in Valkey.

### Outbox, EventBridge, and SQS

Dispatch has two related capacity paths:

- the SQL outbox provides transactionally durable intent and recovery; and
- EventBridge/SQS provide scalable fan-out, buffering, retry, and isolation.

Measure new messages per second, claim rate, completion rate, oldest pending
age, retry distribution, permanent failures, queue depth, age of oldest queue
message, dead-letter growth, and worker heartbeat. Queue depth alone is not
enough: a large queue may drain quickly, while one old poison message can reveal
a broken consumer.

Increase worker concurrency only after confirming downstream database and
provider capacity. Parallel workers can move the bottleneck rather than remove
it. Partition or serialize work that competes for the same ride or wallet.

### SignalR and mobile clients

Count concurrent connections, reconnect rate, connection lifetime, hub method
latency, backplane publish failures, outbound message rate, and client recovery
polls. Bound group membership and message sizes.

Realtime delivery is an acceleration path. The client merges events by a
persisted monotonic entity version, discards only truly stale data, and performs
a recovery read after reconnect. This keeps a dropped message from becoming a
permanent stale screen.

### Maps and routing

Autocomplete, place details, routes, traffic matrices, and OSRM matching have
different costs and quotas. Debounce type-ahead, cancel superseded reads, cache
short-lived place details, and measure each provider operation independently.

For matching, use cheap Valkey/spatial/straight-line filters before a bounded
road matrix. Sending every online driver to a route provider is an expensive
fan-out bug. For toll and route-deviation work, bound trace points before map
matching and fail honestly when route evidence is weak.

### LiveKit and TURN

Voice capacity is usually constrained by bandwidth before ordinary API CPU.
Peer-to-peer media may avoid server forwarding, but TURN relay and egress
recording send media through infrastructure. Estimate separately:

- concurrent rooms and participants;
- percentage of sessions requiring TURN;
- average codec bitrate plus protocol overhead;
- ingress and egress bandwidth;
- egress/transcoding CPU and memory;
- recording upload rate and object-storage throughput; and
- room/orphan cleanup work.

Run foreground, background, killed-app launch, network handoff, reconnect,
decline, timeout, and orphan-cleanup exercises on physical Android and iOS
devices. A synthetic token test does not certify call quality.

### External providers

Each provider has account-level quotas, destination rules, regional limits,
spend limits, sender approval, and failure semantics. Dashboards distinguish
local latency from provider latency and show remaining quota where the provider
makes it available.

Automatic retry is limited to safe reads unless the provider offers a stable
idempotency key and unknown-result reconciliation. Retrying a payment or message
submission blindly can duplicate customer-visible work.

## Controlled capacity testing

Production capacity work uses dedicated non-user fixtures and controlled ramps.
It does not point an uncontrolled stress tool at real users or financial
workflows.

### Before the run

1. Name the scenario, endpoints, fixtures, maximum request rate, duration, and
   abort thresholds.
2. Confirm operators, dashboards, rollback owner, and provider/test-account
   restrictions.
3. Verify fixture cleanup and unique idempotency references.
4. Establish a quiet baseline with the same deployment.
5. Confirm backups and normal health; do not benchmark through an active
   incident.

### During the run

Ramp gradually and pause at plateaus. Record the complete operating point:
throughput, concurrency, p50/p95/p99, errors, saturation, DB waits, pool use,
cache hit/latency, queue lag, provider time, and device/realtime behavior.

Abort when a pre-agreed customer-safety or data-integrity threshold is crossed.
The goal is to find the first limit without causing a cascade.

### After the run

Stop generators, verify fixture cleanup, wait for queues to drain, run ledger
and schema/readiness checks, and compare recovery to the baseline. Retain only
sanitized evidence and correlation identifiers.

## Finding the first customer-visible bottleneck

A bottleneck is not simply the highest utilization number. It is the resource
whose saturation first causes an important customer workflow to miss its
latency, error, freshness, or correctness objective.

| Observation | Possible interpretation | Next controlled check |
| --- | --- | --- |
| API CPU high, DB/provider time flat | Serialization, crypto, rendering, or app logic bound | Profile one fixture path; test larger API node |
| DB wait rises with pool occupancy | Query/lock/IO bound | Inspect top normalized queries and lock graph |
| Quote p95 rises only on cache miss | Provider or cold-route bound | Split provider span and test quota/cache policy |
| Outbox age rises, API stays fast | Worker/downstream throughput bound | Check handler duration, poison retries, provider quota |
| SignalR reconnects rise, reads stay healthy | Socket/backplane/network bound | Inspect backplane ACL/latency and node connection limits |
| Driver matching slows as candidates grow | Unbounded candidate enrichment/matrix fan-out | Verify GEO/pruning limits and indexes |
| Voice degrades while API is healthy | TURN/LiveKit bandwidth or device network bound | Compare relayed sessions, packet loss, egress load |

Change one material variable at a time. Otherwise, the team cannot tell which
change improved or harmed the system.

## Scale thresholds and cost bands

Do not publish one permanent threshold in source documentation. Establish
thresholds from legitimate peak traffic, tested headroom, recovery time, and
cost. A useful internal capacity record includes:

- current safe operating envelope;
- early-warning, scale, and emergency thresholds;
- required consecutive windows to avoid alert flapping;
- scale-up and scale-out action with expected lead time;
- rollback trigger;
- estimated infrastructure and provider cost band; and
- date, deployment version, dataset, and test evidence.

Review the record after large features, provider changes, schema/index changes,
instance changes, or meaningful traffic growth. Capacity expires as software
and traffic change.

## Failure exercises

Performance without recovery is an incomplete capacity claim. Exercise:

- API process crash during and after commit;
- MySQL connection loss and reconnect storm;
- deadlock and lock-wait timeout;
- stuck outbox handler and poison message;
- Valkey loss, empty-cache rebuild, and ACL denial;
- OSRM or map-provider timeout;
- EventBridge/SQS permission or availability failure with SQL recovery;
- messaging provider timeout/quota exhaustion;
- SignalR disconnect and multi-node reconnect;
- LiveKit/TURN instance or network failure; and
- restore from backup into an isolated environment.

For each exercise, prove customer-visible behavior, data invariants, alarm
delivery, runbook accuracy, and recovery time. “The process restarted” is not
enough if the wallet journal, ride state, or queue remained inconsistent.

## Common mistakes

### Quoting capacity from a laptop benchmark

A local benchmark may reveal code regressions, but it does not include real
network, provider, database, TLS, telemetry, or device behavior. Label the
environment and do not turn it into a sales promise.

### Disabling rate limits to make a test pass

Rate limits are part of capacity protection. Publish per-route budgets and
`Retry-After` behavior, then tune only after observing legitimate peaks. A load
test may use a dedicated approved policy; production limits stay on.

### Scaling workers without downstream headroom

More consumers can exhaust the database pool or provider quota faster. Measure
end-to-end drain rate and downstream saturation.

### Treating averages as user experience

An average can stay low while a meaningful minority waits several seconds.
Always inspect tail latency and error distribution.

### Caching authorization or money too aggressively

A fast stale answer is unsafe. Cache reference and provider data with explicit
TTL/invalidation. Revalidate permissions, compliance, assignment, and wallet
state at the locked decision point.

## Review checklist

- Is the workload described as operations per unit time, not registered users?
- Are p50/p95/p99, throughput, errors, saturation, and queue lag captured?
- Are provider and local times separate?
- Are warm and cold/cache-miss paths separate?
- Does the test use dedicated fixtures and production-safe abort limits?
- Is the first customer-visible bottleneck identified with evidence?
- Does each proposed scale action include cost, lead time, and rollback?
- Are shared-state prerequisites complete before adding API nodes?
- Were failure recovery and invariant checks exercised?
- Are dashboards and evidence free of payloads, tokens, contact data, and exact
  locations?

## Related reading

- [Hosting topology](hosting.md)
- [Observability](observability.md)
- [Realtime and events](realtime-and-events.md)
- [Geospatial processing](geospatial.md)
- [Financial systems](financial-systems.md)
- [Dispatch runbook](../runbooks/dispatching.md)
- [Readiness triage](../runbooks/readiness-triage.md)
