# Payment and wallet operation recovery

- **Owner:** Payments and Wallet Platform
- **Status:** Reviewed public procedure
- **Last exercised:** 2026-09-23 (source and automated-test review)
- **Related architecture:** [Financial systems](../architecture/financial-systems.md)

## Trigger

Use this runbook when the client lost a response, a payment remains unresolved,
a provider webhook cannot bind to an internal operation, wallet credit and
provider capture disagree, or a user sees repeated recovery prompts.

## Classify the operation

1. Identify operation ID, payment ID, idempotency key, account scope,
   environment and safe support reference.
2. Determine the last proven boundary: no provider request, provider rejection,
   possible remote success, verified remote success, local commit, or local
   commit plus completed notification.
3. Join payment, provider event, FX snapshot, fee snapshot, wallet transaction,
   accounting journal, hold/cashout, receipt, notification and review case.
4. Never infer failure from a timeout or success from a browser redirect.

## Outcome handling

| Proven outcome | User-safe state | Permitted action |
| --- | --- | --- |
| No provider mutation / deterministic rejection | Failed | Correct the stated cause and deliberately start a new operation |
| Provider still processing | Checking | Continue bounded status checks with the same operation |
| Possible remote success | Outcome unknown | Reconcile; block blind duplicate submission |
| Provider success and local posting agree | Completed | Refresh wallet/history and clear the submitted draft |
| Provider success but local evidence mismatches | Manual review | Preserve evidence and open/reuse one restricted case |
| Customer cancelled before success | Cancelled | Return to draft without claiming money moved |

## Webhook binding

Verify signature and environment first. Bind using server-owned provider order,
capture, custom or payment references. Log only presence flags and stable hashes,
never raw identifiers or payloads. An unmatched verified event is retained or
counted for investigation according to provider policy; it does not create a
new wallet credit.

## Verification

- Replaying the original key returns the original result or current status.
- Exactly one wallet posting and balanced journal exist for completion.
- Rejected/failed checkout creates no wallet credit.
- The app does not show recovery before checkout has actually started.
- Completed recovery does not keep producing a global blocking prompt.
- Refund, dispute and reversal are compensating records linked to the original
  evidence graph.

## Abort and escalation

Escalate for account/environment mismatch, invalid signature, unidentified
provider success, duplicate money, broken journal balance, unsupported currency,
missing FX snapshot or provider history disagreement. Do not delete financial
evidence to make a test pass.
