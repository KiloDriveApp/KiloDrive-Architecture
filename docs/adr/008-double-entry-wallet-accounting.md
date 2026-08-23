# ADR 008: Pair wallet subledgers with immutable double-entry accounting

- **Status:** Accepted
- **Date:** 2026-08-23
- **Decision owners:** Finance, Payments, Architecture, and Operations
- **Related systems:** Wallets, payments, cashouts, memberships, rides, deliveries, rentals, vouchers, refunds, and reconciliation

## Context

KiloDrive shows people a wallet balance, but a balance is only the latest answer.
It cannot explain which event changed the answer, whether value came from a
provider, whether a cashout is merely held or already settled, or whether a
refund reversed the correct purchase. A mutable balance by itself also gives an
operator no reliable way to distinguish a real business loss from a display or
query bug.

The platform handles several kinds of value: customer top-ups, transfers, ride
and delivery escrow, driver earnings, membership fees, vouchers, cashouts,
refunds, disputes, chargebacks, promotions, and provider settlement. Many of
these operations cross time and failure boundaries. A payment provider may
capture after the caller times out. A payout may be approved today and settle
tomorrow. A store may send a renewal notification twice or out of order.

We therefore need evidence that answers both a product question—“why did this
user's balance change?”—and an accounting question—“where did the value come
from, where did it go, and do the books still balance?”

## Decision drivers

- Monetary amounts must be exact across zero-, two-, and three-decimal
  currencies.
- A customer-visible balance needs an understandable transaction history.
- Every material financial event needs balanced accounting evidence.
- Duplicate, delayed, and out-of-order provider messages must not move money
  twice.
- Held funds must be distinguishable from spendable funds.
- Refunds, reversals, disputes, and chargebacks must preserve history rather
  than rewrite it.
- A country cell must settle locally without a distributed transaction against
  the global control database.
- Operations needs a reconciliation process that can fail cashout closed when
  a real unexplained difference exists.

## Decision

KiloDrive records each material money movement in four connected layers:

1. the domain entity and lifecycle state, such as a transfer, payment,
   membership, cashout, trip, or refund;
2. an append-only wallet subledger that explains the user's available and held
   balance;
3. an immutable double-entry journal whose debit lines equal its credit lines;
   and
4. provider evidence, where an outside processor or store is involved.

All durable amounts use signed 64-bit minor units plus an ISO 4217 currency
code. A journal entry contains one or more debit lines and one or more credit
lines, a posting timestamp, tenant/country ownership, a stable business
reference, and a link to the originating payment or domain event. A posting
rule rejects zero-value lines, a line that is both debit and credit, an
unbalanced entry, a currency mismatch, or a duplicate canonical reference.

The domain transition, wallet/subledger mutation, journal, and durable outbox
messages commit in one short country-cell transaction. Provider I/O, email,
receipt rendering, push, and webhooks do not run inside that transaction.

### Available balance and held balance

A hold does not subtract money from history and invent it again later. It moves
value from available to reserved state with a linked reason. Completion can
release the hold into the recipient entitlement; cancellation can release it
back to available funds. Reconciliation proves that active holds agree with the
domain records that justify them.

### Stable references and idempotency

Each posting rule derives one canonical reference from the actual business
event, for example the payment identifier plus the posting purpose. The same
reference is used by command idempotency, the journal, provider reconciliation,
and duplicate detection. Different code paths for an initial store purchase and
a store renewal may use different event types, but they must still link to the
same internal payment identity convention.

### Corrections

Posted evidence is never edited in place to make a report balance. A correction
is a reversing or adjusting journal with its own reference, reason, actor, and
link to the original. Partial refunds carry an explicit minor-unit amount and
cannot exceed the unreversed original value. A full membership chargeback may
also revoke the remaining entitlement, but a partial refund does not silently
pretend the entire service period disappeared.

### Locking and transactions

Commands acquire wallet rows in a deterministic identifier order, revalidate
status and limits inside the transaction, and use conditional state/version
updates for lifecycle rows. This keeps opposite-direction transfers from
deadlocking unnecessarily and prevents two concurrent requests from spending
the same available funds. Cross-country transfers are not introduced until an
approved settlement model can preserve these invariants without a distributed
database transaction.

### Reconciliation

