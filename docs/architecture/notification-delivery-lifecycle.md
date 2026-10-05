# Notifications: authority, delivery and recipient isolation

**Owner:** Mobile platform and Notifications API. **Last verified:** 2026-10-05 source review. **Environment:** Local modified product checkout, not a signed-device/provider exercise. **Evidence:** product repository committed HEAD [`8bfe08881bce51535d1165552f2d5be8e05fc872`](https://github.com/KiloDriveApp/KiloDrive/tree/8bfe08881bce51535d1165552f2d5be8e05fc872), plus separately identified dirty working-tree changes. This is not a production delivery certification.

A KiloDrive notification is not the business event that caused it. A completed
trip, account change or payment is owned by its domain transaction; a
notification is a durable attempt to tell an eligible recipient about that
state. The consumer app and separate System Admin app have different audiences
and native app channels. This chapter describes source-level behavior and
evidence needed to make a delivery claim, without exposing private message
content or provider configuration.

## The five moments of a message

| Moment | Authoritative evidence | What may be shown |
| --- | --- | --- |
| Business state committed | Owning identity or country-cell transaction | The domain result, independent of messaging |
| Delivery work staged | Outbox/notification record with intended recipient and template | Queued, with a safe reference |
| Provider attempt completed | Attempt record and sanitized provider outcome | Accepted, rejected, failed, retrying or skipped |
| OS/app presented | Platform-specific device observation where available | Presented only when actually observed; provider acceptance is insufficient |
| Person opened/read | Authenticated inbox or target action | Read only after current recipient and scope reauthorization |

Workers may retry at-least-once delivery. The domain event and each attempt
therefore need stable correlation and deduplication; “exactly once to the
person” is not a defensible provider guarantee. A suppressed push is an
explicit `Skipped` outcome, not a successful send. A missing or failed provider
initialization remains a retryable failure when policy requires delivery.

```mermaid
flowchart LR
    Domain[Committed business action] --> Outbox[Durable outbox]
    Outbox --> Worker[Scoped worker]
    Worker --> Preference[Recipient and category policy]
    Preference -->|Allowed| Provider[Configured channel provider]
    Preference -->|Suppressed| Skipped[Recorded skipped outcome]
    Provider --> Attempt[Recorded attempt outcome]
    Attempt --> Inbox[Authorized in-app history]
    Attempt --> Device[OS or app presentation, if observed]
    Device --> Open[Reauthorized open/read]
```

The current consumer build declared in [`pubspec.yaml`](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/pubspec.yaml) is `1.0.0+192`. That source version does not identify the exact installed, signed artifact. Native notification and voice files were modified in the working tree at review time; those edits are not part of the pinned HEAD and require a fresh commit/artifact review before certification.

## Handoff and authority

```mermaid
sequenceDiagram
    participant Domain as Domain transaction
    participant Outbox as Scoped outbox worker
    participant FCM as FCM / APNs transport
    participant OS as Android / iOS
    participant App as Consumer app
    participant API as API read model
    Domain->>Outbox: Commit domain state and notification intent
    Outbox->>Outbox: Check recipient, category, token generation
    Outbox->>FCM: Send reviewed payload to current app-channel token
    FCM-->>Outbox: Provider acceptance or rejection
    FCM-->>OS: Best-effort delivery
    OS-->>App: Foreground event, tap, or background callback when permitted
    App->>App: Check account, event ID, route and lifecycle scope
    App->>API: Fetch current authorized trip/inbox/call state
    API-->>App: Authoritative state or denial
```

| Transition | Evidence and owner | Recovery rule |
| --- | --- | --- |
| Committed → queued | Domain transaction and outbox intent | Worker retry cannot repeat the domain mutation. |
| Queued → attempted/skipped | Notification worker, preference and active token binding | A suppressed category is recorded `Skipped`; a retry keeps its intended recipient and correlation. |
| Attempted → provider accepted/rejected | FCM response, not a handset receipt | Reject invalid/unregistered token and deactivate its current generation; retry transient failures within worker policy. |
| Accepted → OS presented | Only signed-device observation can prove it | Permission, Focus/Doze, channel settings, app lifecycle and network may prevent presentation. Do not upgrade `accepted` to `received`. |
| Presented → opened | OS tap or local callback, then app scope gate | Reauthorize after unlock/login; fetch fresh API state. A tap never repeats a bid, payment or trip mutation. |

The [server event matrix](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/server/KiloDrive.Api/Services/Notifications/NotificationEventMatrix.cs) maps request/bid, trip acceptance/arrival/start/stop/completion/cancellation, chat, payment, safety and security to reviewed categories and sounds. Safety/security bypass optional category preferences, not OS permission. The [FCM adapter](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/server/KiloDrive.Api/Services/Notifications/FirebasePushProvider.cs) rechecks ownership immediately before send and deactivates unregistered/invalid tokens. An FCM message ID is provider-attempt evidence only.

## Platform presentation and audible policy

| State/policy | Android consumer | iOS consumer |
| --- | --- | --- |
| Foreground | Dart `onMessage` drives an in-app visual or native attention after recipient/event checks; app avoids duplicate OS foreground alerts. | The app disables automatic foreground alert/sound and uses its controlled local presentation/attention. |
| Background/terminated | FCM and Android notification channels may present; data-only call rings seek a background callback. Doze, permission and OEM policy remain external. | APNs and iOS may present eligible notifications. A Dart background callback or data-only call ring is not guaranteed, especially after force-quit. |
| Quiet hours/opt-out | Optional attention can be suppressed; current channel capabilities determine a quiet or no-vibration channel, otherwise the server uses data-only handoff instead of claiming sound. | Sound/haptics remain OS-managed; KiloDrive may request a quiet notification but cannot independently guarantee vibration control. |
| Channel/sound | Channel IDs are stable, user-owned OS settings; the app must not recreate a customized audible channel to override it. | APNs sound asset and OS notification settings control audible presentation; Focus and permissions can silence it. |
| Notification tap | Initial/opened/local callbacks are deduplicated in the active account scope and routed after authentication/unlock. | Same app route policy, with iOS lifecycle-dependent callback delivery. |

The concrete interfaces are [`NotificationPlatformAdapter`](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/notifications/notification_platform_adapter.dart), [`NotificationAttentionAdapter`](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/notifications/notification_attention_adapter.dart), and the [channel/receipt policy](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/notifications/notification_sound.dart). The [Firebase lifecycle](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/firebase.dart) registers foreground, opened, initial and background paths. Android declares `POST_NOTIFICATIONS` and `VIBRATE` in its [manifest](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/android/app/src/main/AndroidManifest.xml); declaration alone does not prove grant or presentation.

Chat, bid and lifecycle attention use bounded in-memory event receipts to avoid duplicate noise when SignalR and FCM carry the same committed event. A missing legacy event ID weakens deduplication; it does not authorize dropping the message. [Realtime connection state](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/realtime/realtime_service.dart) is a low-latency hint, never the trip/payment authority. After reconnect or app restart, fetch current API state rather than replaying a stale realtime command.

## Installation, account and privacy boundaries

The [push registration attempt](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/notifications/push_token_service.dart) is scoped to credential, tenant/country and authorization revision; it cancels stale flights, bounds startup/provider waiting and retries on later resume/refresh. Explicit enabling persists preference intent before token lookup. The server binds tokens to the consumer or System Admin app channel and a current installation/session generation. A token is a replaceable address, not a physical-device identifier or proof of account ownership. Fresh-install iOS token rotation addresses Keychain/app-data asymmetry. Account switch clears pending opens and best-effort delivered tray cards; queued sends still require the server's current binding check.

The [recipient gate](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/notifications/push_recipient.dart), [open gate](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/notifications/notification_open_gate.dart), and [deep-link parser](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/navigation/deep_links.dart) protect account/route handoff; the destination API must still authorize the current user. Avoid rendered private content, raw push tokens, destinations and provider payloads in generic diagnostics. Retain only sanitized event/operation identifiers, app channel, category, attempt outcome, time and provider error class for support. See [mobile sessions](mobile-session-and-device-lifecycle.md) for installation versus person identity.

Failure examples: FCM accepts a ride alert but Android's user-disabled channel makes it silent; an iPhone in Focus receives a notification without audible presentation; a token refresh races an old queued send; a `voice.call_ended` arrives before its ring; or a notification tap occurs after logout. In every case, preserve the committed API state, report the presentation uncertainty, and recheck recipient and resource authority before showing detail. For an “accepted but no sound” incident, retain app/build/OS, channel ID and effective OS settings, category/quiet policy, lifecycle state, provider attempt class and sanitized event ID—not the raw payload. The operator runbook is [notification canaries](../runbooks/notification-canaries.md).

Source-test anchors (not device certification): [notification platform adapter](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/test/notification_platform_adapter_test.dart), [open dedupe](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/test/notification_open_gate_test.dart), [preference race](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/test/notification_preferences_scope_race_test.dart), [event matrix](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/tests/KiloDrive.Tests/Api/NotificationEventMatrixTests.cs), and [server lifecycle](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/tests/KiloDrive.Tests/Api/NotificationLifecycleTests.cs). No current-build iOS/Android foreground, background, terminated, reinstall, Focus/Doze or force-quit case was executed by this documentation review; those cells remain untested or require the separate signed-device evidence ledger.

## Consumer notification policy

Consumer categories include ride/trip, delivery, wallet and promotions.
Promotions default off; account/security communication follows its mandatory
policy rather than a marketing toggle. The backend applies the preference when
dispatching, because a local switch cannot govern an already queued send.
The in-app notification history is useful even if OS permission is denied.

Push, SMS and email are channel adapters. Push uses a registered native token;
SMS and email resolve approved wording from a shared template catalog with
reviewed tenant overrides. Templates and recipient data are not assembled by
arbitrary screen code. A provider failure is recorded and retried according to
the outbox policy. A payment or account mutation is not rolled back because a
notification provider is temporarily unavailable.

Private chat text, document facts and sensitive account details should not be
placed in a generic OS-rendered preview. A foreground presentation can load
safe detail only for the currently authenticated recipient. Background and
terminated states have different platform behavior and require signed-device
testing on each supported OS; a foreground Dart callback is not proof of
killed-app behavior.

## Administrator alerts and sends

The System Admin app has an opt-in private alert inbox distinct from consumer
notification history. An alert's push is a generic hint. Opening a case or
person record requires a fresh session, selected country/tenant, event type,
route and target permission check. An old push cannot grant access after a
capability is removed. Read and archive actions have their own durable result
and must retain a stable operation identity after an interrupted response.

An administrator's guarded compose/send flow requires the relevant grant and
proof. It can queue a notification and inspect its delivery history, but the
client must not report “received” simply because a provider accepted it. The
full batch-to-provider graph and administrator alert email delivery remain
incremental in the current mobile migration.

Exact-installation notification is narrower than ordinary account messaging.
The source checks for one current user, session family, installation, active
token generation, verified app channel, permission and deployment-approved
presenter. The operator chooses an approved fixed template and records a
purpose; arbitrary private text is not sent. Queueing creates an audited
operation. The dispatch worker rechecks eligibility so a logout, rotation or
restriction between queue and send does not use an obsolete binding. The
reviewed presenter is platform/state-specific; unsupported states are
unavailable rather than redirected to an OS preview that cannot verify the
recipient. This is source design, not proof of production delivery.

## Token and account lifecycle

| Change | Expected delivery behavior |
| --- | --- |
| First permitted registration | Bind token to the signed-in account, app channel, installation and active session as required |
| Token rotation | New generation supersedes the old; pending exact sends re-evaluate eligibility |
| Permission denied | Do not claim push presentation; retain authorized in-app history where applicable |
| Logout or workspace exit | Deactivate the relevant binding and clear local routes/notifications where the OS permits |
| Account switch | Old-account notification cannot open content in the new account |
| Session revocation or installation restriction | Protected detail and targeted delivery fail current checks |
| App reinstall | New installation must not inherit old recipient eligibility |
| Provider timeout or duplicate callback | Record/reconcile one intended attempt; do not create a second business action |

The delivery history should carry safe operation, template, channel, attempt,
status, time and correlation fields. It should not store rendered private bodies,
raw destinations, push tokens, receipts or full provider payloads in general
telemetry. A user-facing audit description explains who requested a send and
what class of notification was attempted without revealing the content.

## What to test before claiming delivery

Unit and component tests cover category policy, template fallback, dedupe,
redaction and worker outcome mapping. API tests cover authorized/denied reads,
recipient rebind, tenant/country isolation and stale token rejection. Provider
tests cover acceptance, rejection, timeout, duplicate and retry. Signed-device
tests cover foreground, background, terminated launch, account switch,
permission denial, Focus/Doze where relevant, and notification-tap
reauthorization. The exact artifact, OS, app channel, provider environment and
sanitized operation reference must be recorded together.

See [realtime and events](realtime-and-events.md),
[mobile sessions and installations](mobile-session-and-device-lifecycle.md),
[notification canaries](../runbooks/notification-canaries.md), and
[testing and verification](../quality/testing-and-verification.md). A green
widget test or an accepted FCM response alone does not close the device matrix.
