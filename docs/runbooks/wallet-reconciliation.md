# Wallet and accounting reconciliation runbook

- **Owner:** Financial operations, accounting engineering, and payment-provider owners
- **Status:** Operational financial-control procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Financial systems](../architecture/financial-systems.md), [tenancy and country cells](../architecture/tenancy-and-country-cells.md), and [observability](../architecture/observability.md)

## Purpose and scope

Use this runbook to prove that KiloDrive's customer-facing wallet summaries,
wallet subledger, immutable double-entry journals, held funds, domain lifecycles,
and external provider settlements agree for each country and currency.

It covers top-ups, transfers, ride/delivery payments and escrow, memberships,
refunds, chargebacks, vouchers, cashouts, provider settlements, and administrative
adjustments. Reconciliation detects and contains inconsistencies. It does not
authorize an operator to edit a balance or rewrite history.

## Owners and roles

| Role | Responsibility |
| --- | --- |
| Financial incident lead | Owns scope, customer-money containment, and closure |
| Reconciliation owner | Runs invariant checks and classifies exceptions |
| Domain owner | Explains the expected lifecycle/posting rule for affected product |
| Provider owner | Confirms external outcomes by stable provider reference |
| Database operator | Runs bounded read-only queries and reviewed compensating scripts |
| Reviewer/approver | Independently approves repair and cashout re-enablement |

No operator should both invent and approve a financial repair. Separate customer
support communication from technical evidence so private account details are not
copied into engineering channels.

## Accounting model in plain language

KiloDrive keeps several views of the same economic event:

1. **Wallet snapshot** — fast current available and held totals.
2. **Wallet subledger** — customer-visible movements with unique business
   references.
3. **Accounting journal** — immutable balanced debit and credit lines.
4. **Domain state** — trip, delivery, membership, voucher, payment, cashout, or
   dispute lifecycle that explains why the movement exists.
5. **Provider state** — capture, settlement, refund, chargeback, payout, or store
   transaction outside KiloDrive.

The snapshot is a derived convenience, not permission to ignore the journal. The
journal being balanced is necessary but not sufficient: a balanced posting can
still point to the wrong wallet, currency, term, or provider outcome.

## Core invariants

For every supported event type:

- sum of debit lines equals sum of credit lines per journal/currency;
- every business reference is unique for its idempotency scope;
- wallet snapshot equals opening position plus subledger movements;
- available and held movements conserve value according to the state machine;
- active escrow/cashout holds equal held balances attributed to those domains;
- provider captures/refunds/settlements equal recognized payment/journal totals;
- membership entitlement, paid term/service period, payment, and journal agree;
- voucher face/credit/currency conversion follows the approved rate/exponent;
- partial refunds reverse only the refunded amount; and
- administrative adjustments have authorization, reason, durable audit, and a
  balanced journal.

Minor-unit integers are authoritative. Never reconcile by binary floating-point
or assume all currencies have two decimal places.

## Preconditions

- Reconciliation code/version and query timestamp are known.
- Control and relevant country-cell schema fingerprints are valid.
- Provider exports/APIs are accessed with approved read-only or scoped roles.
- Time window, country, currency, product types, and settlement cutoff are clear.
- A safe way exists to disable cashout or a narrower affected mutation.
- Provider reference, payment ID, business reference, and correlation ID can be
  traced without searching by raw card/bank/contact data.
- A disposable fixture environment supports crash-point and provider-fake tests.

## Safety and stop conditions

Immediately stop affected cashout or money movement when:

- debit does not equal credit;
- a wallet snapshot/subledger mismatch could permit overspend;
- held funds cannot be tied to valid active obligations;
- a provider success/failure outcome is unknown and retry could duplicate value;
- duplicate journal/subledger references exist;
- currency code/exponent is inconsistent;
- reconciliation logic itself excludes a valid terminal state; or
- the proposed repair edits/deletes an immutable journal or directly overwrites a
  balance.

Do not disable reconciliation to reopen cashout. Do not rerun a capture, payout,
refund, voucher, or transfer until the original outcome is classified. Do not put
bank details, payment tokens, contact information, or full provider payloads in
the incident record.

## Scheduled daily procedure

Run per country cell and currency, then aggregate safely:

1. Record UTC cutoff, schema/package/reconciliation version, and run ID.
2. Verify worker heartbeat and completeness of required source data.
3. Check journal debit-equals-credit and orphan header/line records.
4. Check duplicate business/provider/idempotency references.
5. Rebuild expected wallet totals from opening snapshot plus subledger and compare
   available/held balances.
6. Reconcile holds to active ride escrow, delivery escrow, pending/approved
   cashouts, and any other hold-owning lifecycle.
7. Reconcile top-ups, transfers, vouchers, fares, memberships, refunds,
   chargebacks, and admin adjustments to payments and journals.
8. Reconcile provider capture/refund/dispute/settlement/payout/store state using a
   defined cutoff and expected timing window.
9. Separate payable cashout clearing from settled cashout clearing; both Approved
   and Completed states remain represented appropriately.
10. Publish a sanitized exception report grouped by invariant, country, currency,
    age, count, and amount.
