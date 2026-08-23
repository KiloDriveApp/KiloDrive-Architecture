# AWS Messaging and Notifications

## Channels

KiloDrive's notification abstraction supports push, SMS, WhatsApp, voice OTP,
and email. AWS adapters can provide End User Messaging SMS/Voice, Social
Messaging for WhatsApp, and SES email. Alternate providers are available behind
the same interface for approved failover.

## Durable dispatch

Application handlers do not wait for SMS/email delivery. They enqueue a
`notification.send` outbox operation and commit the user-facing mutation.
Workers render approved templates, invoke the provider with an explicit timeout,
and persist sanitized delivery status. Provider retries are bounded and
idempotent.

## Template governance

One JSON template catalogue defines SMS bodies and email subject/HTML structure;
authorized tenant overrides are stored in the database and audited. Variables
are escaped according to channel. Secrets, tokens, and raw payloads never enter
logs.

## Provider selection

SMS and WhatsApp can use a configured primary and approved backup. Failover occurs
only for classified provider failures, not for invalid destination, consent,
opt-out, or policy rejection. Sender IDs, origination identities, WhatsApp
packages, and country permissions are deployment configuration.

## Canaries

Scheduled canaries use dedicated non-user destinations. Records contain provider
ID, latency, sanitized status, and correlation ID only. Maintenance controls
disable a canary without disabling real notifications globally.
