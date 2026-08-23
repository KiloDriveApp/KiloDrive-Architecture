# Capacity Baseline and Controlled Load Runbook

- **Owner:** Site reliability and performance engineering
- **Status:** Controlled benchmarking procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Scaling and capacity](../architecture/scaling-and-capacity.md) and [observability](../architecture/observability.md)

## Purpose

Use this runbook to establish or refresh KiloDrive's safe operating envelope.
It is not permission to run an unbounded stress test against production. The
goal is to find the first customer-visible constraint with dedicated fixtures,
controlled ramps, clear abort limits, and complete cleanup.

Read [Scaling and capacity planning](../architecture/scaling-and-capacity.md)
before the first exercise.

## When to run it

- before a market launch or material traffic increase;
- after changing API, MySQL, Valkey, OSRM, queue, LiveKit, or worker capacity;
- after a critical query/index, dispatch, or realtime architecture change;
- after provider quota or payment/messaging routing changes;
- when dashboards show sustained movement toward an existing limit; or
- on the scheduled capacity-review cadence.

Do not run through an unresolved incident, database change, provider
maintenance window, or incomplete financial reconciliation.

## Roles

| Role | Responsibility |
| --- | --- |
| Exercise lead | Owns scope, approval, timing, abort decision, and evidence |
| API/mobile operator | Confirms exact clients/builds and watches customer workflows |
| Database operator | Watches pools, queries, locks, IO, backups, and abort conditions |
| Cloud/realtime operator | Watches Valkey, queues, telemetry, edge, OSRM, and media |
| Financial verifier | Confirms fixture-only money and post-run zero reconciliation |
| Safety observer | Stops the exercise if production users, location, or emergency paths are affected |

One person may fill several roles in a small team, but the responsibilities
must still be named before the run.

## Required inputs

- reviewed scenario and traffic model;
- exact deployment version/commit and schema fingerprint;
- dedicated non-user fixture identities and provider destinations;
- fixture readiness evidence for every exercised workflow;
- normal baseline dashboard snapshot;
- route list and per-route rate-limit budget;
- maximum concurrency/RPS, plateau duration, and total duration;
- provider sandbox/production-safe quota approval;
- cleanup plan and owner; and
- internal abort thresholds and recovery contacts.

This public runbook intentionally does not list live host sizes, account IDs,
credentials, or exact defensive thresholds.

## Stop conditions

Stop new load immediately if any of these occurs:

- real customer records or destinations are touched;
- ledger/reconciliation shows unexplained money;
- error or latency crosses the approved safety threshold;
- database lock, connection, or IO pressure threatens ordinary traffic;
- outbox or queue age cannot recover at the current plateau;
- provider spend/quota approaches the approved cap;
- readiness becomes unhealthy for a correctness dependency;
- alerts fail to reach the confirmed operator channel; or
- cleanup identity or ownership is uncertain.

Stopping load is not the same as killing workers or databases. Let committed
work complete unless the incident lead identifies a specific containment need.

## Step 1: define one scenario

Do not begin with “100 virtual users.” Define actions and timing. Example:

```text
online fixture drivers publish permitted telemetry at the expected cadence
fixture riders autocomplete, quote, and create rides
eligible drivers retrieve and bid
one bid per ride is accepted
fixture trips are cancelled through a supported cleanup transition
notifications use dedicated non-user destinations
```

State whether the run includes cold cache, warm cache, provider calls, SignalR,
voice, reports, or settlement. Separate scenarios whose bottlenecks differ.

## Step 2: inventory the chain

Record the current capacity-relevant configuration without copying secrets:

- IIS/API node CPU, memory, process limits, and deployment count;
- API and control/country MySQL pool limits;
- MySQL topology, storage, buffer, and backup state;
- Valkey memory class, TLS/ACL health, clients, eviction policy, and namespaces;
- OSRM instances, region/data version, and resource headroom;
- EventBridge/SQS route, worker concurrency, and dead-letter policy;
- SignalR connection and backplane state;
- LiveKit/TURN bandwidth and egress capacity when included;
- S3 and provider quotas; and
- edge cache, WAF, and rate-limit behavior.

The inventory is restricted evidence. The public report contains component
classes and conclusions, not access details.

## Step 3: prove fixture readiness

Use supported fixture or administrative APIs. For a two-client ride test, the
driver readiness assertion should prove:

- verified licence and required evidence;
- compliant assigned primary vehicle;
- active applicable membership and limits;
- explicit online state and fresh permitted telemetry;
- no active assignment;
- correct tenant/country; and
- `canBid=true` with a reason breakdown.

Use funded fixture wallets, fake payment providers, and dedicated notification
destinations. Never “make the test pass” with inconsistent direct row edits.

## Step 4: capture the quiet baseline

