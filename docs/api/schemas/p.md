# Field dictionary: P

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

The explanation basis distinguishes model-specific meaning, shared conventions,
name-derived units and type-only entries awaiting semantic review. See the
[coverage report](../reference/coverage.md); field presence is not semantic completeness.

## Models on this page

- [ParcelDto](#parceldto)
- [ParcelInputDto](#parcelinputdto)
- [ParcelProtectionClaimDto](#parcelprotectionclaimdto)
- [ParcelProtectionClaimReason](#parcelprotectionclaimreason)
- [ParcelProtectionClaimStatus](#parcelprotectionclaimstatus)
- [ParcelProtectionStatus](#parcelprotectionstatus)
- [ParcelSize](#parcelsize)
- [PasskeyCeremonyDto](#passkeyceremonydto)
- [PasskeyDto](#passkeydto)
- [PasskeyLoginBeginRequest](#passkeyloginbeginrequest)
- [PasskeyLoginCompleteRequest](#passkeylogincompleterequest)
- [PasskeyRegisterCompleteRequest](#passkeyregistercompleterequest)
- [PasswordStrengthDto](#passwordstrengthdto)
- [PasswordStrengthRequest](#passwordstrengthrequest)
- [PayPalTopUpStatusDto](#paypaltopupstatusdto)
- [PaymentConversionEvidenceDto](#paymentconversionevidencedto)
- [PaymentEntityType](#paymententitytype)
- [PaymentMethod](#paymentmethod)
- [PaymentStatus](#paymentstatus)
- [PayoutMethodDto](#payoutmethoddto)
- [PayoutMethodType](#payoutmethodtype)
- [PayoutTransferStatus](#payouttransferstatus)
- [PendingMembershipChangeDto](#pendingmembershipchangedto)
- [PendingSocialLinkDto](#pendingsociallinkdto)
- [PendingSocialLinkTokenRequest](#pendingsociallinktokenrequest)
- [PlaceBidDto](#placebiddto)
- [PreferredDriverDto](#preferreddriverdto)
- [PreferredDriverStatus](#preferreddriverstatus)
- [PrepareStorePurchaseDto](#preparestorepurchasedto)
- [ProblemDetails](#problemdetails)
- [ProviderBillingDto](#providerbillingdto)
- [PublicCountrySiteDto](#publiccountrysitedto)
- [PublicMembershipPlanPriceDto](#publicmembershipplanpricedto)
- [PublicMembershipPriceTermDto](#publicmembershippricetermdto)
- [PublicMembershipPricesDto](#publicmembershippricesdto)
- [PublicVehicleCategoryDto](#publicvehiclecategorydto)
- [PushChannelCapabilitiesDto](#pushchannelcapabilitiesdto)
- [PushPlatform](#pushplatform)

## ParcelDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `description` | `string` | Yes | Not declared nullable | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `sizeCategory` | [ParcelSize](p.md#parcelsize) | Yes | Not declared nullable | Size category represented by the `ParcelSize` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `weightKg` | `number (double)` | No | Explicitly allowed | Numeric weight kg for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `quantity` | `integer (int32)` | Yes | Not declared nullable | Numeric quantity for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `deliveryStopId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related delivery stop record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `declaredContents` | `string` | Yes | Not declared nullable | Declared contents text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `declaredValueMinor` | `integer (int64)` | Yes | Not declared nullable | Declared value in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `declaredValueCurrency` | `string` | Yes | Not declared nullable | Declared value currency text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isFragile` | `boolean` | Yes | Not declared nullable | Whether is fragile applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `photoCount` | `integer (int32)` | Yes | Not declared nullable | Number of photo in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ParcelInputDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `description` | `string` | Yes | Not declared nullable | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `sizeCategory` | [ParcelSize](p.md#parcelsize) | Yes | Not declared nullable | Size category represented by the `ParcelSize` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `weightKg` | `number (double)` | No | Explicitly allowed | Numeric weight kg for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `quantity` | `integer (int32)` | Yes | Not declared nullable | Numeric quantity for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `dropoffStopIndex` | `integer (int32)` | No | Explicitly allowed | Numeric dropoff stop index for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `declaredContents` | `string` | No | Explicitly allowed | Declared contents text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `declaredValueMinor` | `integer (int64)` | No | Not declared nullable | Declared value in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `isFragile` | `boolean` | No | Not declared nullable | Whether is fragile applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `containsRestrictedItems` | `boolean` | No | Not declared nullable | Whether contains restricted items applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `photoFileRefs` | `string[]` | No | Explicitly allowed | Collection of photo file refs for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ParcelProtectionClaimDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `deliveryRequestId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related delivery request record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `status` | [ParcelProtectionClaimStatus](p.md#parcelprotectionclaimstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `reason` | [ParcelProtectionClaimReason](p.md#parcelprotectionclaimreason) | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |
| `description` | `string` | Yes | Not declared nullable | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `claimedAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Claimed amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `approvedAmountMinor` | `integer (int64)` | No | Explicitly allowed | Approved amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `reviewNote` | `string` | No | Explicitly allowed | Human-readable reviewer explanation, including remediation where applicable. | Shared convention | No further constraint recorded |
| `settlementReference` | `string` | No | Explicitly allowed | Settlement reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `reviewedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for reviewed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `settledAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for settled at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `evidence` | [DeliveryEvidenceDto](d.md#deliveryevidencedto)[] | Yes | Not declared nullable | Collection of evidence for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ParcelProtectionClaimReason

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `99`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Lost | Lost state/choice in this specific enum. |
| `2` | Damaged | Damaged state/choice in this specific enum. |
| `3` | PartialLoss | Partial loss state/choice in this specific enum. |
| `4` | Theft | Theft state/choice in this specific enum. |
| `99` | Other | Other state/choice in this specific enum. |

## ParcelProtectionClaimStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Submitted | Submitted state/choice in this specific enum. |
| `2` | UnderReview | Under review state/choice in this specific enum. |
| `3` | Approved | Approved state/choice in this specific enum. |
| `4` | Rejected | Rejected state/choice in this specific enum. |
| `5` | Settled | Settled state/choice in this specific enum. |
| `6` | Withdrawn | Withdrawn state/choice in this specific enum. |

## ParcelProtectionStatus

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`, `4`, `5`, `6`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | NotRequested | Not requested state/choice in this specific enum. |
| `1` | Quoted | Quoted state/choice in this specific enum. |
| `2` | Active | Active state/choice in this specific enum. |
| `3` | Voided | Voided state/choice in this specific enum. |
| `4` | ClaimOpened | Claim opened state/choice in this specific enum. |
| `5` | ClaimSettled | Claim settled state/choice in this specific enum. |
| `6` | ClaimRejected | Claim rejected state/choice in this specific enum. |

## ParcelSize

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Small | Small state/choice in this specific enum. |
| `2` | Medium | Medium state/choice in this specific enum. |
| `3` | Large | Large state/choice in this specific enum. |
| `4` | ExtraLarge | Extra large state/choice in this specific enum. |

## PasskeyCeremonyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `options` | `string` | Yes | Not declared nullable | Options text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `state` | `string` | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PasskeyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `lastUsedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last used at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PasskeyLoginBeginRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket` | `string` | Yes | Not declared nullable | Ticket text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PasskeyLoginCompleteRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket` | `string` | Yes | Not declared nullable | Ticket text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `state` | `string` | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `response` | `string` | Yes | Not declared nullable | Response text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PasskeyRegisterCompleteRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `state` | `string` | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `response` | `string` | Yes | Not declared nullable | Response text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `name` | `string` | No | Explicitly allowed | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PasswordStrengthDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `score` | `integer (int32)` | Yes | Not declared nullable | Numeric score for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `label` | `string` | Yes | Not declared nullable | Label text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `suggestions` | `string[]` | Yes | Not declared nullable | Collection of suggestions for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `compromised` | `boolean` | Yes | Not declared nullable | Whether compromised applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PasswordStrengthRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `password` | `string` | No | Explicitly allowed | Secret password input for the established secure identity ceremony; never echo or log it. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PayPalTopUpStatusDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `operationId` | `string (uuid)` | Yes | Not declared nullable | Durable operation reference used for applicable outcome discovery. | Shared convention | No further constraint recorded |
| `paymentId` | `string (uuid)` | Yes | Not declared nullable | Server-owned payment record used for state/reconciliation. | Shared convention | No further constraint recorded |
| `lifecycleStatus` | `string` | Yes | Not declared nullable | Lifecycle status text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `providerAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Provider amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `providerCurrency` | `string` | Yes | Not declared nullable | Provider currency text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `walletCreditMinor` | `integer (int64)` | Yes | Not declared nullable | Wallet credit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `walletCurrency` | `string` | Yes | Not declared nullable | Wallet currency text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `providerEnvironment` | `string` | Yes | Not declared nullable | Provider environment text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `nextCheckAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for next check at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `nextAction` | `string` | Yes | Not declared nullable | Suggested next workflow step returned by the server; it does not override authorization. | Shared convention | No further constraint recorded |
| `supportReference` | `string` | Yes | Not declared nullable | Support reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PaymentConversionEvidenceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `sourcePrincipalMinor` | `integer (int64)` | Yes | Not declared nullable | Source principal in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `sourceFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Source fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `sourceTotalMinor` | `integer (int64)` | Yes | Not declared nullable | Source total in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `sourceCurrency` | `string` | Yes | Not declared nullable | Source currency text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `walletCreditMinor` | `integer (int64)` | Yes | Not declared nullable | Wallet credit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `walletCurrency` | `string` | Yes | Not declared nullable | Wallet currency text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `exchangeRate` | `number (double)` | No | Explicitly allowed | Reference FX rate for this result; use server amount snapshots instead of floating-point monetary recalculation. | Shared convention | No further constraint recorded |
| `exchangeRateDirection` | `string` | No | Explicitly allowed | Exchange rate direction text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `exchangeRateSource` | `string` | No | Explicitly allowed | Exchange rate source text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `exchangeRateEvidenceReference` | `string` | No | Explicitly allowed | Exchange rate evidence reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `exchangeRateAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for exchange rate at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `quotePolicyVersion` | `string` | No | Explicitly allowed | Quote policy version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `paymentLifecycleStatus` | `string` | Yes | Not declared nullable | Payment lifecycle status text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `supportReference` | `string` | No | Explicitly allowed | Support reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PaymentEntityType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Trip | Trip state/choice in this specific enum. |
| `2` | Delivery | Delivery state/choice in this specific enum. |
| `3` | WalletTopUp | Wallet top up state/choice in this specific enum. |
| `4` | MembershipFee | Membership fee state/choice in this specific enum. |
| `5` | DocumentVerificationFee | Document verification fee state/choice in this specific enum. |
| `6` | BadgeFee | Badge fee state/choice in this specific enum. |
| `7` | WalletTopUpCard | Wallet top up card state/choice in this specific enum. |
| `8` | Rental | Rental state/choice in this specific enum. |

## PaymentMethod

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Cash | Cash state/choice in this specific enum. |
| `2` | Wallet | Wallet state/choice in this specific enum. |
| `3` | Card | Card state/choice in this specific enum. |
| `4` | External | External state/choice in this specific enum. |

## PaymentStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Completed | Completed state/choice in this specific enum. |
| `3` | Failed | Failed state/choice in this specific enum. |
| `4` | Refunded | Refunded state/choice in this specific enum. |
| `5` | PartiallyRefunded | Partially refunded state/choice in this specific enum. |
| `6` | Authorized | Authorized state/choice in this specific enum. |
| `7` | Voided | Voided state/choice in this specific enum. |

## PayoutMethodDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `type` | [PayoutMethodType](p.md#payoutmethodtype) | Yes | Not declared nullable | Type represented by the `PayoutMethodType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `detailsMasked` | `string` | Yes | Not declared nullable | Details masked text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `estimatedDaysMin` | `integer (int32)` | Yes | Not declared nullable | Numeric estimated days min for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `estimatedDaysMax` | `integer (int32)` | Yes | Not declared nullable | Numeric estimated days max for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `isVerified` | `boolean` | Yes | Not declared nullable | Whether is verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `verifiedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for verified at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `automationEligible` | `boolean` | No | Not declared nullable | Whether automation eligible applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `payoutProvider` | `string` | No | Explicitly allowed | Payout provider text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PayoutMethodType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Bank | Bank state/choice in this specific enum. |
| `2` | PayPal | Pay pal state/choice in this specific enum. |

## PayoutTransferStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Queued | Queued state/choice in this specific enum. |
| `2` | Submitting | Submitting state/choice in this specific enum. |
| `3` | Submitted | Submitted state/choice in this specific enum. |
| `4` | Processing | Processing state/choice in this specific enum. |
| `5` | Completed | Completed state/choice in this specific enum. |
| `6` | Failed | Failed state/choice in this specific enum. |
| `7` | NeedsAttention | Needs attention state/choice in this specific enum. |
| `8` | Returned | Returned state/choice in this specific enum. |
| `9` | Reversed | Reversed state/choice in this specific enum. |

## PendingMembershipChangeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `changeType` | `string` | Yes | Not declared nullable | Change type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `targetPlanId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related target plan record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `targetPlanName` | `string` | Yes | Not declared nullable | Target plan name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `effectiveAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for effective at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `source` | `string` | Yes | Not declared nullable | Source text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `provider` | `string` | No | Explicitly allowed | Configured provider selector for this operation; a named provider is not proof of readiness. | Shared convention | No further constraint recorded |
| `termDays` | `integer (int32)` | Yes | Not declared nullable | Requested/applicable membership term in days; only configured valid terms are allowed. | Shared convention | No further constraint recorded |
| `quotedPriceMinor` | `integer (int64)` | No | Explicitly allowed | Quoted price in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | No | Explicitly allowed | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `priceSource` | `string` | No | Explicitly allowed | Price source text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `lifecycleReasonCode` | `string` | Yes | Not declared nullable | Reason for the current membership lifecycle state; render through its contract vocabulary. | Shared convention | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |
| `canCancel` | `boolean` | Yes | Not declared nullable | Whether can cancel applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PendingSocialLinkDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `intentToken` | `string` | Yes | Not declared nullable | Private intent token used by this specific ceremony; never log, publish or substitute it for another proof. | Naming convention | No further constraint recorded |
| `provider` | `string` | Yes | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | Shared convention | No further constraint recorded |
| `providerIdentity` | `string` | Yes | Not declared nullable | Provider identity text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `existingAccount` | `string` | Yes | Not declared nullable | Existing account text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `correlationId` | `string` | Yes | Not declared nullable | Safe request correlation reference; not an access token or proof of success. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PendingSocialLinkTokenRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `intentToken` | `string` | Yes | Not declared nullable | Private intent token used by this specific ceremony; never log, publish or substitute it for another proof. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PlaceBidDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `type` | [BidType](b.md#bidtype) | Yes | Not declared nullable | Type represented by the `BidType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `amountMinor` | `integer (int64)` | No | Explicitly allowed | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `message` | `string` | No | Explicitly allowed | Message text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `vehicleId` | `string (uuid)` | No | Explicitly allowed | Account vehicle record associated with this operation or result. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PreferredDriverDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `status` | [PreferredDriverStatus](p.md#preferreddriverstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `eligible` | `boolean` | Yes | Not declared nullable | Whether eligible applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `goldPlan` | `boolean` | Yes | Not declared nullable | Whether gold plan applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `ratingCount` | `integer (int32)` | Yes | Not declared nullable | Number of rating in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `requiredRatings` | `integer (int32)` | Yes | Not declared nullable | Numeric required ratings for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `tripCount` | `integer (int32)` | Yes | Not declared nullable | Number of trip in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `requiredTrips` | `integer (int32)` | Yes | Not declared nullable | Numeric required trips for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `fullyVerified` | `boolean` | Yes | Not declared nullable | Whether fully verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `shirtEntitlement` | `integer (int32)` | Yes | Not declared nullable | Numeric shirt entitlement for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `shirtsIssued` | `integer (int32)` | Yes | Not declared nullable | Numeric shirts issued for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `reviewNote` | `string` | No | Explicitly allowed | Human-readable reviewer explanation, including remediation where applicable. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PreferredDriverStatus

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | None | None state/choice in this specific enum. |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Approved | Approved state/choice in this specific enum. |
| `3` | Rejected | Rejected state/choice in this specific enum. |
| `4` | Suspended | Suspended state/choice in this specific enum. |

## PrepareStorePurchaseDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `operationId` | `string (uuid)` | Yes | Not declared nullable | Durable operation reference used for applicable outcome discovery. | Shared convention | No further constraint recorded |
| `platform` | `string` | Yes | Not declared nullable | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | Shared convention | No further constraint recorded |
| `productId` | `string` | Yes | Not declared nullable | Identifier of the related product record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `quoteToken` | `string` | Yes | Not declared nullable | Server-owned quote evidence; preserve currency/amount/expiry binding and treat it as private. | Shared convention | No further constraint recorded |
| `rentalOrganizationId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related rental organization record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ProblemDetails

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `type` | `string` | No | Explicitly allowed | Problem-type URI identifying the class of failure; not a resource ID. | Model-specific | No further constraint recorded |
| `title` | `string` | No | Explicitly allowed | Short human-readable summary of the problem class. | Model-specific | No further constraint recorded |
| `status` | `integer (int32)` | No | Explicitly allowed | HTTP status for this problem response, not a trip/payment lifecycle enum. | Model-specific | No further constraint recorded |
| `detail` | `string` | No | Explicitly allowed | Sanitized explanation of this failure occurrence; display safely and do not interpret it as executable recovery instructions. | Model-specific | No further constraint recorded |
| `instance` | `string` | No | Explicitly allowed | Reference to this problem occurrence when supplied; do not assume it is a public URL. | Model-specific | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Machine-readable KiloDrive error category used for client error handling. | Model-specific | No further constraint recorded |
| `supportCode` | `string` | Yes | Not declared nullable | Sanitized support reference for a failure/warning; suitable for protected troubleshooting context. | Shared convention | pattern: `^KD-[0-9]{5}$` |
| `outcome` | `string` | Yes | Not declared nullable | Result/recovery state of this operation; unknown or pending is not failed or successful. | Shared convention | Allowed wire values: `not_completed`, `in_progress`, `unknown` |
| `safeAction` | `string` | Yes | Not declared nullable | Server guidance for safe recovery; preserve operation evidence before retrying. | Shared convention | No further constraint recorded |

**Additional property value type:** `schema`.

## ProviderBillingDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `accountType` | `string` | Yes | Not declared nullable | Account type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `accountId` | `string (uuid)` | Yes | Not declared nullable | Billing subject identifier interpreted with accountType; it is not universally the global user ID. | Model-specific | No further constraint recorded |
| `billingMode` | `string` | Yes | Not declared nullable | Configured billing arrangement for this subject; it does not establish entitlement by itself. | Model-specific | No further constraint recorded |
| `planId` | `string (uuid)` | No | Explicitly allowed | Membership catalog record; it does not itself prove a user entitlement. | Shared convention | No further constraint recorded |
| `planName` | `string` | No | Explicitly allowed | Human plan name; use plan/entitlement records for identity and authority. | Shared convention | No further constraint recorded |
| `planExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for plan expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `autoRenew` | `boolean` | Yes | Not declared nullable | Membership renewal preference/state for this model; it does not itself prove the next charge will succeed. | Shared convention | No further constraint recorded |
| `availableTermDays` | `integer (int32)[]` | Yes | Not declared nullable | Durations offered in this billing context; do not assume every catalog term is purchasable. | Model-specific | No further constraint recorded |
| `paymentMethods` | [BillingPaymentMethodDto](b.md#billingpaymentmethoddto)[] | Yes | Not declared nullable | Collection of payment methods for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `billingHistory` | [BillingHistoryItemDto](b.md#billinghistoryitemdto)[] | Yes | Not declared nullable | Collection of billing history for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `storePlatform` | `string` | No | Explicitly allowed | Store platform text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `storeProductId` | `string` | No | Explicitly allowed | Identifier of the related store product record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `storeStatus` | `string` | No | Explicitly allowed | Store status text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `storeWillAutoRenew` | `boolean` | No | Explicitly allowed | Provider-reported renewal intent when known; null must not be displayed as a confirmed cancellation. | Model-specific | No further constraint recorded |
| `storeGracePeriodExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for store grace period expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `storeAcknowledgementStatus` | `string` | No | Explicitly allowed | Store acknowledgement status text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |
| `storeReconciliationStatus` | `string` | No | Explicitly allowed | Store reconciliation status text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `storeLastReconciledAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for store last reconciled at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `storeNextReconciliationAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for store next reconciliation at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `lifecycle` | [MembershipLifecycleDto](m.md#membershiplifecycledto) | No | Not declared nullable | Lifecycle represented by the `MembershipLifecycleDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `storeRenewalState` | `string` | No | Explicitly allowed | Store renewal state text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PublicCountrySiteDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `currencyCode` | `string` | Yes | Not declared nullable | ISO currency code; do not infer it from a dollar symbol. | Shared convention | No further constraint recorded |
| `currencySymbol` | `string` | Yes | Not declared nullable | Currency symbol text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `timezone` | `string` | Yes | Not declared nullable | Timezone context used by this contract; apply documented IANA/display semantics. | Shared convention | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | Shared convention | No further constraint recorded |
| `launchReady` | `boolean` | Yes | Not declared nullable | Whether launch ready applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `launchState` | `string` | Yes | Not declared nullable | Launch state text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `unavailableReason` | `string` | No | Explicitly allowed | Unavailable reason text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PublicMembershipPlanPriceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `audience` | `string` | Yes | Not declared nullable | Applicable product/client audience, distinct from verified security authority. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `baseCurrency` | `string` | Yes | Not declared nullable | Currency of the catalog/quote's base amount, distinct from the displayed local currency. | Shared convention | No further constraint recorded |
| `planRevision` | `integer (int64)` | Yes | Not declared nullable | Plan revision for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `terms` | [PublicMembershipPriceTermDto](p.md#publicmembershippricetermdto)[] | Yes | Not declared nullable | Collection of terms for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PublicMembershipPriceTermDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `termDays` | `integer (int32)` | Yes | Not declared nullable | Requested/applicable membership term in days; only configured valid terms are allowed. | Shared convention | No further constraint recorded |
| `baseAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Base amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `fxRateFromUsd` | `number (double)` | Yes | Not declared nullable | Numeric fx rate from usd for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `fxFreshUntilUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for fx fresh until; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PublicMembershipPricesDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `quotedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for quoted at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `plans` | [PublicMembershipPlanPriceDto](p.md#publicmembershipplanpricedto)[] | Yes | Not declared nullable | Collection of plans for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PublicVehicleCategoryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `description` | `string` | No | Explicitly allowed | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `iconUrl` | `string` | No | Explicitly allowed | URL for icon; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `maxPassengers` | `integer (int32)` | Yes | Not declared nullable | Numeric max passengers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `fareMultiplier` | `number (double)` | Yes | Not declared nullable | Numeric fare multiplier for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PushChannelCapabilitiesDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `version` | `integer (int32)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `quietChannel` | `boolean` | Yes | Not declared nullable | Whether quiet channel applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `noVibrationChannels` | `boolean` | Yes | Not declared nullable | Whether no vibration channels applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## PushPlatform

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Ios | Ios state/choice in this specific enum. |
| `2` | Android | Android state/choice in this specific enum. |
| `3` | Web | Web state/choice in this specific enum. |
