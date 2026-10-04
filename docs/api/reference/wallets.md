# Wallet, top-up, transfer and payout workflows

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## Operations on this page

- [GET `/api/v1/operations/status`](#get-apiv1operationsstatus)
- [GET `/api/v1/wallet`](#get-apiv1wallet)
- [GET `/api/v1/wallet/cashout`](#get-apiv1walletcashout)
- [POST `/api/v1/wallet/cashout`](#post-apiv1walletcashout)
- [GET `/api/v1/wallet/cashout/limits`](#get-apiv1walletcashoutlimits)
- [GET `/api/v1/wallet/cashout/{cashoutId}/status`](#get-apiv1walletcashoutcashoutidstatus)
- [GET `/api/v1/wallet/command-recovery`](#get-apiv1walletcommand-recovery)
- [GET `/api/v1/wallet/fee-products`](#get-apiv1walletfee-products)
- [POST `/api/v1/wallet/fee-products/{productId}/purchase`](#post-apiv1walletfee-productsproductidpurchase)
- [GET `/api/v1/wallet/fees`](#get-apiv1walletfees)
- [GET `/api/v1/wallet/financial-history`](#get-apiv1walletfinancial-history)
- [GET `/api/v1/wallet/financial-history/export/pdf`](#get-apiv1walletfinancial-historyexportpdf)
- [GET `/api/v1/wallet/financial-history/{entryId}`](#get-apiv1walletfinancial-historyentryid)
- [POST `/api/v1/wallet/financial-history/{entryId}/disputes`](#post-apiv1walletfinancial-historyentryiddisputes)
- [GET `/api/v1/wallet/financial-history/{entryId}/export/pdf`](#get-apiv1walletfinancial-historyentryidexportpdf)
- [GET `/api/v1/wallet/payments/status`](#get-apiv1walletpaymentsstatus)
- [GET `/api/v1/wallet/payments/{paymentId}/status`](#get-apiv1walletpaymentspaymentidstatus)
- [GET `/api/v1/wallet/payout-methods`](#get-apiv1walletpayout-methods)
- [POST `/api/v1/wallet/payout-methods`](#post-apiv1walletpayout-methods)
- [DELETE `/api/v1/wallet/payout-methods/{id}`](#delete-apiv1walletpayout-methodsid)
- [GET `/api/v1/wallet/recipients`](#get-apiv1walletrecipients)
- [POST `/api/v1/wallet/recipients`](#post-apiv1walletrecipients)
- [DELETE `/api/v1/wallet/recipients/{id}`](#delete-apiv1walletrecipientsid)
- [POST `/api/v1/wallet/topup`](#post-apiv1wallettopup)
- [GET `/api/v1/wallet/topup/bank-transfers`](#get-apiv1wallettopupbank-transfers)
- [POST `/api/v1/wallet/topup/bank-transfers/{paymentId}/cancel`](#post-apiv1wallettopupbank-transferspaymentidcancel)
- [GET `/api/v1/wallet/topup/limits`](#get-apiv1wallettopuplimits)
- [GET `/api/v1/wallet/topup/quote`](#get-apiv1wallettopupquote)
- [POST `/api/v1/wallet/topups/paypal/{operationId}/reconcile`](#post-apiv1wallettopupspaypaloperationidreconcile)
- [GET `/api/v1/wallet/topups/paypal/{operationId}/status`](#get-apiv1wallettopupspaypaloperationidstatus)
- [GET `/api/v1/wallet/transactions`](#get-apiv1wallettransactions)
- [GET `/api/v1/wallet/transactions/export`](#get-apiv1wallettransactionsexport)
- [GET `/api/v1/wallet/transactions/history`](#get-apiv1wallettransactionshistory)
- [POST `/api/v1/wallet/transfers`](#post-apiv1wallettransfers)
- [GET `/api/v1/wallet/transfers/quote`](#get-apiv1wallettransfersquote)

## GET `/api/v1/operations/status`

**What it does:** Read the caller's durable command outcome using its original key/reference; this read never executes the command.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [MoneyCommandRecoveryDto](../schemas/m.md#moneycommandrecoverydto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/wallet`

**What it does:** Read the current user's authoritative wallet, currency, held/available breakdown and revision.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [WalletDto](../schemas/w.md#walletdto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision` |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/wallet/cashout`

**What it does:** List the current account's withdrawal requests and their lifecycle states.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [CashoutDto](../schemas/c.md#cashoutdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/wallet/cashout`

**What it does:** Request a withdrawal and applicable hold; approval, provider dispatch and settlement are subsequent states.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

**Body:** [RequestCashoutDto](../schemas/r.md#requestcashoutdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. | minLength: `1`; maxLength: `256` |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | minLength: `1`; maxLength: `256` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [CashoutDto](../schemas/c.md#cashoutdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. The server can require recent authentication; local app unlock is not proof.

## GET `/api/v1/wallet/cashout/limits`

**What it does:** Read the current withdrawal bounds and applicable plan context before requesting a cashout.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [CashoutLimitsDto](../schemas/c.md#cashoutlimitsdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/wallet/cashout/{cashoutId}/status`

**What it does:** Read the owner's existing withdrawal outcome; pending approval or dispatch is not settlement.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cashoutId` | path | Yes | `string (uuid)` | Identifier of the related cashout record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [CashoutStatusResourceDto](../schemas/c.md#cashoutstatusresourcedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/wallet/command-recovery`

**What it does:** Read the compatibility command-recovery state; new clients prefer /api/v1/operations/status.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [MoneyCommandRecoveryDto](../schemas/m.md#moneycommandrecoverydto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/wallet/fee-products`

**What it does:** Read the permitted records/state for wallet / fee products. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [FeeProductDto](../schemas/f.md#feeproductdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/wallet/fee-products/{productId}/purchase`

**What it does:** Start the applicable purchase with server-owned financial validation in the wallet / fee products / purchase workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `productId` | path | Yes | `string (uuid)` | Identifier of the related product record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [FeePurchaseDto](../schemas/f.md#feepurchasedto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/wallet/fees`

**What it does:** Read the permitted records/state for wallet / fees. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [WalletFeeScheduleDto](../schemas/w.md#walletfeescheduledto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/wallet/financial-history`

**What it does:** Read the account's financial-history projection across supported payment and wallet events.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `preset` | query | Conditional or optional | `string` | Named range/filter preset accepted by this endpoint; explicit date bounds have separate semantics. | No further constraint recorded |
| `search` | query | Conditional or optional | `string` | Search text applied within this endpoint's authorized collection; it does not widen account/tenant scope. | No further constraint recorded |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `timezone` | query | Conditional or optional | `string` | Timezone context used by this contract; apply documented IANA/display semantics. | No further constraint recorded |
| `page` | query | Conditional or optional | `integer (int32)` | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `asOfUtc` | query | Conditional or optional | `string (date-time)` | UTC instant for as of; parse strictly and localize only for display. | No further constraint recorded |
| `postingSequenceCutoff` | query | Conditional or optional | `integer (int64)` | Numeric posting sequence cutoff for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `sort` | query | Conditional or optional | `string` | Sort text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `direction` | query | Conditional or optional | `string` | Direction text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [FinancialHistoryPageDto](../schemas/f.md#financialhistorypagedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/wallet/financial-history/export/pdf`

**What it does:** Read the permitted records/state for wallet / financial history / export / pdf. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `preset` | query | Conditional or optional | `string` | Named range/filter preset accepted by this endpoint; explicit date bounds have separate semantics. | No further constraint recorded |
| `search` | query | Conditional or optional | `string` | Search text applied within this endpoint's authorized collection; it does not widen account/tenant scope. | No further constraint recorded |
| `timezone` | query | Conditional or optional | `string` | Timezone context used by this contract; apply documented IANA/display semantics. | No further constraint recorded |
| `asOfUtc` | query | Conditional or optional | `string (date-time)` | UTC instant for as of; parse strictly and localize only for display. | No further constraint recorded |
| `postingSequenceCutoff` | query | Conditional or optional | `integer (int64)` | Numeric posting sequence cutoff for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `sort` | query | Conditional or optional | `string` | Sort text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |
| `direction` | query | Conditional or optional | `string` | Direction text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/wallet/financial-history/{entryId}`

**What it does:** Read a permitted financial-history entry and its linked transaction facts.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `entryId` | path | Yes | `string (uuid)` | Identifier of the related entry record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `source` | query | Yes | [FinancialHistoryEntrySource](../schemas/f.md#financialhistoryentrysource) | Source represented by the `FinancialHistoryEntrySource` model or enum; use that definition's fields/values. | No further constraint recorded |
| `timezone` | query | Conditional or optional | `string` | Timezone context used by this contract; apply documented IANA/display semantics. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [FinancialHistoryEntryDto](../schemas/f.md#financialhistoryentrydto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/wallet/financial-history/{entryId}/disputes`

**What it does:** Open a dispute concerning an eligible financial-history entry; opening a case does not refund money.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

**Body:** [FinancialHistoryDisputeRequestDto](../schemas/f.md#financialhistorydisputerequestdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `entryId` | path | Yes | `string (uuid)` | Identifier of the related entry record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [FinancialHistoryDisputeDto](../schemas/f.md#financialhistorydisputedto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/wallet/financial-history/{entryId}/export/pdf`

**What it does:** Read the permitted records/state for wallet / financial history / export / pdf. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `entryId` | path | Yes | `string (uuid)` | Identifier of the related entry record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `source` | query | Yes | [FinancialHistoryEntrySource](../schemas/f.md#financialhistoryentrysource) | Source represented by the `FinancialHistoryEntrySource` model or enum; use that definition's fields/values. | No further constraint recorded |
| `timezone` | query | Conditional or optional | `string` | Timezone context used by this contract; apply documented IANA/display semantics. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/wallet/payments/status`

**What it does:** Read the permitted records/state for wallet / payments / status. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [WalletPaymentStatusDto](../schemas/w.md#walletpaymentstatusdto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/wallet/payments/{paymentId}/status`

**What it does:** Read the permitted records/state for wallet / payments / status. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `paymentId` | path | Yes | `string (uuid)` | Server-owned payment record used for state/reconciliation. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [WalletPaymentStatusDto](../schemas/w.md#walletpaymentstatusdto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/wallet/payout-methods`

**What it does:** List the account's saved masked payout destinations; returned masking is not sufficient to reconstruct bank credentials.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [PayoutMethodDto](../schemas/p.md#payoutmethoddto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/wallet/payout-methods`

**What it does:** Save an eligible payout destination through the account-owned payout-method workflow.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

**Body:** [CreatePayoutMethodDto](../schemas/c.md#createpayoutmethoddto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. | minLength: `1`; maxLength: `256` |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | minLength: `1`; maxLength: `256` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [PayoutMethodDto](../schemas/p.md#payoutmethoddto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. The server can require recent authentication; local app unlock is not proof.

## DELETE `/api/v1/wallet/payout-methods/{id}`

**What it does:** Remove an eligible saved payout method; an outstanding withdrawal can prevent deletion.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | Yes | `string (uuid)` | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | pattern: `^\"[1-9][0-9]*\"$` |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. | minLength: `1`; maxLength: `256` |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | minLength: `1`; maxLength: `256` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit. The server can require recent authentication; local app unlock is not proof.

## GET `/api/v1/wallet/recipients`

**What it does:** List saved wallet-transfer recipients for the current account.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [WalletRecipientDto](../schemas/w.md#walletrecipientdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/wallet/recipients`

**What it does:** Add a transfer recipient after the server resolves and validates the intended beneficiary.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

**Body:** [AddWalletRecipientDto](../schemas/a.md#addwalletrecipientdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [WalletRecipientDto](../schemas/w.md#walletrecipientdto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## DELETE `/api/v1/wallet/recipients/{id}`

**What it does:** Remove the saved recipient relationship without deleting historical transfers.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | Yes | `string (uuid)` | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | pattern: `^\"[1-9][0-9]*\"$` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## POST `/api/v1/wallet/topup`

**What it does:** Start an owner-scoped top-up/payment intent; provider reconciliation, not checkout navigation, establishes wallet credit.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

**Body:** [TopUpWalletDto](../schemas/t.md#topupwalletdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [TopUpResultDto](../schemas/t.md#topupresultdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/wallet/topup/bank-transfers`

**What it does:** List the account's bank-transfer top-ups awaiting or carrying a review outcome.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [BankTransferTopUpDto](../schemas/b.md#banktransfertopupdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/wallet/topup/bank-transfers/{paymentId}/cancel`

**What it does:** Request cancellation of the account's eligible pending bank-transfer top-up; reconcile if the review state changed concurrently.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `paymentId` | path | Yes | `string (uuid)` | Server-owned payment record used for state/reconciliation. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | pattern: `^\"[1-9][0-9]*\"$` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/wallet/topup/limits`

**What it does:** Read current top-up limits for the resolved account, country and payment context.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `provider` | query | Conditional or optional | `string` | Configured provider selector for this operation; a named provider is not proof of readiness. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [TopUpLimitsDto](../schemas/t.md#topuplimitsdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/wallet/topup/quote`

**What it does:** Read a server top-up quote with applicable amount, currency and fee evidence before committing payment.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `amountMinor` | query | Yes | `integer (int64)` | Monetary amount in the accompanying currency's integer minor units. | No further constraint recorded |
| `provider` | query | Conditional or optional | `string` | Configured provider selector for this operation; a named provider is not proof of readiness. | No further constraint recorded |
| `payCurrency` | query | Conditional or optional | `string` | Pay currency text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [TopUpQuoteDto](../schemas/t.md#topupquotedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/wallet/topups/paypal/{operationId}/reconcile`

**What it does:** Ask the server to reconcile the existing PayPal top-up against provider evidence; reuse the original operation instead of creating a second payment.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `operationId` | path | Yes | `string (uuid)` | Durable operation reference used for applicable outcome discovery. | No further constraint recorded |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | pattern: `^\"[1-9][0-9]*\"$` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [PayPalTopUpStatusDto](../schemas/p.md#paypaltopupstatusdto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/wallet/topups/paypal/{operationId}/status`

**What it does:** Read the existing PayPal top-up operation's server state without creating a new checkout.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `operationId` | path | Yes | `string (uuid)` | Durable operation reference used for applicable outcome discovery. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [PayPalTopUpStatusDto](../schemas/p.md#paypaltopupstatusdto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/wallet/transactions`

**What it does:** Read the permitted records/state for wallet / transactions. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `preset` | query | Conditional or optional | `string` | Named range/filter preset accepted by this endpoint; explicit date bounds have separate semantics. | No further constraint recorded |
| `search` | query | Conditional or optional | `string` | Search text applied within this endpoint's authorized collection; it does not widen account/tenant scope. | No further constraint recorded |
| `continuation` | query | Conditional or optional | `string` | Endpoint-specific continuation value from the previous response; preserve its scope and ordering. | No further constraint recorded |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `timezone` | query | Conditional or optional | `string` | Timezone context used by this contract; apply documented IANA/display semantics. | No further constraint recorded |
| `page` | query | Conditional or optional | `integer (int32)` | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [WalletLedgerPageDto](../schemas/w.md#walletledgerpagedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/wallet/transactions/export`

**What it does:** Read the permitted records/state for wallet / transactions / export. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `preset` | query | Conditional or optional | `string` | Named range/filter preset accepted by this endpoint; explicit date bounds have separate semantics. | No further constraint recorded |
| `search` | query | Conditional or optional | `string` | Search text applied within this endpoint's authorized collection; it does not widen account/tenant scope. | No further constraint recorded |
| `timezone` | query | Conditional or optional | `string` | Timezone context used by this contract; apply documented IANA/display semantics. | No further constraint recorded |
| `asOfUtc` | query | Conditional or optional | `string (date-time)` | UTC instant for as of; parse strictly and localize only for display. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/wallet/transactions/history`

**What it does:** Read owner-scoped seek-paged ledger history; its row-set cutoff is separate from the live wallet balance.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `preset` | query | Conditional or optional | `string` | Named range/filter preset accepted by this endpoint; explicit date bounds have separate semantics. | No further constraint recorded |
| `search` | query | Conditional or optional | `string` | Search text applied within this endpoint's authorized collection; it does not widen account/tenant scope. | No further constraint recorded |
| `cursor` | query | Conditional or optional | `string` | Opaque scope-bound seek cursor from the previous page; do not modify it or reuse it under different filters. | No further constraint recorded |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `timezone` | query | Conditional or optional | `string` | Timezone context used by this contract; apply documented IANA/display semantics. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [WalletLedgerSeekPageDto](../schemas/w.md#walletledgerseekpagedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/wallet/transfers`

**What it does:** Execute the authorized value transfer to the documented saved recipient, with fees/FX and durable recovery where applicable.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

**Body:** [WalletTransferRequest](../schemas/w.md#wallettransferrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. | minLength: `1`; maxLength: `256` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [WalletTransferDto](../schemas/w.md#wallettransferdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. The server can require recent authentication; local app unlock is not proof.

## GET `/api/v1/wallet/transfers/quote`

**What it does:** Read a transfer quote before confirmation; retain its recipient, currencies, fees and expiry rather than recalculating them on the device.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `recipientFavoriteId` | query | Yes | `string (uuid)` | Saved recipient reference used by this transfer; not an arbitrary target user ID. | No further constraint recorded |
| `sourceUsdMinor` | query | Yes | `integer (int64)` | Source usd in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. | minLength: `1`; maxLength: `256` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [WalletTransferQuoteDto](../schemas/w.md#wallettransferquotedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** The server can require recent authentication; local app unlock is not proof.