For a representative no-load or normal-load window, capture:

- endpoint p50/p95/p99, throughput, and errors;
- API CPU, memory, threads, GC, requests, and connection count;
- MySQL query/transaction time, pool occupancy, waits, locks, deadlocks, IO;
- Valkey latency, memory, evictions, commands, and connections;
- outbox/queue depth, oldest age, handler time, retry, and failure;
- SignalR connections, reconnects, and publish failures;
- map/messaging/payment provider latency, error, and quota state; and
- warm/cold cache hit and route-stage metrics.

Use the same dashboard definitions during the run. Changing queries midway
invalidates the comparison.

## Step 5: ramp at plateaus

Start below expected normal traffic. Increase one workload dimension at a time
and hold long enough for pools, queues, caches, and autoscaling to settle.

At each plateau:

1. record offered and successful throughput;
2. capture p50/p95/p99 and error categories;
3. inspect resource saturation and database waits;
4. inspect provider duration/quota and cache hit rate;
5. inspect outbox/queue arrival versus drain rate;
6. confirm ordinary fixture UX and realtime convergence; and
7. decide continue, hold longer, or abort.

Do not disable rate limiting globally. A dedicated approved test policy can
separate fixture traffic while retaining bounded protection and realistic
`Retry-After` behavior.

## Step 6: introduce one failure

Failure exercises are controlled and separately approved. Examples include a
single API process recycle, Valkey interruption, OSRM timeout, provider timeout,
stuck fixture outbox handler, or database reconnect. Introduce only one at a
time.

Prove:

- the alarm reaches a confirmed human destination;
- committed state remains correct;
- clients show a bounded and honest degraded state;
- retry does not duplicate a command;
- queues drain after recovery;
- realtime clients reconcile; and
- the runbook recovery path works with current tooling.

## Step 7: stop and drain

1. Stop generating new load.
2. Record the stop time and final offered rate.
3. Let in-flight requests and workers settle.
4. Watch outbox/queue age return to its baseline.
5. Verify database connections, locks, CPU, IO, and Valkey memory recover.
6. Confirm no fixture session remains online unintentionally.
7. Run financial and schema/readiness checks.

If the system does not recover promptly, declare an incident rather than
silently extending the test.

## Step 8: clean up

Use canonical lifecycle transitions and fixture cleanup utilities. Cancel or
complete fixture trips according to scenario, revoke fixture sessions, expire
temporary objects, and delete or anonymize fixture data in a `finally` path.

Retain only sanitized evidence: build/schema version, scenario, aggregate
metrics, safe entity references, provider request IDs, and correlation IDs.
Never retain passwords, tokens, phone numbers, email addresses, coordinates,
message bodies, call media, or raw payloads in the public result.

## Step 9: determine the operating envelope

The safe envelope is below the point where sustained customer objectives begin
to fail and includes recovery headroom. Document:

- maximum tested plateau and its workload mix;
- first customer-visible bottleneck and supporting metrics;
- sustainable throughput with target latency, error, and freshness;
- queue drain and failure-recovery time;
- early-warning, scale-action, and emergency thresholds in restricted config;
- vertical and horizontal action with expected benefit and lead time;
- provider quota/cost constraint; and
- unresolved risk and next test.

Do not extrapolate linearly beyond the highest stable plateau. Queueing systems
often degrade sharply near saturation.

## Troubleshooting patterns

### Latency rises while CPU is low

Look for pool waits, database locks, provider duration, DNS/TLS delay, queue
backpressure, or thread starvation. Low CPU does not mean spare capacity.

### Throughput stops increasing while latency climbs

The system is saturating. Hold or stop the ramp, find the constrained resource,
and do not increase concurrency to force more work into the queue.

### Outbox age climbs after load stops

Check worker heartbeat, poison-message retry, provider throttle, queue consumer
permissions, and downstream database pool. Preserve failed-message metadata;
do not bulk mark work successful.

### Warm p95 is good but riders complain

Compare cache-miss/provider path, mobile rendering, network geography, and p99.
The dashboard may be observing a faster subset than the customer journey.

## Completion evidence

- scenario and approval record;
- exact application/schema/config version identifiers;
- fixture readiness and cleanup confirmation;
- baseline and plateau metrics;
- first bottleneck analysis;
- failure/recovery result;
- zero unexplained financial reconciliation;
- queue/outbox returned to normal;
- alarms and human notification verified; and
- reviewed next action, owner, and date.

## Escalation

If the run affects real users, cannot clean up fixtures, leaves unexplained
money, or fails to recover after load stops, convert the exercise to the
appropriate incident severity. Follow [Readiness triage](readiness-triage.md),
[wallet reconciliation](wallet-reconciliation.md), or the affected provider
runbook rather than continuing the ramp.
