# Build 168 operational handover

- **Owner:** Release Engineering, Identity, Financial Control and Messaging Operations
- **Status:** Reviewed public-safe checkpoint and incident decision aid; not whole-app certification
- **Last exercised:** 2026-10-03, bounded automated, production-readback and Samsung observations; historical Play results retain build 167
- **Related architecture:** [Native adapters and billing](../architecture/native-adapters-and-store-billing.md), [financial systems](../architecture/financial-systems.md), and [two-app boundary](../architecture/two-mobile-apps-and-security-2026-09-30.md)

## Release facts and evidence source

Historical build-168 source snapshot: consumer **1.0.0+168**, separate System Admin **0.1.0+10**,
schema **2026.10.02.3**, read from the application's two pubspecs and canonical
schema contract. The reviewed application source is
[commit df37a2a7](https://github.com/KiloDriveApp/KiloDrive/commit/df37a2a7bac8810ea74c570434dc9a68fa22901b).
The public [change record](https://kilodrive.com/changelog/1.0.0/build/168)
describes the customer-visible improvements. Publication of notes is not store
approval or proof of a completed iOS release.

This public-safe record omits account identities, resource names, credentials,
provider tokens, device IDs, private payloads and copy-and-paste production
access instructions. Protected result bundles stay in restricted evidence
storage under their retention policy. The application repository's dated
build-168 verification snapshot supplies exact rerun cases and commands for
authorized maintainers; this repository describes their limits.

## What is authoritative now

| Boundary | Current rule | First safe operator action |
| --- | --- | --- |
| Session and document capture | Native callbacks are scoped/generation-fenced; transient device checks preserve the route, terminal restrictions still clean it up | Check identity/session decision and exact installed artifact before repeating picker/upload work |
| Current membership | Effective server tier/term, access-through and pending change determine display | Reconcile the provider-owned operation, not the visible purchase sheet |
| Google lifecycle | Authenticated RTDN is a wake-up; provider status and immutable exact-order/period evidence are separate authorities | Check account binding, acknowledgement, notification freshness and money proof independently |
| Push attention | Current verified installation capability and preference revision determine quiet/no-vibration handling | Refresh normal registration; never infer channel support from the build number or override opt-out |
| Outbox | A committed intent must be claimable under its actual enum; Pending is one | Inspect exact producer/type/state/lease and idempotent handler before a reviewed replay |
| Public errors | `KD-XXXXX` identifies a catalogued situation; correlation identifies an occurrence | Read the code's outcome and one remediation action before recommending retry |

## What was actually checked

- Complete Release solution build passed without warnings/errors. The default
  .NET lane passed **7,748**, failed zero and explicitly skipped **137** cases.
  Skipped integration/provider cases are not passes.
- The selected current-schema MySQL lane passed **nine** cases. It proves
  those controlled first-token, renewal/cancellation/refund-recovery and trip
  boundaries, not the whole integration manifest or genuine provider refunds.
- The exact complete pre-push gate passed **4,275 consumer Flutter** and
  **1,242 Admin Flutter** tests. Counts are suite results, not feature counts.
- The tested API/error catalog deployed and readiness was Healthy; the control
  schema plus seven country schemas matched. No fresh DDL was needed. Structure
  and health are not provider or country certification.
- Signed Android packaging passed. Samsung build-168 checks exercised inactive
  membership, Manage/Current tab agreement and background/resume. Earlier
  build-167 purchase/cancellation and session-cycle observations retain their
  original artifact identity.
- Seven exact invalid-zero membership outbox rows were recovered with audit,
  then independently found Completed; six reporting facts were ingested once
  and an administrator notification reached provider handoff. No historical
  charge, fee, balance or paid entitlement was fabricated. Provider handoff is
  not an inbox-delivery certificate.

## Diagnose the right kind of failure

1. Assign one owner and record app/API/schema identity, role, country and safe
   support/correlation references. Use UTC in retained technical timelines;
   show the user's or selected administrator's timezone in the UI.
2. Classify confirmed commit, confirmed no-op/not completed, normal waiting,
   unknown/checking or manual review. Cancelled, empty, stale read and failed
   mutation must not collapse into the same generic error.
3. Inspect durable authority: central identity, country aggregate, or the
   provider/payment/ledger/hold/membership/receipt evidence graph. Realtime and
   push tell the client to reconcile; they are not the transition itself.
4. Preserve original operation, revision and idempotency identity. Check
   independent outcome before retry. A missing row, closed screen or lost
   response alone does not prove the action did not commit.
5. Route to the owned runbook: [store reconciliation](store-entitlement-reconciliation.md),
   [payment recovery](payment-operation-recovery.md),
   [outbox recovery](outbox-recovery.md), or
   [authentication](authentication-session.md).
6. Verify the affected user's result and backlog convergence. Record what was
   observed, blocked or unperformed rather than closing on a green feature flag.

## Queue repairs are not financial correction

The historical seven-row recovery is not a reusable wildcard query. Any repair
needs an exact authorized scope, current row locks and state/lease/payload
preconditions, a fully rolled-back rehearsal, backup and deduplicated audit.
Preserve historical source timestamps. Prove dispatch and ingestion afterward.
Never delete history or manufacture provider cost to clear a warning. Money
correction uses a reviewed compensating command and remains separate from queue
status repair.

## Public warning and error support path

Use [the authoritative public catalog](https://kilodrive.com/help/codes).
Every situation uses the hyphenated five-digit format; a semantic machine code
and occurrence correlation stay separate. The catalog defines meaning, outcome
certainty, likely causes, prevention, retry behavior and a primary safe action.
An actionable typed warning on a successful operation is not an ordinary failed
mutation. Public documentation must not include internal provider responses,
tokens, credentials, personal details or private evidence.

## Remaining gates and rollback

Physical first-purchase interruption, genuine provider refund/chargeback, fresh
post-fix renewal financial proof, a new complete build-168 two-device push/call/GPS
matrix, iOS StoreKit/APNs/CallKit and Apple production notification activation
still need their own evidence. Four Caribbean numeric import packs remain
reference-only. Missing provider costs remain explicit rather than invented zero.

Contain the narrow failing capability, not unrelated countries or all accounts.
Rollback only to a reviewed API/client pair compatible with schema and queued
work. Preserve pending operations, immutable money and audit. Existing public
code aliases retain history; never recycle a code to disguise a changed cause.
Use [two-app release control](two-app-release-and-compatibility.md) and the
restricted completion matrix for the actual go/no-go decision.
