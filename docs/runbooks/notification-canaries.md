# Runbook: notification and provider canaries

- **Owner:** Messaging operations and provider reliability
- **Status:** Operational canary procedure; disabled until dedicated destinations are approved
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [AWS messaging](../aws/messaging.md), [realtime and events](../architecture/realtime-and-events.md), and [observability](../architecture/observability.md)

Canaries prove that a provider path works before a real user depends on it. They
are synthetic operations sent to dedicated, non-user destinations. They are not
a licence to message employees' personal phones every few minutes.

## Preconditions

The canary runner stays disabled until both operator attestations are true:

- dedicated non-user destinations are configured; and
- least-privilege provider credentials are confirmed.

Destinations are injected from protected environment/secret references. Do not
put registration tokens, phone numbers, WhatsApp destinations, or email
addresses in Git or ordinary application settings.

Supported transports include FCM, APNs, primary/backup SMS, primary/backup
WhatsApp, SES, LiveKit token/room/egress, and opt-in AWS voice. AWS voice is not
part of the default provider list; add it only when the destination country,
origination identity, quota, IAM, cost, and dedicated non-user voice destination
are approved. Provider availability remains deployment-specific.

The runner's accepted result is only the first evidence item. Device-receipt
ingestion exists for FCM/APNs, and AWS WhatsApp has delivery and inbound-reply
correlation. Other delivery/inbound evidence named by the certification contract
must have an approved, authenticated producer before that provider can become
certified. A missing producer is not repaired by labelling provider acceptance as
delivery.

## What a result may contain

- normalized provider name;
- operation/probe type;
- safe provider receipt ID;
- `healthy`, `failed`, `timeout`, `maintenance`, or `not_configured` status;
- bounded sanitized reason code;
- latency;
- correlation ID; and
- check timestamp.

It must not contain destination, message body, OTP, token, credential, room
secret, audio/object URL, or raw provider response.

## Enabling scheduled probes

1. Provision one destination per channel/provider route. A single device token
   is not proof of both Android FCM and iOS/APNs delivery.
2. Create a role/API credential limited to the canary operations/resources.
3. Test each provider manually through the protected System Administrator
   diagnostic endpoint.
4. Confirm safe persisted results and telemetry.
5. Set provider quotas, timeout, consecutive-failure threshold, cooldown, and
   retention.
6. Enable scheduling. Use a longer interval for expensive egress than lightweight
   token checks.
7. Trigger a controlled failure and confirm the alert reaches a confirmed human
   destination with a runbook link.

Do not enable every provider in the list if it is intentionally unused. Either
remove it from the configured provider set or keep `AlertOnNotConfigured` false
according to policy. Repeated warnings about every unconfigured channel usually
mean the scheduler was activated before readiness.

## Responding to a failed canary

1. Check whether maintenance mode is active and properly reason coded.
2. Confirm failure is consecutive and not a single cold/network sample.
3. Compare synthetic failure with real notification outbox/provider metrics.
4. Classify configuration, credential/IAM, quota, provider incident, template,
   destination, network, or application adapter.
5. Test the provider's status and safe diagnostic path; do not switch to a real
   user's destination.
6. Follow [Provider outage](provider-outage.md) for containment/failover.

### Provider-specific clues

- FCM/APNs: expired/revoked device registration, Firebase/APNs credential,
  environment mismatch, or app bundle/project configuration.
- AWS SMS/voice: production access, destination country, origination identity,
  protect configuration, spend limit, or IAM.
- WhatsApp: sender registration, approved template/language, package/signature,
  destination opt-in, or provider routing.
- SES: sandbox/identity/region/configuration set, suppression, or IAM.
- LiveKit token: API key/secret/URL; room: signalling/admin reachability; egress:
  worker, consent-safe fixture, S3/KMS/role, or capacity.

## Primary and backup routing

Probe primary and backup independently. A backup should not be declared healthy
because the primary works. During a real outage, fail over only transient/
eligible operations. Permanent user/policy errors are not retried through the
backup.

## Maintenance mode

Maintenance is deployment configuration at this baseline, while the System
Administrator diagnostics surface is read-only for that state. Change it through
the reviewed configuration/release path, record a safe reason code and owner,
then verify the scheduler and diagnostics after deployment. It stops scheduled
and manual probes without erasing history; it does not disable real notification
delivery globally. Do not describe this as an in-app runtime toggle until a
separately authorized, audited mutation contract exists.

## Recovery and verification

- Run the failed canary manually and observe the required evidence set, not only
  provider acceptance.
- Observe at least the configured number of scheduled healthy windows.
- Verify real outbox oldest age/failure count drains normally.
- Verify backup routing returned to intended state.
- Search stored results/logs/alerts for destinations, bodies, and tokens.
- Check the alert transitions to OK/recovery and reaches operators.
- Record root cause and whether a configuration/startup guard should prevent
  recurrence.

## Cost and privacy notes

Canaries consume provider quota and may create data in external systems. Use the
lowest useful frequency, retention, and content. A dedicated mailbox/device/phone
still needs access control and lifecycle ownership. Delete/rotate destinations
when the owning test device or provider identity changes.