11. Alert on new or worsening actionable exceptions; do not page repeatedly for
    a documented maintenance suppression.

A report must show its data-through timestamp. A green badge based on yesterday's
run is not current assurance.

## Diagnosis and investigation workflow

### 1. Find the earliest bad reference

Start with the earliest exception in the causal chain, not the latest aggregate
balance. Trace the stable business reference across domain entity, payment,
wallet subledger, journal, outbox, webhook, audit, and provider evidence.

### 2. Classify the provider outcome

Mark external outcome as **confirmed success**, **confirmed rejection**, or
**unknown**. A timeout is unknown, not failure. Query the provider by the stable
idempotency/reference before retrying.

### 3. Identify defect class

- posting rule omitted/wrong accounts;
- non-atomic domain/subledger/journal transition;
- missing idempotency or conditional state/version enforcement;
- lifecycle expectation omitted a valid state;
- provider mapping/reference mismatch;
- currency exponent/FX conversion defect;
- partial reversal handled as full;
- membership term/price snapshot lost;
- stale/incorrect reconciliation query; or
- unauthorized/manual data modification.

### 4. Reproduce with fixtures and crash points

Reproduce at: before commit, after commit/before response, before outbox publish,
after provider success/before local finalization, duplicate/out-of-order webhook,
and concurrent request. Prove both first execution and idempotent replay.

### 5. Design an additive repair

Repair through a supported domain transition or a reviewed compensating journal
linked to the original reference. Include reason, approver, currency, exact minor
amount, and audit. Never mutate the original balanced journal to make the report
look correct.

### 6. Verify globally enough

After the repair, rerun the entire country/currency reconciliation and the
cross-system aggregate—not only the affected row.

## Mismatch playbook

| Finding | Common cause | Containment | Repair direction |
| --- | --- | --- | --- |
| Unbalanced journal | incomplete posting/manual edit | stop affected path and cashout | restore integrity via reviewed compensating entry and code fix |
| Duplicate reference | retry/race without idempotent claim | stop replay source | select authoritative outcome, compensate duplicate, enforce uniqueness |
| Wallet snapshot differs | partial commit or stale repair | block wallet spend/cashout | rebuild expected state, compensate, fix atomic boundary |
| Held funds differ | missed release/refund or wrong terminal state | pause relevant lifecycle | execute idempotent hold release/refund transition |
| Provider capture lacks payment/journal | timeout or webhook/outbox gap | no recapture | finalize existing success by stable provider reference |
| Payment exists, provider rejected | premature local entitlement/credit | block spend/entitlement | entity-aware reversal plus notification/audit |
| Completed cashout mismatches | reconciler ignores settled clearing | keep cashout blocked until query proven | correct payable-versus-settled expectation; preserve history |
| Store membership mismatches | inconsistent journal reference/product/base plan | pause affected purchase mapping | canonical payment-linked reference; reconcile entitlement/ack |
| Renewal wrong term/price | plan defaults used instead of purchased snapshot | pause auto-renew for plan | restore renewable term/price/service-period source |
| Partial refund revokes all | reversal contract lacks amount | stop automated reversal | amount-aware proportional reversal and entitlement rule |
| FX mismatch | multiplied minor units without exponent conversion | stop cross-currency feature | exact decimal/exponent-aware conversion and compensation |

## Domain-specific checks

### Top-ups and vouchers

Verify provider capture or approved voucher redemption, payment currency, credited
wallet currency, FX source/effective time, unique redemption, journal, and wallet
credit. A voucher code must not be the only durable security secret; its redemption
is conditionally claimed.

For wallet top-ups, compare the durable customer status keyed by payment ID and
idempotency key with provider, payment, journal, and wallet state. `Pending`,
`Completed`, `Failed`, and `Needs attention` are recovery states, not display
guesses. A timeout after capture, process death, delayed/duplicate/out-of-order
webhook, or stale client must converge through the original reference. Confirm
the protected pending reference belongs to the current account, completion
refreshes wallet state, and receipt/support actions reference the same payment.
Do not generalize this implemented top-up status contract to every payment type
without equivalent crash-point tests.

For an administrative issuance batch, start with the durable operation
reference—not a plaintext code list. Confirm:

- tenant, administrator, route, request hash, face value, credit currency and
  quantity are one idempotency scope;
- one completed scope owns exactly one contiguous response set and expected
  aggregate promotional value;
- a replay returned the same voucher identifiers rather than creating another
  set, while a payload mismatch was rejected;
- the encrypted replay body is readable only through the intended Data
  Protection purpose and the HMAC lookup key is present and protected;
- active, redeemed, expired and revoked counts sum to issued count;
- each redemption appears at most once and links to one wallet credit and one
  balanced journal; and
- no full code, replay body, HMAC key, or customer identity entered evidence.

If the administrator reports a timeout after generation, **do not issue another
batch with a new idempotency key**. Reconcile the original operation reference
and key first. If the key ring is unavailable, contain issuance and preserve the
encrypted record; changing voucher state or minting replacements is not a key-
recovery procedure.

