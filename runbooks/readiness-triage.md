# Runbook: Readiness and Incident Triage

## Interpret the endpoints

- **Liveness** answers whether the process can respond.
- **Readiness** answers whether it is safe to serve normal traffic.

## Triage order

1. Capture time, service version, correlation ID, status, and sanitized readiness
   fields.
2. Determine whether the issue is schema, MySQL, Valkey, outbox/worker,
   reconciliation, required provider, configuration validation, or process
   saturation.
3. Compare with deployment/change history and dependency dashboards.
4. Remove only the affected node/country/capability from service where possible.
5. Follow the domain runbook; do not globally disable security, rate limiting,
   reconciliation, or schema validation to make readiness green.
6. Verify recovery for two consecutive observation windows.

## Common decisions

- Schema drift → [schema alignment](schema-alignment.md)
- Valkey failure → [Valkey degradation](valkey-degradation.md)
- Outbox lag/failure → [outbox recovery](outbox-recovery.md)
- Provider failure → [provider outage](provider-outage.md)
- Wallet reconciliation exception → stop cashout and reconcile accounting before
  re-enabling it.
