# Field dictionary: T

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

The explanation basis distinguishes model-specific meaning, shared conventions,
name-derived units and type-only entries awaiting semantic review. See the
[coverage report](../reference/coverage.md); field presence is not semantic completeness.

## Models on this page

- [TollEstimateDto](#tollestimatedto)
- [TollJourneyOptionDto](#tolljourneyoptiondto)
- [TollPlazaChargeDto](#tollplazachargedto)
- [TollPlazaDto](#tollplazadto)
- [TollPricingPeriodDto](#tollpricingperioddto)
- [TollRouteEstimateDto](#tollrouteestimatedto)
- [TollRouteEstimateRequest](#tollrouteestimaterequest)
- [TollRouteLegDto](#tollroutelegdto)
- [TollRoutePointDto](#tollroutepointdto)
- [TollRouteSegmentDto](#tollroutesegmentdto)
- [TopUpLimitsDto](#topuplimitsdto)
- [TopUpQuoteDto](#topupquotedto)
- [TopUpResultDto](#topupresultdto)
- [TopUpWalletDto](#topupwalletdto)
- [TravelBookingPartiesDto](#travelbookingpartiesdto)
- [TravelBookingPartyDto](#travelbookingpartydto)
- [TravelCostCenterDto](#travelcostcenterdto)
- [TravelMemberDto](#travelmemberdto)
- [TravelProfileSummaryDto](#travelprofilesummarydto)
- [TravelProfileWorkspaceDto](#travelprofileworkspacedto)
- [TravelRideBookingDto](#travelridebookingdto)
- [TravelRidePolicyDto](#travelridepolicydto)
- [TravelStatementDto](#travelstatementdto)
- [TravelTrackingDto](#traveltrackingdto)
- [TravelTripDto](#traveltripdto)
- [TravelTripReceiptDto](#traveltripreceiptdto)
- [TripCallLogDto](#tripcalllogdto)
- [TripChatDto](#tripchatdto)
- [TripChatMutationDto](#tripchatmutationdto)
- [TripCustomerStatusDto](#tripcustomerstatusdto)
- [TripDistanceProvenance](#tripdistanceprovenance)
- [TripDistanceSummaryDto](#tripdistancesummarydto)
- [TripDto](#tripdto)
- [TripDtoPagedResult](#tripdtopagedresult)
- [TripHistorySeekPageDto](#triphistoryseekpagedto)
- [TripLifecycleEvidenceDto](#triplifecycleevidencedto)
- [TripLocationPolicyDto](#triplocationpolicydto)
- [TripLocationStatusDto](#triplocationstatusdto)
- [TripPickupCeremonyStatusDto](#trippickupceremonystatusdto)
- [TripPickupCodeDto](#trippickupcodedto)
- [TripReceiptDto](#tripreceiptdto)
- [TripRouteAlterationDto](#triproutealterationdto)
- [TripRouteProposalSnapshotDto](#triprouteproposalsnapshotdto)
- [TripShareDto](#tripsharedto)
- [TripStatus](#tripstatus)
- [TripStopTransitionRequest](#tripstoptransitionrequest)
- [TripTerminationDto](#tripterminationdto)
- [TripTerminationRequest](#tripterminationrequest)
- [TripTimelineDto](#triptimelinedto)
- [TripTimelineEventDto](#triptimelineeventdto)
- [TripTimelineEvidenceLinkDto](#triptimelineevidencelinkdto)
- [TripTipDto](#triptipdto)
- [TrustedContactRequest](#trustedcontactrequest)
- [TwoFactorCodeRequest](#twofactorcoderequest)
- [TwoFactorConfirmedDto](#twofactorconfirmeddto)
- [TwoFactorEnrollmentDto](#twofactorenrollmentdto)
- [TwoFactorStatusDto](#twofactorstatusdto)
- [TwoFactorStepUpDto](#twofactorstepupdto)

## TollEstimateDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `corridorCode` | `string` | Yes | Not declared nullable | Corridor code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `corridorName` | `string` | Yes | Not declared nullable | Corridor name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `originName` | `string` | Yes | Not declared nullable | Origin name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `destinationName` | `string` | Yes | Not declared nullable | Destination name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `vehicleClass` | `integer (int32)` | Yes | Not declared nullable | Numeric vehicle class for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `oneWayKilometers` | `number (double)` | Yes | Not declared nullable | Numeric one way kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `oneWayMiles` | `number (double)` | Yes | Not declared nullable | Numeric one way miles for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `oneWayPlazaCount` | `integer (int32)` | Yes | Not declared nullable | Number of one way plaza in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `outboundCharges` | [TollPlazaChargeDto](t.md#tollplazachargedto)[] | Yes | Not declared nullable | Collection of outbound charges for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `returnCharges` | [TollPlazaChargeDto](t.md#tollplazachargedto)[] | Yes | Not declared nullable | Collection of return charges for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `oneWayAmountMinor` | `integer (int64)` | Yes | Not declared nullable | One way amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `totalAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Total amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `returnTrip` | `boolean` | Yes | Not declared nullable | Whether return trip applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `effectiveFrom` | `string (date)` | Yes | Not declared nullable | Calendar date for effective from; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |
| `sourceUrl` | `string` | Yes | Not declared nullable | URL for source; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `oneWayDistanceAmountMinor` | `integer (int64)` | No | Not declared nullable | One way distance amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `returnDistanceAmountMinor` | `integer (int64)` | No | Not declared nullable | Return distance amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `totalDistanceAmountMinor` | `integer (int64)` | No | Not declared nullable | Total distance amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `grandTotalAmountMinor` | `integer (int64)` | No | Not declared nullable | Grand total amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `costPerKilometerMinor` | `integer (int64)` | No | Explicitly allowed | Cost per kilometer in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TollJourneyOptionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `corridorCode` | `string` | Yes | Not declared nullable | Corridor code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `corridorName` | `string` | Yes | Not declared nullable | Corridor name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `originCode` | `string` | Yes | Not declared nullable | Origin code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `originName` | `string` | Yes | Not declared nullable | Origin name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `destinationCode` | `string` | Yes | Not declared nullable | Destination code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `destinationName` | `string` | Yes | Not declared nullable | Destination name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `distanceKilometers` | `number (double)` | Yes | Not declared nullable | Numeric distance kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `vehicleClasses` | `integer (int32)[]` | Yes | Not declared nullable | Collection of vehicle classes for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TollPlazaChargeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `code` | `string` | No | Explicitly allowed | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `latitude` | `number (double)` | No | Explicitly allowed | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | No | Explicitly allowed | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TollPlazaDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `corridorCode` | `string` | Yes | Not declared nullable | Corridor code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `sequence` | `integer (int32)` | Yes | Not declared nullable | Numeric sequence for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TollPricingPeriodDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `effectiveFrom` | `string (date)` | Yes | Not declared nullable | Calendar date for effective from; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |
| `effectiveTo` | `string (date)` | No | Explicitly allowed | Calendar date for effective to; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TollRouteEstimateDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `segments` | [TollRouteSegmentDto](t.md#tollroutesegmentdto)[] | Yes | Not declared nullable | Collection of segments for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `oneWayKilometers` | `number (double)` | Yes | Not declared nullable | Numeric one way kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `oneWayMiles` | `number (double)` | Yes | Not declared nullable | Numeric one way miles for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `oneWayPlazaCount` | `integer (int32)` | Yes | Not declared nullable | Number of one way plaza in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `oneWayAmountMinor` | `integer (int64)` | Yes | Not declared nullable | One way amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `totalAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Total amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `returnTrip` | `boolean` | Yes | Not declared nullable | Whether return trip applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `legs` | [TollRouteLegDto](t.md#tollroutelegdto)[] | No | Explicitly allowed | Collection of legs for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `detectedPlazas` | [TollPlazaDto](t.md#tollplazadto)[] | No | Explicitly allowed | Collection of detected plazas for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `returnKilometers` | `number (double)` | No | Not declared nullable | Numeric return kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `returnMiles` | `number (double)` | No | Not declared nullable | Numeric return miles for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `oneWayDistanceAmountMinor` | `integer (int64)` | No | Not declared nullable | One way distance amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `returnAmountMinor` | `integer (int64)` | No | Not declared nullable | Return amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `returnDistanceAmountMinor` | `integer (int64)` | No | Not declared nullable | Return distance amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `totalDistanceAmountMinor` | `integer (int64)` | No | Not declared nullable | Total distance amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `grandTotalAmountMinor` | `integer (int64)` | No | Not declared nullable | Grand total amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `costPerKilometerMinor` | `integer (int64)` | No | Explicitly allowed | Cost per kilometer in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `returnSegments` | [TollRouteSegmentDto](t.md#tollroutesegmentdto)[] | No | Explicitly allowed | Collection of return segments for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `returnLegs` | [TollRouteLegDto](t.md#tollroutelegdto)[] | No | Explicitly allowed | Collection of return legs for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `pricePeriodFrom` | `string (date)` | No | Explicitly allowed | Calendar date for price period from; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |
| `pricePeriodTo` | `string (date)` | No | Explicitly allowed | Calendar date for price period to; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TollRouteEstimateRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `points` | [TollRoutePointDto](t.md#tollroutepointdto)[] | Yes | Not declared nullable | Collection of points for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `vehicleClass` | `integer (int32)` | Yes | Not declared nullable | Numeric vehicle class for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `returnTrip` | `boolean` | No | Not declared nullable | Whether return trip applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `countryCode` | `string` | No | Explicitly allowed | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `onDate` | `string (date)` | No | Explicitly allowed | Calendar date for on date; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |
| `costPerKilometerMinor` | `integer (int64)` | No | Explicitly allowed | Cost per kilometer in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TollRouteLegDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `fromAddress` | `string` | Yes | Not declared nullable | From address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `toAddress` | `string` | Yes | Not declared nullable | To address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `distanceKilometers` | `number (double)` | Yes | Not declared nullable | Numeric distance kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `distanceMiles` | `number (double)` | Yes | Not declared nullable | Numeric distance miles for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `includesToll` | `boolean` | Yes | Not declared nullable | Whether includes toll applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `tollSegment` | [TollRouteSegmentDto](t.md#tollroutesegmentdto) | No | Not declared nullable | Toll segment represented by the `TollRouteSegmentDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `polyline` | `string` | No | Explicitly allowed | Polyline text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `distanceAmountMinor` | `integer (int64)` | No | Not declared nullable | Distance amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `tollVerificationStatus` | `string` | No | Explicitly allowed | Toll verification status text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TollRoutePointDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `address` | `string` | Yes | Not declared nullable | Address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TollRouteSegmentDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `fromAddress` | `string` | Yes | Not declared nullable | From address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `toAddress` | `string` | Yes | Not declared nullable | To address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `corridorName` | `string` | Yes | Not declared nullable | Corridor name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `entryPlaza` | `string` | Yes | Not declared nullable | Entry plaza text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `exitPlaza` | `string` | Yes | Not declared nullable | Exit plaza text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `distanceKilometers` | `number (double)` | Yes | Not declared nullable | Numeric distance kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `distanceMiles` | `number (double)` | Yes | Not declared nullable | Numeric distance miles for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `charges` | [TollPlazaChargeDto](t.md#tollplazachargedto)[] | Yes | Not declared nullable | Collection of charges for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `returnCharges` | [TollPlazaChargeDto](t.md#tollplazachargedto)[] | No | Explicitly allowed | Collection of return charges for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `distanceAmountMinor` | `integer (int64)` | No | Not declared nullable | Distance amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `grandTotalMinor` | `integer (int64)` | No | Not declared nullable | Grand total in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TopUpLimitsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `provider` | `string` | Yes | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `minimumAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Minimum amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `maximumAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Maximum amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `feeBasisPoints` | `integer (int32)` | No | Not declared nullable | Numeric fee basis points for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `isAvailable` | `boolean` | No | Not declared nullable | Whether is available applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `unavailableReasonCode` | `string` | No | Explicitly allowed | Unavailable reason code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TopUpQuoteDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `quoteToken` | `string` | Yes | Not declared nullable | Server-owned quote evidence; preserve currency/amount/expiry binding and treat it as private. | Shared convention | No further constraint recorded |
| `payAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Pay amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `payCurrency` | `string` | Yes | Not declared nullable | Pay currency text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `walletCreditMinor` | `integer (int64)` | Yes | Not declared nullable | Wallet credit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `walletCurrency` | `string` | Yes | Not declared nullable | Wallet currency text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `providerFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Provider fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `fxFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Fx fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `fxRate` | `number (double)` | Yes | Not declared nullable | Numeric fx rate for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `rateSource` | `string` | Yes | Not declared nullable | Rate source text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `rateTimestampUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for rate timestamp; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `provider` | `string` | Yes | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | Shared convention | No further constraint recorded |
| `policyVersion` | `string` | No | Explicitly allowed | Policy revision used for this assessment; not the mobile app build number. | Shared convention | No further constraint recorded |
| `quoteId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related quote record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `quoteRevision` | `integer (int64)` | No | Not declared nullable | Quote revision for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `providerEnvironment` | `string` | No | Explicitly allowed | Provider environment text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `rateDirection` | `string` | No | Explicitly allowed | Rate direction text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `rateEvidenceReference` | `string` | No | Explicitly allowed | Rate evidence reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `disclaimer` | `string` | No | Explicitly allowed | Disclaimer text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `settlementBaseMinor` | `integer (int64)` | No | Explicitly allowed | Settlement base in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `rateVersionId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related rate version record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `rateVersion` | `integer (int32)` | No | Not declared nullable | Rate version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `rateRevision` | `integer (int64)` | No | Not declared nullable | Rate revision for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `isDerivedRate` | `boolean` | No | Not declared nullable | Whether is derived rate applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `feePolicyVersionId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related fee policy version record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `feePolicyVersion` | `integer (int32)` | No | Not declared nullable | Fee policy version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `feePercentageRate` | `number (double)` | No | Not declared nullable | Numeric fee percentage rate for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `feeFixedComponentMinor` | `integer (int64)` | No | Not declared nullable | Fee fixed component in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `roundingDisclosure` | `string` | No | Explicitly allowed | Rounding disclosure text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `rateEvidenceHash` | `string` | No | Explicitly allowed | Rate evidence hash text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `feeEvidenceReference` | `string` | No | Explicitly allowed | Fee evidence reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `feeEvidenceHash` | `string` | No | Explicitly allowed | Fee evidence hash text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TopUpResultDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `paymentId` | `string (uuid)` | Yes | Not declared nullable | Server-owned payment record used for state/reconciliation. | Shared convention | No further constraint recorded |
| `providerName` | `string` | Yes | Not declared nullable | Provider name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `checkoutUrl` | `string` | No | Explicitly allowed | URL for checkout; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `instructions` | `string` | No | Explicitly allowed | Instructions text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `wallet` | [WalletDto](w.md#walletdto) | Yes | Not declared nullable | Wallet represented by the `WalletDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `operationReference` | `string` | No | Explicitly allowed | Operation reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `feeMinor` | `integer (int64)` | No | Not declared nullable | Fee amount in the accompanying currency's integer minor units; the owning operation defines what the fee charges for. | Shared convention | No further constraint recorded |
| `walletCreditMinor` | `integer (int64)` | No | Explicitly allowed | Wallet credit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TopUpWalletDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `provider` | `string` | Yes | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | Shared convention | No further constraint recorded |
| `promoCode` | `string` | No | Explicitly allowed | Promotion code supplied for server validation; it is not a guaranteed discount or credit. | Shared convention | No further constraint recorded |
| `quoteToken` | `string` | No | Explicitly allowed | Server-owned quote evidence; preserve currency/amount/expiry binding and treat it as private. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TravelBookingPartiesDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `requester` | [TravelBookingPartyDto](t.md#travelbookingpartydto) | Yes | Not declared nullable | Requester represented by the `TravelBookingPartyDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `traveler` | [TravelBookingPartyDto](t.md#travelbookingpartydto) | Yes | Not declared nullable | Traveler represented by the `TravelBookingPartyDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `payer` | [TravelBookingPartyDto](t.md#travelbookingpartydto) | Yes | Not declared nullable | Payer represented by the `TravelBookingPartyDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `supervisor` | [TravelBookingPartyDto](t.md#travelbookingpartydto) | Yes | Not declared nullable | Supervisor represented by the `TravelBookingPartyDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TravelBookingPartyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `string (uuid)` | No | Explicitly allowed | Related account identity; the server still proves the caller's ownership or permitted relationship. | Shared convention | No further constraint recorded |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | Shared convention | No further constraint recorded |
| `role` | `string` | Yes | Not declared nullable | Role text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TravelCostCenterDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `monthlyBudgetMinor` | `integer (int64)` | Yes | Not declared nullable | Monthly budget in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `spendThisMonthMinor` | `integer (int64)` | Yes | Not declared nullable | Spend this month in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TravelMemberDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `userId` | `string (uuid)` | No | Explicitly allowed | Related account identity; the server still proves the caller's ownership or permitted relationship. | Shared convention | No further constraint recorded |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | Shared convention | No further constraint recorded |
| `email` | `string` | No | Explicitly allowed | Email address for this model's person/destination; its presence does not prove verification. | Shared convention | No further constraint recorded |
| `phoneNumber` | `string` | No | Explicitly allowed | Country-aware contact number; its presence does not prove verification or provider provisioning. | Shared convention | No further constraint recorded |
| `role` | `string` | Yes | Not declared nullable | Role text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `relationship` | `string` | No | Explicitly allowed | Relationship text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `employeeCode` | `string` | No | Explicitly allowed | Employee code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `defaultCostCenterId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related default cost center record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `canBook` | `boolean` | Yes | Not declared nullable | Whether can book applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canViewLiveTrips` | `boolean` | Yes | Not declared nullable | Whether can view live trips applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canManageMembers` | `boolean` | Yes | Not declared nullable | Whether can manage members applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canManageBilling` | `boolean` | Yes | Not declared nullable | Whether can manage billing applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `perRideLimitMinor` | `integer (int64)` | Yes | Not declared nullable | Per ride limit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `monthlyLimitMinor` | `integer (int64)` | Yes | Not declared nullable | Monthly limit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | Shared convention | No further constraint recorded |
| `invitationPending` | `boolean` | Yes | Not declared nullable | Whether invitation pending applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `liveTrackingConsentGrantedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for live tracking consent granted at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `liveTrackingConsentRevokedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for live tracking consent revoked at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TravelProfileSummaryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `type` | `string` | Yes | Not declared nullable | Type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `isOwner` | `boolean` | Yes | Not declared nullable | Whether is owner applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `role` | `string` | Yes | Not declared nullable | Role text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `activeMembers` | `integer (int32)` | Yes | Not declared nullable | Numeric active members for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `tripsThisMonth` | `integer (int32)` | Yes | Not declared nullable | Numeric trips this month for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `spendThisMonthMinor` | `integer (int64)` | Yes | Not declared nullable | Spend this month in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `monthlyBudgetMinor` | `integer (int64)` | Yes | Not declared nullable | Monthly budget in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `centralBillingEnabled` | `boolean` | Yes | Not declared nullable | Whether central billing enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `allowDelegatedBooking` | `boolean` | Yes | Not declared nullable | Whether allow delegated booking applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `liveTrackingEnabled` | `boolean` | Yes | Not declared nullable | Whether live tracking enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `notifyRideCreated` | `boolean` | Yes | Not declared nullable | Whether notify ride created applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `notifyDriverAssigned` | `boolean` | Yes | Not declared nullable | Whether notify driver assigned applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `notifyTripStarted` | `boolean` | Yes | Not declared nullable | Whether notify trip started applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `notifyTripCompleted` | `boolean` | Yes | Not declared nullable | Whether notify trip completed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `notifyTripCancelled` | `boolean` | Yes | Not declared nullable | Whether notify trip cancelled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `notifyByPush` | `boolean` | Yes | Not declared nullable | Whether notify by push applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `notifyByEmail` | `boolean` | Yes | Not declared nullable | Whether notify by email applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `notifyBySms` | `boolean` | Yes | Not declared nullable | Whether notify by sms applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TravelProfileWorkspaceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `profile` | [TravelProfileSummaryDto](t.md#travelprofilesummarydto) | Yes | Not declared nullable | Profile represented by the `TravelProfileSummaryDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `members` | [TravelMemberDto](t.md#travelmemberdto)[] | Yes | Not declared nullable | Collection of members for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `costCenters` | [TravelCostCenterDto](t.md#travelcostcenterdto)[] | Yes | Not declared nullable | Collection of cost centers for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `policy` | [TravelRidePolicyDto](t.md#travelridepolicydto) | Yes | Not declared nullable | Policy represented by the `TravelRidePolicyDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `canManageMembers` | `boolean` | Yes | Not declared nullable | Whether can manage members applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canManageBilling` | `boolean` | Yes | Not declared nullable | Whether can manage billing applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canBook` | `boolean` | Yes | Not declared nullable | Whether can book applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canViewLiveTrips` | `boolean` | Yes | Not declared nullable | Whether can view live trips applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TravelRideBookingDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `booking` | [RideRequestDto](r.md#riderequestdto) | Yes | Not declared nullable | Booking represented by the `RideRequestDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `parties` | [TravelBookingPartiesDto](t.md#travelbookingpartiesdto) | Yes | Not declared nullable | Parties represented by the `TravelBookingPartiesDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TravelRidePolicyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `maxFarePerRideMinor` | `integer (int64)` | Yes | Not declared nullable | Max fare per ride in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `maxSpendPerDayMinor` | `integer (int64)` | Yes | Not declared nullable | Max spend per day in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `maxSpendPerMonthMinor` | `integer (int64)` | Yes | Not declared nullable | Max spend per month in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `maxRidesPerDay` | `integer (int32)` | Yes | Not declared nullable | Numeric max rides per day for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `allowCash` | `boolean` | Yes | Not declared nullable | Whether allow cash applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `allowWallet` | `boolean` | Yes | Not declared nullable | Whether allow wallet applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `allowScheduledRides` | `boolean` | Yes | Not declared nullable | Whether allow scheduled rides applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `allowAirportRides` | `boolean` | Yes | Not declared nullable | Whether allow airport rides applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `allowedWeekdaysMask` | `integer (int32)` | Yes | Not declared nullable | Numeric allowed weekdays mask for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `earliestMinuteLocal` | `integer (int32)` | Yes | Not declared nullable | Numeric earliest minute local for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `latestMinuteLocal` | `integer (int32)` | Yes | Not declared nullable | Numeric latest minute local for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TravelStatementDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `profileId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related profile record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `profileName` | `string` | Yes | Not declared nullable | Profile name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `fromUtc` | `string (date-time)` | Yes | Not declared nullable | UTC start of the requested range; apply this endpoint's inclusion/validation rules. | Shared convention | No further constraint recorded |
| `toUtc` | `string (date-time)` | Yes | Not declared nullable | UTC end of the requested range; apply this endpoint's inclusion/validation rules. | Shared convention | No further constraint recorded |
| `tripCount` | `integer (int32)` | Yes | Not declared nullable | Number of trip in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `totalFareMinor` | `integer (int64)` | Yes | Not declared nullable | Total fare in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `costCenters` | [TravelCostCenterDto](t.md#travelcostcenterdto)[] | Yes | Not declared nullable | Collection of cost centers for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `trips` | [TravelTripDto](t.md#traveltripdto)[] | Yes | Not declared nullable | Collection of trips for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TravelTrackingDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `status` | [TripStatus](t.md#tripstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `travelerName` | `string` | Yes | Not declared nullable | Traveler name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `latitude` | `number (double)` | No | Explicitly allowed | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | No | Explicitly allowed | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `accuracyMeters` | `number (double)` | No | Explicitly allowed | Accuracy, measured in metres. | Naming convention | No further constraint recorded |
| `sampledAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for sampled at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `isFresh` | `boolean` | Yes | Not declared nullable | Whether is fresh applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `trackingClosesAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for tracking closes at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `parties` | [TravelBookingPartiesDto](t.md#travelbookingpartiesdto) | No | Not declared nullable | Parties represented by the `TravelBookingPartiesDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `locationVersion` | `integer (int64)` | No | Explicitly allowed | Location version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `locationSource` | `string` | No | Explicitly allowed | Location source text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `locationAgeSeconds` | `integer (int32)` | No | Explicitly allowed | Location age, measured in seconds. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TravelTripDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `rideRequestId` | `string (uuid)` | Yes | Not declared nullable | Rider request record, distinct from an accepted trip. | Shared convention | No further constraint recorded |
| `memberId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related member record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `travelerName` | `string` | Yes | Not declared nullable | Traveler name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `costCenterCode` | `string` | No | Explicitly allowed | Cost center code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `status` | [TripStatus](t.md#tripstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `fareMinor` | `integer (int64)` | Yes | Not declared nullable | Fare in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `startedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for started at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `completedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for completed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `pickupAddress` | `string` | Yes | Not declared nullable | Human pickup-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `dropoffAddress` | `string` | Yes | Not declared nullable | Human destination-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `parties` | [TravelBookingPartiesDto](t.md#travelbookingpartiesdto) | No | Not declared nullable | Parties represented by the `TravelBookingPartiesDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TravelTripReceiptDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `receipt` | [TripReceiptDto](t.md#tripreceiptdto) | Yes | Not declared nullable | Receipt represented by the `TripReceiptDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `parties` | [TravelBookingPartiesDto](t.md#travelbookingpartiesdto) | Yes | Not declared nullable | Parties represented by the `TravelBookingPartiesDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripCallLogDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `callerUserId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related caller user record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `callerName` | `string` | Yes | Not declared nullable | Caller name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `callerRole` | [UserRole](u.md#userrole) | Yes | Not declared nullable | Caller role represented by the `UserRole` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `outcome` | `string` | Yes | Not declared nullable | Result/recovery state of this operation; unknown or pending is not failed or successful. | Shared convention | No further constraint recorded |
| `startedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for started at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `endedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for ended at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `durationSeconds` | `integer (int64)` | No | Explicitly allowed | Duration, measured in seconds. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripChatDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `items` | [ChatMessageDto](c.md#chatmessagedto)[] | Yes | Not declared nullable | Records returned in this collection/page, each using the referenced item model. | Shared convention | No further constraint recorded |
| `unreadCount` | `integer (int32)` | Yes | Not declared nullable | Current unread count in the applicable notification/chat model. | Shared convention | No further constraint recorded |
| `hasMore` | `boolean` | Yes | Not declared nullable | Whether the seek-paged result indicates more records after this page. | Shared convention | No further constraint recorded |
| `isReadOnly` | `boolean` | Yes | Not declared nullable | Whether is read only applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `tripStatus` | [TripStatus](t.md#tripstatus) | Yes | Not declared nullable | Trip status represented by the `TripStatus` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `lifecycleVersion` | `integer (int64)` | No | Not declared nullable | Lifecycle version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `readCursor` | `integer (int64)` | No | Not declared nullable | Numeric read cursor for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `callLogs` | [TripCallLogDto](t.md#tripcalllogdto)[] | No | Explicitly allowed | Collection of call logs for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripChatMutationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `lifecycleVersion` | `integer (int64)` | Yes | Not declared nullable | Lifecycle version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `readCursor` | `integer (int64)` | No | Not declared nullable | Numeric read cursor for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripCustomerStatusDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `explanation` | `string` | Yes | Not declared nullable | Explanation text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `freshness` | `string` | Yes | Not declared nullable | Freshness text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `confidence` | `string` | Yes | Not declared nullable | Confidence text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `nextAction` | `string` | No | Explicitly allowed | Suggested next workflow step returned by the server; it does not override authorization. | Shared convention | No further constraint recorded |
| `allowedActions` | `string[]` | Yes | Not declared nullable | Collection of allowed actions for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `lastSyncedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last synced at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripDistanceProvenance

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Unavailable | Unavailable state/choice in this specific enum. |
| `1` | ValidatedRoute | Validated route state/choice in this specific enum. |
| `2` | ValidatedTelemetry | Validated telemetry state/choice in this specific enum. |

## TripDistanceSummaryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `meters` | `integer (int32)` | No | Explicitly allowed | Numeric meters for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `provenance` | [TripDistanceProvenance](t.md#tripdistanceprovenance) | Yes | Not declared nullable | Provenance represented by the `TripDistanceProvenance` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `rideRequestId` | `string (uuid)` | Yes | Not declared nullable | Rider request record, distinct from an accepted trip. | Shared convention | No further constraint recorded |
| `status` | [TripStatus](t.md#tripstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `driverProfileId` | `string (uuid)` | Yes | Not declared nullable | Driver-profile record associated with this operation or result. | Shared convention | No further constraint recorded |
| `driverName` | `string` | Yes | Not declared nullable | Driver name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `driverRating` | `number (double)` | Yes | Not declared nullable | Numeric driver rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `vehicleDescription` | `string` | No | Explicitly allowed | Vehicle description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `plateNumber` | `string` | No | Explicitly allowed | Country-specific vehicle registration plate; validate through the applicable country workflow. | Shared convention | No further constraint recorded |
| `passengerId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related passenger record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `passengerName` | `string` | Yes | Not declared nullable | Passenger name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `pickupAddress` | `string` | Yes | Not declared nullable | Human pickup-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `dropoffAddress` | `string` | Yes | Not declared nullable | Human destination-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `fareMinor` | `integer (int64)` | Yes | Not declared nullable | Fare in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `surgeMultiplier` | `number (double)` | Yes | Not declared nullable | Numeric surge multiplier for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `promoCodeId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related promo code record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `promoDiscountMinor` | `integer (int64)` | Yes | Not declared nullable | Promo discount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `commissionRate` | `number (double)` | Yes | Not declared nullable | Numeric commission rate for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `commissionMinor` | `integer (int64)` | Yes | Not declared nullable | Commission in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `driverEarningMinor` | `integer (int64)` | Yes | Not declared nullable | Driver earning in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `paymentMethod` | [PaymentMethod](p.md#paymentmethod) | No | Not declared nullable | Payment method enum; availability and settlement rules are checked separately. | Shared convention | No further constraint recorded |
| `paymentStatus` | [PaymentStatus](p.md#paymentstatus) | Yes | Not declared nullable | Payment status represented by the `PaymentStatus` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `driverArrivedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for driver arrived at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `startedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for started at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `completedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for completed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `chatUnread` | `integer (int32)` | Yes | Not declared nullable | Numeric chat unread for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `tipMinor` | `integer (int64)` | No | Not declared nullable | Tip in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `routeVersion` | `integer (int32)` | No | Not declared nullable | Route version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `pendingRouteAlteration` | [TripRouteAlterationDto](t.md#triproutealterationdto) | No | Not declared nullable | Pending route alteration represented by the `TripRouteAlterationDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `currentUserHasRated` | `boolean` | No | Not declared nullable | Whether current user has rated applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `pickupLatitude` | `number (double)` | No | Not declared nullable | Pickup latitude in degrees; latitude is separate from address text. | Shared convention | No further constraint recorded |
| `pickupLongitude` | `number (double)` | No | Not declared nullable | Pickup longitude in degrees; preserve coordinate order. | Shared convention | No further constraint recorded |
| `dropoffLatitude` | `number (double)` | No | Not declared nullable | Destination latitude in degrees. | Shared convention | No further constraint recorded |
| `dropoffLongitude` | `number (double)` | No | Not declared nullable | Destination longitude in degrees. | Shared convention | No further constraint recorded |
| `distanceMeters` | `integer (int32)` | No | Not declared nullable | Distance represented by this model, in metres; its source/assessment depends on the operation. | Shared convention | No further constraint recorded |
| `distance` | [TripDistanceSummaryDto](t.md#tripdistancesummarydto) | No | Not declared nullable | Distance represented by the `TripDistanceSummaryDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `estimatedDurationSeconds` | `integer (int32)` | No | Not declared nullable | Estimated duration in seconds; an estimate is not actual elapsed trip time. | Shared convention | No further constraint recorded |
| `driverAvatarRef` | `string` | No | Explicitly allowed | Driver avatar ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `lifecycleVersion` | `integer (int64)` | No | Not declared nullable | Lifecycle version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `driverLatitude` | `number (double)` | No | Explicitly allowed | Numeric driver latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `driverLongitude` | `number (double)` | No | Explicitly allowed | Numeric driver longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `driverLocationAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for driver location at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `scheduledForUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for scheduled for; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `scheduledGuaranteeStatus` | [ScheduledRideGuaranteeStatus](s.md#scheduledrideguaranteestatus) | No | Not declared nullable | Scheduled guarantee status represented by the `ScheduledRideGuaranteeStatus` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `driverConfirmationOpensAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for driver confirmation opens at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `driverConfirmationDeadlineUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for driver confirmation deadline; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `driverConfirmedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for driver confirmed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `replacementAttemptCount` | `integer (int32)` | No | Not declared nullable | Number of replacement attempt in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `guaranteeStatusReason` | `string` | No | Explicitly allowed | Guarantee status reason text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `productType` | [RideProductType](r.md#rideproducttype) | No | Not declared nullable | Product type represented by the `RideProductType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `bookedHourlyMinutes` | `integer (int32)` | No | Not declared nullable | Booked hourly, measured in minutes. | Naming convention | No further constraint recorded |
| `hourlyServiceEndsAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for hourly service ends at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `hourlyOvertimeSeconds` | `integer (int32)` | No | Not declared nullable | Hourly overtime, measured in seconds. | Naming convention | No further constraint recorded |
| `plannedWaitingSeconds` | `integer (int32)` | No | Not declared nullable | Planned waiting, measured in seconds. | Naming convention | No further constraint recorded |
| `actualWaitingSeconds` | `integer (int32)` | No | Not declared nullable | Actual waiting, measured in seconds. | Naming convention | No further constraint recorded |
| `activeStopSequence` | `integer (int32)` | No | Explicitly allowed | Numeric active stop sequence for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `stops` | [RideStopDto](r.md#ridestopdto)[] | No | Explicitly allowed | Ordered journey/delivery stops in the referenced stop model. | Shared convention | No further constraint recorded |
| `driverLocationAccuracyMeters` | `number (double)` | No | Explicitly allowed | Driver location accuracy, measured in metres. | Naming convention | No further constraint recorded |
| `guaranteePolicyVersion` | `string` | No | Explicitly allowed | Guarantee policy version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `guaranteeTermsUrl` | `string` | No | Explicitly allowed | URL for guarantee terms; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `guaranteeSupportPolicy` | `string` | No | Explicitly allowed | Guarantee support policy text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `guaranteeSupportSlaMinutes` | `integer (int32)` | No | Explicitly allowed | Guarantee support sla, measured in minutes. | Naming convention | No further constraint recorded |
| `guaranteeCompensationMinor` | `integer (int64)` | No | Explicitly allowed | Guarantee compensation in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `pickupConfirmationRequired` | `boolean` | No | Not declared nullable | Whether pickup confirmation required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `transactionFeeMinor` | `integer (int64)` | No | Not declared nullable | Transaction fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `passengerAvatarRef` | `string` | No | Explicitly allowed | Passenger avatar ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `consistencyState` | `string` | No | Explicitly allowed | Consistency state text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `terminationAction` | `string` | No | Explicitly allowed | Termination action text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `financialOutcome` | `string` | No | Explicitly allowed | Financial outcome text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `driverLocationVersion` | `integer (int64)` | No | Explicitly allowed | Driver location version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `driverLocationSource` | `string` | No | Explicitly allowed | Driver location source text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `driverLocationAgeSeconds` | `integer (int32)` | No | Explicitly allowed | Driver location age, measured in seconds. | Naming convention | No further constraint recorded |
| `customerStatus` | [TripCustomerStatusDto](t.md#tripcustomerstatusdto) | No | Not declared nullable | Customer status represented by the `TripCustomerStatusDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `driverLocationStatus` | [TripLocationStatusDto](t.md#triplocationstatusdto) | No | Not declared nullable | Driver location status represented by the `TripLocationStatusDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `locationPolicy` | [TripLocationPolicyDto](t.md#triplocationpolicydto) | No | Not declared nullable | Location policy represented by the `TripLocationPolicyDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `lifecycleEvidence` | [TripLifecycleEvidenceDto](t.md#triplifecycleevidencedto) | No | Not declared nullable | Lifecycle evidence represented by the `TripLifecycleEvidenceDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `scheduledRideOperatingStatus` | [ScheduledRideOperatingStatusDto](s.md#scheduledrideoperatingstatusdto) | No | Not declared nullable | Scheduled ride operating status represented by the `ScheduledRideOperatingStatusDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripDtoPagedResult

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `items` | [TripDto](t.md#tripdto)[] | No | Explicitly allowed | Records returned in this collection/page, each using the referenced item model. | Shared convention | No further constraint recorded |
| `page` | `integer (int32)` | No | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | Shared convention | No further constraint recorded |
| `pageSize` | `integer (int32)` | No | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | Shared convention | No further constraint recorded |
| `totalCount` | `integer (int64)` | No | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | Shared convention | No further constraint recorded |
| `totalPages` | `integer (int32)` | No | Not declared nullable | Number of pages represented by this page-number model. | Shared convention | readOnly: `True` |
| `hasPreviousPage` | `boolean` | No | Not declared nullable | Whether has previous page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |
| `hasNextPage` | `boolean` | No | Not declared nullable | Whether has next page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## TripHistorySeekPageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `items` | [TripDto](t.md#tripdto)[] | Yes | Not declared nullable | Records returned in this collection/page, each using the referenced item model. | Shared convention | No further constraint recorded |
| `pageSize` | `integer (int32)` | Yes | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | Shared convention | No further constraint recorded |
| `hasMore` | `boolean` | Yes | Not declared nullable | Whether the seek-paged result indicates more records after this page. | Shared convention | No further constraint recorded |
| `nextCursor` | `string` | No | Explicitly allowed | Opaque, scope-bound continuation token; preserve it unchanged and reset it when filters/context change. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripLifecycleEvidenceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `pickupArrivalReady` | `boolean` | Yes | Not declared nullable | Whether pickup arrival ready applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `pickupOutcome` | `string` | Yes | Not declared nullable | Pickup outcome text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `pickupSampleCount` | `integer (int32)` | Yes | Not declared nullable | Number of pickup sample in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `pickupWindowSeconds` | `integer (int32)` | Yes | Not declared nullable | Pickup window, measured in seconds. | Naming convention | No further constraint recorded |
| `destinationArrivalReady` | `boolean` | Yes | Not declared nullable | Whether destination arrival ready applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `destinationOutcome` | `string` | Yes | Not declared nullable | Destination outcome text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `destinationSampleCount` | `integer (int32)` | Yes | Not declared nullable | Number of destination sample in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `destinationWindowSeconds` | `integer (int32)` | Yes | Not declared nullable | Destination window, measured in seconds. | Naming convention | No further constraint recorded |
| `startSuspected` | `boolean` | No | Not declared nullable | Whether start suspected applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `startOutcome` | `string` | No | Explicitly allowed | Start outcome text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `startSampleCount` | `integer (int32)` | No | Not declared nullable | Number of start sample in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `startWindowSeconds` | `integer (int32)` | No | Not declared nullable | Start window, measured in seconds. | Naming convention | No further constraint recorded |
| `completionReminderDue` | `boolean` | No | Not declared nullable | Whether completion reminder due applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `policyVersion` | `string` | No | Explicitly allowed | Policy revision used for this assessment; not the mobile app build number. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripLocationPolicyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `scope` | `string` | Yes | Not declared nullable | Scope text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `canViewDriverLocation` | `boolean` | Yes | Not declared nullable | Whether can view driver location applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canViewPickup` | `boolean` | Yes | Not declared nullable | Whether can view pickup applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canViewDropoff` | `boolean` | Yes | Not declared nullable | Whether can view dropoff applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canViewVehicleSnapshot` | `boolean` | Yes | Not declared nullable | Whether can view vehicle snapshot applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripLocationStatusDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `state` | `string` | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `sampledAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for sampled at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `ageSeconds` | `integer (int32)` | No | Explicitly allowed | Age, measured in seconds. | Naming convention | No further constraint recorded |
| `accuracyMeters` | `number (double)` | No | Explicitly allowed | Accuracy, measured in metres. | Naming convention | No further constraint recorded |
| `revision` | `integer (int64)` | No | Explicitly allowed | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |
| `source` | `string` | No | Explicitly allowed | Source text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripPickupCeremonyStatusDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `state` | `string` | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `driverArrivedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for driver arrived at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `waitElapsedSeconds` | `integer (int32)` | Yes | Not declared nullable | Wait elapsed, measured in seconds. | Naming convention | No further constraint recorded |
| `contactAttemptCount` | `integer (int32)` | Yes | Not declared nullable | Number of contact attempt in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `lastContactAttemptAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last contact attempt at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `canRecordContactAttempt` | `boolean` | Yes | Not declared nullable | Whether can record contact attempt applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canStartTrip` | `boolean` | Yes | Not declared nullable | Whether can start trip applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canDeclareNoShow` | `boolean` | Yes | Not declared nullable | Whether can declare no show applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `noShowCode` | `string` | Yes | Not declared nullable | No show code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `nextAction` | `string` | Yes | Not declared nullable | Suggested next workflow step returned by the server; it does not override authorization. | Shared convention | No further constraint recorded |
| `tripLifecycleVersion` | `integer (int64)` | Yes | Not declared nullable | Trip lifecycle version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripPickupCodeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `riderPin` | `string` | No | Explicitly allowed | Rider pin text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `challengeId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related challenge record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `qrPayload` | `string` | Yes | Not declared nullable | Qr payload text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `required` | `boolean` | Yes | Not declared nullable | Whether required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `maximumAttempts` | `integer (int32)` | Yes | Not declared nullable | Numeric maximum attempts for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripReceiptDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `receiptNumber` | `string` | Yes | Not declared nullable | Receipt number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `passengerName` | `string` | Yes | Not declared nullable | Passenger name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `driverName` | `string` | Yes | Not declared nullable | Driver name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `vehicleDescription` | `string` | Yes | Not declared nullable | Vehicle description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `pickupAddress` | `string` | Yes | Not declared nullable | Human pickup-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `dropoffAddress` | `string` | Yes | Not declared nullable | Human destination-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `startedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for started at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `completedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for completed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `distanceMeters` | `integer (int32)` | Yes | Not declared nullable | Distance represented by this model, in metres; its source/assessment depends on the operation. | Shared convention | No further constraint recorded |
| `distanceKilometers` | `number (double)` | Yes | Not declared nullable | Numeric distance kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `distanceMiles` | `number (double)` | Yes | Not declared nullable | Numeric distance miles for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `durationSeconds` | `integer (int32)` | Yes | Not declared nullable | Duration, measured in seconds. | Naming convention | No further constraint recorded |
| `grossFareMinor` | `integer (int64)` | Yes | Not declared nullable | Gross fare in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `promoDiscountMinor` | `integer (int64)` | Yes | Not declared nullable | Promo discount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `passengerPaidMinor` | `integer (int64)` | Yes | Not declared nullable | Passenger paid in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `tipMinor` | `integer (int64)` | Yes | Not declared nullable | Tip in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `paymentMethod` | [PaymentMethod](p.md#paymentmethod) | Yes | Not declared nullable | Payment method enum; availability and settlement rules are checked separately. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `timezone` | `string` | No | Explicitly allowed | Timezone context used by this contract; apply documented IANA/display semantics. | Shared convention | No further constraint recorded |
| `startedAtLocal` | `string` | No | Explicitly allowed | Started at local text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `completedAtLocal` | `string` | No | Explicitly allowed | Completed at local text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `createdAtLocal` | `string` | No | Explicitly allowed | Created at local text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripRouteAlterationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `version` | `integer (int32)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `previousDropoffAddress` | `string` | Yes | Not declared nullable | Previous dropoff address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `newDropoffAddress` | `string` | Yes | Not declared nullable | New dropoff address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `revisedDistanceMeters` | `integer (int32)` | Yes | Not declared nullable | Revised distance, measured in metres. | Naming convention | No further constraint recorded |
| `revisedDurationSeconds` | `integer (int32)` | Yes | Not declared nullable | Revised duration, measured in seconds. | Naming convention | No further constraint recorded |
| `previousFareMinor` | `integer (int64)` | Yes | Not declared nullable | Previous fare in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `revisedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Revised fare in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `differenceMinor` | `integer (int64)` | Yes | Not declared nullable | Difference in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `appliedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for applied at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `proposal` | [TripRouteProposalSnapshotDto](t.md#triprouteproposalsnapshotdto) | No | Not declared nullable | Proposal represented by the `TripRouteProposalSnapshotDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripRouteProposalSnapshotDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `oldRoute` | `string` | Yes | Not declared nullable | Old route text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `newRoute` | `string` | Yes | Not declared nullable | New route text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `waitingTimeSeconds` | `integer (int32)` | Yes | Not declared nullable | Waiting time, measured in seconds. | Naming convention | No further constraint recorded |
| `fareDeltaMinor` | `integer (int64)` | Yes | Not declared nullable | Fare delta in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `paymentImpact` | `string` | Yes | Not declared nullable | Payment impact text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `requiredActor` | `string` | Yes | Not declared nullable | Required actor text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `requiresActorApproval` | `boolean` | Yes | Not declared nullable | Whether requires actor approval applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `transactionFeeDeltaMinor` | `integer (int64)` | Yes | Not declared nullable | Transaction fee delta in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `additionalAuthorizationMinor` | `integer (int64)` | Yes | Not declared nullable | Additional authorization in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `supportPathCode` | `string` | No | Explicitly allowed | Support path code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripShareDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `shortCode` | `string` | Yes | Not declared nullable | Short code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `url` | `string` | Yes | Not declared nullable | Url text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Assigned | Assigned state/choice in this specific enum. |
| `2` | DriverArrived | Driver arrived state/choice in this specific enum. |
| `3` | InProgress | In progress state/choice in this specific enum. |
| `4` | Completed | Completed state/choice in this specific enum. |
| `5` | Cancelled | Cancelled state/choice in this specific enum. |
| `6` | Reserved | Reserved state/choice in this specific enum. |
| `7` | AwaitingReplacement | Awaiting replacement state/choice in this specific enum. |

## TripStopTransitionRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `expectedLifecycleVersion` | `integer (int64)` | Yes | Not declared nullable | Expected lifecycle version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripTerminationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `trip` | [TripDto](t.md#tripdto) | Yes | Not declared nullable | Trip represented by the `TripDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `action` | `string` | Yes | Not declared nullable | Action text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `financialOutcome` | `string` | Yes | Not declared nullable | Financial outcome text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `cancellationFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Cancellation fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `refundAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Refund amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `locationSharingStopped` | `boolean` | Yes | Not declared nullable | Whether location sharing stopped applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requiresReconciliation` | `boolean` | No | Not declared nullable | Whether requires reconciliation applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripTerminationRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `reason` | `string` | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripTimelineDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `status` | [TripStatus](t.md#tripstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `chatAvailable` | `boolean` | Yes | Not declared nullable | Whether chat available applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `events` | [TripTimelineEventDto](t.md#triptimelineeventdto)[] | Yes | Not declared nullable | Collection of events for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripTimelineEventDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `eventCode` | `string` | Yes | Not declared nullable | Event code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `labelKey` | `string` | Yes | Not declared nullable | Label key text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `summary` | `string` | Yes | Not declared nullable | Summary text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `actorRole` | `string` | Yes | Not declared nullable | Actor role text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `timestampUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for timestamp; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `correlationId` | `string` | No | Explicitly allowed | Safe request correlation reference; not an access token or proof of success. | Shared convention | No further constraint recorded |
| `evidenceLinks` | [TripTimelineEvidenceLinkDto](t.md#triptimelineevidencelinkdto)[] | Yes | Not declared nullable | Collection of evidence links for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripTimelineEvidenceLinkDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `kind` | `string` | Yes | Not declared nullable | Kind text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `labelKey` | `string` | Yes | Not declared nullable | Label key text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `route` | `string` | Yes | Not declared nullable | Route text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TripTipDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `paidAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for paid at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TrustedContactRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `phone` | `string` | Yes | Not declared nullable | Phone text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `canReceiveLiveTrip` | `boolean` | Yes | Not declared nullable | Whether can receive live trip applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TwoFactorCodeRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TwoFactorConfirmedDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `enabled` | `boolean` | Yes | Not declared nullable | Whether enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `recoveryCodes` | `string[]` | Yes | Not declared nullable | Collection of recovery codes for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TwoFactorEnrollmentDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `secret` | `string` | Yes | Not declared nullable | Secret text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `otpAuthUri` | `string` | Yes | Not declared nullable | Otp auth uri text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TwoFactorStatusDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `enabled` | `boolean` | Yes | Not declared nullable | Whether enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `hasPassword` | `boolean` | No | Not declared nullable | Private has password used by this specific ceremony; never log, publish or substitute it for another proof. | Naming convention | No further constraint recorded |
| `availableFallbackChannels` | `string[]` | No | Explicitly allowed | Collection of available fallback channels for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `method` | `string` | No | Explicitly allowed | Method text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `maskedDestination` | `string` | No | Explicitly allowed | Privacy-reduced contact display for the ceremony; not the raw credential or full destination. | Shared convention | No further constraint recorded |
| `required` | `boolean` | No | Not declared nullable | Whether required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `hasSocialLogin` | `boolean` | No | Not declared nullable | Whether has social login applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## TwoFactorStepUpDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `token` | `string` | Yes | Not declared nullable | Token for this specific contract, such as push registration; sensitive values must not be logged or reused in another ceremony. | Shared convention | No further constraint recorded |
| `action` | `string` | Yes | Not declared nullable | Action text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