### Transfers

Lock sender and receiver in deterministic order. Verify sender/receiver are
allowed to transact, amount is within country/account limits, debit/credit are one
atomic operation, trace number is unique, and notifications/receipt happen after
commit through durable work. A notification failure does not reverse a transfer.

### Rides and deliveries

Compare fare/payment method, escrow hold/release/refund, driver net, commission or
membership mode, cash debt, completion/cancellation state, and receipt. Actual
distance/duration should come from validated telemetry/map matching or an audited
bounded override.

For a fare split, compare the plan quote/authorized/settled totals, every payer's
accepted allocation, wallet hold, payment row, settlement or release, fallback
responsibility, and trip state. At this baseline the feature remains unavailable:
canonical bootstrap parity, mandatory version/stable retry, renewed consent after
fare changes, insufficient-funds fallback, expiry/audit queues, Portal status,
and reversal integration are incomplete. Do not repair a missing share with an
ordinary wallet transfer or enable the feature merely because alignment SQL can
create the tables.

### Memberships

Verify plan foreign key, customer type, term, actual billed price source, service
period, upgrade credit/proration, renewal/grace deadline, payment, journal,
entitlement, store product/base plan/offer, acknowledgement state, refund,
revocation, and chargeback. Use one canonical payment-linked journal reference
for initial purchase and renewal.

### Cashouts

Require a verified payout method and immutable encrypted destination snapshot.
Verify requested hold, Approved payable clearing, Completed settled clearing,
rejection/reversal release, provider payout ID, limits, 2FA/step-up, and admin
audit. Prevent payout-method deletion while Pending or Approved work references it.

The payout automation backend remains dormant. Do not populate certification
timestamps by direct row edit or describe a locally confirmed destination as
provider verified. Activation requires a supported dual-controlled command,
named-provider ownership proof, tenant/country-safe signed callback handling,
duplicate/out-of-order/unknown/crash tests, return/reversal journals, measured
processing evidence, and zero unexplained reconciliation. “Instant payout” stays
unavailable until its separate measured certification passes.

## Recovery and repair execution

1. Write tests that fail for the original defect and pass for duplicate/retry
   paths.
2. Review the compensating domain command/journal and exact affected set.
3. Prove on a production-shape disposable clone using sanitized fixtures.
4. Record before-state run ID and amounts by country/currency.
5. Disable the narrow mutation and drain conflicting workers.
6. Execute the idempotent repair with a stable repair reference.
7. Rerun complete reconciliation and compare before/after exceptions.
8. Deploy the preventing code/constraint before reenabling the path.
9. Observe provider settlement and the next scheduled reconciliation cycle.

## Cashout re-enablement gate

Cashout can resume only when:

- there are zero unresolved critical exceptions;
- every known provider outcome around the incident is classified;
- schema, worker, queue, outbox, and reconciliation are healthy;
- payout credentials/method verification are valid;
- a controlled non-user cashout approval/completion/reversal fixture passes;
- the financial owner and independent reviewer approve; and
- monitoring/alert thresholds are active.

## Rollback

Financial repair rollback is another compensating transaction, not deletion of
the repair. If a new release causes mismatches, disable its feature, preserve
committed truth, and return the binary only when schema/contracts remain
compatible. Do not reverse a confirmed provider event merely because the
application release is rolled back.

## Verification criteria

- Debit equals credit for every journal.
- Business/provider/idempotency references are unique as designed.
- Wallet available/held snapshots equal subledger-derived values.
- Holds reconcile to active and terminal domain states.
- Payment, entitlement, cashout, voucher, ride/delivery, and provider totals agree
  per country/currency/cutoff.
- No customer can spend value twice or lose value silently.
- Exception report shows zero unexplained critical findings and a fresh timestamp.
- Regression/property/crash-point/concurrency tests pass.
- The next provider settlement and scheduled reconciliation remain clean.

## Evidence to retain

Retain run/incident ID, UTC cutoff, package/schema/query version, affected
country/currency/count/amount, invariant category, stable business/provider IDs,
before/after reports, compensating references, tests, reviewer approvals,
deployment, cashout gate decision, and monitoring result.

Redact names, emails, phone numbers, bank/account details, payment tokens,
document paths, and raw provider payloads.

## Escalation

Escalate unexplained value creation/loss, cross-wallet/currency posting, duplicate
capture/payout, provider compromise, unauthorized adjustment, widespread stale
reconciliation, or inability to identify the authoritative outcome immediately
to incident command, financial leadership, security, and legal/compliance as
required.

## Common pitfalls

- Declaring success because journals balance while they point to the wrong wallet.
- Excluding Completed cashouts from expected clearing and blocking all future
  withdrawals.
- Using different membership journal references for purchase and renewal.
- Treating provider timeout as failure and retrying a successful capture.
- Reversing a partial refund as if it were full.
- Renewing at the plan's current fee/period instead of the purchased term snapshot.
- Multiplying minor units by FX without respecting zero-/three-decimal currencies.
- Directly setting a wallet balance and losing the accounting explanation.
- Reenabling cashout after a single green query with a stale timestamp.
