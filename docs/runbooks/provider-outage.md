# Runbook: external provider outage or degradation

- **Owner:** Platform operations with the owning product domain
- **Status:** Operational policy
- **Last exercised:** Record the most recent provider failover/tabletop date here
- **Related architecture:** [AWS messaging](../aws/messaging.md), [observability](../architecture/observability.md), [documents/media/voice](../architecture/documents-media-voice.md)

## Purpose and safety boundary

This runbook covers maps, geocoding, routing, push, SMS, voice OTP, WhatsApp,
email, social identity, payments, store billing, malware scanning, LiveKit, and
other remote providers. Its purpose is to preserve committed KiloDrive state,
communicate honest degraded behavior, and recover without duplicating an
external mutation.

The most dangerous provider failure is not always a clear rejection. A timeout
may occur **after** the provider accepted a payment, message, or recording start.
Treat that as an unknown outcome and reconcile it with a stable reference before
retrying.

## Trigger and customer symptoms

- consecutive non-user canary failures;
- provider-stage latency or error rate outside its observed budget;
- notification/outbox oldest age growing;
- payment/store acknowledgement pending beyond policy;
- maps, route, autocomplete, or toll provider-stage timeout;
- upload scans remaining quarantined;
- social-login validation failing broadly;
- call signalling, TURN, or egress degradation; or
- quota, sandbox, permission, sender, template, or regional policy rejection.

One failed canary is evidence, not a root cause. Compare it with application
traffic, provider status, recent configuration/deployment changes, quotas, and
network observations.

## Preconditions

- Use dedicated non-user canary destinations and provider sandbox/test accounts.
- Identify the provider owner, fallback policy, last healthy revision, and
  customer-facing degraded state.
- Keep credentials, destinations, request/response bodies, payment tokens,
  message bodies, object URLs, and social tokens out of incident channels.
- For money movement, establish whether new mutations must be paused until
  unknown outcomes reconcile.
- For security/identity or malware scanning, fail closed unless a reviewed
  alternate proof path exists.

## Classify before acting

| Class | Examples | Retry posture |
| --- | --- | --- |
| Local configuration | wrong region, disabled adapter, missing secret reference | correct configuration; do not retry blindly |
| Authentication/authorization | expired credential, IAM denial, invalid sender authorization | fix narrow permission/identity |
| Policy/permanent request | opted-out destination, bad template, invalid token, unsupported country | no provider failover loop |
| Quota/throttle | spend limit, rate quota, provider 429 | respect provider delay and back-pressure |
| Network/transient service | connect timeout, provider 5xx | bounded retry for safe/idempotent work |
| Unknown mutation result | timeout after capture/send/start | reconcile by stable provider reference first |
| Application defect | malformed adapter payload, parser error, missing outbox handler | contain release and fix code |

Failing over a permanently invalid destination from one provider to another can
be abusive and expensive. Backup routing applies only to operations and failure
classes approved by policy.

## Diagnose from committed truth outward

1. **Domain state:** Did the ride, wallet, membership, document, or notification
   intent commit? If not, investigate the command first.
2. **Durable intent:** Is there an outbox/provider-attempt row? Check safe type,
   state, attempt, availability, age, provider, and correlation ID—never payload.
3. **Adapter:** Confirm enabled provider, endpoint/region, timeout, credential
   source, and deployed binary. A settings file alone does not prove active code.
4. **Provider:** Check safe status APIs/dashboard, quotas, sender/template
   approval, suppression/opt-out state, and regional incident status.
5. **Network:** Check DNS, TLS, proxy/egress, and connection saturation.
6. **Consumer:** Check worker heartbeat, concurrency, queue/outbox age, poison
   messages, and circuit-breaker state.
7. **Client:** Confirm the app shows a bounded retryable/queued/degraded state
   rather than spinning or reporting success early.

Use one known synthetic correlation ID to follow the path. Do not “debug” by
turning on body logging in production.

## Channel-specific containment

### Notifications

Keep notification intent durable. Use the approved backup only for eligible
transient failures and preserve one logical notification reference. Security
messages are never silently downgraded to an insecure channel. User requests do
not wait synchronously for email/SMS completion.

### Maps and routing

Separate autocomplete, place details, route, map match, toll matching, and
geocode timing. Use a cached/reference fallback only where accuracy is honest.
Do not fabricate a toll-free answer or an exact route from a straight-line
estimate. Disable affected calculations with a useful explanation if their
correctness boundary is unavailable.

### Payments and store billing

Pause repeated capture/acknowledgement where outcomes are unknown. Reconcile by
provider transaction/purchase token and local payment reference. Never grant or
revoke entitlement solely because a client timed out. Cashout stays fail closed
when ledger reconciliation is not clean.

### Upload scanning

Keep new objects quarantined. Do not switch a production scanner to a null or
allow-all implementation. Existing approved content can remain available if its
authorization and integrity are unaffected.

### Identity providers

Preserve password/passkey/OTP alternatives according to policy. Do not link a
social identity by unverified email to work around a provider outage. Security
ceremonies that need unavailable distributed state fail closed.

### LiveKit and voice

Follow [LiveKit voice](livekit-voice.md). Provide GSM fallback only where the
trip, membership, privacy, and product policy permit it.

## Recover

1. Correct or wait out the narrow fault; avoid unrelated configuration edits.
2. Validate with the provider's dedicated canary or sandbox path.
3. Reconcile unknown external results before redrive.
4. Resume one bounded worker/provider route and observe a small batch.
5. Drain backlog with rate and provider quotas respected. Avoid a recovery
   stampede that causes a second outage.
6. Verify user-facing status and durable records converge.
7. Return primary/backup routing to its documented normal state.

Messages and provider calls can be at least once. Handlers need idempotency,
conditional state transitions, and stable external references. Never “solve” a
backlog by deleting intents or manually marking them successful.

## Verification

- The non-user canary is healthy for the required consecutive windows.
- Real pending/oldest-age metrics decrease without a new failure spike.
- No duplicate payment, entitlement, message, recording, or document release
  occurred.
- Quotas, throttles, and circuit breakers returned to stable levels.
- Readiness reports required versus optional provider state accurately.
- The mobile/portal UX shows a useful recovered state and no infinite spinner.
- Stored diagnostics contain only provider ID, sanitized status, latency, and
  correlation ID.
- The operator alert recovers and a human destination receives the transition.

## Rollback or abort criteria

Abort failover/redrive if duplicates appear, unknown money outcomes grow,
provider quota is being exhausted, PII enters telemetry, or the backup has not
been independently verified. Restore the last known routing/configuration and
keep the risky feature paused while committed domain state remains available.

## Evidence and follow-up

Retain provider name, operation class, safe receipt/reference, correlation ID,
timestamps, latency/status aggregates, deployment/config revision, alarm state,
and reconciliation result. Never copy provider payloads or destinations into the
postmortem.

Add a contract or failure-injection test for the root cause, review timeout and
quota assumptions, update the provider owner/rollback/recovery record, and
schedule a repeat exercise. Thresholds change only after legitimate peak data,
not because an alarm was inconvenient.
