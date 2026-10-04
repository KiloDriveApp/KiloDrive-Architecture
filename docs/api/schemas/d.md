# Field dictionary: D

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

## DeleteAccountDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `forfeitRemainingBalance` | `boolean` | Yes | Not declared nullable | Whether forfeit remaining balance applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeliveryAcceptancePreviewDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `deliveryRequestId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related delivery request record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `bidId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related bid record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `deliveryRequestRevision` | `integer (int64)` | Yes | Not declared nullable | Delivery request revision for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `bidRevision` | `integer (int64)` | Yes | Not declared nullable | Bid revision for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `quoteRevision` | `integer (int64)` | Yes | Not declared nullable | Quote revision for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `authorizationFingerprint` | `string` | Yes | Not declared nullable | Authorization fingerprint text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `paymentMethod` | [PaymentMethod](p.md#paymentmethod) | Yes | Not declared nullable | Payment method enum; availability and settlement rules are checked separately. | No further constraint recorded |
| `bidAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Bid amount in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `promoDiscountMinor` | `integer (int64)` | Yes | Not declared nullable | Promo discount in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `protectionFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Protection fee in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `transactionFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Transaction fee in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `totalAuthorizationMinor` | `integer (int64)` | Yes | Not declared nullable | Total authorization in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `availableBalanceMinor` | `integer (int64)` | Yes | Not declared nullable | Available balance in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `heldBalanceMinor` | `integer (int64)` | Yes | Not declared nullable | Funds reserved by applicable holds/escrow; they are not freely spendable. | No further constraint recorded |
| `projectedAvailableBalanceMinor` | `integer (int64)` | Yes | Not declared nullable | Projected available balance in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `cashAllowed` | `boolean` | Yes | Not declared nullable | Whether cash allowed applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `paymentEligible` | `boolean` | Yes | Not declared nullable | Whether payment eligible applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `ineligibilityCode` | `string` | No | Explicitly allowed | Ineligibility code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `isCurrent` | `boolean` | Yes | Not declared nullable | Whether is current applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `nextAction` | `string` | Yes | Not declared nullable | Suggested next workflow step returned by the server; it does not override authorization. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeliveryBidDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `driverProfileId` | `string (uuid)` | Yes | Not declared nullable | Driver-profile record associated with this operation or result. | No further constraint recorded |
| `driverName` | `string` | Yes | Not declared nullable | Driver name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `driverRating` | `number (double)` | Yes | Not declared nullable | Numeric driver rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `driverTotalTrips` | `integer (int32)` | Yes | Not declared nullable | Numeric driver total trips for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `type` | [BidType](b.md#bidtype) | Yes | Not declared nullable | Type represented by the `BidType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | No further constraint recorded |
| `message` | `string` | No | Explicitly allowed | Message text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `status` | [BidStatus](b.md#bidstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeliveryBulkOrderStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Processing | Processing state/choice in this specific enum. |
| `2` | Completed | Completed state/choice in this specific enum. |
| `3` | PartiallyCompleted | Partially completed state/choice in this specific enum. |
| `4` | Failed | Failed state/choice in this specific enum. |

## DeliveryCustodyEventDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `eventType` | `string` | Yes | Not declared nullable | Event type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `summary` | `string` | Yes | Not declared nullable | Summary text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `actorType` | `string` | Yes | Not declared nullable | Actor type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `stopId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related stop record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `reasonCode` | `string` | No | Explicitly allowed | Stable reason code; map through the applicable reason catalog instead of displaying an unrelated enum. | No further constraint recorded |
| `occurredAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for occurred at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeliveryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `deliveryRequestId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related delivery request record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `status` | [DeliveryStatus](d.md#deliverystatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `driverProfileId` | `string (uuid)` | Yes | Not declared nullable | Driver-profile record associated with this operation or result. | No further constraint recorded |
| `driverName` | `string` | Yes | Not declared nullable | Driver name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `senderId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related sender record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `priceMinor` | `integer (int64)` | Yes | Not declared nullable | Price in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `commissionRate` | `number (double)` | Yes | Not declared nullable | Numeric commission rate for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `commissionMinor` | `integer (int64)` | Yes | Not declared nullable | Commission in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `driverEarningMinor` | `integer (int64)` | Yes | Not declared nullable | Driver earning in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `paymentMethod` | [PaymentMethod](p.md#paymentmethod) | No | Not declared nullable | Payment method enum; availability and settlement rules are checked separately. | No further constraint recorded |
| `paymentStatus` | [PaymentStatus](p.md#paymentstatus) | Yes | Not declared nullable | Payment status represented by the `PaymentStatus` model or enum; use that definition's fields/values. | No further constraint recorded |
| `startedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for started at; parse strictly and localize only for display. | No further constraint recorded |
| `completedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for completed at; parse strictly and localize only for display. | No further constraint recorded |
| `stops` | [DeliveryStopDto](d.md#deliverystopdto)[] | Yes | Not declared nullable | Ordered journey/delivery stops in the referenced stop model. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `pickupConfirmedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for pickup confirmed at; parse strictly and localize only for display. | No further constraint recorded |
| `pickupVerificationMethod` | [DeliveryVerificationMethod](d.md#deliveryverificationmethod) | No | Not declared nullable | Pickup verification method represented by the `DeliveryVerificationMethod` model or enum; use that definition's fields/values. | No further constraint recorded |
| `recipientConfirmedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for recipient confirmed at; parse strictly and localize only for display. | No further constraint recorded |
| `recipientVerificationMethod` | [DeliveryVerificationMethod](d.md#deliveryverificationmethod) | No | Not declared nullable | Recipient verification method represented by the `DeliveryVerificationMethod` model or enum; use that definition's fields/values. | No further constraint recorded |
| `recipientName` | `string` | No | Explicitly allowed | Recipient name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `failedDeliveryAttempts` | `integer (int32)` | Yes | Not declared nullable | Numeric failed delivery attempts for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `returnInitiatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for return initiated at; parse strictly and localize only for display. | No further constraint recorded |
| `returnedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for returned at; parse strictly and localize only for display. | No further constraint recorded |
| `verificationChallengeId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related verification challenge record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `verificationPurpose` | `string` | No | Explicitly allowed | Verification purpose text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `verificationExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for verification expires at; parse strictly and localize only for display. | No further constraint recorded |
| `promoDiscountMinor` | `integer (int64)` | No | Not declared nullable | Promo discount in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `returnPolicy` | [DeliveryReturnPolicy](d.md#deliveryreturnpolicy) | No | Not declared nullable | Return policy represented by the `DeliveryReturnPolicy` model or enum; use that definition's fields/values. | No further constraint recorded |
| `maximumFailedAttempts` | `integer (int32)` | No | Not declared nullable | Numeric maximum failed attempts for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `transactionFeeMinor` | `integer (int64)` | No | Not declared nullable | Transaction fee in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `trackingNumber` | `string` | No | Explicitly allowed | Tracking number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `authorizationAmountMinor` | `integer (int64)` | No | Not declared nullable | Authorization amount in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeliveryDtoPagedResult

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `items` | [DeliveryDto](d.md#deliverydto)[] | No | Explicitly allowed | Records returned in this collection/page, each using the referenced item model. | No further constraint recorded |
| `page` | `integer (int32)` | No | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | `integer (int32)` | No | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `totalCount` | `integer (int64)` | No | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | No further constraint recorded |
| `totalPages` | `integer (int32)` | No | Not declared nullable | Number of pages represented by this page-number model. | readOnly: `True` |
| `hasPreviousPage` | `boolean` | No | Not declared nullable | Whether has previous page applies in this model's context. This flag does not replace server permission or lifecycle checks. | readOnly: `True` |
| `hasNextPage` | `boolean` | No | Not declared nullable | Whether has next page applies in this model's context. This flag does not replace server permission or lifecycle checks. | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## DeliveryEvidenceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `type` | [DeliveryEvidenceType](d.md#deliveryevidencetype) | Yes | Not declared nullable | Type represented by the `DeliveryEvidenceType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `stopId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related stop record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `fileUrl` | `string` | Yes | Not declared nullable | URL for file; validate the intended origin/access and never assume private links are public. | No further constraint recorded |
| `caption` | `string` | No | Explicitly allowed | Caption text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeliveryEvidenceInputDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `fileRef` | `string` | Yes | Not declared nullable | Private storage reference; not a permanent public URL or approval decision. | No further constraint recorded |
| `type` | [DeliveryEvidenceType](d.md#deliveryevidencetype) | Yes | Not declared nullable | Type represented by the `DeliveryEvidenceType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `stopId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related stop record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `caption` | `string` | No | Explicitly allowed | Caption text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeliveryEvidenceType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | PackageAtBooking | Package at booking state/choice in this specific enum. |
| `2` | PackageAtPickup | Package at pickup state/choice in this specific enum. |
| `3` | FailedAttempt | Failed attempt state/choice in this specific enum. |
| `4` | ProofOfDelivery | Proof of delivery state/choice in this specific enum. |
| `5` | Signature | Signature state/choice in this specific enum. |
| `6` | ReturnToSender | Return to sender state/choice in this specific enum. |
| `7` | ProtectionClaim | Protection claim state/choice in this specific enum. |

## DeliveryFailureReason

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `99`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | RecipientUnavailable | Recipient unavailable state/choice in this specific enum. |
| `2` | IncorrectAddress | Incorrect address state/choice in this specific enum. |
| `3` | RecipientRefused | Recipient refused state/choice in this specific enum. |
| `4` | UnsafeLocation | Unsafe location state/choice in this specific enum. |
| `5` | DamagedPackage | Damaged package state/choice in this specific enum. |
| `6` | VerificationFailed | Verification failed state/choice in this specific enum. |
| `99` | Other | Other state/choice in this specific enum. |

## DeliveryQuoteDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `quoteId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related quote record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `quoteRevision` | `integer (int64)` | Yes | Not declared nullable | Quote revision for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `inputFingerprint` | `string` | Yes | Not declared nullable | Input fingerprint text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `isServiceable` | `boolean` | Yes | Not declared nullable | Whether is serviceable applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `unavailableReason` | `string` | No | Explicitly allowed | Unavailable reason text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `routeDistanceMeters` | `integer (int32)` | Yes | Not declared nullable | Route distance, measured in metres. | No further constraint recorded |
| `routeDurationSeconds` | `integer (int32)` | Yes | Not declared nullable | Route duration, measured in seconds. | No further constraint recorded |
| `routeSource` | `string` | Yes | Not declared nullable | Route source text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `confidence` | `string` | Yes | Not declared nullable | Confidence text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `suggestedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Suggested fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `protectionFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Protection fee in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `transactionFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Transaction fee in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `totalAuthorizationMinor` | `integer (int64)` | Yes | Not declared nullable | Total authorization in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `nextAction` | `string` | Yes | Not declared nullable | Suggested next workflow step returned by the server; it does not override authorization. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeliveryRequestDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `status` | [DeliveryRequestStatus](d.md#deliveryrequeststatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `vehicleCategoryId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related vehicle category record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `vehicleCategoryName` | `string` | Yes | Not declared nullable | Vehicle category name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `suggestedPriceMinor` | `integer (int64)` | Yes | Not declared nullable | Suggested price in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `proposedPriceMinor` | `integer (int64)` | Yes | Not declared nullable | Proposed price in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `finalPriceMinor` | `integer (int64)` | No | Explicitly allowed | Final price in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `totalDistanceMeters` | `integer (int32)` | Yes | Not declared nullable | Total distance, measured in metres. | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `bidCount` | `integer (int32)` | Yes | Not declared nullable | Number of bid in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `stops` | [DeliveryStopDto](d.md#deliverystopdto)[] | Yes | Not declared nullable | Ordered journey/delivery stops in the referenced stop model. | No further constraint recorded |
| `parcels` | [ParcelDto](p.md#parceldto)[] | Yes | Not declared nullable | Collection of parcels for this model; interpret each item through the declared item type. | No further constraint recorded |
| `deliveryId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related delivery record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `pickupWindowStartUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for pickup window start; parse strictly and localize only for display. | No further constraint recorded |
| `pickupWindowEndUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for pickup window end; parse strictly and localize only for display. | No further constraint recorded |
| `deliveryWindowStartUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for delivery window start; parse strictly and localize only for display. | No further constraint recorded |
| `deliveryWindowEndUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for delivery window end; parse strictly and localize only for display. | No further constraint recorded |
| `declaredValueMinor` | `integer (int64)` | Yes | Not declared nullable | Declared value in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `declaredValueCurrency` | `string` | Yes | Not declared nullable | Declared value currency text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `protectionStatus` | [ParcelProtectionStatus](p.md#parcelprotectionstatus) | Yes | Not declared nullable | Protection status represented by the `ParcelProtectionStatus` model or enum; use that definition's fields/values. | No further constraint recorded |
| `protectionFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Protection fee in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `protectionCoverageMinor` | `integer (int64)` | Yes | Not declared nullable | Protection coverage in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `businessShippingAccountId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related business shipping account record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `externalReference` | `string` | No | Explicitly allowed | External reference text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `signatureRequired` | `boolean` | No | Not declared nullable | Whether signature required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `pickupVerificationRequired` | `boolean` | No | Not declared nullable | Whether pickup verification required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `recipientVerificationRequired` | `boolean` | No | Not declared nullable | Whether recipient verification required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `proofPhotoRequired` | `boolean` | No | Not declared nullable | Whether proof photo required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `returnPolicy` | [DeliveryReturnPolicy](d.md#deliveryreturnpolicy) | No | Not declared nullable | Return policy represented by the `DeliveryReturnPolicy` model or enum; use that definition's fields/values. | No further constraint recorded |
| `maximumFailedAttempts` | `integer (int32)` | No | Not declared nullable | Numeric maximum failed attempts for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `returnVerificationRequired` | `boolean` | No | Not declared nullable | Whether return verification required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `returnEvidenceRequired` | `boolean` | No | Not declared nullable | Whether return evidence required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `trackingNumber` | `string` | No | Explicitly allowed | Tracking number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `deliveryQuoteId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related delivery quote record in this model; ownership and scope are checked separately. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeliveryRequestDtoPagedResult

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `items` | [DeliveryRequestDto](d.md#deliveryrequestdto)[] | No | Explicitly allowed | Records returned in this collection/page, each using the referenced item model. | No further constraint recorded |
| `page` | `integer (int32)` | No | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | `integer (int32)` | No | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `totalCount` | `integer (int64)` | No | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | No further constraint recorded |
| `totalPages` | `integer (int32)` | No | Not declared nullable | Number of pages represented by this page-number model. | readOnly: `True` |
| `hasPreviousPage` | `boolean` | No | Not declared nullable | Whether has previous page applies in this model's context. This flag does not replace server permission or lifecycle checks. | readOnly: `True` |
| `hasNextPage` | `boolean` | No | Not declared nullable | Whether has next page applies in this model's context. This flag does not replace server permission or lifecycle checks. | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## DeliveryRequestStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Requested | Requested state/choice in this specific enum. |
| `2` | Assigned | Assigned state/choice in this specific enum. |
| `3` | InProgress | In progress state/choice in this specific enum. |
| `4` | Completed | Completed state/choice in this specific enum. |
| `5` | Cancelled | Cancelled state/choice in this specific enum. |
| `6` | Expired | Expired state/choice in this specific enum. |
| `7` | ReturnedToSender | Returned to sender state/choice in this specific enum. |

## DeliveryReturnPolicy

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | ReturnAfterMaximumAttempts | Return after maximum attempts state/choice in this specific enum. |
| `2` | ReturnAfterFirstFailedAttempt | Return after first failed attempt state/choice in this specific enum. |

## DeliveryStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Assigned | Assigned state/choice in this specific enum. |
| `2` | InProgress | In progress state/choice in this specific enum. |
| `3` | Completed | Completed state/choice in this specific enum. |
| `4` | Cancelled | Cancelled state/choice in this specific enum. |
| `5` | ReturningToSender | Returning to sender state/choice in this specific enum. |
| `6` | ReturnedToSender | Returned to sender state/choice in this specific enum. |
| `7` | Failed | Failed state/choice in this specific enum. |

## DeliveryStopDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `sequence` | `integer (int32)` | Yes | Not declared nullable | Numeric sequence for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `type` | [DeliveryStopType](d.md#deliverystoptype) | Yes | Not declared nullable | Type represented by the `DeliveryStopType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `contactName` | `string` | Yes | Not declared nullable | Contact name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `contactPhone` | `string` | No | Explicitly allowed | Contact phone text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | No further constraint recorded |
| `address` | `string` | Yes | Not declared nullable | Address text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `instructions` | `string` | No | Explicitly allowed | Instructions text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `placeId` | `string` | No | Explicitly allowed | Identifier of the related place record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `status` | [DeliveryStopStatus](d.md#deliverystopstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `completedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for completed at; parse strictly and localize only for display. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeliveryStopInputDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `type` | [DeliveryStopType](d.md#deliverystoptype) | Yes | Not declared nullable | Type represented by the `DeliveryStopType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `contactName` | `string` | Yes | Not declared nullable | Contact name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `contactPhone` | `string` | No | Explicitly allowed | Contact phone text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | No further constraint recorded |
| `address` | `string` | Yes | Not declared nullable | Address text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `instructions` | `string` | No | Explicitly allowed | Instructions text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `placeId` | `string` | No | Explicitly allowed | Identifier of the related place record in this model; ownership and scope are checked separately. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeliveryStopStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Completed | Completed state/choice in this specific enum. |
| `3` | Failed | Failed state/choice in this specific enum. |
| `4` | Attempted | Attempted state/choice in this specific enum. |
| `5` | ReturnedToSender | Returned to sender state/choice in this specific enum. |

## DeliveryStopType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pickup | Pickup state/choice in this specific enum. |
| `2` | Dropoff | Dropoff state/choice in this specific enum. |

## DeliveryVerificationChallengeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `challengeId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related challenge record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `purpose` | `string` | Yes | Not declared nullable | Purpose text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `qrPayload` | `string` | Yes | Not declared nullable | Qr payload text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeliveryVerificationMethod

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Otp | Otp state/choice in this specific enum. |
| `2` | Qr | Qr state/choice in this specific enum. |
| `3` | ManualOverride | Manual override state/choice in this specific enum. |

## DependentTravelDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `memberId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related member record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `guardianUserId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related guardian user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | No further constraint recorded |
| `dateOfBirth` | `string (date)` | Yes | Not declared nullable | Calendar date for date of birth; preserve date-only semantics rather than shifting it through a timezone. | No further constraint recorded |
| `ageBand` | `string` | Yes | Not declared nullable | Age band text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `consentPolicyVersion` | `string` | Yes | Not declared nullable | Consent policy version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `consentGrantedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for consent granted at; parse strictly and localize only for display. | No further constraint recorded |
| `consentRevokedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for consent revoked at; parse strictly and localize only for display. | No further constraint recorded |
| `consentEvidenceRetainUntilUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for consent evidence retain until; parse strictly and localize only for display. | No further constraint recorded |
| `allowCash` | `boolean` | Yes | Not declared nullable | Whether allow cash applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `allowedWeekdaysMask` | `integer (int32)` | Yes | Not declared nullable | Numeric allowed weekdays mask for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `earliestMinuteLocal` | `integer (int32)` | Yes | Not declared nullable | Numeric earliest minute local for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `latestMinuteLocal` | `integer (int32)` | Yes | Not declared nullable | Numeric latest minute local for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `minimumDriverTrustLevel` | `integer (int32)` | Yes | Not declared nullable | Numeric minimum driver trust level for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `requirePickupGuardianConfirmation` | `boolean` | Yes | Not declared nullable | Whether require pickup guardian confirmation applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `requireDropoffGuardianConfirmation` | `boolean` | Yes | Not declared nullable | Whether require dropoff guardian confirmation applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `familySafetyPolicyId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related family safety policy record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `familySafetyPolicyRevision` | `integer (int64)` | Yes | Not declared nullable | Family safety policy revision for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `guardianAuthorityType` | `string` | Yes | Not declared nullable | Guardian authority type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `consentExpiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for consent expires at; parse strictly and localize only for display. | No further constraint recorded |
| `reconsentRequiredAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for reconsent required at; parse strictly and localize only for display. | No further constraint recorded |
| `liveTrackingConsentGranted` | `boolean` | Yes | Not declared nullable | Whether live tracking consent granted applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `threeWayCommunicationConsentGranted` | `boolean` | Yes | Not declared nullable | Whether three way communication consent granted applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `emergencyContactConfirmed` | `boolean` | Yes | Not declared nullable | Whether emergency contact confirmed applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeviceAccessStatusDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `deviceId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related device record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `serverTimeUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for server time; parse strictly and localize only for display. | No further constraint recorded |
| `banType` | [DeviceBanType](d.md#devicebantype) | No | Not declared nullable | Ban type represented by the `DeviceBanType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `publicExplanation` | `string` | No | Explicitly allowed | Public explanation text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `supportUrl` | `string` | Yes | Not declared nullable | URL for support; validate the intended origin/access and never assume private links are public. | No further constraint recorded |
| `allowed` | `boolean` | Yes | Not declared nullable | Whether allowed applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Explicitly allowed | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeviceBanType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Temporary | Temporary state/choice in this specific enum. |
| `2` | Permanent | Permanent state/choice in this specific enum. |

## DeviceMetadataDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `platform` | `string` | Yes | Not declared nullable | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | No further constraint recorded |
| `manufacturer` | `string` | Yes | Not declared nullable | Manufacturer text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `brand` | `string` | Yes | Not declared nullable | Brand text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `model` | `string` | Yes | Not declared nullable | Model in the owning domain; for vehicle contracts, the vehicle model associated with the manufacturer. | No further constraint recorded |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | No further constraint recorded |
| `operatingSystem` | `string` | Yes | Not declared nullable | Operating system text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `osVersion` | `string` | Yes | Not declared nullable | Os version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `appVersion` | `string` | Yes | Not declared nullable | App version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `buildNumber` | `integer (int32)` | Yes | Not declared nullable | Numeric build number for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `locale` | `string` | Yes | Not declared nullable | Locale text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DeviceRegistrationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `deviceId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related device record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `deviceToken` | `string` | Yes | Not declared nullable | Private admitted-installation credential; not a user password or portable account authority. | No further constraint recorded |
| `serverTimeUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for server time; parse strictly and localize only for display. | No further constraint recorded |
| `access` | [DeviceAccessStatusDto](d.md#deviceaccessstatusdto) | Yes | Not declared nullable | Access represented by the `DeviceAccessStatusDto` model or enum; use that definition's fields/values. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DisputeDriverReviewRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `reason` | `string` | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DisputeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | No further constraint recorded |
| `openedById` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related opened by record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `reason` | `string` | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | No further constraint recorded |
| `status` | [DisputeStatus](d.md#disputestatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `resolutionNote` | `string` | No | Explicitly allowed | Resolution note text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DisputeStatus

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Open | Open state/choice in this specific enum. |
| `1` | Resolved | Resolved state/choice in this specific enum. |

## DocumentStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Approved | Approved state/choice in this specific enum. |
| `3` | Rejected | Rejected state/choice in this specific enum. |
| `4` | Expired | Expired state/choice in this specific enum. |
| `5` | Staged | Staged state/choice in this specific enum. |

## DocumentType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | DriversLicense | Drivers license state/choice in this specific enum. |
| `2` | VehicleRegistration | Vehicle registration state/choice in this specific enum. |
| `3` | VehicleInsurance | Vehicle insurance state/choice in this specific enum. |
| `4` | ProfilePhoto | Profile photo state/choice in this specific enum. |
| `5` | VehiclePhoto | Vehicle photo state/choice in this specific enum. |
| `6` | Other | Other state/choice in this specific enum. |
| `7` | MilitaryId | Military id state/choice in this specific enum. |
| `8` | Passport | Passport state/choice in this specific enum. |
| `9` | NationalId | National id state/choice in this specific enum. |
| `10` | BirthCertificate | Birth certificate state/choice in this specific enum. |
| `11` | MarriageCertificate | Marriage certificate state/choice in this specific enum. |
| `12` | SocialSecurityCard | Social security card state/choice in this specific enum. |
| `13` | VoterRegistrationCard | Voter registration card state/choice in this specific enum. |
| `14` | NaturalizationCertificate | Naturalization certificate state/choice in this specific enum. |
| `15` | ProofOfAddress | Proof of address state/choice in this specific enum. |
| `16` | PoliceRecord | Police record state/choice in this specific enum. |
| `17` | VehicleFitness | Vehicle fitness state/choice in this specific enum. |
| `18` | SchoolId | School id state/choice in this specific enum. |
| `19` | CitizenCard | Citizen card state/choice in this specific enum. |
| `20` | JusticeOfPeaceAttestation | Justice of peace attestation state/choice in this specific enum. |

## DriverAccountType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Individual | Individual state/choice in this specific enum. |
| `2` | SoleTrader | Sole trader state/choice in this specific enum. |
| `3` | Company | Company state/choice in this specific enum. |

## DriverAssistanceCapabilityDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `acceptsAssistedRides` | `boolean` | Yes | Not declared nullable | Whether accepts assisted rides applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `canAssistBoarding` | `boolean` | Yes | Not declared nullable | Whether can assist boarding applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `acceptsServiceAnimals` | `boolean` | Yes | Not declared nullable | Whether accepts service animals applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `supportsHearingCommunication` | `boolean` | Yes | Not declared nullable | Whether supports hearing communication applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `supportsVisionCommunication` | `boolean` | Yes | Not declared nullable | Whether supports vision communication applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `attestedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for attested at; parse strictly and localize only for display. | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverDeliveryOfferDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `vehicleCategoryName` | `string` | Yes | Not declared nullable | Vehicle category name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `proposedPriceMinor` | `integer (int64)` | Yes | Not declared nullable | Proposed price in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `stopCount` | `integer (int32)` | Yes | Not declared nullable | Number of stop in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `parcelCount` | `integer (int32)` | Yes | Not declared nullable | Number of parcel in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `totalDistanceMeters` | `integer (int32)` | Yes | Not declared nullable | Total distance, measured in metres. | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | No further constraint recorded |
| `firstPickupAddress` | `string` | Yes | Not declared nullable | First pickup address text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `firstPickupLatitude` | `number (double)` | Yes | Not declared nullable | Numeric first pickup latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `firstPickupLongitude` | `number (double)` | Yes | Not declared nullable | Numeric first pickup longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `pickupVerificationRequired` | `boolean` | No | Not declared nullable | Whether pickup verification required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `recipientVerificationRequired` | `boolean` | No | Not declared nullable | Whether recipient verification required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `proofPhotoRequired` | `boolean` | No | Not declared nullable | Whether proof photo required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `signatureRequired` | `boolean` | No | Not declared nullable | Whether signature required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `returnPolicy` | [DeliveryReturnPolicy](d.md#deliveryreturnpolicy) | No | Not declared nullable | Return policy represented by the `DeliveryReturnPolicy` model or enum; use that definition's fields/values. | No further constraint recorded |
| `maximumFailedAttempts` | `integer (int32)` | No | Not declared nullable | Numeric maximum failed attempts for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `returnVerificationRequired` | `boolean` | No | Not declared nullable | Whether return verification required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `returnEvidenceRequired` | `boolean` | No | Not declared nullable | Whether return evidence required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverDeliveryOfferDtoPagedResult

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `items` | [DriverDeliveryOfferDto](d.md#driverdeliveryofferdto)[] | No | Explicitly allowed | Records returned in this collection/page, each using the referenced item model. | No further constraint recorded |
| `page` | `integer (int32)` | No | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | `integer (int32)` | No | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `totalCount` | `integer (int64)` | No | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | No further constraint recorded |
| `totalPages` | `integer (int32)` | No | Not declared nullable | Number of pages represented by this page-number model. | readOnly: `True` |
| `hasPreviousPage` | `boolean` | No | Not declared nullable | Whether has previous page applies in this model's context. This flag does not replace server permission or lifecycle checks. | readOnly: `True` |
| `hasNextPage` | `boolean` | No | Not declared nullable | Whether has next page applies in this model's context. This flag does not replace server permission or lifecycle checks. | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## DriverDocument

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `driverProfileId` | `string (uuid)` | No | Not declared nullable | Driver-profile record associated with this operation or result. | No further constraint recorded |
| `driverProfile` | [DriverProfile](d.md#driverprofile) | No | Not declared nullable | Driver profile represented by the `DriverProfile` model or enum; use that definition's fields/values. | No further constraint recorded |
| `vehicleId` | `string (uuid)` | No | Explicitly allowed | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `vehicle` | [Vehicle](v.md#vehicle) | No | Not declared nullable | Vehicle represented by the `Vehicle` model or enum; use that definition's fields/values. | No further constraint recorded |
| `type` | [DocumentType](d.md#documenttype) | No | Not declared nullable | Type represented by the `DocumentType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `fileRef` | `string` | No | Explicitly allowed | Private storage reference; not a permanent public URL or approval decision. | No further constraint recorded |
| `fileName` | `string` | No | Explicitly allowed | Document/file display name; it is not a storage authorization or approved-document status. | No further constraint recorded |
| `status` | [DocumentStatus](d.md#documentstatus) | No | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `reviewNote` | `string` | No | Explicitly allowed | Human-readable reviewer explanation, including remediation where applicable. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `expiryNotificationSentAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expiry notification sent at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverDocumentDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `type` | [DocumentType](d.md#documenttype) | Yes | Not declared nullable | Type represented by the `DocumentType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `status` | [DocumentStatus](d.md#documentstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `fileRef` | `string` | Yes | Not declared nullable | Private storage reference; not a permanent public URL or approval decision. | No further constraint recorded |
| `fileName` | `string` | Yes | Not declared nullable | Document/file display name; it is not a storage authorization or approved-document status. | No further constraint recorded |
| `vehicleId` | `string (uuid)` | No | Explicitly allowed | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `reviewNote` | `string` | No | Explicitly allowed | Human-readable reviewer explanation, including remediation where applicable. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `driverRevision` | `integer (int64)` | No | Not declared nullable | Driver aggregate revision associated with the document/readiness state. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverFareRangeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `minimumMinor` | `integer (int64)` | Yes | Not declared nullable | Minimum in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `recommendedMinor` | `integer (int64)` | Yes | Not declared nullable | Recommended in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `maximumMinor` | `integer (int64)` | Yes | Not declared nullable | Maximum in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `modelVersion` | `string` | Yes | Not declared nullable | Model version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `confidence` | `string` | Yes | Not declared nullable | Confidence text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `calculatedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for calculated at; parse strictly and localize only for display. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverFirstEarningJourneyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `stage` | `string` | Yes | Not declared nullable | Stage text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `completed` | `boolean` | Yes | Not declared nullable | Whether completed applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `nextAction` | `string` | No | Explicitly allowed | Suggested next workflow step returned by the server; it does not override authorization. | No further constraint recorded |
| `hasSubmittedBid` | `boolean` | Yes | Not declared nullable | Whether has submitted bid applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `hasAcceptedAssignment` | `boolean` | Yes | Not declared nullable | Whether has accepted assignment applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `hasCompletedTrip` | `boolean` | Yes | Not declared nullable | Whether has completed trip applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `hasRecordedEarning` | `boolean` | Yes | Not declared nullable | Whether has recorded earning applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `firstBidAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for first bid at; parse strictly and localize only for display. | No further constraint recorded |
| `firstAssignmentAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for first assignment at; parse strictly and localize only for display. | No further constraint recorded |
| `firstCompletedTripAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for first completed trip at; parse strictly and localize only for display. | No further constraint recorded |
| `firstEarningAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for first earning at; parse strictly and localize only for display. | No further constraint recorded |
| `firstEarningMinor` | `integer (int64)` | No | Explicitly allowed | First earning in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | No | Explicitly allowed | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `assessedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for assessed at; parse strictly and localize only for display. | No further constraint recorded |
| `policyVersion` | `string` | No | Explicitly allowed | Policy revision used for this assessment; not the mobile app build number. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverOfferEarningsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `grossFareMinor` | `integer (int64)` | Yes | Not declared nullable | Gross fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `commissionMinor` | `integer (int64)` | Yes | Not declared nullable | Commission in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `estimatedNetMinor` | `integer (int64)` | Yes | Not declared nullable | Estimated net in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `basis` | `string` | Yes | Not declared nullable | Basis text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverOfferFreshnessDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `requestAgeSeconds` | `integer (int32)` | Yes | Not declared nullable | Request age, measured in seconds. | No further constraint recorded |
| `expiresInSeconds` | `integer (int32)` | Yes | Not declared nullable | Expires in, measured in seconds. | No further constraint recorded |
| `scheduleStatus` | `string` | Yes | Not declared nullable | Schedule status text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `routeEvidenceAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for route evidence at; parse strictly and localize only for display. | No further constraint recorded |
| `routeEvidenceSource` | `string` | Yes | Not declared nullable | Route evidence source text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverOfferGateDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `allowed` | `boolean` | Yes | Not declared nullable | Whether allowed applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `primaryAction` | `string` | Yes | Not declared nullable | Primary action text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverOfferPaymentEvidenceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `state` | `string` | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | No further constraint recorded |
| `fundsHeld` | `boolean` | Yes | Not declared nullable | Whether funds held applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `settlementTiming` | `string` | Yes | Not declared nullable | Settlement timing text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverOfferScheduleFilter

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | All | All state/choice in this specific enum. |
| `2` | Immediate | Immediate state/choice in this specific enum. |
| `3` | Scheduled | Scheduled state/choice in this specific enum. |

## DriverOfferSort

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Newest | Newest state/choice in this specific enum. |
| `2` | Urgency | Urgency state/choice in this specific enum. |
| `3` | PickupDistance | Pickup distance state/choice in this specific enum. |
| `4` | ExpectedNetEarnings | Expected net earnings state/choice in this specific enum. |

## DriverOnboardingContactPolicyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `phoneOptional` | `boolean` | Yes | Not declared nullable | Whether phone optional applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `emailVerified` | `boolean` | Yes | Not declared nullable | Whether email verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `phoneProvided` | `boolean` | Yes | Not declared nullable | Whether phone provided applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `phoneVerified` | `boolean` | Yes | Not declared nullable | Whether phone verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverOnboardingDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `driverProfileId` | `string (uuid)` | Yes | Not declared nullable | Driver-profile record associated with this operation or result. | No further constraint recorded |
| `driverStatus` | [DriverStatus](d.md#driverstatus) | Yes | Not declared nullable | Driver status represented by the `DriverStatus` model or enum; use that definition's fields/values. | No further constraint recorded |
| `identityVerified` | `boolean` | Yes | Not declared nullable | Whether identity verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `driverLicenseNumber` | `string` | No | Explicitly allowed | Driver license number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `driverLicenseControlNumber` | `string` | No | Explicitly allowed | Driver license control number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `driverLicenseOriginalIssueDate` | `string (date)` | No | Explicitly allowed | Calendar date for driver license original issue date; preserve date-only semantics rather than shifting it through a timezone. | No further constraint recorded |
| `driverLicenseExpiresOn` | `string (date)` | No | Explicitly allowed | Calendar date for driver license expires on; preserve date-only semantics rather than shifting it through a timezone. | No further constraint recorded |
| `rejectedReason` | `string` | No | Explicitly allowed | Rejected reason text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `steps` | [OnboardingStepDto](o.md#onboardingstepdto)[] | Yes | Not declared nullable | Collection of steps for this model; interpret each item through the declared item type. | No further constraint recorded |
| `completedSteps` | `integer (int32)` | Yes | Not declared nullable | Numeric completed steps for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `totalSteps` | `integer (int32)` | Yes | Not declared nullable | Numeric total steps for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `readyForReview` | `boolean` | Yes | Not declared nullable | Whether ready for review applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `wizardCompleted` | `boolean` | Yes | Not declared nullable | Whether wizard completed applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `approved` | `boolean` | Yes | Not declared nullable | Whether approved applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `operationallyEligible` | `boolean` | Yes | Not declared nullable | Whether operationally eligible applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `missingRequirements` | `string[]` | Yes | Not declared nullable | Collection of missing requirements for this model; interpret each item through the declared item type. | No further constraint recorded |
| `pages` | [DriverOnboardingPageDto](d.md#driveronboardingpagedto)[] | Yes | Not declared nullable | Collection of pages for this model; interpret each item through the declared item type. | No further constraint recorded |
| `currentPage` | `integer (int32)` | Yes | Not declared nullable | Numeric current page for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `requiresOnboarding` | `boolean` | Yes | Not declared nullable | Whether requires onboarding applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `backgroundCheckDeferred` | `boolean` | Yes | Not declared nullable | Whether background check deferred applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `backgroundCheckDueAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for background check due at; parse strictly and localize only for display. | No further constraint recorded |
| `backgroundCheckDaysRemaining` | `integer (int32)` | Yes | Not declared nullable | Numeric background check days remaining for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `backgroundCheckDeferralDays` | `integer (int32)` | Yes | Not declared nullable | Background check deferral, measured in days under this workflow's calendar rules. | No further constraint recorded |
| `complianceLocked` | `boolean` | Yes | Not declared nullable | Whether compliance locked applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `contactPolicy` | [DriverOnboardingContactPolicyDto](d.md#driveronboardingcontactpolicydto) | No | Not declared nullable | Contact policy represented by the `DriverOnboardingContactPolicyDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `estimatedMinutes` | `integer (int32)` | No | Not declared nullable | Estimated, measured in minutes. | No further constraint recorded |
| `reviewSlaHours` | `integer (int32)` | No | Not declared nullable | Numeric review sla hours for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `percentComplete` | `integer (int32)` | No | Not declared nullable | Numeric percent complete for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `nextAction` | `string` | No | Explicitly allowed | Suggested next workflow step returned by the server; it does not override authorization. | No further constraint recorded |
| `trainingSafetyAcknowledged` | `boolean` | No | Not declared nullable | Whether training safety acknowledged applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `trainingSafetyPolicyVersion` | `string` | No | Explicitly allowed | Training safety policy version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `trainingSafetyAcknowledgedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for training safety acknowledged at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverOnboardingPageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `number` | `integer (int32)` | Yes | Not declared nullable | Numeric number for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `missingRequirements` | `string[]` | Yes | Not declared nullable | Collection of missing requirements for this model; interpret each item through the declared item type. | No further constraint recorded |
| `dueAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for due at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverProfile

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `userId` | `string (uuid)` | No | Not declared nullable | Related account identity; the server still proves the caller's ownership or permitted relationship. | No further constraint recorded |
| `user` | [User](u.md#user) | No | Not declared nullable | User represented by the `User` model or enum; use that definition's fields/values. | No further constraint recorded |
| `driverLicenseNumber` | `string` | No | Explicitly allowed | Driver license number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `driverLicenseNumberNormalized` | `string` | No | Explicitly allowed | Driver license number normalized text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `driverLicenseControlNumber` | `string` | No | Explicitly allowed | Driver license control number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `driverLicenseControlNumberNormalized` | `string` | No | Explicitly allowed | Driver license control number normalized text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `driverLicenseOriginalIssueDate` | `string (date)` | No | Explicitly allowed | Calendar date for driver license original issue date; preserve date-only semantics rather than shifting it through a timezone. | No further constraint recorded |
| `driverLicenseExpiresOn` | `string (date)` | No | Explicitly allowed | Calendar date for driver license expires on; preserve date-only semantics rather than shifting it through a timezone. | No further constraint recorded |
| `status` | [DriverStatus](d.md#driverstatus) | No | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `accountType` | [DriverAccountType](d.md#driveraccounttype) | No | Not declared nullable | Account type represented by the `DriverAccountType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `businessLegalName` | `string` | No | Explicitly allowed | Business legal name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `businessTradingName` | `string` | No | Explicitly allowed | Business trading name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `businessRegistrationNumber` | `string` | No | Explicitly allowed | Business registration number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `businessTaxNumber` | `string` | No | Explicitly allowed | Business tax number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `businessEmail` | `string` | No | Explicitly allowed | Business email text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `businessPhone` | `string` | No | Explicitly allowed | Business phone text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `businessRegisteredAddress` | `string` | No | Explicitly allowed | Business registered address text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `approvedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for approved at; parse strictly and localize only for display. | No further constraint recorded |
| `rejectedReason` | `string` | No | Explicitly allowed | Rejected reason text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `privacyAcceptedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for privacy accepted at; parse strictly and localize only for display. | No further constraint recorded |
| `termsAcceptedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for terms accepted at; parse strictly and localize only for display. | No further constraint recorded |
| `onboardingCompletedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for onboarding completed at; parse strictly and localize only for display. | No further constraint recorded |
| `onboardingCurrentPage` | `integer (int32)` | No | Not declared nullable | Numeric onboarding current page for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `backgroundCheckDeferredUntilUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for background check deferred until; parse strictly and localize only for display. | No further constraint recorded |
| `membershipChoiceConfirmedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for membership choice confirmed at; parse strictly and localize only for display. | No further constraint recorded |
| `contactDetailsConfirmedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for contact details confirmed at; parse strictly and localize only for display. | No further constraint recorded |
| `preferencesConfirmedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for preferences confirmed at; parse strictly and localize only for display. | No further constraint recorded |
| `businessPreferencesConfirmedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for business preferences confirmed at; parse strictly and localize only for display. | No further constraint recorded |
| `complianceVersion` | `integer (int64)` | No | Not declared nullable | Compliance version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `complianceHash` | `string` | No | Explicitly allowed | Compliance hash text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `complianceAppliedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for compliance applied at; parse strictly and localize only for display. | No further constraint recorded |
| `approvalOverrideActive` | `boolean` | No | Not declared nullable | Whether approval override active applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `approvalOverrideReason` | `string` | No | Explicitly allowed | Approval override reason text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `approvalOverrideByUserId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related approval override by user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `approvalOverrideAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for approval override at; parse strictly and localize only for display. | No further constraint recorded |
| `commissionRateOverride` | `number (double)` | No | Explicitly allowed | Numeric commission rate override for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `billingMode` | `string` | No | Explicitly allowed | Billing mode text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `totalTrips` | `integer (int32)` | No | Not declared nullable | Numeric total trips for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `totalEarningsMinor` | `integer (int64)` | No | Not declared nullable | Total earnings in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `ratingSum` | `integer (int64)` | No | Not declared nullable | Numeric rating sum for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `ratingCount` | `integer (int32)` | No | Not declared nullable | Number of rating in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `importedRatingSum` | `integer (int64)` | No | Not declared nullable | Numeric imported rating sum for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `importedRatingCount` | `integer (int32)` | No | Not declared nullable | Number of imported rating in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `preferredDriverStatus` | [PreferredDriverStatus](p.md#preferreddriverstatus) | No | Not declared nullable | Preferred driver status represented by the `PreferredDriverStatus` model or enum; use that definition's fields/values. | No further constraint recorded |
| `preferredAppliedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for preferred applied at; parse strictly and localize only for display. | No further constraint recorded |
| `preferredApprovedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for preferred approved at; parse strictly and localize only for display. | No further constraint recorded |
| `preferredReviewNote` | `string` | No | Explicitly allowed | Preferred review note text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `preferredShirtsIssuedCount` | `integer (int32)` | No | Not declared nullable | Number of preferred shirts issued in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `drivingSum` | `integer (int64)` | No | Not declared nullable | Numeric driving sum for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `drivingCount` | `integer (int32)` | No | Not declared nullable | Number of driving in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `courtesySum` | `integer (int64)` | No | Not declared nullable | Numeric courtesy sum for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `courtesyCount` | `integer (int32)` | No | Not declared nullable | Number of courtesy in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `cleanlinessSum` | `integer (int64)` | No | Not declared nullable | Numeric cleanliness sum for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `cleanlinessCount` | `integer (int32)` | No | Not declared nullable | Number of cleanliness in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `punctualitySum` | `integer (int64)` | No | Not declared nullable | Numeric punctuality sum for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `punctualityCount` | `integer (int32)` | No | Not declared nullable | Number of punctuality in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `isOnline` | `boolean` | No | Not declared nullable | Whether is online applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `lastLatitude` | `number (double)` | No | Explicitly allowed | Numeric last latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `lastLongitude` | `number (double)` | No | Explicitly allowed | Numeric last longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `lastLocationAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last location at; parse strictly and localize only for display. | No further constraint recorded |
| `locationSequence` | `integer (int64)` | No | Not declared nullable | Numeric location sequence for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `acceptsAssistedRides` | `boolean` | No | Not declared nullable | Whether accepts assisted rides applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `canAssistBoarding` | `boolean` | No | Not declared nullable | Whether can assist boarding applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `acceptsServiceAnimals` | `boolean` | No | Not declared nullable | Whether accepts service animals applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `supportsHearingCommunication` | `boolean` | No | Not declared nullable | Whether supports hearing communication applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `supportsVisionCommunication` | `boolean` | No | Not declared nullable | Whether supports vision communication applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `assistanceCapabilityAttestedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for assistance capability attested at; parse strictly and localize only for display. | No further constraint recorded |
| `assistanceCapabilityRevision` | `integer (int64)` | No | Not declared nullable | Assistance capability revision for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `membershipPlanId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related membership plan record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `membershipExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for membership expires at; parse strictly and localize only for display. | No further constraint recorded |
| `membershipRenewalTermDays` | `integer (int32)` | No | Explicitly allowed | Membership renewal term, measured in days under this workflow's calendar rules. | No further constraint recorded |
| `membershipRenewalBasePriceMinor` | `integer (int64)` | No | Explicitly allowed | Membership renewal base price in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `membershipRenewalBaseCurrency` | `string` | No | Explicitly allowed | Membership renewal base currency text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `membershipRenewalPriceSource` | `string` | No | Explicitly allowed | Membership renewal price source text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `autoRenewMembership` | `boolean` | No | Not declared nullable | Whether auto renew membership applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `vehicleChangesUsed` | `integer (int32)` | No | Not declared nullable | Numeric vehicle changes used for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `vehicleChangesWindowStartUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for vehicle changes window start; parse strictly and localize only for display. | No further constraint recorded |
| `vehicles` | [Vehicle](v.md#vehicle)[] | No | Explicitly allowed | Collection of vehicles for this model; interpret each item through the declared item type. | No further constraint recorded |
| `documents` | [DriverDocument](d.md#driverdocument)[] | No | Explicitly allowed | Collection of documents for this model; interpret each item through the declared item type. | No further constraint recorded |
| `totalRatingCount` | `integer (int32)` | No | Not declared nullable | Number of total rating in this model's stated scope; not automatically a global/live total. | readOnly: `True` |
| `nativeAverageRating` | `number (double)` | No | Not declared nullable | Numeric native average rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | readOnly: `True` |
| `averageRating` | `number (double)` | No | Not declared nullable | Numeric average rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | readOnly: `True` |
| `externalAverageRating` | `number (double)` | No | Not declared nullable | Numeric external average rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | readOnly: `True` |
| `drivingRating` | `number (double)` | No | Not declared nullable | Numeric driving rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | readOnly: `True` |
| `courtesyRating` | `number (double)` | No | Not declared nullable | Numeric courtesy rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | readOnly: `True` |
| `cleanlinessRating` | `number (double)` | No | Not declared nullable | Numeric cleanliness rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | readOnly: `True` |
| `punctualityRating` | `number (double)` | No | Not declared nullable | Numeric punctuality rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | readOnly: `True` |
| `displayName` | `string` | No | Explicitly allowed | Human-readable display label; do not use it as a stable identifier. | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## DriverProfileDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `driverProfileId` | `string (uuid)` | Yes | Not declared nullable | Driver-profile record associated with this operation or result. | No further constraint recorded |
| `fullName` | `string` | Yes | Not declared nullable | Full name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `accountType` | [DriverAccountType](d.md#driveraccounttype) | Yes | Not declared nullable | Account type represented by the `DriverAccountType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | No further constraint recorded |
| `businessLegalName` | `string` | No | Explicitly allowed | Business legal name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `businessTradingName` | `string` | No | Explicitly allowed | Business trading name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `businessRegistrationNumber` | `string` | No | Explicitly allowed | Business registration number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `businessTaxNumber` | `string` | No | Explicitly allowed | Business tax number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `businessEmail` | `string` | No | Explicitly allowed | Business email text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `businessPhone` | `string` | No | Explicitly allowed | Business phone text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `businessRegisteredAddress` | `string` | No | Explicitly allowed | Business registered address text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `driverLicenseNumber` | `string` | No | Explicitly allowed | Driver license number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `driverLicenseControlNumber` | `string` | No | Explicitly allowed | Driver license control number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `driverLicenseOriginalIssueDate` | `string (date)` | No | Explicitly allowed | Calendar date for driver license original issue date; preserve date-only semantics rather than shifting it through a timezone. | No further constraint recorded |
| `driverLicenseExpiresOn` | `string (date)` | No | Explicitly allowed | Calendar date for driver license expires on; preserve date-only semantics rather than shifting it through a timezone. | No further constraint recorded |
| `status` | [DriverStatus](d.md#driverstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `identityVerified` | `boolean` | Yes | Not declared nullable | Whether identity verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `rejectedReason` | `string` | No | Explicitly allowed | Rejected reason text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `rating` | [RatingBreakdownDto](r.md#ratingbreakdowndto) | Yes | Not declared nullable | Rating represented by the `RatingBreakdownDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `totalTrips` | `integer (int32)` | Yes | Not declared nullable | Numeric total trips for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `firstCompletedTripAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for first completed trip at; parse strictly and localize only for display. | No further constraint recorded |
| `totalEarningsMinor` | `integer (int64)` | Yes | Not declared nullable | Total earnings in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `membershipPlanName` | `string` | No | Explicitly allowed | Membership plan name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `membershipExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for membership expires at; parse strictly and localize only for display. | No further constraint recorded |
| `vehicleCount` | `integer (int32)` | Yes | Not declared nullable | Number of vehicle in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `maxRegisteredVehicles` | `integer (int32)` | Yes | Not declared nullable | Legacy plan metadata; it must not cap account-owned vehicle storage or Maintenance Center access. | No further constraint recorded |
| `activeVehicleId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related active vehicle record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `activeVehicleDescription` | `string` | No | Explicitly allowed | Active vehicle description text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `activeVehicleInsured` | `boolean` | Yes | Not declared nullable | Whether active vehicle insured applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `trustProfile` | [DriverTrustProfileDto](d.md#drivertrustprofiledto) | Yes | Not declared nullable | Trust profile represented by the `DriverTrustProfileDto` model or enum; use that definition's fields/values. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverReadinessCheckDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `satisfied` | `boolean` | Yes | Not declared nullable | Whether satisfied applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `reasonCode` | `string` | No | Explicitly allowed | Stable reason code; map through the applicable reason catalog instead of displaying an unrelated enum. | No further constraint recorded |
| `action` | `string` | No | Explicitly allowed | Action text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `state` | `string` | No | Explicitly allowed | State in this model's workflow; do not map it with another domain's status registry. | No further constraint recorded |
| `reasonMessageKey` | `string` | No | Explicitly allowed | Reason message key text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `evidenceMessageKey` | `string` | No | Explicitly allowed | Evidence message key text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `reviewSlaMessageKey` | `string` | No | Explicitly allowed | Review sla message key text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `supportAction` | `string` | No | Explicitly allowed | Support action text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `policyVersion` | `string` | No | Explicitly allowed | Policy revision used for this assessment; not the mobile app build number. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverReadinessDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `driverProfileId` | `string (uuid)` | Yes | Not declared nullable | Driver-profile record associated with this operation or result. | No further constraint recorded |
| `profileStatus` | [DriverStatus](d.md#driverstatus) | Yes | Not declared nullable | Profile status represented by the `DriverStatus` model or enum; use that definition's fields/values. | No further constraint recorded |
| `emailVerified` | `boolean` | Yes | Not declared nullable | Whether email verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `phoneVerified` | `boolean` | Yes | Not declared nullable | Whether phone verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `driversLicenseVerified` | `boolean` | Yes | Not declared nullable | Whether drivers license verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `driversLicenseExpiresOn` | `string (date)` | No | Explicitly allowed | Calendar date for drivers license expires on; preserve date-only semantics rather than shifting it through a timezone. | No further constraint recorded |
| `primaryVehicleId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related primary vehicle record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `vehicleAssigned` | `boolean` | Yes | Not declared nullable | Whether vehicle assigned applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `primaryVehicleVerified` | `boolean` | Yes | Not declared nullable | Whether primary vehicle verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `registrationCurrent` | `boolean` | Yes | Not declared nullable | Whether registration current applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `insuranceCurrent` | `boolean` | Yes | Not declared nullable | Whether insurance current applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `fitnessCurrent` | `boolean` | Yes | Not declared nullable | Whether fitness current applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `complianceVersion` | `integer (int64)` | Yes | Not declared nullable | Compliance version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `complianceHash` | `string` | Yes | Not declared nullable | Compliance hash text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `complianceProjectionCurrent` | `boolean` | Yes | Not declared nullable | Whether the projected compliance state agrees with the authoritative assessed version. | No further constraint recorded |
| `membershipPlanName` | `string` | Yes | Not declared nullable | Membership plan name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `membershipExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for membership expires at; parse strictly and localize only for display. | No further constraint recorded |
| `membershipEntitled` | `boolean` | Yes | Not declared nullable | Whether current membership evidence supplies the applicable entitlement. | No further constraint recorded |
| `dutyEligible` | `boolean` | Yes | Not declared nullable | Whether duty eligible applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `dutyMinutesUsed` | `integer (int32)` | Yes | Not declared nullable | Numeric duty minutes used for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `dutyMaximumMinutes` | `integer (int32)` | Yes | Not declared nullable | Duty maximum, measured in minutes. | No further constraint recorded |
| `dutyEligibleAgainAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for duty eligible again at; parse strictly and localize only for display. | No further constraint recorded |
| `isOnline` | `boolean` | Yes | Not declared nullable | Whether is online applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `onlineState` | `string` | Yes | Not declared nullable | Online state text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `lastLatitude` | `number (double)` | No | Explicitly allowed | Numeric last latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `lastLongitude` | `number (double)` | No | Explicitly allowed | Numeric last longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `lastLocationAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last location at; parse strictly and localize only for display. | No further constraint recorded |
| `lastLocationAccuracyMeters` | `number (double)` | No | Explicitly allowed | Last location accuracy, measured in metres. | No further constraint recorded |
| `locationAgeSeconds` | `integer (int32)` | No | Explicitly allowed | Location age, measured in seconds. | No further constraint recorded |
| `locationFresh` | `boolean` | Yes | Not declared nullable | Whether location fresh applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `hasActiveAssignment` | `boolean` | Yes | Not declared nullable | Whether has active assignment applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `canBid` | `boolean` | Yes | Not declared nullable | Server's current assessment of bidding eligibility, not a client-computed approval. | No further constraint recorded |
| `bidGateCode` | `string` | No | Explicitly allowed | Bid gate code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `blockingReasons` | `string[]` | Yes | Not declared nullable | Readable or coded reasons that currently block the assessed workflow. | No further constraint recorded |
| `checklist` | [DriverReadinessCheckDto](d.md#driverreadinesscheckdto)[] | Yes | Not declared nullable | Requirement-by-requirement setup/readiness state. | No further constraint recorded |
| `nextAction` | `string` | No | Explicitly allowed | Suggested next workflow step returned by the server; it does not override authorization. | No further constraint recorded |
| `primaryVehicleLabel` | `string` | No | Explicitly allowed | Primary vehicle label text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `onlineLeaseExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for online lease expires at; parse strictly and localize only for display. | No further constraint recorded |
| `locationVersion` | `integer (int64)` | No | Not declared nullable | Location version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `locationSource` | `string` | No | Explicitly allowed | Location source text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `locationSampledAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for location sampled at; parse strictly and localize only for display. | No further constraint recorded |
| `canGoOnline` | `boolean` | No | Not declared nullable | Server's current assessment of online eligibility. | No further constraint recorded |
| `onlineGateCode` | `string` | No | Explicitly allowed | Online gate code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `assessedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for assessed at; parse strictly and localize only for display. | No further constraint recorded |
| `policyVersion` | `string` | No | Explicitly allowed | Policy revision used for this assessment; not the mobile app build number. | No further constraint recorded |
| `firstEarningJourney` | [DriverFirstEarningJourneyDto](d.md#driverfirstearningjourneydto) | No | Not declared nullable | First earning journey represented by the `DriverFirstEarningJourneyDto` model or enum; use that definition's fields/values. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverReviewCategoryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `average` | `number (double)` | Yes | Not declared nullable | Numeric average for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `count` | `integer (int32)` | Yes | Not declared nullable | Numeric count for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverReviewDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | No further constraint recorded |
| `customerName` | `string` | Yes | Not declared nullable | Customer name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `stars` | `integer (int32)` | Yes | Not declared nullable | Numeric stars for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `comment` | `string` | No | Explicitly allowed | Comment text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `tags` | `string[]` | Yes | Not declared nullable | Collection of tags for this model; interpret each item through the declared item type. | No further constraint recorded |
| `tripCompletedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for trip completed at; parse strictly and localize only for display. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `safeDriving` | `integer (int32)` | No | Explicitly allowed | Numeric safe driving for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `communication` | `integer (int32)` | No | Explicitly allowed | Numeric communication for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `cleanliness` | `integer (int32)` | No | Explicitly allowed | Numeric cleanliness for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `punctuality` | `integer (int32)` | No | Explicitly allowed | Numeric punctuality for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `publishedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for published at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverReviewStarCountDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `stars` | `integer (int32)` | Yes | Not declared nullable | Numeric stars for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `count` | `integer (int64)` | Yes | Not declared nullable | Numeric count for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverReviewsPageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `items` | [DriverReviewDto](d.md#driverreviewdto)[] | Yes | Not declared nullable | Records returned in this collection/page, each using the referenced item model. | No further constraint recorded |
| `page` | `integer (int32)` | Yes | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | `integer (int32)` | Yes | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `totalCount` | `integer (int64)` | Yes | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | No further constraint recorded |
| `averageStars` | `number (double)` | Yes | Not declared nullable | Numeric average stars for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `starCounts` | [DriverReviewStarCountDto](d.md#driverreviewstarcountdto)[] | Yes | Not declared nullable | Collection of star counts for this model; interpret each item through the declared item type. | No further constraint recorded |
| `categories` | [DriverReviewCategoryDto](d.md#driverreviewcategorydto)[] | Yes | Not declared nullable | Collection of categories for this model; interpret each item through the declared item type. | No further constraint recorded |
| `totalPages` | `integer (int32)` | No | Not declared nullable | Number of pages represented by this page-number model. | readOnly: `True` |
| `hasPreviousPage` | `boolean` | No | Not declared nullable | Whether has previous page applies in this model's context. This flag does not replace server permission or lifecycle checks. | readOnly: `True` |
| `hasNextPage` | `boolean` | No | Not declared nullable | Whether has next page applies in this model's context. This flag does not replace server permission or lifecycle checks. | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## DriverRideAlertPreferencesDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `isEnabled` | `boolean` | Yes | Not declared nullable | Whether is enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `minimumFareMinor` | `integer (int64)` | No | Explicitly allowed | Minimum fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `maximumFareMinor` | `integer (int64)` | No | Explicitly allowed | Maximum fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `maximumTripDistanceMeters` | `integer (int32)` | No | Explicitly allowed | Maximum trip distance, measured in metres. | No further constraint recorded |
| `standardTrips` | `boolean` | Yes | Not declared nullable | Whether standard trips applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `airportTrips` | `boolean` | Yes | Not declared nullable | Whether airport trips applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `petFriendlyTrips` | `boolean` | Yes | Not declared nullable | Whether pet friendly trips applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `childSeatTrips` | `boolean` | Yes | Not declared nullable | Whether child seat trips applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `wheelchairAccessibleTrips` | `boolean` | Yes | Not declared nullable | Whether wheelchair accessible trips applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `vehicleCategoryIds` | `string (uuid)[]` | Yes | Not declared nullable | Identifiers of the related vehicle category records; each remains subject to scope/relationship checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverRideOfferDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `vehicleCategoryName` | `string` | Yes | Not declared nullable | Vehicle category name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `pickupAddress` | `string` | Yes | Not declared nullable | Human pickup-address text accompanying the structured location. | No further constraint recorded |
| `pickupLatitude` | `number (double)` | Yes | Not declared nullable | Pickup latitude in degrees; latitude is separate from address text. | No further constraint recorded |
| `pickupLongitude` | `number (double)` | Yes | Not declared nullable | Pickup longitude in degrees; preserve coordinate order. | No further constraint recorded |
| `dropoffAddress` | `string` | Yes | Not declared nullable | Human destination-address text accompanying the structured location. | No further constraint recorded |
| `distanceMeters` | `integer (int32)` | Yes | Not declared nullable | Distance represented by this model, in metres; its source/assessment depends on the operation. | No further constraint recorded |
| `estimatedDurationSeconds` | `integer (int32)` | Yes | Not declared nullable | Estimated duration in seconds; an estimate is not actual elapsed trip time. | No further constraint recorded |
| `proposedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Rider's proposed fare in currency minor units, subject to applicable quote and marketplace rules. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `paymentMethod` | [PaymentMethod](p.md#paymentmethod) | Yes | Not declared nullable | Payment method enum; availability and settlement rules are checked separately. | No further constraint recorded |
| `passengerCount` | `integer (int32)` | Yes | Not declared nullable | Number of passenger in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | No further constraint recorded |
| `scheduledForUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for scheduled for; parse strictly and localize only for display. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `riderScore` | `number (double)` | Yes | Not declared nullable | Numeric rider score for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `riderRatingCount` | `integer (int32)` | Yes | Not declared nullable | Number of rider rating in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `stops` | [RideStopDto](r.md#ridestopdto)[] | No | Explicitly allowed | Ordered journey/delivery stops in the referenced stop model. | No further constraint recorded |
| `petFriendlyRequired` | `boolean` | No | Not declared nullable | Whether pet friendly required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `childSeatRequired` | `boolean` | No | Not declared nullable | Whether child seat required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `childSeatCount` | `integer (int32)` | No | Not declared nullable | Number of child seat in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `wheelchairAccessibleRequired` | `boolean` | No | Not declared nullable | Whether wheelchair accessible required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `airportPickup` | `boolean` | No | Not declared nullable | Whether airport pickup applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `flightNumber` | `string` | No | Explicitly allowed | Flight number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `dispatchMode` | [RideDispatchMode](r.md#ridedispatchmode) | No | Not declared nullable | Dispatch mode represented by the `RideDispatchMode` model or enum; use that definition's fields/values. | No further constraint recorded |
| `currentBidId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related current bid record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `currentBidStatus` | [BidStatus](b.md#bidstatus) | No | Not declared nullable | Current bid status represented by the `BidStatus` model or enum; use that definition's fields/values. | No further constraint recorded |
| `currentBidAmountMinor` | `integer (int64)` | No | Explicitly allowed | Current bid amount in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currentBidVersion` | `integer (int64)` | No | Explicitly allowed | Current bid version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `lifecycleVersion` | `integer (int64)` | No | Not declared nullable | Lifecycle version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `productType` | [RideProductType](r.md#rideproducttype) | No | Not declared nullable | Product type represented by the `RideProductType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `bookedHourlyMinutes` | `integer (int32)` | No | Not declared nullable | Booked hourly, measured in minutes. | No further constraint recorded |
| `plannedWaitingSeconds` | `integer (int32)` | No | Not declared nullable | Planned waiting, measured in seconds. | No further constraint recorded |
| `riderCompletedTrips` | `integer (int32)` | No | Not declared nullable | Numeric rider completed trips for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `riderCategories` | [ReputationCategoryDto](r.md#reputationcategorydto)[] | No | Explicitly allowed | Collection of rider categories for this model; interpret each item through the declared item type. | No further constraint recorded |
| `riderAchievements` | `string[]` | No | Explicitly allowed | Collection of rider achievements for this model; interpret each item through the declared item type. | No further constraint recorded |
| `assistance` | [RideAssistanceDto](r.md#rideassistancedto) | No | Not declared nullable | Assistance represented by the `RideAssistanceDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `exactLocationAvailable` | `boolean` | No | Not declared nullable | Whether exact location available applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `pickupDistanceMeters` | `integer (int32)` | No | Explicitly allowed | Pickup distance, measured in metres. | No further constraint recorded |
| `pickupDistanceSampledAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for pickup distance sampled at; parse strictly and localize only for display. | No further constraint recorded |
| `suggestedFareMinor` | `integer (int64)` | No | Explicitly allowed | Suggested fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `fareRange` | [DriverFareRangeDto](d.md#driverfarerangedto) | No | Not declared nullable | Fare range represented by the `DriverFareRangeDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `dropoffLatitude` | `number (double)` | No | Explicitly allowed | Destination latitude in degrees. | No further constraint recorded |
| `dropoffLongitude` | `number (double)` | No | Explicitly allowed | Destination longitude in degrees. | No further constraint recorded |
| `pickupEtaSeconds` | `integer (int32)` | No | Explicitly allowed | Pickup eta, measured in seconds. | No further constraint recorded |
| `earnings` | [DriverOfferEarningsDto](d.md#driverofferearningsdto) | No | Not declared nullable | Earnings represented by the `DriverOfferEarningsDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `paymentEvidence` | [DriverOfferPaymentEvidenceDto](d.md#driverofferpaymentevidencedto) | No | Not declared nullable | Payment evidence represented by the `DriverOfferPaymentEvidenceDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `gate` | [DriverOfferGateDto](d.md#driveroffergatedto) | No | Not declared nullable | Gate represented by the `DriverOfferGateDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `freshness` | [DriverOfferFreshnessDto](d.md#driverofferfreshnessdto) | No | Not declared nullable | Freshness represented by the `DriverOfferFreshnessDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `rankingReasons` | `string[]` | No | Explicitly allowed | Collection of ranking reasons for this model; interpret each item through the declared item type. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverRideOfferDtoPagedResult

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `items` | [DriverRideOfferDto](d.md#driverrideofferdto)[] | No | Explicitly allowed | Records returned in this collection/page, each using the referenced item model. | No further constraint recorded |
| `page` | `integer (int32)` | No | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | `integer (int32)` | No | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `totalCount` | `integer (int64)` | No | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | No further constraint recorded |
| `totalPages` | `integer (int32)` | No | Not declared nullable | Number of pages represented by this page-number model. | readOnly: `True` |
| `hasPreviousPage` | `boolean` | No | Not declared nullable | Whether has previous page applies in this model's context. This flag does not replace server permission or lifecycle checks. | readOnly: `True` |
| `hasNextPage` | `boolean` | No | Not declared nullable | Whether has next page applies in this model's context. This flag does not replace server permission or lifecycle checks. | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## DriverRideOfferSeekPageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `items` | [DriverRideOfferDto](d.md#driverrideofferdto)[] | Yes | Not declared nullable | Records returned in this collection/page, each using the referenced item model. | No further constraint recorded |
| `pageSize` | `integer (int32)` | Yes | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `hasMore` | `boolean` | Yes | Not declared nullable | Whether the seek-paged result indicates more records after this page. | No further constraint recorded |
| `nextCursor` | `string` | No | Explicitly allowed | Opaque, scope-bound continuation token; preserve it unchanged and reset it when filters/context change. | No further constraint recorded |
| `snapshotAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for snapshot at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverRiderFavoriteDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `riderUserId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related rider user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverRouteEarningsEstimateDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `fareMinor` | `integer (int64)` | Yes | Not declared nullable | Fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `commissionMinor` | `integer (int64)` | Yes | Not declared nullable | Commission in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `driverNetBeforeCostsMinor` | `integer (int64)` | Yes | Not declared nullable | Driver net before costs in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverRoutePointDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | No further constraint recorded |
| `label` | `string` | Yes | Not declared nullable | Label text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverRoutePreviewDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `rideRequestId` | `string (uuid)` | Yes | Not declared nullable | Rider request record, distinct from an accepted trip. | No further constraint recorded |
| `lifecycleVersion` | `integer (int64)` | Yes | Not declared nullable | Lifecycle version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `exactLocationAvailable` | `boolean` | Yes | Not declared nullable | Whether exact location available applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `stops` | [DriverRoutePointDto](d.md#driverroutepointdto)[] | Yes | Not declared nullable | Ordered journey/delivery stops in the referenced stop model. | No further constraint recorded |
| `driverOrigin` | [DriverRoutePointDto](d.md#driverroutepointdto) | No | Not declared nullable | Driver origin represented by the `DriverRoutePointDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `driverLocationAgeSeconds` | `integer (int32)` | No | Explicitly allowed | Driver location age, measured in seconds. | No further constraint recorded |
| `driverLocationAccuracyMeters` | `number (double)` | No | Explicitly allowed | Driver location accuracy, measured in metres. | No further constraint recorded |
| `approach` | [DriverRouteSegmentDto](d.md#driverroutesegmentdto) | Yes | Not declared nullable | Approach represented by the `DriverRouteSegmentDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `journey` | [DriverRouteSegmentDto](d.md#driverroutesegmentdto) | Yes | Not declared nullable | Journey represented by the `DriverRouteSegmentDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `retrievedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for retrieved at; parse strictly and localize only for display. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `scheduledForUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for scheduled for; parse strictly and localize only for display. | No further constraint recorded |
| `proposedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Rider's proposed fare in currency minor units, subject to applicable quote and marketplace rules. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `earningsEstimate` | [DriverRouteEarningsEstimateDto](d.md#driverrouteearningsestimatedto) | No | Not declared nullable | Earnings estimate represented by the `DriverRouteEarningsEstimateDto` model or enum; use that definition's fields/values. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverRouteSegmentDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `kind` | `string` | Yes | Not declared nullable | Kind text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `distanceMeters` | `integer (int32)` | No | Explicitly allowed | Distance represented by this model, in metres; its source/assessment depends on the operation. | No further constraint recorded |
| `durationSeconds` | `integer (int32)` | No | Explicitly allowed | Duration, measured in seconds. | No further constraint recorded |
| `polyline` | `string` | No | Explicitly allowed | Polyline text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `roadRouteAvailable` | `boolean` | Yes | Not declared nullable | Whether road route available applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `source` | `string` | Yes | Not declared nullable | Source text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | PendingApproval | Pending approval state/choice in this specific enum. |
| `2` | Active | Active state/choice in this specific enum. |
| `3` | Suspended | Suspended state/choice in this specific enum. |
| `4` | Rejected | Rejected state/choice in this specific enum. |

## DriverStatusRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `isOnline` | `boolean` | Yes | Not declared nullable | Whether is online applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `latitude` | `number (double)` | No | Explicitly allowed | Latitude in degrees for the location represented by this model. | No further constraint recorded |
| `longitude` | `number (double)` | No | Explicitly allowed | Longitude in degrees for the location represented by this model. | No further constraint recorded |
| `accuracyMeters` | `number (double)` | No | Explicitly allowed | Accuracy, measured in metres. | No further constraint recorded |
| `speedMetersPerSecond` | `number (double)` | No | Explicitly allowed | Numeric speed meters per second for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `headingDegrees` | `number (double)` | No | Explicitly allowed | Numeric heading degrees for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverTrustAchievementDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `evidence` | `string` | Yes | Not declared nullable | Evidence text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `evidenceCount` | `integer (int32)` | Yes | Not declared nullable | Number of evidence in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `earnedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for earned at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## DriverTrustLevel

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`, `4`, `5`, `6`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | AllDrivers | All drivers state/choice in this specific enum. |
| `1` | IdentityVerified | Identity verified state/choice in this specific enum. |
| `2` | IdentityAndAddressVerified | Identity and address verified state/choice in this specific enum. |
| `3` | VehicleInsuranceVerified | Vehicle insurance verified state/choice in this specific enum. |
| `4` | MultipleRatings | Multiple ratings state/choice in this specific enum. |
| `5` | FullyVerified | Fully verified state/choice in this specific enum. |
| `6` | PreferredDriver | Preferred driver state/choice in this specific enum. |

## DriverTrustProfileDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `verifiedKiloDriveTrips` | `integer (int32)` | Yes | Not declared nullable | Numeric verified kilo drive trips for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `reliabilityMonths` | `integer (int32)` | Yes | Not declared nullable | Numeric reliability months for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `identityVerified` | `boolean` | Yes | Not declared nullable | Whether identity verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `primaryVehicleVerified` | `boolean` | Yes | Not declared nullable | Whether primary vehicle verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `documentsCurrent` | `boolean` | Yes | Not declared nullable | Whether documents current applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `achievements` | [DriverTrustAchievementDto](d.md#drivertrustachievementdto)[] | Yes | Not declared nullable | Collection of achievements for this model; interpret each item through the declared item type. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
