# Field dictionary: F

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

## FailedDeliveryAttemptDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `stopId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related stop record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `reason` | [DeliveryFailureReason](d.md#deliveryfailurereason) | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | No further constraint recorded |
| `evidence` | [DeliveryEvidenceInputDto](d.md#deliveryevidenceinputdto)[] | Yes | Not declared nullable | Collection of evidence for this model; interpret each item through the declared item type. | No further constraint recorded |
| `initiateReturnToSender` | `boolean` | No | Not declared nullable | Whether initiate return to sender applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | No | Explicitly allowed | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FamilySafetyPolicyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `travelProfileId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related travel profile record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |
| `policyVersion` | `string` | Yes | Not declared nullable | Policy revision used for this assessment; not the mobile app build number. | No further constraint recorded |
| `isEnabled` | `boolean` | Yes | Not declared nullable | Whether is enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `minimumTravelerAge` | `integer (int32)` | Yes | Not declared nullable | Numeric minimum traveler age for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `maximumTravelerAge` | `integer (int32)` | Yes | Not declared nullable | Numeric maximum traveler age for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `consentValidityDays` | `integer (int32)` | Yes | Not declared nullable | Consent validity, measured in days under this workflow's calendar rules. | No further constraint recorded |
| `consentRenewalWarningDays` | `integer (int32)` | Yes | Not declared nullable | Consent renewal warning, measured in days under this workflow's calendar rules. | No further constraint recorded |
| `requireLiveTrackingConsent` | `boolean` | Yes | Not declared nullable | Whether require live tracking consent applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `requireThreeWayCommunicationConsent` | `boolean` | Yes | Not declared nullable | Whether require three way communication consent applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `requireEmergencyContactConfirmation` | `boolean` | Yes | Not declared nullable | Whether require emergency contact confirmation applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `allowCash` | `boolean` | Yes | Not declared nullable | Whether allow cash applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `allowedWeekdaysMask` | `integer (int32)` | Yes | Not declared nullable | Numeric allowed weekdays mask for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `earliestMinuteLocal` | `integer (int32)` | Yes | Not declared nullable | Numeric earliest minute local for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `latestMinuteLocal` | `integer (int32)` | Yes | Not declared nullable | Numeric latest minute local for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `minimumDriverTrustLevel` | `integer (int32)` | Yes | Not declared nullable | Numeric minimum driver trust level for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `requirePickupGuardianConfirmation` | `boolean` | Yes | Not declared nullable | Whether require pickup guardian confirmation applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `requireDropoffGuardianConfirmation` | `boolean` | Yes | Not declared nullable | Whether require dropoff guardian confirmation applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `effectiveAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for effective at; parse strictly and localize only for display. | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `dependentsRequiringConsent` | `integer (int32)` | Yes | Not declared nullable | Numeric dependents requiring consent for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FareQuoteBreakdownDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `baseFareMinor` | `integer (int64)` | Yes | Not declared nullable | Base fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `distanceChargeMinor` | `integer (int64)` | Yes | Not declared nullable | Distance charge in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `perKilometerMinor` | `integer (int64)` | Yes | Not declared nullable | Per kilometer in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `timeChargeMinor` | `integer (int64)` | Yes | Not declared nullable | Time charge in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `tollSurchargeMinor` | `integer (int64)` | Yes | Not declared nullable | Toll surcharge in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `routeFareMinor` | `integer (int64)` | Yes | Not declared nullable | Route fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `stopChargeMinor` | `integer (int64)` | Yes | Not declared nullable | Stop charge in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `waitingChargeMinor` | `integer (int64)` | Yes | Not declared nullable | Waiting charge in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `hourlyChargeMinor` | `integer (int64)` | Yes | Not declared nullable | Hourly charge in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `maximumStops` | `integer (int32)` | Yes | Not declared nullable | Numeric maximum stops for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `maximumWaitMinutesPerStop` | `integer (int32)` | Yes | Not declared nullable | Numeric maximum wait minutes per stop for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `hourlyMinimumMinutes` | `integer (int32)` | Yes | Not declared nullable | Hourly minimum, measured in minutes. | No further constraint recorded |
| `hourlyMaximumMinutes` | `integer (int32)` | Yes | Not declared nullable | Hourly maximum, measured in minutes. | No further constraint recorded |
| `categoryMultiplier` | `number (double)` | Yes | Not declared nullable | Numeric category multiplier for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `minimumFareMinor` | `integer (int64)` | Yes | Not declared nullable | Minimum fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `calculatedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Calculated fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FareQuoteRequestDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `vehicleCategoryId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related vehicle category record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `fromLatitude` | `number (double)` | Yes | Not declared nullable | Numeric from latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `fromLongitude` | `number (double)` | Yes | Not declared nullable | Numeric from longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `toLatitude` | `number (double)` | Yes | Not declared nullable | Numeric to latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `toLongitude` | `number (double)` | Yes | Not declared nullable | Numeric to longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `stops` | [FareQuoteStopDto](f.md#farequotestopdto)[] | No | Explicitly allowed | Ordered journey/delivery stops in the referenced stop model. | No further constraint recorded |
| `scheduledForUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for scheduled for; parse strictly and localize only for display. | No further constraint recorded |
| `petFriendlyRequired` | `boolean` | No | Not declared nullable | Whether pet friendly required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `childSeatRequired` | `boolean` | No | Not declared nullable | Whether child seat required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `childSeatCount` | `integer (int32)` | No | Not declared nullable | Number of child seat in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `wheelchairAccessibleRequired` | `boolean` | No | Not declared nullable | Whether wheelchair accessible required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `airportPickup` | `boolean` | No | Not declared nullable | Whether airport pickup applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `productType` | [RideProductType](r.md#rideproducttype) | No | Not declared nullable | Product type represented by the `RideProductType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `bookedHourlyMinutes` | `integer (int32)` | No | Not declared nullable | Booked hourly, measured in minutes. | No further constraint recorded |
| `roundTripWaitSeconds` | `integer (int32)` | No | Not declared nullable | Round trip wait, measured in seconds. | No further constraint recorded |
| `proposedFareMinor` | `integer (int64)` | No | Explicitly allowed | Rider's proposed fare in currency minor units, subject to applicable quote and marketplace rules. | No further constraint recorded |
| `dispatchMode` | [RideDispatchMode](r.md#ridedispatchmode) | No | Not declared nullable | Dispatch mode represented by the `RideDispatchMode` model or enum; use that definition's fields/values. | No further constraint recorded |
| `pickupPlaceId` | `string` | No | Explicitly allowed | Identifier of the related pickup place record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `pickupAddress` | `string` | No | Explicitly allowed | Human pickup-address text accompanying the structured location. | No further constraint recorded |
| `dropoffPlaceId` | `string` | No | Explicitly allowed | Identifier of the related dropoff place record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `dropoffAddress` | `string` | No | Explicitly allowed | Human destination-address text accompanying the structured location. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FareQuoteResponseDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `suggestedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Suggested fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `distanceMeters` | `integer (int32)` | Yes | Not declared nullable | Distance represented by this model, in metres; its source/assessment depends on the operation. | No further constraint recorded |
| `durationSeconds` | `integer (int32)` | Yes | Not declared nullable | Duration, measured in seconds. | No further constraint recorded |
| `includesToll` | `boolean` | Yes | Not declared nullable | Whether includes toll applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `surgeMultiplier` | `number (double)` | Yes | Not declared nullable | Numeric surge multiplier for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `rateBand` | `string` | No | Explicitly allowed | Rate band text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `marketplaceGuidance` | [MarketplaceFareGuidanceDto](m.md#marketplacefareguidancedto) | No | Not declared nullable | Marketplace guidance represented by the `MarketplaceFareGuidanceDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `breakdown` | [FareQuoteBreakdownDto](f.md#farequotebreakdowndto) | Yes | Not declared nullable | Breakdown represented by the `FareQuoteBreakdownDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `quoteId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related quote record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `quoteVersion` | `integer (int64)` | Yes | Not declared nullable | Quote version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `quoteExpiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for quote expires at; parse strictly and localize only for display. | No further constraint recorded |
| `routeSource` | [RideFareRouteSource](r.md#ridefareroutesource) | No | Not declared nullable | Route source represented by the `RideFareRouteSource` model or enum; use that definition's fields/values. | No further constraint recorded |
| `routeAssessment` | [FareRouteAssessmentDto](f.md#farerouteassessmentdto) | No | Not declared nullable | Route assessment represented by the `FareRouteAssessmentDto` model or enum; use that definition's fields/values. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FareQuoteStopDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | No further constraint recorded |
| `plannedWaitSeconds` | `integer (int32)` | No | Not declared nullable | Planned wait, measured in seconds. | No further constraint recorded |
| `type` | [RideStopType](r.md#ridestoptype) | No | Not declared nullable | Type represented by the `RideStopType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `address` | `string` | No | Explicitly allowed | Address text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `placeId` | `string` | No | Explicitly allowed | Identifier of the related place record in this model; ownership and scope are checked separately. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FareRouteAssessmentDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `source` | [RideFareRouteSource](r.md#ridefareroutesource) | Yes | Not declared nullable | Source represented by the `RideFareRouteSource` model or enum; use that definition's fields/values. | No further constraint recorded |
| `confidence` | `string` | Yes | Not declared nullable | Confidence text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `freshForSeconds` | `integer (int32)` | Yes | Not declared nullable | Fresh for, measured in seconds. | No further constraint recorded |
| `calculatedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for calculated at; parse strictly and localize only for display. | No further constraint recorded |
| `distanceBasis` | `string` | Yes | Not declared nullable | Distance basis text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `label` | `string` | Yes | Not declared nullable | Label text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `requiresAcknowledgement` | `boolean` | Yes | Not declared nullable | Whether requires acknowledgement applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FareSplitPlanDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `rideRequestId` | `string (uuid)` | Yes | Not declared nullable | Rider request record, distinct from an accepted trip. | No further constraint recorded |
| `tripId` | `string (uuid)` | No | Explicitly allowed | Accepted trip record, distinct from the originating ride request. | No further constraint recorded |
| `status` | [FareSplitPlanStatus](f.md#faresplitplanstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `quotedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Quoted fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `authorizedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Authorized fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `settledFareMinor` | `integer (int64)` | Yes | Not declared nullable | Settled fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `version` | `integer (int64)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | No further constraint recorded |
| `policyVersion` | `string` | Yes | Not declared nullable | Policy revision used for this assessment; not the mobile app build number. | No further constraint recorded |
| `shares` | [FareSplitShareDto](f.md#faresplitsharedto)[] | Yes | Not declared nullable | Collection of shares for this model; interpret each item through the declared item type. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FareSplitPlanStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Inviting | Inviting state/choice in this specific enum. |
| `2` | Authorized | Authorized state/choice in this specific enum. |
| `3` | Settled | Settled state/choice in this specific enum. |
| `4` | Cancelled | Cancelled state/choice in this specific enum. |
| `5` | Expired | Expired state/choice in this specific enum. |
| `6` | Failed | Failed state/choice in this specific enum. |

## FareSplitResponseDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `accept` | `boolean` | Yes | Not declared nullable | Whether accept applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FareSplitShareDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `payerUserId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related payer user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `isCurrentUser` | `boolean` | Yes | Not declared nullable | Whether is current user applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `isFallback` | `boolean` | Yes | Not declared nullable | Whether is fallback applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `fixedMinor` | `integer (int64)` | No | Explicitly allowed | Fixed in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `percentageBasisPoints` | `integer (int32)` | No | Explicitly allowed | Numeric percentage basis points for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `calculatedMinor` | `integer (int64)` | Yes | Not declared nullable | Calculated in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `heldMinor` | `integer (int64)` | Yes | Not declared nullable | Held in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `settledMinor` | `integer (int64)` | Yes | Not declared nullable | Settled in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `status` | [FareSplitShareStatus](f.md#faresplitsharestatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `respondedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for responded at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FareSplitShareInputDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `recipientFavoriteId` | `string (uuid)` | Yes | Not declared nullable | Saved recipient reference used by this transfer; not an arbitrary target user ID. | No further constraint recorded |
| `fixedMinor` | `integer (int64)` | No | Explicitly allowed | Fixed in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `percentageBasisPoints` | `integer (int32)` | No | Explicitly allowed | Numeric percentage basis points for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FareSplitShareStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Accepted | Accepted state/choice in this specific enum. |
| `3` | Declined | Declined state/choice in this specific enum. |
| `4` | Authorized | Authorized state/choice in this specific enum. |
| `5` | Settled | Settled state/choice in this specific enum. |
| `6` | Refunded | Refunded state/choice in this specific enum. |
| `7` | Failed | Failed state/choice in this specific enum. |

## FavoriteDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | No further constraint recorded |
| `address` | `string` | Yes | Not declared nullable | Address text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `latitude` | `number (double)` | No | Explicitly allowed | Latitude in degrees for the location represented by this model. | No further constraint recorded |
| `longitude` | `number (double)` | No | Explicitly allowed | Longitude in degrees for the location represented by this model. | No further constraint recorded |
| `placeId` | `string` | No | Explicitly allowed | Identifier of the related place record in this model; ownership and scope are checked separately. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FeatureAvailability

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Unavailable | Unavailable state/choice in this specific enum. |
| `1` | Available | Available state/choice in this specific enum. |
| `2` | LimitedRollout | Limited rollout state/choice in this specific enum. |
| `3` | Maintenance | Maintenance state/choice in this specific enum. |

## FeaturePolicyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `key` | `string` | Yes | Not declared nullable | Key text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `owner` | `string` | Yes | Not declared nullable | Owner text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `customerLabel` | `string` | Yes | Not declared nullable | Customer label text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `availability` | [FeatureAvailability](f.md#featureavailability) | Yes | Not declared nullable | Availability represented by the `FeatureAvailability` model or enum; use that definition's fields/values. | No further constraint recorded |
| `available` | `boolean` | Yes | Not declared nullable | Whether available applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `configuredEnabled` | `boolean` | Yes | Not declared nullable | Whether configured enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `destructive` | `boolean` | Yes | Not declared nullable | Whether destructive applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `rolloutPercentage` | `integer (int32)` | Yes | Not declared nullable | Numeric rollout percentage for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `killSwitch` | `boolean` | Yes | Not declared nullable | Whether kill switch applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `maintenance` | `boolean` | Yes | Not declared nullable | Whether maintenance applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `availabilityLabel` | `string` | Yes | Not declared nullable | Availability label text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `legalProviderDependencies` | `string[]` | Yes | Not declared nullable | Collection of legal provider dependencies for this model; interpret each item through the declared item type. | No further constraint recorded |
| `unmetDependencies` | `string[]` | Yes | Not declared nullable | Collection of unmet dependencies for this model; interpret each item through the declared item type. | No further constraint recorded |
| `rollbackReference` | `string` | No | Explicitly allowed | Rollback reference text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `policyVersion` | `string` | Yes | Not declared nullable | Policy revision used for this assessment; not the mobile app build number. | No further constraint recorded |
| `evaluatedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for evaluated at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FeaturePolicyEnvelopeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `generatedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for generated at; parse strictly and localize only for display. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |
| `policyVersion` | `string` | Yes | Not declared nullable | Policy revision used for this assessment; not the mobile app build number. | No further constraint recorded |
| `policies` | [FeaturePolicyDto](f.md#featurepolicydto)[] | Yes | Not declared nullable | Collection of policies for this model; interpret each item through the declared item type. | No further constraint recorded |
| `policyToken` | `string` | Yes | Not declared nullable | Private policy token used by this specific ceremony; never log, publish or substitute it for another proof. | No further constraint recorded |
| `deliveries` | `boolean` | Yes | Not declared nullable | Whether deliveries applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `cashouts` | `boolean` | Yes | Not declared nullable | Whether cashouts applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `promos` | `boolean` | Yes | Not declared nullable | Whether promos applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `riderIdentityVerificationRequired` | `boolean` | Yes | Not declared nullable | Whether rider identity verification required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FeeProductDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | No further constraint recorded |
| `type` | [GlobalProductType](g.md#globalproducttype) | Yes | Not declared nullable | Type represented by the `GlobalProductType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `feeMinor` | `integer (int64)` | Yes | Not declared nullable | Fee for the applicable default product/plan period, in the stated currency's integer minor units. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `validityDays` | `integer (int32)` | No | Explicitly allowed | Validity, measured in days under this workflow's calendar rules. | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FeePurchaseDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `productCode` | `string` | Yes | Not declared nullable | Product code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `type` | [GlobalProductType](g.md#globalproducttype) | Yes | Not declared nullable | Type represented by the `GlobalProductType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `purchasedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for purchased at; parse strictly and localize only for display. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FinancialHistoryDisputeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `ticketId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related ticket record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `ticketReferenceCode` | `string` | Yes | Not declared nullable | Ticket reference code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FinancialHistoryDisputeRequestDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `source` | [FinancialHistoryEntrySource](f.md#financialhistoryentrysource) | Yes | Not declared nullable | Source represented by the `FinancialHistoryEntrySource` model or enum; use that definition's fields/values. | No further constraint recorded |
| `message` | `string` | No | Explicitly allowed | Message text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `priority` | `string` | No | Explicitly allowed | Priority text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `attachmentFileRefs` | `string[]` | No | Explicitly allowed | Collection of attachment file refs for this model; interpret each item through the declared item type. | No further constraint recorded |
| `issueType` | `string` | No | Explicitly allowed | Issue type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FinancialHistoryEntryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `source` | [FinancialHistoryEntrySource](f.md#financialhistoryentrysource) | Yes | Not declared nullable | Source represented by the `FinancialHistoryEntrySource` model or enum; use that definition's fields/values. | No further constraint recorded |
| `occurredAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for occurred at; parse strictly and localize only for display. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | No further constraint recorded |
| `walletTransactionType` | [WalletTransactionType](w.md#wallettransactiontype) | No | Not declared nullable | Wallet transaction type represented by the `WalletTransactionType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `walletDirection` | [WalletTransactionDirection](w.md#wallettransactiondirection) | No | Not declared nullable | Wallet direction represented by the `WalletTransactionDirection` model or enum; use that definition's fields/values. | No further constraint recorded |
| `balanceAfterMinor` | `integer (int64)` | No | Explicitly allowed | Balance after in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `paymentStatus` | [PaymentStatus](p.md#paymentstatus) | No | Not declared nullable | Payment status represented by the `PaymentStatus` model or enum; use that definition's fields/values. | No further constraint recorded |
| `refundedAmountMinor` | `integer (int64)` | No | Explicitly allowed | Refunded amount in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `paymentMethod` | [PaymentMethod](p.md#paymentmethod) | No | Not declared nullable | Payment method enum; availability and settlement rules are checked separately. | No further constraint recorded |
| `providerName` | `string` | No | Explicitly allowed | Provider name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `reference` | `string` | No | Explicitly allowed | Reference text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | No further constraint recorded |
| `paymentEntityType` | [PaymentEntityType](p.md#paymententitytype) | No | Not declared nullable | Payment entity type represented by the `PaymentEntityType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `entityId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related entity record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `billingTermDays` | `integer (int32)` | No | Explicitly allowed | Billing term, measured in days under this workflow's calendar rules. | No further constraint recorded |
| `servicePeriodStartUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for service period start; parse strictly and localize only for display. | No further constraint recorded |
| `servicePeriodEndUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for service period end; parse strictly and localize only for display. | No further constraint recorded |
| `canOpenDispute` | `boolean` | Yes | Not declared nullable | Whether can open dispute applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `statusCode` | `string` | No | Explicitly allowed | Status code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `feeMinor` | `integer (int64)` | No | Not declared nullable | Fee for the applicable default product/plan period, in the stated currency's integer minor units. | No further constraint recorded |
| `originalCurrency` | `string` | No | Explicitly allowed | Original currency text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `senderDisplayName` | `string` | No | Explicitly allowed | Sender display name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `recipientDisplayName` | `string` | No | Explicitly allowed | Recipient display name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `originatingIpAddress` | `string` | No | Explicitly allowed | Originating ip address text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `deviceDetails` | `string` | No | Explicitly allowed | Device details text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `walletMovement` | [WalletMovementEvidenceDto](w.md#walletmovementevidencedto) | No | Not declared nullable | Wallet movement represented by the `WalletMovementEvidenceDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `conversion` | [PaymentConversionEvidenceDto](p.md#paymentconversionevidencedto) | No | Not declared nullable | Conversion represented by the `PaymentConversionEvidenceDto` model or enum; use that definition's fields/values. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FinancialHistoryEntrySource

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Unknown | Unknown state/choice in this specific enum. |
| `1` | WalletLedger | Wallet ledger state/choice in this specific enum. |
| `2` | ExternalPayment | External payment state/choice in this specific enum. |

## FinancialHistoryPageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `items` | [FinancialHistoryEntryDto](f.md#financialhistoryentrydto)[] | Yes | Not declared nullable | Records returned in this collection/page, each using the referenced item model. | No further constraint recorded |
| `totalCount` | `integer (int64)` | Yes | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | No further constraint recorded |
| `walletLedgerCount` | `integer (int64)` | Yes | Not declared nullable | Number of wallet ledger in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `externalPaymentCount` | `integer (int64)` | Yes | Not declared nullable | Number of external payment in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `hasMore` | `boolean` | Yes | Not declared nullable | Whether the seek-paged result indicates more records after this page. | No further constraint recorded |
| `balance` | [WalletBalanceContextDto](w.md#walletbalancecontextdto) | Yes | Not declared nullable | Balance represented by the `WalletBalanceContextDto` model or enum; use that definition's fields/values. | No further constraint recorded |
| `preset` | `string` | Yes | Not declared nullable | Named range/filter preset accepted by this endpoint; explicit date bounds have separate semantics. | No further constraint recorded |
| `timezone` | `string` | Yes | Not declared nullable | Timezone context used by this contract; apply documented IANA/display semantics. | No further constraint recorded |
| `fromUtc` | `string (date-time)` | Yes | Not declared nullable | UTC start of the requested range; apply this endpoint's inclusion/validation rules. | No further constraint recorded |
| `toUtc` | `string (date-time)` | Yes | Not declared nullable | UTC end of the requested range; apply this endpoint's inclusion/validation rules. | No further constraint recorded |
| `snapshotAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for snapshot at; parse strictly and localize only for display. | No further constraint recorded |
| `page` | `integer (int32)` | Yes | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | `integer (int32)` | Yes | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `totalPages` | `integer (int64)` | Yes | Not declared nullable | Number of pages represented by this page-number model. | No further constraint recorded |
| `postingSequenceCutoff` | `integer (int64)` | No | Not declared nullable | Numeric posting sequence cutoff for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FinancialNextActionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `deepLink` | `string` | Yes | Not declared nullable | Deep link text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `earliestRetryAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for earliest retry at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## FinancialOperationOutcomeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `state` | `string` | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | No further constraint recorded |
| `previousActionCommitted` | `boolean` | Yes | Not declared nullable | Whether previous action committed applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `safeToSubmitAgain` | `boolean` | Yes | Not declared nullable | Whether safe to submit again applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `supportReference` | `string` | Yes | Not declared nullable | Support reference text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `stateRevision` | `integer (int64)` | Yes | Not declared nullable | Revision of the returned state snapshot, distinct from a display timestamp. | No further constraint recorded |
| `nextAction` | [FinancialNextActionDto](f.md#financialnextactiondto) | Yes | Not declared nullable | Suggested next workflow step returned by the server; it does not override authorization. | No further constraint recorded |
| `workflowState` | `string` | No | Explicitly allowed | Workflow state text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
