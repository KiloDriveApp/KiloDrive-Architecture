# Wallet, Membership, Billing, and Accounting

## Money representation

All durable amounts are signed 64-bit integer minor units with an ISO currency.
No financial decision uses binary floating point. Currency exponent and locale
formatting are presentation concerns; conversion uses exact decimal-string
arithmetic and reviewed FX snapshots.

## Wallet and ledger

Wallet balances are supported by immutable transactions and double-entry
accounting journals. Idempotent references prevent duplicate posting. Available,
held, payable, clearing, revenue, expense, and settlement concepts remain
distinct so top-ups, transfers, fares, refunds, chargebacks, cashouts, vouchers,
and membership events can reconcile.

Financial mutations lock and validate the relevant wallet/account state, post
the domain record and ledger/journal in one transaction, and emit provider work
through the outbox. Cashout can fail closed when critical reconciliation
exceptions exist.

## Memberships

Riders remain free. Driver and rental memberships use a no-commission operating
model with plan benefits, usage limits, and supported terms. Store products are
mapped to internal plan and term records; the server validates Apple/Google
evidence before entitlement. Purchase acknowledgement and server notifications
are durable lifecycle concerns.

Renewal preserves the purchased term, price source, service period, grace state,
and journal linkage. Upgrade/downgrade proration is based on actual paid service,
not only a catalogue default.

## External payments

Provider webhooks are authenticated, idempotently claimed, and reconciled to an
existing payment. Unknown outcomes are reconciled before retry. Refunds,
chargebacks, partial reversals, and revocations update payment, entitlement,
ledger, notification, and audit state atomically where they apply.

## Operating controls

- Country wallet features remain gated by an approved legal/money-movement
  matrix.
- KYC/AML flags can restrict sending, receiving, top-up, or cashout.
- Payout destinations use encrypted provider tokens or instructions and an
  immutable cashout snapshot; masked values are for display only.
- Daily exception reports identify imbalance, unreconciled provider settlement,
  and held-fund anomalies without exposing customer payloads.
