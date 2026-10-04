# Field dictionary: W

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

## Wallet

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `userId` | `string (uuid)` | No | Not declared nullable | Related account identity; the server still proves the caller's ownership or permitted relationship. | No further constraint recorded |
| `user` | [User](u.md#user) | No | Not declared nullable | User represented by the `User` model or enum; use that definition's fields/values. | No further constraint recorded |
| `currency` | `string` | No | Explicitly allowed | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `balanceMinor` | `integer (int64)` | No | Not declared nullable | Wallet balance in integer minor units; use the full wallet breakdown to interpret spendable funds. | No further constraint recorded |
| `heldBalanceMinor` | `integer (int64)` | No | Not declared nullable | Funds reserved by applicable holds/escrow; they are not freely spendable. | No further constraint recorded |
| `transferSendEnabled` | `boolean` | No | Not declared nullable | Whether transfer send enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `transferReceiveEnabled` | `boolean` | No | Not declared nullable | Whether transfer receive enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `topUpEnabled` | `boolean` | No | Not declared nullable | Whether top up enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `restrictionReason` | `string` | No | Explicitly allowed | Restriction reason text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `restrictedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for restricted at; parse strictly and localize only for display. | No further constraint recorded |
| `version` | `integer (int32)` | No | Not declared nullable | Version in this model's domain; not automatically an API major version. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletAmountBreakdownDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `availableMinor` | `integer (int64)` | Yes | Not declared nullable | Available in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `heldMinor` | `integer (int64)` | Yes | Not declared nullable | Held in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `pendingMinor` | `integer (int64)` | Yes | Not declared nullable | Pending in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `debtMinor` | `integer (int64)` | Yes | Not declared nullable | Debt in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `heldReleaseCondition` | `string` | Yes | Not declared nullable | Held release condition text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `pendingSettlementCondition` | `string` | Yes | Not declared nullable | Pending settlement condition text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `debtRemediation` | `string` | Yes | Not declared nullable | Debt remediation text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `safeNextAction` | `string` | Yes | Not declared nullable | Safe next action text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `lastUpdatedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for last updated at; parse strictly and localize only for display. | No further constraint recorded |
| `policyVersion` | `string` | No | Explicitly allowed | Policy revision used for this assessment; not the mobile app build number. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletBalanceContextDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `balanceMinor` | `integer (int64)` | Yes | Not declared nullable | Wallet balance in integer minor units; use the full wallet breakdown to interpret spendable funds. | No further constraint recorded |
| `heldBalanceMinor` | `integer (int64)` | Yes | Not declared nullable | Funds reserved by applicable holds/escrow; they are not freely spendable. | No further constraint recorded |
| `availableBalanceMinor` | `integer (int64)` | Yes | Not declared nullable | Available balance in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `balanceMinor` | `integer (int64)` | Yes | Not declared nullable | Wallet balance in integer minor units; use the full wallet breakdown to interpret spendable funds. | No further constraint recorded |
| `heldBalanceMinor` | `integer (int64)` | Yes | Not declared nullable | Funds reserved by applicable holds/escrow; they are not freely spendable. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `transferSendEnabled` | `boolean` | No | Not declared nullable | Whether transfer send enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `transferReceiveEnabled` | `boolean` | No | Not declared nullable | Whether transfer receive enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `topUpEnabled` | `boolean` | No | Not declared nullable | Whether top up enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `redeemedAmountMinor` | `integer (int64)` | No | Explicitly allowed | Redeemed amount in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `redeemedFeeMinor` | `integer (int64)` | No | Not declared nullable | Redeemed fee in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `amounts` | [WalletAmountBreakdownDto](w.md#walletamountbreakdowndto) | No | Not declared nullable | Amounts represented by the `WalletAmountBreakdownDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `userId` | `string (uuid)` | No | Explicitly allowed | Related account identity; the server still proves the caller's ownership or permitted relationship. | No further constraint recorded |
| `walletId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related wallet record in this model; ownership and scope are checked separately. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletFeeScheduleDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `topUpBasisPoints` | `integer (int32)` | Yes | Not declared nullable | Numeric top up basis points for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `transferSendBasisPoints` | `integer (int32)` | Yes | Not declared nullable | Numeric transfer send basis points for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `transferReceiveBasisPoints` | `integer (int32)` | Yes | Not declared nullable | Numeric transfer receive basis points for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `tripPaymentBasisPoints` | `integer (int32)` | Yes | Not declared nullable | Numeric trip payment basis points for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `withdrawalBasisPoints` | `integer (int32)` | Yes | Not declared nullable | Numeric withdrawal basis points for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `deliveryPaymentBasisPoints` | `integer (int32)` | Yes | Not declared nullable | Numeric delivery payment basis points for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `membershipPurchaseBasisPoints` | `integer (int32)` | Yes | Not declared nullable | Numeric membership purchase basis points for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `voucherRedemptionBasisPoints` | `integer (int32)` | Yes | Not declared nullable | Numeric voucher redemption basis points for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletLedgerPageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `items` | [WalletTransactionDto](w.md#wallettransactiondto)[] | Yes | Not declared nullable | Records returned in this collection/page, each using the referenced item model. | No further constraint recorded |
| `totalCount` | `integer (int64)` | Yes | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | No further constraint recorded |
| `continuation` | `string` | No | Explicitly allowed | Endpoint-specific continuation value from the previous response; preserve its scope and ordering. | No further constraint recorded |
| `hasMore` | `boolean` | Yes | Not declared nullable | Whether the seek-paged result indicates more records after this page. | No further constraint recorded |
| `totals` | [WalletLedgerTotalsDto](w.md#walletledgertotalsdto) | Yes | Not declared nullable | Totals represented by the `WalletLedgerTotalsDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `balance` | [WalletBalanceContextDto](w.md#walletbalancecontextdto) | Yes | Not declared nullable | Balance represented by the `WalletBalanceContextDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `preset` | `string` | Yes | Not declared nullable | Named range/filter preset accepted by this endpoint; explicit date bounds have separate semantics. | No further constraint recorded |
| `timezone` | `string` | Yes | Not declared nullable | Timezone context used by this contract; apply documented IANA/display semantics. | No further constraint recorded |
| `fromUtc` | `string (date-time)` | Yes | Not declared nullable | UTC start of the requested range; apply this endpoint's inclusion/validation rules. | No further constraint recorded |
| `toUtc` | `string (date-time)` | Yes | Not declared nullable | UTC end of the requested range; apply this endpoint's inclusion/validation rules. | No further constraint recorded |
| `snapshotAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for snapshot at; parse strictly and localize only for display. | No further constraint recorded |
| `page` | `integer (int32)` | Yes | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | `integer (int32)` | Yes | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `totalPages` | `integer (int64)` | Yes | Not declared nullable | Number of pages represented by this page-number model. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletLedgerSeekPageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `items` | [WalletTransactionDto](w.md#wallettransactiondto)[] | Yes | Not declared nullable | Records returned in this collection/page, each using the referenced item model. | No further constraint recorded |
| `pageSize` | `integer (int32)` | Yes | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `hasMore` | `boolean` | Yes | Not declared nullable | Whether the seek-paged result indicates more records after this page. | No further constraint recorded |
| `nextCursor` | `string` | No | Explicitly allowed | Opaque, scope-bound continuation token; preserve it unchanged and reset it when filters/context change. | No further constraint recorded |
| `preset` | `string` | Yes | Not declared nullable | Named range/filter preset accepted by this endpoint; explicit date bounds have separate semantics. | No further constraint recorded |
| `timezone` | `string` | Yes | Not declared nullable | Timezone context used by this contract; apply documented IANA/display semantics. | No further constraint recorded |
| `fromUtc` | `string (date-time)` | Yes | Not declared nullable | UTC start of the requested range; apply this endpoint's inclusion/validation rules. | No further constraint recorded |
| `toUtc` | `string (date-time)` | Yes | Not declared nullable | UTC end of the requested range; apply this endpoint's inclusion/validation rules. | No further constraint recorded |
| `snapshotAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for snapshot at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletLedgerTotalsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `creditsMinor` | `integer (int64)` | Yes | Not declared nullable | Credits in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `debitsMinor` | `integer (int64)` | Yes | Not declared nullable | Debits in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `netMinor` | `integer (int64)` | Yes | Not declared nullable | Net in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletMovementEvidenceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `activityCode` | `string` | Yes | Not declared nullable | Activity code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `availableBalanceEffectMinor` | `integer (int64)` | Yes | Not declared nullable | Available balance effect in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `heldBalanceEffectMinor` | `integer (int64)` | Yes | Not declared nullable | Held balance effect in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `policyVersion` | `string` | No | Explicitly allowed | Policy revision used for this assessment; not the mobile app build number. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletPaymentStatusDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `paymentId` | `string (uuid)` | Yes | Not declared nullable | Server-owned payment record used for state/reconciliation. | No further constraint recorded |
| `operationReference` | `string` | Yes | Not declared nullable | Operation reference text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `lifecycleStatus` | `string` | Yes | Not declared nullable | Lifecycle status text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `providerStatus` | `string` | Yes | Not declared nullable | Provider status text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `providerName` | `string` | Yes | Not declared nullable | Provider name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `checkoutUrl` | `string` | No | Explicitly allowed | URL for checkout; validate the intended origin/access and never assume private links are public. | No further constraint recorded |
| `failureCode` | `string` | No | Explicitly allowed | Failure code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `completedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for completed at; parse strictly and localize only for display. | No further constraint recorded |
| `nextReconciliationAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for next reconciliation at; parse strictly and localize only for display. | No further constraint recorded |
| `receiptAvailable` | `boolean` | Yes | Not declared nullable | Whether receipt available applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `wallet` | [WalletDto](w.md#walletdto) | Yes | Not declared nullable | Wallet represented by the `WalletDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `resourceStatus` | `string` | No | Explicitly allowed | Resource status text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `evidenceOutcome` | [FinancialOperationOutcomeDto](f.md#financialoperationoutcomedto) | No | Not declared nullable | Evidence outcome represented by the `FinancialOperationOutcomeDto` model or enum; use that definition's fields/values. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletRecipientDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `recipientUserId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related recipient user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | No further constraint recorded |
| `alias` | `string` | No | Explicitly allowed | Alias text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletTransactionDirection

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Credit | Credit state/choice in this specific enum. |
| `2` | Debit | Debit state/choice in this specific enum. |

## WalletTransactionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `type` | [WalletTransactionType](w.md#wallettransactiontype) | Yes | Not declared nullable | Type represented by the `WalletTransactionType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `direction` | [WalletTransactionDirection](w.md#wallettransactiondirection) | Yes | Not declared nullable | Direction represented by the `WalletTransactionDirection` model or enum; use that definition's fields/values. | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | No further constraint recorded |
| `balanceAfterMinor` | `integer (int64)` | Yes | Not declared nullable | Balance after in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `reference` | `string` | Yes | Not declared nullable | Reference text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | No further constraint recorded |
| `relatedEntityType` | `string` | No | Explicitly allowed | Related entity type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `relatedEntityId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related related entity record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `explanation` | [WalletTransactionExplanationDto](w.md#wallettransactionexplanationdto) | No | Not declared nullable | Explanation represented by the `WalletTransactionExplanationDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `walletMovement` | [WalletMovementEvidenceDto](w.md#walletmovementevidencedto) | No | Not declared nullable | Wallet movement represented by the `WalletMovementEvidenceDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `conversion` | [PaymentConversionEvidenceDto](p.md#paymentconversionevidencedto) | No | Not declared nullable | Conversion represented by the `PaymentConversionEvidenceDto` model or enum; use that definition's fields/values. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletTransactionExplanationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `purposeCode` | `string` | Yes | Not declared nullable | Purpose code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `settlementCode` | `string` | Yes | Not declared nullable | Settlement code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `safeNextAction` | `string` | Yes | Not declared nullable | Safe next action text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `isKnown` | `boolean` | Yes | Not declared nullable | Whether is known applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `policyVersion` | `string` | No | Explicitly allowed | Policy revision used for this assessment; not the mobile app build number. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletTransactionType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | TopUp | Top up state/choice in this specific enum. |
| `2` | RidePayment | Ride payment state/choice in this specific enum. |
| `3` | DeliveryPayment | Delivery payment state/choice in this specific enum. |
| `4` | DriverEarning | Driver earning state/choice in this specific enum. |
| `5` | Commission | Commission state/choice in this specific enum. |
| `6` | Refund | Refund state/choice in this specific enum. |
| `7` | Adjustment | Adjustment state/choice in this specific enum. |
| `8` | Cashout | Cashout state/choice in this specific enum. |
| `9` | MembershipFee | Membership fee state/choice in this specific enum. |
| `10` | Referral | Referral state/choice in this specific enum. |
| `11` | PromoCredit | Promo credit state/choice in this specific enum. |
| `12` | MembershipCredit | Membership credit state/choice in this specific enum. |
| `13` | DeliveryEscrow | Delivery escrow state/choice in this specific enum. |
| `14` | DocumentVerificationFee | Document verification fee state/choice in this specific enum. |
| `15` | BadgeFee | Badge fee state/choice in this specific enum. |
| `16` | WalletTransfer | Wallet transfer state/choice in this specific enum. |
| `17` | TopUpCard | Top up card state/choice in this specific enum. |
| `18` | TripTip | Trip tip state/choice in this specific enum. |

## WalletTransferDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `traceNumber` | `string` | Yes | Not declared nullable | Human/support trace reference for the transaction, distinct from its resource ID. | No further constraint recorded |
| `senderUserId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related sender user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `recipientUserId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related recipient user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `senderFeeMinor` | `integer (int64)` | No | Not declared nullable | Sender fee in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `recipientFeeMinor` | `integer (int64)` | No | Not declared nullable | Recipient fee in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `recipientNetAmountMinor` | `integer (int64)` | No | Explicitly allowed | Recipient net amount in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `fxQuoteId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related fx quote record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `sourceUsdMinor` | `integer (int64)` | No | Explicitly allowed | Source usd in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `exchangeRate` | `number (double)` | No | Explicitly allowed | Reference FX rate for this result; use server amount snapshots instead of floating-point monetary recalculation. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletTransferQuoteDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `quoteId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related quote record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `quoteToken` | `string` | Yes | Not declared nullable | Server-owned quote evidence; preserve currency/amount/expiry binding and treat it as private. | No further constraint recorded |
| `recipientFavoriteId` | `string (uuid)` | Yes | Not declared nullable | Saved recipient reference used by this transfer; not an arbitrary target user ID. | No further constraint recorded |
| `recipientUserId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related recipient user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `sourceUsdMinor` | `integer (int64)` | Yes | Not declared nullable | Source usd in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `sourceCurrency` | `string` | Yes | Not declared nullable | Source currency text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `senderFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Sender fee in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `recipientFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Recipient fee in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `totalDebitMinor` | `integer (int64)` | Yes | Not declared nullable | Total debit in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `recipientNetAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Recipient net amount in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `exchangeRate` | `number (double)` | Yes | Not declared nullable | Reference FX rate for this result; use server amount snapshots instead of floating-point monetary recalculation. | No further constraint recorded |
| `rateVersionId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related rate version record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `rateVersion` | `integer (int64)` | Yes | Not declared nullable | Rate version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `rateRevision` | `integer (int64)` | Yes | Not declared nullable | Rate revision for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WalletTransferRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `recipientFavoriteId` | `string (uuid)` | Yes | Not declared nullable | Saved recipient reference used by this transfer; not an arbitrary target user ID. | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | No further constraint recorded |
| `fxQuoteToken` | `string` | No | Explicitly allowed | Private FX quote evidence for the current transfer, distinct from a display rate. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## WeekdayFlags

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `4`, `8`, `16`, `32`, `64`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | None | None state/choice in this specific enum. |
| `1` | Sunday | Sunday state/choice in this specific enum. |
| `2` | Monday | Monday state/choice in this specific enum. |
| `4` | Tuesday | Tuesday state/choice in this specific enum. |
| `8` | Wednesday | Wednesday state/choice in this specific enum. |
| `16` | Thursday | Thursday state/choice in this specific enum. |
| `32` | Friday | Friday state/choice in this specific enum. |
| `64` | Saturday | Saturday state/choice in this specific enum. |
