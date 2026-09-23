# ADR 014: Versioned database authority for foreign exchange

- **Status:** Accepted
- **Date:** 2026-09-23

## Context

Independent configuration rates and current-rate reconstruction can produce
different wallet credits, fees, refunds and reports for the same provider
charge. A live market lookup during settlement also makes historical evidence
non-repeatable.

## Decision

The control database owns immutable FX rate versions, evidence, pair state,
currency metadata and provider-fee policy. Country cells own quotes and
transaction snapshots. Money uses integer minor units, rates use exact decimals
with explicit direction, and one conversion component owns rounding.

Rates follow maker-checker lifecycle and cannot be edited after activation.
Every financial operation binds a fresh approved rate and fee snapshot before
provider I/O. All later lifecycle events use that snapshot. Reconciliation is
read-only; corrections use reviewed compensating postings.

## Consequences

Checkout fails before creating a payment when evidence is missing or stale.
Historical refunds remain explainable after the active rate changes. Operators
need evidence refresh, approval, activation, suspension and exception workflows.
External sources inform review but never become transactional runtime authority.

## Validation

Tests cover direct and derived pairs, identity conversion, rounding boundaries,
overflow, stale/missing/suspended evidence, maker-checker separation, concurrent
activation, quote expiry, provider response loss, refund/dispute reuse of the
snapshot, and reconciliation mismatch without mutation.
