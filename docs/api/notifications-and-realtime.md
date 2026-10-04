# Notifications, push binding and realtime

[API Guide](README.md) · [Notification reference](reference/notifications.md)

## A push token is not an account identifier

An FCM token identifies a delivery destination that can rotate. The reviewed
binding additionally proves the authenticated user/tenant, active session
family, admitted installation, verified app identity, app channel and country.
A caller cannot obtain another channel's authority by sending a different
platform number or app label.

The consumer and System Admin apps have separate verified channels. They can
share the platform's notification infrastructure without sharing recipient
authority. An operator notification action can target the affected consumer
through the server's authorized notification workflow; the Admin app does not
need the driver's FCM credential.

## Push registration fields

`POST /api/v1/notifications/push-token` uses `RegisterPushTokenRequest`:

| Field | Meaning |
| --- | --- |
| `token` | Current provider registration token; sensitive destination data |
| `platform` | Numeric push platform enum; must agree with verified app evidence |
| `notificationPermission` | Reported native permission state |
| `channelCapabilities` | Native capability information for applicable notification behaviors |
| `expectedRevision` | Expected installation-state revision for a guarded update |
| `explicitOptIn` | Explicit user intent where re-enabling requires it |
| `mutationId` | Stable identity for the logical binding change |

The installation-state read returns the current owner's revision/enablement
state without exposing provider tokens or another user's identity. A delayed
registration must not overwrite a later disable or bind an old account after
logout. Use revision/mutation identity and reconcile current installation state
when the response is interrupted.

Refresh native tokens through the binding workflow; deactivate the correct
binding on logout/disable as appropriate. Provider invalid-token results require
server cleanup. Google's guidance discusses maintaining token freshness and
removing stale registrations; see
[FCM registration management](https://firebase.google.com/docs/cloud-messaging/manage-tokens).

## Preferences and the durable inbox

Notification preferences cover applicable categories such as rides, deliveries,
wallet and promotions. Promotions default off; mandatory account/security
notifications follow their established policy. Native permission, server
preference and destination availability are separate facts.

The inbox/history routes expose persisted notification records and unread
state. Read, read-all and archive actions belong to the signed-in owner. A push
tap opens an authorized route and then reads current data. It must not display
another user's cached content or grant a benefit from payload text.

## Review and security notifications

Document approval/rejection should create human-readable durable notification
intent for the affected driver. Email, SMS, WhatsApp and app delivery depend on
available/provisioned destinations, consent and configured providers. A rejection
includes a clear reason and replacement guidance. Do not send private document
bytes or credentials in the notification body.

Template wording is centralized and can have authorized tenant overrides.
Provider adapters isolate transport details. Business transactions enqueue
durable effects; a worker delivers them. This preserves a review/payment outcome
when a provider is unavailable and makes delivery failures visible/recoverable.

## Delivery stages are different

| Evidence | What it proves |
| --- | --- |
| Database/outbox intent | The application committed the notification work |
| Worker attempt | The dispatcher tried a provider |
| Provider accepted | The provider accepted a request; handset/mailbox receipt is not established |
| Delivery callback if available | Provider-reported delivery at its supported boundary |
| Inbox read/native interaction | The application's observable user interaction, where recorded |

Never label all these states “delivered.” Missing permission, invalid token,
unprovisioned destination, suppression and provider failure need different
operator explanations. An HTTP success from a send form can represent queued
work rather than handset delivery.

## Realtime is a fast path

Realtime events improve ride, bid, chat and notification latency. Durable domain
state remains authoritative. Clients should deduplicate events, respect persisted
versions/sequences and refresh after reconnect or gaps. An event echo does not
create a second chat message or settlement.

Realtime grant/discovery contracts and infrastructure details are excluded from
this public OpenAPI. That is a publication boundary, not a claim that those
features are absent. Protected polling must remain behind restored-session and
workflow gates; incoming-call or notification timers must not run indefinitely
after sign-out.

Related: [notification delivery lifecycle](../architecture/notification-delivery-lifecycle.md),
[realtime/events](../architecture/realtime-and-events.md) and
[notification recovery](../runbooks/README.md).
