# Public Operations Runbook Index

These runbooks describe decision flow and safe recovery at an architectural
level. Exact commands, hosts, resource names, credentials, escalation contacts,
and defensive thresholds live in restricted operational documentation.

| Runbook | Trigger | Primary outcome |
| --- | --- | --- |
| [API deployment](api-deployment.md) | Approved release | Deploy and prove a reproducible binary |
| [Schema alignment](schema-alignment.md) | Contract drift/change | Restore fingerprint parity safely |
| [Readiness triage](readiness-triage.md) | Degraded/unhealthy readiness | Isolate the failing dependency |
| [Valkey degradation](valkey-degradation.md) | Cache/backplane/security-state failure | Preserve correctness and restore distribution |
| [Outbox recovery](outbox-recovery.md) | Lag or failed messages | Recover side effects without duplication |
| [Provider outage](provider-outage.md) | Messaging/maps/payment outage | Degrade or queue according to risk |
| [LiveKit voice](livekit-voice.md) | Call/TURN/egress incident | Restore calls and reconcile recordings |
| [Upload quarantine](upload-quarantine.md) | Scan timeout/rejection | Keep files private and recover scanner |
| [JWT rotation](jwt-key-rotation.md) | Scheduled or emergency rotation | Replace signing key without accepting unknown keys |
| [Country activation](country-activation.md) | New/re-enabled country | Prove data and policy readiness before activation |
| [Backup and recovery](backup-and-recovery.md) | Data-loss/recovery exercise | Restore a consistent control/cell state |
| [Security incident](security-incident.md) | Suspected compromise | Contain, preserve evidence, recover, notify |
| [Authentication/session](authentication-session.md) | Login, token, passkey, or 2FA incident | Restore account security without weakening controls |
| [Wallet reconciliation](wallet-reconciliation.md) | Ledger/provider mismatch | Reach zero unexplained money before enabling cashout |
| [Realtime/SignalR](realtime-signalr.md) | Delayed or missing events | Restore realtime while durable state stays correct |
| [Geospatial degradation](geospatial-degradation.md) | Route/geocode/toll failure | Preserve safe UX and pricing truthfulness |
| [Mobile release](mobile-release.md) | Android/iOS release | Certify binary, permissions, privacy, and store metadata |
| [Portal/website release](portal-website-release.md) | Browser-app release | Preserve headers, routes, localization, and API parity |
| [Notification canaries](notification-canaries.md) | Provider health validation | Prove channels without using customer destinations |
| [Privacy/deletion](privacy-deletion.md) | Access/deletion request | Coordinate control and country completion audibly |

## Universal incident rules

1. Protect users and financial integrity first.
2. Assign an incident owner and correlation/evidence record.
3. Do not paste secrets or customer payloads into tickets or chat.
4. Prefer reversible maintenance controls and traffic isolation.
5. Reconcile unknown provider and financial outcomes before retry.
6. Record timeline, decisions, validation, rollback, and follow-up.
