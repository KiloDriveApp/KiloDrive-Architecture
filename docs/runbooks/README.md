# Operations Runbook Guide

- **Owner:** Platform operations and service owners
- **Status:** Maintained index and operating standard
- **Last exercised:** Not applicable; reviewed whenever the runbook set changes
- **Related architecture:** [Architecture guide](../architecture/README.md) and [system context](../architecture/system-context.md)

A runbook is a decision aid for a tired engineer working under pressure. It
should help that engineer protect users, establish facts, choose a reversible
action, and prove recovery. It should not be a wall of commands copied from one
person's terminal history.

The public runbooks in this repository explain safe decision flow. Exact
resource names, access paths, paging contacts, approved thresholds, and
environment-specific commands remain in restricted operational material.

## Runbook index

| Runbook | Use it when | Recovery goal |
| --- | --- | --- |
| [API deployment](api-deployment.md) | An approved API build is being released or rolled back | Prove the intended binary and compatible schema are serving traffic |
| [Portal and website release](portal-website-release.md) | A browser application is being released | Preserve security headers, localization, API contracts, and rollback |
| [Mobile release](mobile-release.md) | Android or iOS binaries are being prepared | Certify the exact signed artifacts, permissions, native dependencies, and store metadata |
| [Schema alignment](schema-alignment.md) | Startup/readiness reports schema drift | Align reviewed metadata without guessing or deleting unexplained data |
| [Country activation](country-activation.md) | A country is being enabled or restored | Prove schema, rules, providers, legal controls, and operational ownership |
| [Readiness triage](readiness-triage.md) | Readiness is degraded or unhealthy | Identify the dependency and preserve truthful traffic handling |
| [Ride dispatch](dispatching.md) | Drivers do not receive, see, or act on current offers | Restore durable and realtime dispatch without duplicating assignments |
| [Active-trip location and privacy](active-trip-location-and-privacy.md) | Trip location will not start, is stale, survives a terminal trip, or conflicts with the privacy/store declaration | Restore truthful trip telemetry and prove collection stops at the authorized boundary |
| [Capacity baseline](capacity-baseline.md) | A launch, scale change, or scheduled review needs a controlled operating envelope | Find the first bottleneck with safe fixtures, bounded ramps, and verified cleanup |
| [Outbox recovery](outbox-recovery.md) | Pending age, failed rows, or worker heartbeat alarms | Deliver or explicitly resolve promised side effects exactly once economically |
| [Realtime and SignalR](realtime-signalr.md) | One device changes state but another stays stale | Restore delivery and client convergence while database truth remains authoritative |
| [Valkey degradation](valkey-degradation.md) | Cache, backplane, location, or short-lived state fails | Protect security/correctness and rebuild replaceable distributed state |
| [Provider outage](provider-outage.md) | Maps, messaging, payments, or another external service fails | Degrade, queue, reconcile, or fail closed according to business risk |
| [Notification canaries](notification-canaries.md) | A channel health probe fails or must enter maintenance | Validate providers without exposing customer destinations or message content |
| [Geospatial degradation](geospatial-degradation.md) | Route, geocode, map-match, or toll calculation is unavailable or implausible | Avoid false precision and preserve safe fallbacks |
| [LiveKit voice](livekit-voice.md) | Calls, TURN, rooms, tokens, or recording egress fail | Restore authorized voice and reconcile consent/recording state |
| [Upload quarantine](upload-quarantine.md) | Scanner timeout, rejection, or retrieval issue occurs | Keep documents private and quarantined until trustworthy disposition |
| [Authentication and sessions](authentication-session.md) | Login, OTP, refresh, passkey, 2FA, or logout behavior is unsafe | Restore account access without weakening security boundaries |
| [JWT key rotation](jwt-key-rotation.md) | Scheduled or emergency signing-key change is required | Introduce a new key, preserve bounded overlap, and retire the old key safely |
| [Security incident](security-incident.md) | Compromise, abuse, leakage, or unauthorized access is suspected | Contain, preserve evidence, assess impact, recover, and notify appropriately |
| [Wallet reconciliation](wallet-reconciliation.md) | A ledger, hold, journal, cashout, or provider total disagrees | Reach zero unexplained money before enabling affected financial operations |
| [Backup and recovery](backup-and-recovery.md) | Data loss is suspected or a restore exercise is running | Restore a consistent control/cell point and prove application invariants |
| [Privacy and deletion](privacy-deletion.md) | An access, deletion, legal-hold, or retention request needs coordination | Complete and audit work across control and authorized country cells |

