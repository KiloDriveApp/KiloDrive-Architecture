# Field dictionary: M

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

## MaintenanceStatusResult

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `status` | [VehicleMaintenanceStatus](v.md#vehiclemaintenancestatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `dueAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for due at; parse strictly and localize only for display. | No further constraint recorded |
| `dueOdometer` | `number (double)` | No | Explicitly allowed | Numeric due odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `daysRemaining` | `integer (int32)` | No | Explicitly allowed | Numeric days remaining for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `distanceRemaining` | `number (double)` | No | Explicitly allowed | Numeric distance remaining for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `triggeringLimit` | [VehicleMaintenanceTrigger](v.md#vehiclemaintenancetrigger) | Yes | Not declared nullable | Triggering limit represented by the `VehicleMaintenanceTrigger` model or enum; use that definition's fields/values. | No further constraint recorded |
| `severity` | [VehicleMaintenanceSeverity](v.md#vehiclemaintenanceseverity) | Yes | Not declared nullable | Severity represented by the `VehicleMaintenanceSeverity` model or enum; use that definition's fields/values. | No further constraint recorded |
| `recommendedAction` | `string` | Yes | Not declared nullable | Recommended action text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MarketplaceFareGuidanceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `fareRange` | [MarketplaceFareRangeDto](m.md#marketplacefarerangedto) | Yes | Not declared nullable | Fare range represented by the `MarketplaceFareRangeDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `pickupEstimate` | [MarketplacePickupEstimateDto](m.md#marketplacepickupestimatedto) | Yes | Not declared nullable | Pickup estimate represented by the `MarketplacePickupEstimateDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `offerScenarios` | [MarketplaceOfferScenarioDto](m.md#marketplaceofferscenariodto)[] | Yes | Not declared nullable | Collection of offer scenarios for this model; interpret each item through the declared item type. | No further constraint recorded |
| `disclosure` | `string` | Yes | Not declared nullable | Disclosure text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MarketplaceFareRangeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `minimumMinor` | `integer (int64)` | Yes | Not declared nullable | Minimum in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `recommendedMinor` | `integer (int64)` | Yes | Not declared nullable | Recommended in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `maximumMinor` | `integer (int64)` | Yes | Not declared nullable | Maximum in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MarketplaceOfferScenarioDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `fareMinor` | `integer (int64)` | Yes | Not declared nullable | Fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `pickupProbabilityPercent` | `integer (int32)` | Yes | Not declared nullable | Numeric pickup probability percent for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `probabilityLowPercent` | `integer (int32)` | Yes | Not declared nullable | Numeric probability low percent for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `probabilityHighPercent` | `integer (int32)` | Yes | Not declared nullable | Numeric probability high percent for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `estimatedResponseSecondsLow` | `integer (int32)` | Yes | Not declared nullable | Numeric estimated response seconds low for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `estimatedResponseSecondsHigh` | `integer (int32)` | Yes | Not declared nullable | Numeric estimated response seconds high for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MarketplacePickupEstimateDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `probabilityPercent` | `integer (int32)` | Yes | Not declared nullable | Numeric probability percent for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `probabilityLowPercent` | `integer (int32)` | Yes | Not declared nullable | Numeric probability low percent for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `probabilityHighPercent` | `integer (int32)` | Yes | Not declared nullable | Numeric probability high percent for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `likelihood` | `string` | Yes | Not declared nullable | Likelihood text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `estimatedResponseSecondsLow` | `integer (int32)` | Yes | Not declared nullable | Numeric estimated response seconds low for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `estimatedResponseSecondsHigh` | `integer (int32)` | Yes | Not declared nullable | Numeric estimated response seconds high for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `supplyLevel` | `string` | Yes | Not declared nullable | Supply level text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `demandLevel` | `string` | Yes | Not declared nullable | Demand level text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `confidence` | `string` | Yes | Not declared nullable | Confidence text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `historicalSampleSize` | `integer (int32)` | Yes | Not declared nullable | Numeric historical sample size for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `asOfUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for as of; parse strictly and localize only for display. | No further constraint recorded |
| `scheduledEstimate` | `boolean` | Yes | Not declared nullable | Whether scheduled estimate applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `modelVersion` | `string` | Yes | Not declared nullable | Model version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `signals` | `string[]` | Yes | Not declared nullable | Collection of signals for this model; interpret each item through the declared item type. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MembershipCheckoutDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `paymentId` | `string (uuid)` | Yes | Not declared nullable | Server-owned payment record used for state/reconciliation. | No further constraint recorded |
| `provider` | `string` | Yes | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `checkoutUrl` | `string` | No | Explicitly allowed | URL for checkout; validate the intended origin/access and never assume private links are public. | No further constraint recorded |
| `instructions` | `string` | No | Explicitly allowed | Instructions text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MembershipCheckoutRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `planId` | `string (uuid)` | Yes | Not declared nullable | Membership catalog record; it does not itself prove a user entitlement. | No further constraint recorded |
| `termDays` | `integer (int32)` | Yes | Not declared nullable | Requested/applicable membership term in days; only configured valid terms are allowed. | No further constraint recorded |
| `provider` | `string` | Yes | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MembershipLifecycleDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `summary` | `string` | Yes | Not declared nullable | Summary text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `assessedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for assessed at; parse strictly and localize only for display. | No further constraint recorded |
| `effectiveAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for effective at; parse strictly and localize only for display. | No further constraint recorded |
| `endsAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for ends at; parse strictly and localize only for display. | No further constraint recorded |
| `benefitsRetained` | `boolean` | Yes | Not declared nullable | Whether benefits retained applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `benefitsRetainedUntilUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for benefits retained until; parse strictly and localize only for display. | No further constraint recorded |
| `actionCode` | `string` | Yes | Not declared nullable | Action code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `restoreAvailable` | `boolean` | Yes | Not declared nullable | Whether restore available applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `isKnown` | `boolean` | Yes | Not declared nullable | Whether is known applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `timeline` | [MembershipLifecycleTimelineItemDto](m.md#membershiplifecycletimelineitemdto)[] | Yes | Not declared nullable | Collection of timeline for this model; interpret each item through the declared item type. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MembershipLifecycleTimelineItemDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `summary` | `string` | Yes | Not declared nullable | Summary text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `occurredAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for occurred at; parse strictly and localize only for display. | No further constraint recorded |
| `effectiveAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for effective at; parse strictly and localize only for display. | No further constraint recorded |
| `endsAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for ends at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MembershipPeriodDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `planId` | `string (uuid)` | No | Explicitly allowed | Membership catalog record; it does not itself prove a user entitlement. | No further constraint recorded |
| `planName` | `string` | No | Explicitly allowed | Human plan name; use plan/entitlement records for identity and authority. | No further constraint recorded |
| `startsAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for starts at; parse strictly and localize only for display. | No further constraint recorded |
| `endsAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for ends at; parse strictly and localize only for display. | No further constraint recorded |
| `accessThroughUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for access through; parse strictly and localize only for display. | No further constraint recorded |
| `source` | `string` | Yes | Not declared nullable | Source text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MembershipPlanDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `audience` | `string` | Yes | Not declared nullable | Applicable product/client audience, distinct from verified security authority. | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | No further constraint recorded |
| `feeMinor` | `integer (int64)` | Yes | Not declared nullable | Fee for the applicable default product/plan period, in the stated currency's integer minor units. | No further constraint recorded |
| `periodDays` | `integer (int32)` | Yes | Not declared nullable | Duration of this catalog plan's default period, expressed in days. | No further constraint recorded |
| `weeklyFeeMinor` | `integer (int64)` | No | Explicitly allowed | Catalog price for the weekly term in currency minor units; availability still depends on the configured offer. | No further constraint recorded |
| `monthlyFeeMinor` | `integer (int64)` | No | Explicitly allowed | Catalog price for the monthly term in currency minor units. | No further constraint recorded |
| `threeMonthFeeMinor` | `integer (int64)` | No | Explicitly allowed | Catalog price for the three-month term in currency minor units. | No further constraint recorded |
| `sixMonthFeeMinor` | `integer (int64)` | No | Explicitly allowed | Catalog price for the six-month term in currency minor units. | No further constraint recorded |
| `annualFeeMinor` | `integer (int64)` | No | Explicitly allowed | Catalog price for the annual term in currency minor units. | No further constraint recorded |
| `maxBidsPerDay` | `integer (int32)` | Yes | Not declared nullable | Plan allotment for new bids in the server-defined daily usage period; re-bid rules are separate. | No further constraint recorded |
| `maxVehicleChangesPerPeriod` | `integer (int32)` | Yes | Not declared nullable | Plan's vehicle-change allotment for its usage period; assignment and verification checks still apply. | No further constraint recorded |
| `maxRegisteredVehicles` | `integer (int32)` | Yes | Not declared nullable | Legacy plan metadata; it must not cap account-owned vehicle storage or Maintenance Center access. | No further constraint recorded |
| `maxFavorites` | `integer (int32)` | Yes | Not declared nullable | Plan's applicable saved-favorite allotment; ownership and feature policy still apply. | No further constraint recorded |
| `canUseBlockList` | `boolean` | Yes | Not declared nullable | Whether can use block list applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `canFavoriteRiders` | `boolean` | Yes | Not declared nullable | Whether can favorite riders applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `canReceiveReviews` | `boolean` | Yes | Not declared nullable | Whether can receive reviews applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `maxAcceptedRidesPerMonth` | `integer (int32)` | No | Explicitly allowed | Catalog allotment for accepted rides in the applicable monthly period; use authoritative usage/readiness checks. | No further constraint recorded |
| `maxAcceptedTripsPerWeek` | `integer (int32)` | No | Explicitly allowed | Catalog allotment for accepted trips in the applicable weekly period; use authoritative usage/readiness checks. | No further constraint recorded |
| `minWithdrawalMinor` | `integer (int64)` | Yes | Not declared nullable | Applicable lower withdrawal bound in currency minor units; read current cashout limits before requesting. | No further constraint recorded |
| `maxWithdrawalMinor` | `integer (int64)` | No | Explicitly allowed | Applicable upper withdrawal bound in currency minor units; current server limits remain authoritative. | No further constraint recorded |
| `sortOrder` | `integer (int32)` | Yes | Not declared nullable | Numeric sort order for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `baseCurrency` | `string` | Yes | Not declared nullable | Currency of the catalog/quote's base amount, distinct from the displayed local currency. | No further constraint recorded |
| `fxRateFromBase` | `number (double)` | Yes | Not declared nullable | Reference conversion rate from the base currency; executable prices come from the server's reviewed quote. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MembershipPriceTermEvidenceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `termDays` | `integer (int32)` | No | Explicitly allowed | Requested/applicable membership term in days; only configured valid terms are allowed. | No further constraint recorded |
| `priceMinor` | `integer (int64)` | No | Explicitly allowed | Price in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | No | Explicitly allowed | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `source` | `string` | Yes | Not declared nullable | Source text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `provider` | `string` | No | Explicitly allowed | Configured provider selector for this operation; a named provider is not proof of readiness. | No further constraint recorded |
| `observedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for observed at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MembershipSafeActionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `deepLink` | `string` | Yes | Not declared nullable | Deep link text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `retryable` | `boolean` | Yes | Not declared nullable | Whether the error permits an applicable retry; it does not authorize a blind second mutation. | No further constraint recorded |
| `earliestRetryAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for earliest retry at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MembershipStoreStatusDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `currentPlanId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related current plan record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `currentPlanName` | `string` | No | Explicitly allowed | Current plan name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `termDays` | `integer (int32)` | No | Explicitly allowed | Requested/applicable membership term in days; only configured valid terms are allowed. | No further constraint recorded |
| `lifecycleState` | `string` | Yes | Not declared nullable | Lifecycle state text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `benefitsActive` | `boolean` | Yes | Not declared nullable | Whether benefits active applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `startsAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for starts at; parse strictly and localize only for display. | No further constraint recorded |
| `accessThroughUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for access through; parse strictly and localize only for display. | No further constraint recorded |
| `providerConfirmedExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for provider confirmed expires at; parse strictly and localize only for display. | No further constraint recorded |
| `renewalStatus` | `string` | Yes | Not declared nullable | Renewal status text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `nextChargeAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for next charge at; parse strictly and localize only for display. | No further constraint recorded |
| `provider` | `string` | Yes | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | No further constraint recorded |
| `source` | `string` | Yes | Not declared nullable | Source text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `usage` | [MembershipUsageDto](m.md#membershipusagedto) | Yes | Not declared nullable | Current benefit consumption/allotment model; plan definition and consumed usage are different facts. | No further constraint recorded |
| `nextReset` | [MembershipUsageResetDto](m.md#membershipusageresetdto) | No | Not declared nullable | Next benefit-usage reset information; it is not automatically membership expiry. | No further constraint recorded |
| `pendingChange` | [PendingMembershipChangeDto](p.md#pendingmembershipchangedto) | No | Not declared nullable | Scheduled or pending membership change, distinct from the currently effective entitlement. | No further constraint recorded |
| `lastSuccessfulProviderCheckAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last successful provider check at; parse strictly and localize only for display. | No further constraint recorded |
| `nextReconciliationAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for next reconciliation at; parse strictly and localize only for display. | No further constraint recorded |
| `isChecking` | `boolean` | Yes | Not declared nullable | Whether is checking applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `requiresManualReview` | `boolean` | Yes | Not declared nullable | Whether requires manual review applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `reasonCode` | `string` | Yes | Not declared nullable | Stable reason code; map through the applicable reason catalog instead of displaying an unrelated enum. | No further constraint recorded |
| `stateRevision` | `integer (int64)` | Yes | Not declared nullable | Revision of the returned state snapshot, distinct from a display timestamp. | No further constraint recorded |
| `policyRevision` | `integer (int64)` | Yes | Not declared nullable | Policy revision for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `supportReference` | `string` | Yes | Not declared nullable | Support reference text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `safeAction` | [MembershipSafeActionDto](m.md#membershipsafeactiondto) | Yes | Not declared nullable | Server guidance for safe recovery; preserve operation evidence before retrying. | No further constraint recorded |
| `renewalPriceEvidence` | [MembershipPriceTermEvidenceDto](m.md#membershippricetermevidencedto) | No | Not declared nullable | Renewal price evidence represented by the `MembershipPriceTermEvidenceDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `cancellationPolicyCode` | `string` | No | Explicitly allowed | Cancellation policy code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MembershipUsageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `acceptedTripsThisWeek` | `integer (int32)` | Yes | Not declared nullable | Numeric accepted trips this week for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `maxAcceptedTripsPerWeek` | `integer (int32)` | No | Explicitly allowed | Catalog allotment for accepted trips in the applicable weekly period; use authoritative usage/readiness checks. | No further constraint recorded |
| `bidsToday` | `integer (int32)` | Yes | Not declared nullable | Numeric bids today for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `maxBidsPerDay` | `integer (int32)` | No | Explicitly allowed | Plan allotment for new bids in the server-defined daily usage period; re-bid rules are separate. | No further constraint recorded |
| `vehicleChangesUsed` | `integer (int32)` | Yes | Not declared nullable | Numeric vehicle changes used for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `maxVehicleChangesPerPeriod` | `integer (int32)` | No | Explicitly allowed | Plan's vehicle-change allotment for its usage period; assignment and verification checks still apply. | No further constraint recorded |
| `vehicleCount` | `integer (int32)` | Yes | Not declared nullable | Number of vehicle in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `maxRegisteredVehicles` | `integer (int32)` | No | Explicitly allowed | Legacy plan metadata; it must not cap account-owned vehicle storage or Maintenance Center access. | No further constraint recorded |
| `favoritesUsed` | `integer (int32)` | Yes | Not declared nullable | Numeric favorites used for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `maxFavorites` | `integer (int32)` | No | Explicitly allowed | Plan's applicable saved-favorite allotment; ownership and feature policy still apply. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MembershipUsageResetDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `bidsResetAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for bids reset at; parse strictly and localize only for display. | No further constraint recorded |
| `acceptedTripsResetAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for accepted trips reset at; parse strictly and localize only for display. | No further constraint recorded |
| `vehicleChangesResetAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for vehicle changes reset at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MoneyCommandOutcome

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`, `4`, `5`, `6`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Missing | Missing state/choice in this specific enum. |
| `1` | Processing | Processing state/choice in this specific enum. |
| `2` | Replayable | Replayable state/choice in this specific enum. |
| `3` | NeedsReview | Needs review state/choice in this specific enum. |
| `4` | Succeeded | Succeeded state/choice in this specific enum. |
| `5` | Rejected | Rejected state/choice in this specific enum. |
| `6` | NoMutation | No mutation state/choice in this specific enum. |

## MoneyCommandRecoveryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `outcome` | [MoneyCommandOutcome](m.md#moneycommandoutcome) | Yes | Not declared nullable | Result/recovery state of this operation; unknown or pending is not failed or successful. | No further constraint recorded |
| `responseStatusCode` | `integer (int32)` | No | Explicitly allowed | Recorded HTTP result status for the operation when available. | No further constraint recorded |
| `noMutation` | `boolean` | No | Not declared nullable | Explicit server evidence that no domain/provider mutation occurred; absence is not equivalent proof. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## MyMembershipDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `planId` | `string (uuid)` | No | Explicitly allowed | Membership catalog record; it does not itself prove a user entitlement. | No further constraint recorded |
| `planName` | `string` | No | Explicitly allowed | Human plan name; use plan/entitlement records for identity and authority. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | No further constraint recorded |
| `usage` | [MembershipUsageDto](m.md#membershipusagedto) | Yes | Not declared nullable | Current benefit consumption/allotment model; plan definition and consumed usage are different facts. | No further constraint recorded |
| `autoRenew` | `boolean` | No | Not declared nullable | Membership renewal preference/state for this model; it does not itself prove the next charge will succeed. | No further constraint recorded |
| `upgradeCreditMinor` | `integer (int64)` | No | Not declared nullable | Server-calculated unused-value upgrade credit in currency minor units. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `currentPeriod` | [MembershipPeriodDto](m.md#membershipperioddto) | No | Not declared nullable | Current authoritative membership usage/entitlement period model. | No further constraint recorded |
| `accessThroughUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for access through; parse strictly and localize only for display. | No further constraint recorded |
| `pendingChange` | [PendingMembershipChangeDto](p.md#pendingmembershipchangedto) | No | Not declared nullable | Scheduled or pending membership change, distinct from the currently effective entitlement. | No further constraint recorded |
| `nextReset` | [MembershipUsageResetDto](m.md#membershipusageresetdto) | No | Not declared nullable | Next benefit-usage reset information; it is not automatically membership expiry. | No further constraint recorded |
| `priceTermEvidence` | [MembershipPriceTermEvidenceDto](m.md#membershippricetermevidencedto) | No | Not declared nullable | Evidence of the accepted price/term mapping used by the membership lifecycle. | No further constraint recorded |
| `lifecycleReasonCode` | `string` | No | Explicitly allowed | Reason for the current membership lifecycle state; render through its contract vocabulary. | No further constraint recorded |
| `safeAction` | [MembershipSafeActionDto](m.md#membershipsafeactiondto) | No | Not declared nullable | Server guidance for safe recovery; preserve operation evidence before retrying. | No further constraint recorded |
| `lifecycle` | [MembershipLifecycleDto](m.md#membershiplifecycledto) | No | Not declared nullable | Lifecycle represented by the `MembershipLifecycleDto` model or enum; use that definition's fields/values. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
