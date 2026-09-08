# Build 101: trip delivery, worker ownership and mobile recovery

## Release identity and evidence boundary

The source release is mobile `1.0.0+101`, with canonical MySQL contract
`2026.09.07.3`. The API remains the authority for eligibility, state and money.
Public routes and request bodies remain compatible. A matching schema fingerprint
does not certify native billing, provider delivery or country product readiness.

This update follows build 100's trip recovery work. Deployment outcome belongs in
the application release record, not in an assumed statement that source is live.

## Driver assignment navigation

Acceptance can change the driver's online availability, so resume must reconcile
an active assignment even if the previous online flag is false. A typed navigation
guard scopes deferred navigation to account, tenant and country. It suppresses
duplicate route requests, invalidates superseded requests, and does not repeatedly
reopen a trip after deliberate Back navigation. Foreground visibility and current
route ownership still matter; a late callback must not navigate another workspace.

## Chat commit and delivery

The durable message is the success boundary. HTTP/SignalR delivery is not a second
database commit. The mobile send queue serializes rapid sends while retaining each
command's identity across uncertain responses. Queue generations are invalidated
when session or workspace changes; a late response cannot append private messages
to the replacement conversation.

Realtime membership operations are ordered so reconnect/join/leave races cannot
silently discard desired subscriptions. Bounded recovery reads and durable outbox
fanout remain necessary when transport delivery is interrupted.

The dispatcher uses separate chat and provider lanes. A slow email, SMS or other
external provider should not monopolize chat dispatch. This is bounded concurrency,
not unlimited parallel execution. Instrument each lane independently and retain
the global backlog view.

## Worker claims and fencing

Each outbox claim receives a distinct UUIDv7 ownership token. Reclamation matches
the observed status, token and expired lease in one conditional database write.
The existing lease-owner column is also an EF concurrency token: finalization by
a replaced worker cannot overwrite its successor. Renewal failure or lost ownership
cancels the handler; shutdown leaves durable recovery state rather than consuming
a provider failure attempt. Outcome metrics follow durable persistence.

Delivery remains **at-least-once**. A provider can succeed just before the process
dies. Financial and provider adapters must preserve stable idempotency identities
and reconcile unknown outcomes; lease fencing is not an exactly-once guarantee.
The EF token uses an existing column and requires no new physical schema version.

## Payment and database recovery

Wallet/payment/receipt reads use a coherent snapshot rather than combining values
from unrelated points during capture. Trip participants are resolved without broad
unrelated entity includes. Background assignment and telemetry workers execute
transactions through the configured retry strategy rather than opening unsupported
user transactions under a retrying provider. Rental race verifiers use server-side
grouping/counting instead of loading all availability records into memory.

Preserve immutable journals and existing uniqueness. Neither UI recovery nor a
deployment should reset accounts, delete failed outbox evidence or weaken arrival
requirements to obtain a passing test.

## Mobile interaction and diagnostic changes

- Trip status identifies the correct peer; chat/call and emergency/cancel actions
  use compact, accessible groupings with server-derived availability.
- Notification sounds are bounded and category/device preferences remain separate
  from durable event delivery. Provider receipts still require dedicated canaries.
- Explicit social-authentication user cancellation is an expected outcome. Generic
  exceptions containing the word cancelled, provider interruption and real failures
  remain reportable to diagnostics.
- Calculator result sheets pin the localized Close action outside the scrolling
  body, keep a minimum 48 logical-pixel target, handle keyboard insets and Escape,
  expose accessible semantics and wrap long results at large text sizes. Formulas
  are unchanged. Tests must assert a dismissed sheet is absent before proceeding.
- Native test entry points make missed hit tests fatal. Suppressing them would hide
  an obstruction, not prove an interaction succeeded.

## Verification and operations

Focused tests cover chat queue isolation, navigation supersession, provider-lane
isolation, lease replacement/reclamation, payment snapshots and calculator dismissal.
The calculator pass recorded 2,721 host tests passing and a clean analyzer. Native
API-35 build/install succeeded, but the runner stalled before assertions; neither
that attempt nor earlier two-device stalls certify the Android journey. Physical
device and iOS/provider/store evidence remain separately required.

For rollout, package the source-derived contract manifests with the API and Portal,
verify actual database objects in every cell, retain application/database backups,
preserve deployment configuration, and check readiness plus anonymous Portal routes.
When objects already match, do not rerun historical pricing/content seeds or stamp
metadata just to make a release appear newer. Monitor chat/provider lane failures,
oldest pending age, reclaimed leases and conflicting finalizations after rollout.

## Source references

The application [build-101 deployment record](https://github.com/KiloDriveApp/KiloDrive/blob/main/docs/reports/RELEASE_101_DEPLOYMENT_2026-09-08.md)
records API/Portal rollout, eight-database object parity, unchanged configuration,
signed Android artifacts and live changelog publication. It also records the
isolated changelog SQL ambiguity caught and corrected before publication. The
release does not promote unexecuted native/provider tests to passed status.

The extended disposable restore gate remains blocked by extra index/FK count
differences already present in canonical bootstrap (JM and mature cells versus
US/CA). Required signatures, balanced data restoration and two alignment passes
passed; restoration introduced no drift. This is not complete physical parity.
Review normalized signatures and workload evidence before changing constraints;
the deployment applied no physical schema DDL.

- [Application repository](https://github.com/KiloDriveApp/KiloDrive)
- [Chat/outbox hardening evidence](https://github.com/KiloDriveApp/KiloDrive/blob/main/docs/reports/TRIP_CHAT_OUTBOX_MATURITY_PASS_2026-09-08.md)
- [Calculator dismissal evidence](https://github.com/KiloDriveApp/KiloDrive/blob/main/docs/reports/CALCULATOR_SHEET_DISMISSAL_2026-09-08.md)
- [Mobile contributor setup](https://github.com/KiloDriveApp/KiloDrive/blob/main/src/client/mobile/README.md)
