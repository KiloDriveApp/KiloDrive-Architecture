# Support, Dispute, and Reputation Case Runbook

- **Owner:** Support operations with Safety, Finance, Privacy, and domain owners
- **Status:** Maintained runbook for implemented/incremental case operations
- **Last exercised:** Record in restricted release/incident evidence
- **Related architecture:** [Marketplace lifecycles](../architecture/marketplace-product-lifecycles.md), [Rider and driver safety](../architecture/rider-driver-safety.md), and [Privacy/deletion](privacy-deletion.md)

Use this runbook when a case or reply is missing, an attachment cannot be viewed,
the wrong participant can see a case, an SLA/assignment is stale, a dispute is
closed incorrectly, or rating/import evidence needs review or appeal.

## Case model

A case has an opaque UUIDv7 plus a short support reference. It binds to an owned
trip, payment, document, parcel, rental, rating/import, travel profile, or
general concern. The principal workflow is:

`Received → Reviewing → Waiting for information → Resolved`.

This is the canonical versioned contract shared by API, Flutter, and Portal.
The published contract version is `1` and exposes stable localization codes;
wire names are not user-facing copy.
Legacy Open/Answered/Closed data is mapped, not relabelled optimistically:
Open becomes Received, Closed becomes Resolved, and Answered uses the latest
user/support message chronology to choose Reviewing or Waiting for information.
If a client sees a future contract version/value it cannot interpret, it shows
unavailable, preserves safe read-only context, and blocks status mutation.

Reopening, rejection, withdrawal, escalation and closure are conditional policy
transitions. A SafetyCase is a separate, more restrictive lifecycle. Do not bury
an immediate safety concern in an ordinary ticket queue merely because both can
carry messages.

The version-one requester policy allows a resolved case to reopen for fourteen
days. After that window, the client creates a follow-up case that references the
original case number; it does not rewrite the closed timeline. The published
escalation policy sends overdue ordinary work to the SLA queue. Immediate danger
uses the safety/emergency path, and a support case promoted into safety becomes
a separately authorized SafetyCase rather than merely changing a label.

## Invariants

- The creator and explicitly authorized participants see only their case and
  safe linked-entity summary.
- Administrators require permission plus the authorized country workspace;
  every view, download, assignment, reply, status and delete/retain action is
  audited.
- Replies have sender identity/type, UTC sent time and stable client message /
  idempotency identity. A retry cannot duplicate the message.
- Evidence is private, quarantine-aware, signed for short-lived retrieval and
  governed by content class, retention and legal hold.
- Status uses expected version; a stale tab cannot close a case after a newer
  reply or escalation.
- Notifications are outbox side effects. Their failure does not roll back the
  committed reply or status.
- “Resolved” requires a closure reason and actor. It is not a dashboard cleanup
  shortcut or deletion instruction.

## First response

1. Record the support reference, country, case type/status/version, assigned
   team/owner, SLA timestamps and safe correlations.
2. Verify the reporter/participant and linked entity through supported queries;
   do not ask for a password, OTP, full payment details or an attachment by
   ordinary email/chat.
3. Escalate safety, account compromise, financial loss, privacy exposure,
   prohibited parcel, rental theft/damage, or legal demand to its governed owner.
4. If cross-user/country access is possible, contain the route/object immediately
   and treat it as a security/privacy incident.

## Diagnose

### Case detail or messages are blank

- Confirm selected country workspace, participant/permission, case ID and route.
- Load core details and each optional tab independently. Attachment or audit
  failure must not erase the case and messages already loaded.
- Check DTO/enum parsing. A client should show human names and a safe unknown
  state, never raw numeric values or JSON.

### Reply committed but recipient is stale

- Read the durable message/version before push or SignalR state.
- Follow outbox attempt, provider result, realtime group and bounded client poll.
- Replay side effects with the original event identity; do not post the reply
  again under a new message ID.

### Attachment returns conflict

- A scan-pending/rejected/quarantined disposition is a safe guard, not a generic
  “409 client error.” Surface the disposition and permitted next action.
- Verify ownership, case binding, content class, scanner result and signed-
  download audit. Never set clean manually or expose the object publicly.

### SLA or assignment is wrong

- Compare country case policy/version, severity/urgency, owner acknowledgement,
  pause conditions and current UTC.
- Waiting for customer information may pause only the policy-approved clock; a
  free-text status does not change the SLA silently.
- Reassign through the canonical command so history and notification remain.

### Rating or third-party import dispute

- Confirm completed-trip ownership, uniqueness, publication delay/pairing,
  moderation state and appeal version.
- Imported Uber, Lyft or inDrive evidence remains labelled by source and count;
  it is not rewritten as KiloDrive trip feedback.
- An administrator-set starting count/score records source, evidence review,
  reason and audit. It does not alter historical KiloDrive reviews.

### Family/business authorization complaint

- Distinguish booking, payment, profile administration, notification and live-
  tracking permissions. One does not imply the others.
- Verify invitation/contact binding, membership state, removal time, cost-centre
  policy and trip-time tracking consent.
- Removing a member ends future authority and active shares under policy but
  does not erase completed financial/support evidence.

## Recovery

Recover through conditional case commands, authorized reassignment, idempotent
message/outbox replay, scan retry from the original object, or a reviewed domain /
financial compensation. Keep one case timeline; link duplicates instead of
silently deleting them.

Never:

- close a case to suppress an SLA alarm;
- change the creator or country to bypass authorization;
- paste a private attachment or presigned URL into an incident channel;
- delete financial, safety, custody, rental or rating evidence under a generic
  ticket-delete action;
- overwrite a rating to settle an appeal; or
- claim notification delivery proves the recipient read the decision.

## Verification

Test with two ordinary users and least-privilege/System Admin fixtures:

- create with each supported linked-entity type and a general concern;
- creator, participant, foreign user, wrong tenant/country and role access;
- concurrent reply/reassign/status/close with expected versions;
- duplicate client message/idempotency replay;
- attachment pending, rejected, clean, expired link and cross-case access;
- Received → Reviewing → Waiting → Resolved, pause and escalation clocks;
- provider/realtime outage with durable message recovery;
- rating publication, import review, moderation and appeal;
- family/business permission removal during an active trip/share; and
- safety escalation into a separately authorized SafetyCase.

Close only when the authoritative case/timeline is visible to the right parties,
private evidence remains controlled, SLA/owner status is correct, linked domain
and financial actions reconcile, notification failures are accounted for, and
the regression matrix passes.

## Evidence and retention

Retain case reference, safe IDs, versions, action names/times, actor role/type,
SLA decisions, scan disposition, provider IDs, closure reason and correlations.
Message bodies, documents, contact details, addresses, precise trip data and
payment data stay in the restricted case/evidence system under country policy.
