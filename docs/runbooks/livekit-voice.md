# Runbook: LiveKit voice, TURN, and recording

- **Owner:** Realtime communications and platform operations
- **Status:** Application support is implemented; infrastructure enablement is deployment-specific
- **Last exercised:** Record the most recent foreground, background, killed-state, TURN, and egress exercise here
- **Related architecture:** [Documents, media, and voice](../architecture/documents-media-voice.md), [LiveKit on AWS](../aws/livekit.md), [ADR 006](../adr/006-private-object-storage.md)

## Purpose and safety boundary

Use this runbook when rider-to-driver calling, ringing, media, TURN relay, or
consented recording is degraded. The goal is to restore an authorized trip call
without weakening participant checks, recording consent, retention, or private
object-storage controls.

Voice is not one dependency. A user-visible call crosses push delivery, mobile
background handling, API authorization, short-lived token issuance, LiveKit
signalling, direct or relayed media, and optionally egress plus encrypted object
storage. A green room API does not prove that two phones can exchange audio.

Never put an API secret, room token, participant contact detail, signed object
URL, recording path, or audio content in a ticket, log, trace, screenshot, or
alarm. Use dedicated non-user test participants for diagnosis.

## Trigger and customer symptoms

Typical triggers include:

- `voice_not_configured` or token endpoint 5xx responses;
- rings that do not appear in the background or after a killed-app launch;
- calls stuck on **Connecting**;
- one-way or silent audio, especially on cellular or restrictive Wi-Fi;
- rapid reconnects, room disconnects, packet loss, or high jitter;
- calls that ring after the caller cancelled;
- orphaned native call UI after the trip or room ended;
- recording consent shown but egress never starting;
- a recording marked complete with no private object;
- egress backlog, failure, or unexpected duplicate jobs; or
- S3/KMS authorization failures for recording output.

Record the affected app version, OS, network transition, trip/call surrogate,
safe provider job ID, correlation ID, and approximate UTC/local time. Do not
record the user's phone number or room credential.

## First classify the failed stage

Work from the outside inward. Each stage has a different owner and recovery.

| Stage | Quick proof | Likely fault domain |
| --- | --- | --- |
| Call eligibility | API returns an authorized call state | trip lifecycle, membership, block policy, participant relation |
| Ring delivery | dedicated device receives data-only high-priority push | FCM/APNs, mobile native integration, notification permission |
| Token issuance | protected endpoint returns a short-lived scoped token | API configuration, signing credentials, URL, authorization |
| Signalling | both synthetic participants join one expected room | TLS, LiveKit service, token grants, clock skew |
| Media | two physical devices exchange audio | microphone permission, ICE, UDP/TCP, TURN, carrier/network |
| Recording | consented canary egress reaches a terminal state | egress worker, room, API permission, capacity |
| Storage | encrypted private object and metadata agree | S3, KMS, egress role, retention workflow |

Do not skip straight to restarting the server. A restart may remove useful
evidence and will not repair an expired push token, incorrect TURN advertisement,
or missing object permission.

## Preconditions

- Use an authorized operational role and a dedicated non-user rider/driver pair.
- Confirm whether recording is permitted for the selected country and fixture.
- Keep GSM fallback available only where product policy and plan entitlement
  permit it.
- Know the last healthy application and infrastructure revisions.
- Confirm a human alert destination is active before triggering alarms.
- If a legal hold or active safety case covers a recording, do not delete,
  replace, or move it without the required approval.

## Diagnose

### 1. Prove the domain and authorization state

Confirm the trip exists, both participants are the expected parties, the trip is
in a call-capable state, the driver entitlement is current, neither party is
blocked, and no closure/revocation event has already expired the channel. Check
the persisted call state and event version, not only what either screen shows.

A 401/403 is not a media outage. A 409 may represent a legitimate lifecycle
conflict. Preserve the stable error code and show a useful client state instead
of surfacing the HTTP library exception.

### 2. Check token issuance safely

Use a synthetic authorized trip. Verify the token is short lived, audience/room
and role are scoped, server clocks are synchronized, and the advertised secure
WebSocket URL resolves to the intended certificate. Decode only a synthetic
token locally if claims need inspection; never paste a production token into an
online decoder or incident ticket.

If issuance says configuration is missing, validate the secret source and
runtime identity without printing values. Restart only after configuration has
been validated and deployed consistently to every node.

### 3. Separate signalling from media

Have two physical test devices join. If signalling succeeds but audio does not,
inspect ICE candidate selection, TURN use, packet loss, jitter, microphone
permission, audio route, and operating-system call state. Test:

