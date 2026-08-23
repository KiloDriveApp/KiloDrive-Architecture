# Tutorial: Add a Money Movement Safely

Money code should begin with accounting sentences, not controller code. This
tutorial uses a fictional wallet transfer, but the method also applies to
top-ups, ride settlement, refunds, memberships, cashouts, and vouchers.

## Write the invariants first

Before choosing tables, state what must remain true:

- the sender cannot spend more available balance than permitted;
- held balance is not available balance;
- one logical transfer has one unique reference;
- the debit and credit use one ISO currency and one minor-unit scale;
- total journal debits equal total journal credits;
- a retry has no second economic effect;
- both parties remain authorized and unrestricted at commit time; and
- the resulting user balances reconcile to immutable transaction history.

If an invariant cannot be expressed clearly, the implementation is not ready.

## Keep the transaction inside one country cell

KiloDrive does not split a settlement transaction across control and country
databases. Both wallets and the financial journal involved in this example must
share one country-cell transaction.

Cross-country money movement is a separate regulated product, not “just” a
wallet transfer with two connection strings. It requires an approved operating
model, explicit FX and settlement, and a durable orchestration design.

## Parse money exactly once

APIs carry integer minor units. Human forms show major units. Convert a localized
decimal string to a minor-unit integer using decimal-string arithmetic and the
ISO exponent. Do not use binary floating point.

Examples:

- JMD `1,234.56` becomes `123456` minor units;
- JPY `1234` remains `1234` because the exponent is zero;
- a three-decimal currency accepts exactly three fractional digits.

Reject excess precision rather than silently rounding financial intent.

## Acquire locks in deterministic order

Two concurrent transfers in opposite directions can deadlock if each locks its
sender first. Sort wallet identifiers and lock in that stable order, then
recheck available balance and account restrictions inside the transaction.

Deadlocks can still occur. A retry policy must rerun the entire short,
idempotent transaction—not continue from a partially executed in-memory state.

## Claim idempotency before economic mutation

The logical request carries an idempotency key scoped to tenant and user. The
server binds it to the payload hash. Concurrent duplicates receive an
in-progress response; a completed retry receives the stored result; a different
payload under the same key is rejected.

Provider idempotency and API idempotency solve related but different problems.
When an external provider participates, pass a stable provider key and retain
the provider reference for reconciliation.

## Write the operational subledger

Each wallet receives an immutable transaction row describing direction,
amount, resulting balance, unique reference, related entity, and time.

The subledger answers the user's question: “Why did my wallet balance change?”
It also allows balance reconstruction and anomaly detection.

## Post the double-entry journal

The same transaction posts one balanced journal. A transfer within the wallet
liability account may debit “sender wallet liability” and credit “recipient
wallet liability,” with both lines tied to the same reference.

The general journal answers the accounting question: “Which economic accounts
changed, and is the event balanced?”

Never update or delete a posted journal to make a report green. Post an approved
reversal with a new unique reference and keep the original evidence.

## Use holds for work not yet settled

A ride or delivery paid by wallet should hold funds when the assignment becomes
binding. The hold reduces spendable balance without prematurely recognizing
final settlement.

Completion releases the hold into the defined settlement accounts. Eligible
cancellation releases it back to availability. Each transition has a unique
reference and concurrency test.

## Commit side-effect intent, not provider calls

Notifications, receipts, emails, and webhooks belong in the outbox. A transfer
must not roll back because an email provider is slow. Conversely, the API must
not tell the user the transfer failed after it actually committed merely
because receipt delivery failed.

## Reconcile from independent evidence

Daily reconciliation compares:

- materialized wallet balances;
- immutable wallet transaction sums;
- balanced journal entries;
- held-fund totals and their owning entities; and
- provider settlement totals and references.

Cashout should fail closed when critical unexplained money exists. Operators
investigate and reverse through approved entries; they do not disable the
reconciler to make the symptom disappear.

## Test cases worth keeping forever

- duplicate and concurrent transfer;
- sender balance changes between screen load and commit;
- sender or receiver becomes restricted before commit;
- zero, negative, overflow, exponent, whitespace, and excess-decimal input;
- database crash before and after commit;
- notification failure after commit;
- reversed transfer and repeated reversal;
- journal reference collision; and
- daily reconciliation after every terminal state.

Continue with [financial systems](../architecture/financial-systems.md) and the
[wallet reconciliation runbook](../runbooks/wallet-reconciliation.md).
