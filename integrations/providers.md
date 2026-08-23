# Third-Party Service Integrations

## Provider catalogue

| Domain | Implemented/configurable providers |
| --- | --- |
| Maps and routes | Google Maps; internal routing abstraction for future approved engines |
| Push | Firebase Cloud Messaging and Apple Push Notification delivery through configured credentials |
| SMS and voice OTP | AWS End User Messaging; Twilio adapter/fallback where approved |
| WhatsApp | AWS Social Messaging primary option; Twilio backup option |
| Email | Amazon SES |
| Social identity | Google, Facebook, and Apple token verification/linking |
| Store billing | Google Play Billing and StoreKit/App Store server validation |
| Payments | Stripe, PayPal, bank transfer, and non-production simulator |
| Voice | LiveKit rooms, TURN, and Egress |
| Malware scanning | ClamAV with a CDR-compatible policy boundary |
| Edge | Cloudflare-compatible trusted proxy and challenge integrations |
| Routing fallback | OSRM-compatible infrastructure in approved deployments |

## Common adapter contract

Each integration defines configuration validation, timeout, idempotency or
reconciliation strategy, health signal, protected diagnostic, sanitized logging,
feature/maintenance controls, and rollback. Provider SDK exceptions never flow
directly to clients.

## Data sharing

Only the minimum data required for the requested function is sent. Contact and
message content is not placed in general telemetry. Precise location goes only to
an approved routing/safety function and follows the applicable privacy policy.

Availability and commercial approval vary by country and provider account.