- Wi-Fi to Wi-Fi;
- cellular to cellular;
- one restrictive network that forces TURN;
- Wi-Fi-to-cellular handoff; and
- screen off/background where the declared platform capability permits it.

An emulator can prove UI and signalling logic, but it is weak evidence for
carrier NAT, Bluetooth/audio routing, killed-state push, or sustained microphone
behavior. Keep a small physical-device matrix.

### 4. Inspect TURN and network posture

Confirm DNS and certificate validity, security-group/firewall rules, public
address advertisement, UDP media range, TURN UDP/TCP/TLS reachability, and
instance bandwidth. A working HTTPS health endpoint proves none of the media
ports.

Track the percentage of relayed sessions. A sudden increase often means direct
ICE is failing; a near-zero rate during restrictive-network tests may mean TURN
is unreachable. Do not expose broad port ranges casually—document and test the
minimum topology required by the deployed configuration.

### 5. Reconcile recording before retrying

Read the durable call/recording request, both consent records, egress job status,
and object metadata. Treat timeout after a start request as an **unknown result**.
Query LiveKit for the stable job ID before creating another job. Duplicate
egress can create conflicting retention objects and unnecessary privacy risk.

Verify the object is private, encrypted with the approved key context, written
under the recording-only prefix, and represented by a matching metadata row.
Partial output stays `partial` or `needs_review`; never mark it complete just
because an object exists.

## Contain

Choose the smallest reversible action:

- disable new in-app calls for the affected country/plan while preserving trip
  service and policy-approved GSM fallback;
- disable only recording initiation while keeping unrecorded consent-compliant
  calls available, if jurisdiction and policy allow;
- route new media away from a saturated node while existing rooms drain;
- pause egress admission when workers or storage are saturated;
- suppress the narrow synthetic egress canary during a declared maintenance
  window, without disabling real delivery or unrelated alarms; or
- expire compromised credentials and tokens immediately.

Do not broaden IAM, remove participant authorization, bypass consent, make the
bucket public, lengthen tokens indiscriminately, or mark unknown egress jobs as
failed merely to permit another start.

## Recover

1. Correct the narrow fault: configuration, certificate, routing, firewall,
   TURN advertisement, worker capacity, IAM, object policy, or mobile release.
2. Deploy to one canary node/device path first.
3. Reconcile every in-flight call and egress job created during the incident.
4. End orphan rooms and native rings through supported idempotent lifecycle
   operations.
5. Redrive durable ring/end/recording intents only after confirming handlers are
   idempotent and current state still permits the action.
6. Restore admission gradually and watch CPU, bandwidth, room count, TURN relay
   rate, packet loss, egress concurrency, object-write failures, and backlog age.

If a recording object is missing after provider success, open an integrity
incident. Do not silently delete the metadata row. If an object exists without a
trusted metadata/consent record, quarantine access and investigate ownership.

## Verification matrix

Use the dedicated rider and driver on both Android and iOS where supported:

1. foreground ring, accept, two-way audio, and normal end;
2. decline, caller cancellation, no-answer timeout, and duplicate end;
3. callee backgrounded and killed-app launch from a real push;
4. permission denied and later enabled from operating-system settings;
5. Wi-Fi/cellular handoff and temporary disconnect/reconnect;
6. TURN-forced network;
7. trip closure expiring call eligibility and orphan cleanup;
8. free-driver GSM-only versus paid in-app entitlement;
9. consent denied, one-party consent pending, and complete required consent;
10. egress start, encrypted private output, authorized playback, retention, and
    legal-hold behavior; and
11. node restart during signalling and egress unknown-result reconciliation.

For every scenario, assert safe audit metadata, terminal state convergence, and
absence of tokens/contact/media in telemetry.

## Rollback or abort criteria

Abort rollout when calls can bypass authorization/consent, tokens are too broad,
objects are public or unencrypted, duplicate recording cannot be reconciled, or
media quality remains unsafe at expected load. Return to the last compatible
binary/configuration and keep the affected capability disabled. Do not roll back
the database by discarding legitimate call or consent history.

## Evidence and follow-up

Retain deployment versions, synthetic call IDs, safe provider IDs, timestamps,
latency/quality aggregates, alarm transitions, and test outcomes. Record no
audio or destinations unless the test procedure explicitly authorizes a
non-user fixture recording.

Before closing, add the regression that would have detected the fault, update
capacity thresholds/runbook diagrams, review permissions and retention, and run
the complete foreground/background/killed-state matrix once more.
