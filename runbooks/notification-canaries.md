# Runbook: Notification and Provider Canaries

## Setup

Provision dedicated non-user FCM/APNs devices, SMS/WhatsApp destinations, SES
mailbox, and LiveKit room/egress targets. Give the canary runner least-privilege
credentials and System Admin-only diagnostics.

## Operation

1. Run probes on a schedule appropriate to provider quotas and cost.
2. Record provider, operation, provider ID, latency, sanitized status,
   correlation ID, and timestamp only.
3. Alert on consecutive failures and route to the provider outage runbook.
4. Use maintenance controls during planned provider work.
5. Test primary and backup independently; do not send both to real users merely
   because the primary returned a policy/user error.

Never store message bodies, destination addresses/numbers, tokens, or provider
credentials in canary results.
