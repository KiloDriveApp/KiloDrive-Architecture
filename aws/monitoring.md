# AWS Monitoring and Telemetry

## Pipeline

KiloDrive exports sanitized OpenTelemetry traces and metrics to an approved
collector. CloudWatch receives operational metrics/logs, dashboards aggregate
service health, and alarms notify an SNS operations topic with confirmed human or
incident-management subscriptions.

## Dashboard domains

- HTTP latency/error/throughput by bounded route group;
- MySQL connection, waits, pool saturation, and query-stage time;
- Valkey latency, reachability, cache hit rate, and connection errors;
- outbox pending/failed count, oldest age, archive and worker heartbeat;
- EventBridge/SQS publish failures, queue age, redrive and dead letters;
- matching, realtime connection, and location freshness signals;
- provider latency/outcome for push, SMS, WhatsApp, email, maps and voice;
- wallet reconciliation and settlement exception counts; and
- LiveKit room/egress/TURN health and capacity indicators.

## Alarm design

Alarms use consecutive windows, missing-data semantics appropriate to the signal,
and runbook links. Alerts never include payloads, phone numbers, email addresses,
tokens, or message bodies. Thresholds are calibrated from legitimate traffic and
reviewed after capacity tests.

## Public-safe limitation

Exact namespaces, dimensions, alarm thresholds, topic identifiers, account
numbers, and dashboard links are restricted operational details.
