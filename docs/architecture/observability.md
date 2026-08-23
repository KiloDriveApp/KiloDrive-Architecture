# Observability architecture

KiloDrive needs to answer two different questions quickly:

1. What did the platform do to a governed user or financial entity?
2. Why is the platform slow or failing right now?

Audit records answer the first. Logs, traces, metrics, health checks, provider
attempts, and dashboards answer the second. Mixing them makes telemetry too
sensitive and audit too unreliable.

## Signal model

### Correlation IDs

Every request accepts a validated identifier or generates one. The same value is
echoed on success, validation failures, redirects, concurrency conflicts, rate
limits, and sanitized 500 responses. Outbox/provider work carries it forward so
an operator can follow a logical flow without logging its payload.

Correlation IDs are useful search keys in logs/traces. Do not use them as metric
dimensions; they are high cardinality.

### Structured logs

Use stable operation names and fields. Prefer:

```text
operation=notification.send provider=ses outcome=timeout elapsed_ms=...
```

over a serialized request/response. Exceptions are sanitized before they reach
client Problem Details. Restricted server logs may retain necessary stack
information, but the logging pipeline still redacts tokens, destinations,
objects, payment data, and payloads.

### Distributed traces

Trace bounded stages: middleware, handler, database, Valkey, route/geocode,
matching, report render, serialization, provider, and outbox. Attach deployment,
service, route group, status, and safe provider fields.

### Metrics

Histograms capture latency distributions; counters capture outcomes; gauges
capture queue age or connection pressure. Labels stay bounded. Use route
templates, not full paths with IDs. Use error categories, not exception messages.

## Stage-level examples

### Fare/toll quote

Measure autocomplete, place detail, Google/OSRM route, geocode, toll matching,
database reference lookup, fare calculation, and serialization separately. Also
measure cache hit/miss and warm versus cold latency. This tells an engineer
whether to improve code, query/indexing, cache, or provider use.

### Reports

Measure authorization/query, row materialization, render (PDF/Excel), object or
response delivery, and serialization. A large report timeout should not be
“fixed” by increasing every HTTP timeout.

### Outbox

Record pending/failed counts, oldest age, claim/processing duration, retry class,
handler type (bounded), archive age, and worker heartbeat. Do not use message
payload as a dimension.

### Realtime

Track active connections, reconnects, send failures, backplane latency/errors,
entity-version resyncs, and durable-event-to-client delay. A SignalR send-success
counter alone cannot prove the phone rendered the update.

## Health endpoints

**Liveness** answers whether the process loop can respond. It should not depend on
every provider, or an optional provider outage will cause restart storms.

**Readiness** answers whether the node should receive normal traffic. KiloDrive's
readiness view can include schema contract, required provider configuration,
Valkey reachability, outbox pending/failed/lag, worker heartbeat, and wallet
reconciliation. A degraded state may still serve safe read/limited operations;
deployment policy decides traffic handling.

Readiness messages are bounded and never include connection strings, resource
identifiers, payloads, or exception dumps.

## OpenTelemetry and ADOT

The API can register OpenTelemetry sources/instrumentation and export traces and
metrics through OTLP. ADOT receives, batches, and forwards them to CloudWatch or
another approved backend. Export is an operational dependency, not a business
transaction dependency: a collector outage must not prevent ride acceptance.

Protect the collector endpoint and its IAM role. Set memory/batch limits so a
backend outage cannot consume the API host. Verify exporter retries are bounded.

## Redaction pipeline

Sensitive data can appear in several places:

- HTTP headers and cookies;
- inbound/outbound URL query strings;
- request/response bodies;
- exception messages;
- SQL parameter logging;
- Activity tags and baggage;
- provider SDK diagnostics; and
- alert text.

Redaction at only the logger is too late if OTel already captured the URL. The
application uses a sensitive-activity processor and sanitized error handling,
and the proxy/collector applies defense-in-depth filtering. Synthetic tests use
known fake secrets and assert they appear nowhere.

Particular care goes to SignalR's `access_token` query parameter and presigned S3
URLs. Drop the query attribute instead of trying to keep a partly masked token.

## Dashboards and SLO thinking

Start with a small set of user journeys: login, quote, ride creation, dispatch,
bid, acceptance, wallet read/transfer, notification, and call join. For each,
show request rate, p50/p95/p99, error rate, and dependency breakdown.

Then add saturation/correctness: pool use, DB waits, Valkey, queue age, dead
letters, worker heartbeat, reconciliation, provider quotas, and media quality.

Thresholds are hypotheses. Tune them after controlled capacity tests and
legitimate peaks. Preserve a concrete budget—such as sustained warm p95 over 500
ms for selected quote stages—without reacting to a single cold request.

## Alarm hygiene

An alarm without an owner, confirmed destination, or runbook is decoration.
Test notification end to end. During maintenance, suppress or annotate the narrow
alarm/canary rather than disabling monitoring globally.

Use safe text. A page should say which service, operation, environment, status,
duration, and runbook—not the phone number, trip route, message body, or token.

## Common anti-patterns

- Logging whole DTOs “temporarily.” Temporary logs become permanent archives.
- Using full URLs or user IDs as metric labels.
- Counting only 5xx while user-visible domain failures spike.
- Calling readiness “health” and restarting on every provider issue.
- Increasing timeouts before measuring provider versus application time.
- Declaring success because telemetry config files exist but the collector,
  dashboard, alarms, or subscription were never deployed.
- Silencing an outbox alarm by deleting failed rows.

## Verification routine

1. Send a synthetic request with a known correlation ID.
2. Follow it through API, database stage, outbox, and provider attempt.
3. Confirm the response retains hardening headers on success and forced failure.
4. Search every sink for seeded fake secrets/PII and verify none appears.
5. Stop Valkey, collector, and a fake provider separately; observe correct
   readiness, degradation, and alarms.
6. Trigger and acknowledge alarms through the actual operator destination.
7. Confirm the linked runbook contains usable recovery and rollback steps.
