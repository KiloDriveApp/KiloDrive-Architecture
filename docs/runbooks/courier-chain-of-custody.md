# Courier Chain-of-Custody Recovery Runbook

- **Owner:** Courier operations with Safety, Support, Finance, and Privacy
- **Status:** Maintained runbook for an implemented/incremental product
- **Last exercised:** Record in restricted release/incident evidence
- **Related architecture:** [Marketplace lifecycles](../architecture/marketplace-product-lifecycles.md), [Financial systems](../architecture/financial-systems.md), and [Upload quarantine](upload-quarantine.md)

Use this runbook when a pickup or recipient OTP/QR fails, the app and durable
custody timeline disagree, proof is unavailable, delivery fails, return-to-
sender stalls, or payment/escrow no longer matches parcel state.

## Protect people and the parcel first

Do not tell a driver to leave a parcel at an unapproved location, reveal an OTP,
photograph an identity document unnecessarily, or hand an item to an unverified
person to clear a queue. If declared contents suggest prohibited or dangerous
goods, follow the country safety/legal procedure and avoid opening the package
unless authorized.

## Authoritative lifecycle

The country cell owns the parcel and its versioned custody events:

`Created → Accepted → ArrivedAtPickup → PickupConfirmed → InTransit →`
`DeliveryAttempted → Delivered`

Failed delivery follows an explicit branch:

`DeliveryAttempted → Failed → ReturnAuthorized → Returning → ReturnedToSender`

Country policy may add cancellation or dispute outcomes, but an operator must
not relabel a failed attempt as delivered or cancelled. Every transition records
the authorized actor, UTC time, expected version and safe reason/evidence links.

## Invariants

- Pickup proof is single-use, short-lived and bound to delivery, sender and
  assigned driver.
- Recipient proof is separately bound to the intended delivery/recipient path.
- A retry with the same client operation ID replays one custody transition.
- Only the current assigned driver and authorized sender/recipient/admin paths
  can act.
- Private photographs, signatures and attachments stay quarantined until clean,
  are never public URLs, and are retrieved through audited expiring access.
- A custody state change, escrow movement, payment and outbox intent commit in
  the appropriate short transaction; notification delivery is not custody
  proof.
- Delivered and ReturnedToSender are mutually exclusive terminal outcomes.

## First response

1. Record the case/reference, country, parcel ID, current version/state,
   assignment, payment/hold state and safe correlation IDs.
2. Establish physical custody through the approved participant/support channel.
   Do not put a contact number, address, code, contents or image in incident chat.
3. If the parcel is unaccounted for, damaged, dangerous, or the participant may
   be at risk, open/escalate the appropriate SafetyCase and preserve evidence.
4. Stop automated settlement or return actions when durable custody is
   ambiguous. Do not globally stop unrelated deliveries.

## Diagnose

### OTP or QR rejected

- Confirm the challenge belongs to the exact delivery, purpose, actor and current
  assignment, is unexpired, not superseded, and has attempts remaining.
- Compare only protected challenge identifiers/status; never log or request the
  plaintext proof through support.
- Check device clock display separately from server UTC authority.
- Reissuing proof invalidates the earlier challenge and requires an authorized
  participant action. An administrator does not read the old code.

### Custody event committed but peer is stale

- Read durable state/version and outbox row first.
- Follow worker, broker/fallback, push/SignalR and client merge state.
- Use the ordinary tracking refresh as reconciliation. Do not resubmit the
  custody mutation under a new key.

### Proof image/signature unavailable

- Confirm the object key belongs to the delivery and expected evidence class.
- Inspect quarantine scan disposition. Pending, timeout or rejected is not
  clean and should produce a safe status rather than a raw conflict.
- Verify private-object IAM/KMS and signed-download issuance without copying the
  URL. A thumbnail may be re-encoded; an identity document is attachment-only.

### Failed delivery or return stalls

- Confirm failure reason, permitted attempts, delivery window, current custodian
  and country return policy.
- Check return authorization and assignment independently from notification.
- Ensure the same parcel identity and evidence chain continue through return;
  do not create a replacement “delivery” to move the state.

### Money disagrees

- Compare payment method, escrow held, release/refund, driver entitlement,
  commission/membership mode, provider reference and journal.
- Do not mark Delivered to release funds. Correct state through the supported
  custody decision, then use a reviewed reversal/compensation if accounting
  needs correction.

## Recovery actions

Allowed recovery mechanisms are conditional lifecycle commands, idempotent
outbox replay, provider reconciliation, scan retry from the original object, or
an audited support decision permitted by country policy. Preserve the original
event/reference and expected version.

Never:

- regenerate an OTP without invalidating its predecessor;
- disclose a proof code or full recipient identity to an operator;
- replace rejected evidence with a database status edit;
- delete an inconvenient custody event;
- retry an unknown payment mutation before provider reconciliation; or
- release/refund escrow based only on a notification screenshot.

## Verification fixture

Exercise create, quote, accept, pickup arrival, pickup OTP/QR, photo, in-transit,
recipient proof, signature/photo, and delivery. Then cover:

- duplicate and out-of-order custody commands;
- expired/superseded/wrong-delivery proof;
- cross-user evidence and tracking IDOR;
- scanner timeout, rejection, clean retry and signed access;
- offline driver queue replay with original client IDs;
- recipient absent, failed attempt, return authorization and returned proof;
- cancellation at each legal state;
- payment timeout, escrow release/refund and reconciliation; and
- killed/background clients recovering the authoritative timeline.

Close only when physical custody is accounted for, one legal terminal or active
state is authoritative, evidence access is correct, payment/journal/hold totals
reconcile, notifications have converged or are explicitly degraded, and the
case/SafetyCase owner acknowledges the outcome.

## Evidence and privacy

Retain safe IDs, versions, transition names/times, scan disposition, provider
identifiers, reconciliation totals and decision owner. Package contents,
addresses, proof codes, signatures, images and recipient contact data belong in
the restricted case/evidence system under the country retention rule—not in
general logs, metrics or public runbooks.
