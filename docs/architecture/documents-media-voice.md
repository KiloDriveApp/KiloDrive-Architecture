# Documents, media, and voice architecture

**Owner:** Mobile platform and Voice API. **Last verified:** 2026-10-05 source review. **Environment:** Local modified product checkout, not a signed-device/provider exercise. **Evidence:** product committed HEAD [`8bfe08881bce51535d1165552f2d5be8e05fc872`](https://github.com/KiloDriveApp/KiloDrive/tree/8bfe08881bce51535d1165552f2d5be8e05fc872). The working tree also contains uncommitted native/voice changes and no new signed-device result is inferred from them.

Documents, profile images, and call recordings are all “files” at the storage
layer, but their risks are different. This design starts with the business
content class and keeps object bytes, metadata, review state, consent, and
retention as separate concerns.

## Private upload pipeline

```mermaid
sequenceDiagram
    participant U as Authorized user
    participant API as Upload API
    participant S3 as Private quarantine
    participant AV as ClamAV/CDR
    participant DB as Country cell

    U->>API: file + content class
    API->>API: auth, size, declared type, magic bytes
    API->>S3: opaque private object
    API->>DB: quarantined metadata
    API->>AV: bounded scan
    alt trusted clean
        AV-->>API: clean result
        API->>DB: mark available + audit
    else malware/policy reject
        AV-->>API: reject
        API->>DB: mark rejected + safe reason
    else timeout/unavailable
        API->>DB: remain quarantined for retry
    end
```

New uploads are not immediately viewable. Production scanning fails closed. A
reviewer receiving a `409` quarantine guard should see a friendly “still being
scanned” or “rejected” state, not a raw HTTP-client exception.

## Metadata and content are different records

The country database stores opaque storage key, owner, content class, document
type, upload time, review state, expiry, reviewer, safe notes, scan state, and
revision. S3 stores bytes. A document page can show metadata before the bytes are
available, but its download/view action honors quarantine and authorization.

Driver/vehicle compliance reads approved, unexpired evidence. Rejecting or
expiring required evidence revokes eligibility and publishes an idempotent
compliance update. System administrators can override only through explicit
permission, reason, audit, and the same state machine—not arbitrary row edits.

## Displayable images

Original avatars and vehicle photos stay private. The server produces a bounded,
re-encoded thumbnail that removes metadata and active content. The Flutter image
provider requests an authenticated thumbnail sized from logical pixels and
device pixel ratio, deduplicates in-flight requests, and uses a strict LRU byte
budget.

Revision participates in the cache key. Replacing an avatar changes revision;
logout wipes account-bound entries. Initials and an error state remain available
when image delivery fails.

## Document delivery policy

| Content | Browser behavior | Cache posture | Audit |
| --- | --- | --- | --- |
| Identity evidence | attachment or controlled authenticated viewer | no public cache | every view/download/review |
| Vehicle compliance | authenticated viewer/download | private, short where allowed | view and status mutation |
| Ticket attachment | ticket-party/admin authorization | private | view/download/reply context |
| Avatar thumbnail | authenticated bounded image | revision-aware private cache | metadata access as policy requires |
| Report | short-lived stream/download | no public cache | generation/download |
| Recording | explicit authorized playback/download | private, no public cache | access, hold, delete |

A presigned URL is a temporary bearer credential. Keep it very short lived and
out of logs, analytics, email, referrers, and screenshots.

### Restricted System Administrator viewer

Identity and compliance evidence does not use the operating system's generic
share/open flow. An authorized System Administrator obtains a short-lived
protected viewer session after the required recent authentication and 2FA
step-up. Every byte request rechecks the active administrator session/token
version, document-view capability, selected country workspace, tenant,
document ownership, and clean scan state.

The UI shows reviewed metadata—document type, human-readable status, upload
date, review notes, and audited actions—without exposing an object key, storage
path, internal user identifier, or raw signed URL. Restricted content cannot be
shared through the ordinary OS sheet. Temporary bytes are cleared on close,
logout, session revocation, and process restoration. Platform screenshot
protection is a useful best-effort control, not digital-rights management and
not a reason to weaken authorization or audit.

Expected `401`, `403`, `404`, expired-session, and `409` quarantine outcomes
render stable guidance. Cross-tenant/country and revoked-session tests prove
denial; access-audit tests prove that a successful view leaves accountable
evidence without copying the document contents.

## In-app voice boundary

LiveKit rooms belong to a specific trip and call session. The API authorizes both
participants, verifies trip contact state and driver membership, checks block
rules, and issues a short token. Call invitations and end events are durable
notification intents. The mobile app has source paths for foreground,
background and terminated-launch invitations, cancellation, decline, timeout,
reconnect and orphan cleanup. Their presence does not prove delivery after OS
force-quit or on every signed device.

```mermaid
flowchart LR
    Trip[Authorized active trip] --> CallAPI[Voice call API]
    CallAPI --> Ring[Current peer call session]
    Ring --> Push[FCM data-only ring]
    Ring --> Realtime[SignalR hint]
    Push --> Native[CallKit or Android calling UI]
    Realtime --> Native
    Native --> Validate[Account, call ID, expiry and server status]
    Validate --> Token[Short-lived LiveKit room token]
    Token --> Audio[RTC audio]
    CallAPI --> End[Terminal call state]
    End --> Teardown[Peer push/realtime plus local tombstone]
```

```mermaid
sequenceDiagram
    participant Caller as Caller app
    participant API as Voice API
    participant Peer as Peer app/OS
    participant RTC as LiveKit
    Caller->>API: POST call with stable idempotency key
    API-->>Caller: call ID or authoritative rejection
    API-->>Peer: push and realtime ring hints
    Peer->>Peer: Validate recipient, call ID, bounded expiry
    Peer->>API: Read current call status and request token on answer
    API-->>Peer: Authorized short-lived token
    Caller->>RTC: Join room with own token
    Peer->>RTC: Join room with own token
    Caller->>API: End/decline/timeout with call identity
    API-->>Peer: Terminal event (may race the ring)
    Peer->>Peer: Mark tombstone, dismiss native UI and RTC
```

| Call transition | Authority | Interruption/recovery |
| --- | --- | --- |
| Not started → ringing | Server call row after trip/participant/entitlement checks | Preserve the original start idempotency key on timeout or unknown response; do not launch a second call blindly. |
| Ring observed → native UI | Current recipient, call ID and server expiry; OS controls presentation | Persist bounded local call binding before native presentation. A late ring cannot resurrect a tombstoned terminal call. |
| Answer → connecting | Current server status and short-lived token | Native callback ID alone is not a trip ID. Resolve persisted account/trip/call binding, then recheck server eligibility. |
| Connecting → connected | LiveKit participant/room state plus active call | An audio-room connection is not permission to keep a call open after trip/call closure. |
| Ringing/connected → ended, declined, no answer or failed | Server terminal state and local teardown | Peer terminal push/realtime event closes UI; a bounded timeout and startup sweep recover missing events. |

The [client orchestrator](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/voice/voice_service.dart) preserves a start-operation key for unknown outcomes, subscribes to realtime call events, and sweeps orphan rings. The [typed native call adapter](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/voice/native_call_adapter.dart) maps accept/decline/end/timeout callbacks; [local session records](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/voice/native_voice_session.dart) bind opaque call and trip IDs to the current account, expiry and terminal tombstones. The [Firebase background path](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/firebase.dart) checks recipient and device opt-out before presentation. None of these local records grants RTC access.

Android uses the plugin's calling surface/ConnectionService integration where permitted. The [Android manifest](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/android/app/src/main/AndroidManifest.xml) requests microphone/audio-settings permissions but explicitly removes transitive microphone/phone-call foreground-service permissions; do not describe indefinite background audio as supported. On iOS, independent call haptic control is OS-owned: quiet or vibration-disabled policy falls back to a passive, generic local notice instead of claiming a silent interactive CallKit ring. An answered call still needs fresh server token authorization. Audio focus, phone interruption and background/force-quit behavior require artifact-specific device evidence.

The [server FCM adapter](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/server/KiloDrive.Api/Services/Notifications/FirebasePushProvider.cs) sends `voice.*` as data-only high-priority FCM with APNs alert headers; provider acceptance is not proof that a background isolate woke or CallKit displayed. Reconcile missing rings against the current server call state. Do not log RTC tokens, caller contact details, private room identifiers or raw push envelopes. Safe support evidence is call-operation reference, app/build/OS, lifecycle state, event order, permission category, provider outcome class and teardown result.

Source-test anchors (not signed-device evidence): [native session binding](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/test/native_voice_session_test.dart), [call-status recovery](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/test/call_status_recovery_test.dart), [quiet iOS fallback](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/test/native_call_quiet_fallback_test.dart), [API incoming recovery](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/tests/KiloDrive.Tests/Api/IncomingVoiceCallRecoveryTests.cs), and [start boundary](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/tests/KiloDrive.Tests/Api/VoiceCallStartBoundaryTests.cs). The current signed-artifact matrix still needs real-device foreground/background/terminated/force-quit, microphone denial, audio interruption, Wi-Fi/cellular handoff, and peer-end races on both platforms. Failed or missing delivery is a call-recovery incident, not evidence that the trip itself changed.

The visible product state should distinguish:

- ringing;
- connecting;
- connected;
- recording awaiting consent;
- recording active;
- ended/declined/no answer/failed; and
- GSM fallback when in-app calling is unavailable or not entitled.

Closing/cancelling the trip closes chat/call channels. Old trip detail pages may
show safe call metadata and authorized recordings but cannot start a new call.

## Consent-aware recording

Recording is configurable and country restricted. If policy requires both
participants' consent, egress does not start until both durable consent
timestamps exist. The recording indicator remains visible while active.

An outbox handler reconciles LiveKit egress before starting or retrying. It stores
safe state and provider ID, never the API secret or media. Encrypted output uses
a private S3 prefix and least-privilege write role. Retention metadata records
jurisdiction, deletion deadline, and legal hold.

Safe call audit events include call/trip identifiers, actor surrogate, role,
timestamps, consent, status, end reason, and bounded duration. They exclude audio,
tokens, room secrets, contact details, and signed object URLs.

## Failure and recovery principles

- Scanner outage leaves uploads quarantined.
- S3 delivery failure does not change an approved document to rejected.
- A missing object is reconciled as an integrity incident, not hidden by a blank
  viewer.
- A LiveKit token failure offers only a policy-approved GSM fallback.
- Egress timeout is an unknown result; reconcile before starting another.
- Partial recording is not labeled complete.
- Repeated deletion is idempotent, while legal hold fails closed.
- User-facing provider errors use localized stable states, not raw JSON/409/503.

## Tests that matter

For uploads: wrong extension, mismatched magic, oversized file, EICAR/test
malware, scanner timeout, retry, cross-user access, cross-tenant access, clean
release, thumbnail metadata removal, and deletion/hold.

For voice: two participants, unauthorized third party, free/paid entitlement,
foreground/background/killed app, permission denial, Wi-Fi/cellular handoff,
TURN relay, decline/timeout/cancel, trip closure, two-party consent, egress
unknown result, object encryption, playback authorization, retention, and legal
hold.

See [Private storage](../aws/storage.md), [LiveKit on AWS](../aws/livekit.md),
[Upload quarantine](../runbooks/upload-quarantine.md), and
[LiveKit voice](../runbooks/livekit-voice.md).