## Severity without drama

Use the organization's restricted severity matrix, but reason about impact in
four dimensions:

- **Safety:** Can a rider, driver, renter, or member of the public be harmed?
- **Financial integrity:** Can money be duplicated, lost, held incorrectly, or
  reported inaccurately?
- **Security and privacy:** Can an unauthorized person gain access, or can
  sensitive data leave its intended boundary?
- **Availability and trust:** How many users or countries are affected, and is
  the system giving them truthful status?

An incident with low request volume can still be severe if it affects account
takeover or money. A noisy provider outage can be less severe if the product
fails safely and durable work remains recoverable.

## The universal incident cycle

### 1. Detect and declare

Confirm the alert is current, identify customer-visible symptoms, assign an
incident owner, and create a restricted evidence record. Record times in UTC;
display local time separately when it helps responders.

### 2. Contain

Choose the smallest reversible control that stops harm. Examples include
disabling one provider route, pausing a worker, failing a financial action
closed, taking stale drivers offline, or blocking a compromised key.

Do not perform a broad restart or database edit simply because it is familiar.
Restarts erase volatile evidence and can amplify retries.

### 3. Establish authoritative state

Start with the owner of truth. For a ride, inspect the country-cell state and
version before looking at a push notification. For money, inspect immutable
subledger/journal/provider references before a dashboard total. For identity,
inspect the control plane before a country projection.

### 4. Diagnose one boundary at a time

Follow the correlation ID through edge, API, database, outbox, broker, provider,
and client. Compare timestamps and versions. Distinguish absence of evidence
from evidence of absence.

### 5. Recover safely

Prefer a supported replay, conditional transition, compensating action, or
rollback. Unknown provider outcomes are reconciled before retry. Immutable
financial history is corrected by reversal, never mutation.

### 6. Verify from the user's perspective

Green infrastructure is necessary but insufficient. Verify the public health
contract, the affected workflow, backlog convergence, error rate, and the
actual client experience. Use dedicated non-user fixtures and canaries.

### 7. Close and learn

Record impact, root cause, contributing conditions, timeline, evidence,
recovery, and follow-up owners. Add the regression test and update the runbook
while the details are still fresh.

## Evidence record

Keep the following without copying sensitive payloads:

- incident and correlation identifiers;
- build/commit and schema contract versions;
- country, tenant, feature, and bounded event type;
- sanitized state transitions and entity versions;
- worker heartbeat, queue age/count, and provider request identifier;
- UTC timeline of decisions and actions;
- recovery and rollback verification; and
- links to restricted evidence under the proper retention policy.

Never place passwords, tokens, OTPs, full phone numbers, addresses, document
contents, message bodies, presigned URLs, or raw provider payloads in incident
chat or metric labels.

## Unknown outcomes

An unknown outcome deserves its own category. It occurs when the caller cannot
tell whether another system performed an action—for example, a timeout after a
payment provider may have captured funds.

The safe response is:

1. keep the original idempotency/provider reference;
2. query or consume authoritative provider state;
3. compare it with local durable state;
4. finalize or compensate exactly once; and
5. only then consider another provider request.

“Try again” is dangerous advice when the previous attempt may have succeeded.

## Command hygiene

- Resolve the exact environment and target before any mutation.
- Use read-only queries first.
- Prefer reviewed scripts with hashes and explicit preconditions.
- Never build destructive targets from unresolved variables, broad globs, or a
  workspace root.
- Capture pre- and post-state counts for material changes.
- Keep a tested rollback or compensating action.
- Do not weaken validation, disable reconciliation, or mark work successful
  merely to clear an alert.

Use [_template.md](_template.md) when adding a runbook.