The daily reconciliation process compares wallet balances, held funds, payment
states, accounting journals, payout clearing, provider/store evidence, refunds,
and settlement totals by tenant, country, date, and currency. “Approved” and
“Completed” cashouts are not collapsed into one expectation: approved amounts
are payable, while completed amounts move through settled clearing. An
unexplained critical exception blocks new cashouts for the affected scope and
pages the accountable operator; it does not delete evidence or hide the row.

## Alternatives considered

### Store only a mutable wallet balance

This is easy to build and fast to read, but it cannot explain changes, detect a
missing entry, reconstruct history, or support defensible reconciliation. It
was rejected for every financial feature.

### Keep a single-entry wallet transaction list

A subledger is valuable for support and product views, but one-sided entries do
not prove where value came from or went. A bug can credit a user without a
corresponding liability or clearing movement. We keep the subledger and pair it
with the general journal rather than choosing one or the other.

### Treat the payment provider as the accounting system

A provider sees only its own rails. It does not understand cash rides, internal
wallet transfers, holds, vouchers, membership entitlements, or another
provider's transactions. Provider reports are reconciliation evidence, not
KiloDrive's complete books.

### Put accounting in a separate service immediately

An independent ledger service can become appropriate when a dedicated finance
platform team and throughput justify it. Today it would split transactions and
add network failure to every money mutation. The country-cell transaction keeps
the invariants local while interfaces and posting rules keep a future boundary
possible.

## Consequences

### Benefits

- Every displayed balance has a traceable explanation.
- Debits-equal-credits catches entire classes of one-sided implementation bugs.
- Holds, payable, clearing, settled, refund, and dispute states remain visible.
- Provider reconciliation can identify missing, duplicated, or incorrectly
  classified events.
- Support, finance, compliance, and engineering can use the same stable trace
  without exposing payment instruments.
- Corrections preserve a trustworthy history.

### Costs and risks

- Every new money feature needs a reviewed lifecycle and posting rule, not just
  a balance update.
- Read models and reports are more involved than a single balance column.
- A wrong posting template can be balanced yet semantically wrong; finance must
  review account meaning as well as arithmetic.
- Backfills require careful reference construction and reconciliation evidence.
- Journal and subledger storage grows continuously and needs governed retention
  and archival rules rather than deletion.

## Security, privacy, and compliance

Journals and subledgers store safe business identifiers, masked display details,
amount, currency, state, and actor/correlation evidence. They do not contain raw
bank accounts, card numbers, access tokens, OTPs, or provider secrets. Executable
payout instructions are encrypted or tokenized with a dedicated protected key
and snapshotted immutably onto the cashout.

Administrative adjustments require fine-grained permission, recent step-up
authentication where policy requires it, a reason, a balanced journal, and an
audit event. No admin interface exposes a “set balance” shortcut.

## Reliability and operations

- Financial writes use idempotency keys and unique business references.
- Outbox handlers tolerate at-least-once delivery.
- A provider timeout after mutation is treated as an unknown outcome and
  reconciled before retry.
- Reconciliation metrics report counts and amounts by safe dimensions, never
  customer details.
- Recovery posts an approved correction or resumes an idempotent transition; it
  does not patch a production balance casually.
- The [wallet reconciliation runbook](../runbooks/wallet-reconciliation.md)
  defines triage, containment, repair, and proof.

## Validation

- Property tests generate transfers, holds, releases, settlements, refunds,
  and reversals and assert debit total equals credit total.
- MySQL crash-point tests stop before and after domain, wallet, journal, and
  outbox writes and prove all-or-nothing commit.
- Concurrent opposite transfers prove deterministic locking and no overspend.
- Duplicate and payload-mismatched idempotency tests prove exactly-once business
  effect.
- Provider fixtures cover duplicate/out-of-order webhook, timeout after capture,
  partial refund, chargeback, currency mismatch, and cashout reversal.
- Daily fixture reconciliation must end with zero unexplained money before
  production cashout is enabled.

## Follow-up

- Keep [financial systems](../architecture/financial-systems.md) and posting-rule
  examples synchronized with implemented lifecycles.
- Require a finance owner to approve every new account and posting template.
- Archive release reconciliation evidence and provider totals by currency.
- Revisit a dedicated ledger service only with measured scale and an atomic
  migration design.
