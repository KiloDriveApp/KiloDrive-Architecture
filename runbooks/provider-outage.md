# Runbook: Provider Outage

## Scope

Applies to maps, push, SMS, WhatsApp, email, social login, payments, store
billing, LiveKit, or malware scanning.

## Response

1. Confirm the failure with a dedicated non-user canary and provider status;
   never test by messaging a real user without consent.
2. Classify timeout, authentication/permission, quota, policy rejection,
   malformed request, provider incident, or local network failure.
3. Disable the canary during maintenance if necessary; do not disable the
   production limiter or security boundary globally.
4. For notifications, let durable outbox retry or select an approved backup only
   for eligible transient failures.
5. For payments, freeze repeated mutation, reconcile unknown captures, and keep
   entitlement/cashout fail closed.
6. For maps, provide only the documented safe fallback; do not fabricate route or
   toll accuracy.
7. For scanner failure, keep uploads quarantined.
8. Verify recovery through canary, backlog drain, user-facing state, and audit.

Provider credentials and raw error payloads remain restricted.
