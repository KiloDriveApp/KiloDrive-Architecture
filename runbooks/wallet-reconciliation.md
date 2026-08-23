# Runbook: Wallet and Accounting Reconciliation

## Trigger

Ledger imbalance, held-fund mismatch, provider settlement difference,
unreconciled refund/chargeback, duplicate reference, or cashout readiness block.

## Procedure

1. Stop new cashout when the critical reconciliation gate requires it.
2. Identify currency, country cell, payment/cashout reference, journal, wallet
   transactions, provider IDs, and lifecycle status.
3. Prove debits equal credits and distinguish available, held, payable, clearing,
   settled, revenue, and reversal states.
4. Reconcile provider evidence for unknown capture/refund/payout outcomes.
5. Correct with an idempotent reversing/adjusting journal and governed domain
   transition; never edit/delete a posted journal.
6. Verify user balance, held funds, provider total, entitlement, receipt,
   notification, audit, and daily exception report.
7. Require zero unexplained money before re-enabling production cashout.

All investigation artifacts redact payment instruments, bank details, contact
data, and provider secrets.
