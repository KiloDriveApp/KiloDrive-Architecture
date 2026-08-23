# Observability

## Signals

The API emits structured logs, traces, metrics, health/readiness results, audit
events, and provider attempt records. OpenTelemetry instruments ASP.NET Core,
HTTP clients, runtime behavior, request pipeline stages, database/provider work,
matching, accounting, wallets, outbox, and operations.

OTLP export can feed an AWS Distro for OpenTelemetry collector or another
approved backend. CloudWatch-compatible logs, metrics, dashboards, alarms, and
SNS notifications provide the AWS operating view.

## Data minimization

Telemetry must not contain:

- access/refresh tokens, passkeys, OTPs, secrets, or signed URLs;
- message bodies, email addresses, phone numbers, or document contents;
- payment instruments, bank instructions, precise customer routes, or raw
  location payloads; or
- exception stack traces in client responses.

Allowed diagnostic dimensions are bounded: operation, provider, outcome, status
class, tenant/country surrogate where approved, service version, deployment
environment, latency, queue lag, and correlation ID.

## Service-level views

Dashboards separate application time from database, cache, and provider time.
Warm-cache p50/p95/p99 is measured independently. Alerts require sustained
breaches rather than single samples, and thresholds are tuned from legitimate
peak traffic.

Readiness includes schema contract state, outbox lag/failure, worker heartbeat,
wallet reconciliation, required providers, and Valkey reachability. Liveness only
states whether the process can respond; it does not imply dependency readiness.

## Audit versus telemetry

Audit records answer who performed a governed action and what changed. Telemetry
answers how the system behaved. They have different retention, access, and
privacy rules and must not be conflated.
