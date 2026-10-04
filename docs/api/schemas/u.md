# Field dictionary: U

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

## UpdateContactDetailsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `email` | `string` | No | Explicitly allowed | Email address for this model's person/destination; its presence does not prove verification. | No further constraint recorded |
| `phoneNumber` | `string` | No | Explicitly allowed | Country-aware contact number; its presence does not prove verification or provider provisioning. | No further constraint recorded |
| `requestEmailVerification` | `boolean` | No | Not declared nullable | Whether request email verification applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateDriverAssistanceCapabilityDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `acceptsAssistedRides` | `boolean` | Yes | Not declared nullable | Whether accepts assisted rides applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `canAssistBoarding` | `boolean` | Yes | Not declared nullable | Whether can assist boarding applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `acceptsServiceAnimals` | `boolean` | Yes | Not declared nullable | Whether accepts service animals applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `supportsHearingCommunication` | `boolean` | Yes | Not declared nullable | Whether supports hearing communication applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `supportsVisionCommunication` | `boolean` | Yes | Not declared nullable | Whether supports vision communication applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | No | Explicitly allowed | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateDriverRideAlertPreferencesDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `isEnabled` | `boolean` | Yes | Not declared nullable | Whether is enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `minimumFareMinor` | `integer (int64)` | No | Explicitly allowed | Minimum fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `maximumFareMinor` | `integer (int64)` | No | Explicitly allowed | Maximum fare in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `maximumTripDistanceMeters` | `integer (int32)` | No | Explicitly allowed | Maximum trip distance, measured in metres. | No further constraint recorded |
| `standardTrips` | `boolean` | Yes | Not declared nullable | Whether standard trips applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `airportTrips` | `boolean` | Yes | Not declared nullable | Whether airport trips applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `petFriendlyTrips` | `boolean` | Yes | Not declared nullable | Whether pet friendly trips applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `childSeatTrips` | `boolean` | Yes | Not declared nullable | Whether child seat trips applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `wheelchairAccessibleTrips` | `boolean` | Yes | Not declared nullable | Whether wheelchair accessible trips applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `vehicleCategoryIds` | `string (uuid)[]` | No | Explicitly allowed | Identifiers of the related vehicle category records; each remains subject to scope/relationship checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateNotificationPreferencesDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `rides` | `boolean` | Yes | Not declared nullable | Whether rides applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `driverBidAlerts` | `boolean` | No | Explicitly allowed | Whether driver bid alerts applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `deliveries` | `boolean` | Yes | Not declared nullable | Whether deliveries applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `wallet` | `boolean` | Yes | Not declared nullable | Whether wallet applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `promotions` | `boolean` | Yes | Not declared nullable | Whether promotions applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `tripCalls` | `boolean` | No | Explicitly allowed | Whether trip calls applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `tripStatus` | `boolean` | No | Explicitly allowed | Whether trip status applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `chat` | `boolean` | No | Explicitly allowed | Whether chat applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `walletAndMembership` | `boolean` | No | Explicitly allowed | Whether wallet and membership applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `vibration` | `boolean` | No | Explicitly allowed | Whether vibration applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `readAloud` | `boolean` | No | Explicitly allowed | Whether read aloud applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `quietHoursStartMinutes` | `integer (int32)` | No | Explicitly allowed | Quiet hours start, measured in minutes. | No further constraint recorded |
| `quietHoursEndMinutes` | `integer (int32)` | No | Explicitly allowed | Quiet hours end, measured in minutes. | No further constraint recorded |
| `quietHoursTimeZone` | `string` | No | Explicitly allowed | Quiet hours time zone text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateRentalBookingStatusDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `status` | [RentalBookingStatus](r.md#rentalbookingstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `reason` | `string` | No | Explicitly allowed | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | No further constraint recorded |
| `expectedVersion` | `integer (int32)` | Yes | Not declared nullable | Expected version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `reasonCode` | `string` | No | Explicitly allowed | Stable reason code; map through the applicable reason catalog instead of displaying an unrelated enum. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateRentalOrganizationProfileImageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `fileRef` | `string` | Yes | Not declared nullable | Private storage reference; not a permanent public URL or approval decision. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateRentalOrganizationSettingsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `legalName` | `string` | Yes | Not declared nullable | Legal name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `tradingName` | `string` | No | Explicitly allowed | Trading name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `registrationNumber` | `string` | No | Explicitly allowed | Registration number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `taxNumber` | `string` | No | Explicitly allowed | Tax number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `contactEmail` | `string` | Yes | Not declared nullable | Contact email text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `contactPhone` | `string` | Yes | Not declared nullable | Contact phone text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `websiteUrl` | `string` | No | Explicitly allowed | URL for website; validate the intended origin/access and never assume private links are public. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateRentalTeamMemberDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `role` | [RentalOrganizationRole](r.md#rentalorganizationrole) | Yes | Not declared nullable | Role represented by the `RentalOrganizationRole` model or enum; use that definition's fields/values. | No further constraint recorded |
| `permissions` | [RentalOrganizationPermission](r.md#rentalorganizationpermission) | Yes | Not declared nullable | Permissions represented by the `RentalOrganizationPermission` model or enum; use that definition's fields/values. | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateRentalVehicleDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `branchId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related branch record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `make` | `string` | Yes | Not declared nullable | Vehicle manufacturer name/catalog selection. | No further constraint recorded |
| `model` | `string` | Yes | Not declared nullable | Model in the owning domain; for vehicle contracts, the vehicle model associated with the manufacturer. | No further constraint recorded |
| `year` | `integer (int32)` | Yes | Not declared nullable | Numeric year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `category` | `string` | Yes | Not declared nullable | Category text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `transmission` | `string` | Yes | Not declared nullable | Transmission text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `fuelType` | `string` | Yes | Not declared nullable | Fuel type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `seats` | `integer (int32)` | Yes | Not declared nullable | Numeric seats for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `color` | `string` | Yes | Not declared nullable | Color text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `plateNumber` | `string` | Yes | Not declared nullable | Country-specific vehicle registration plate; validate through the applicable country workflow. | No further constraint recorded |
| `dailyRateMinor` | `integer (int64)` | Yes | Not declared nullable | Daily rate in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `weeklyRateMinor` | `integer (int64)` | No | Explicitly allowed | Weekly rate in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `securityDepositMinor` | `integer (int64)` | Yes | Not declared nullable | Security deposit in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `bookingMode` | [RentalBookingMode](r.md#rentalbookingmode) | Yes | Not declared nullable | Booking mode represented by the `RentalBookingMode` model or enum; use that definition's fields/values. | No further constraint recorded |
| `distanceUnit` | `string` | Yes | Not declared nullable | Distance unit text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `includedDistancePerDay` | `integer (int32)` | Yes | Not declared nullable | Numeric included distance per day for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `extraKilometerRateMinor` | `integer (int64)` | Yes | Not declared nullable | Extra kilometer rate in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `handoverMode` | [RentalVehicleHandoverMode](r.md#rentalvehiclehandovermode) | Yes | Not declared nullable | Handover mode represented by the `RentalVehicleHandoverMode` model or enum; use that definition's fields/values. | No further constraint recorded |
| `pickupFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Pickup fee in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `deliveryFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Delivery fee in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `serviceRadius` | `integer (int32)` | Yes | Not declared nullable | Numeric service radius for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `lateGraceMinutes` | `integer (int32)` | Yes | Not declared nullable | Late grace, measured in minutes. | No further constraint recorded |
| `lateFeePerHourMinor` | `integer (int64)` | Yes | Not declared nullable | Late fee per hour in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `registrationExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for registration expires at; parse strictly and localize only for display. | No further constraint recorded |
| `insuranceExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for insurance expires at; parse strictly and localize only for display. | No further constraint recorded |
| `fitnessExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for fitness expires at; parse strictly and localize only for display. | No further constraint recorded |
| `complianceReminderDays` | `integer (int32)` | Yes | Not declared nullable | Compliance reminder, measured in days under this workflow's calendar rules. | No further constraint recorded |
| `expectedPolicyVersion` | `integer (int32)` | Yes | Not declared nullable | Expected policy version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `policyConfirmed` | `boolean` | Yes | Not declared nullable | Whether policy confirmed applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateRideFareDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `proposedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Rider's proposed fare in currency minor units, subject to applicable quote and marketplace rules. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateRiderAssistanceProfileDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `isEnabled` | `boolean` | Yes | Not declared nullable | Whether is enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `mobilityCode` | `string` | Yes | Not declared nullable | Mobility code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `wheelchairWidthMillimeters` | `integer (int32)` | No | Explicitly allowed | Numeric wheelchair width millimeters for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `wheelchairLengthMillimeters` | `integer (int32)` | No | Explicitly allowed | Numeric wheelchair length millimeters for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `wheelchairCombinedWeightKilograms` | `integer (int32)` | No | Explicitly allowed | Numeric wheelchair combined weight kilograms for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `serviceAnimal` | `boolean` | Yes | Not declared nullable | Whether service animal applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `hearingCommunicationCode` | `string` | Yes | Not declared nullable | Hearing communication code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `visionCommunicationCode` | `string` | Yes | Not declared nullable | Vision communication code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `communicationCode` | `string` | Yes | Not declared nullable | Communication code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `extraBoardingMinutes` | `integer (int32)` | Yes | Not declared nullable | Extra boarding, measured in minutes. | No further constraint recorded |
| `caregiverName` | `string` | No | Explicitly allowed | Caregiver name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `caregiverContact` | `string` | No | Explicitly allowed | Caregiver contact text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `caregiverTripNotificationsEnabled` | `boolean` | Yes | Not declared nullable | Whether caregiver trip notifications enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | No | Explicitly allowed | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateTravelCostCenterDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | No further constraint recorded |
| `monthlyBudgetMinor` | `integer (int64)` | Yes | Not declared nullable | Monthly budget in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | Yes | Not declared nullable | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateTravelMemberDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | No further constraint recorded |
| `role` | `string` | Yes | Not declared nullable | Role text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `relationship` | `string` | No | Explicitly allowed | Relationship text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `employeeCode` | `string` | No | Explicitly allowed | Employee code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `defaultCostCenterId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related default cost center record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `canBook` | `boolean` | Yes | Not declared nullable | Whether can book applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `canViewLiveTrips` | `boolean` | Yes | Not declared nullable | Whether can view live trips applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `canManageMembers` | `boolean` | Yes | Not declared nullable | Whether can manage members applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `canManageBilling` | `boolean` | Yes | Not declared nullable | Whether can manage billing applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `perRideLimitMinor` | `integer (int64)` | Yes | Not declared nullable | Per ride limit in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `monthlyLimitMinor` | `integer (int64)` | Yes | Not declared nullable | Monthly limit in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | Yes | Not declared nullable | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateTravelProfileDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | No further constraint recorded |
| `centralBillingEnabled` | `boolean` | Yes | Not declared nullable | Whether central billing enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `monthlyBudgetMinor` | `integer (int64)` | Yes | Not declared nullable | Monthly budget in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `allowDelegatedBooking` | `boolean` | Yes | Not declared nullable | Whether allow delegated booking applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `liveTrackingEnabled` | `boolean` | Yes | Not declared nullable | Whether live tracking enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `notifyRideCreated` | `boolean` | Yes | Not declared nullable | Whether notify ride created applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `notifyDriverAssigned` | `boolean` | Yes | Not declared nullable | Whether notify driver assigned applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `notifyTripStarted` | `boolean` | Yes | Not declared nullable | Whether notify trip started applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `notifyTripCompleted` | `boolean` | Yes | Not declared nullable | Whether notify trip completed applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `notifyTripCancelled` | `boolean` | Yes | Not declared nullable | Whether notify trip cancelled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `notifyByPush` | `boolean` | Yes | Not declared nullable | Whether notify by push applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `notifyByEmail` | `boolean` | Yes | Not declared nullable | Whether notify by email applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `notifyBySms` | `boolean` | Yes | Not declared nullable | Whether notify by sms applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | Yes | Not declared nullable | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpdateVehicleDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `make` | `string` | Yes | Not declared nullable | Vehicle manufacturer name/catalog selection. | No further constraint recorded |
| `model` | `string` | Yes | Not declared nullable | Model in the owning domain; for vehicle contracts, the vehicle model associated with the manufacturer. | No further constraint recorded |
| `year` | `integer (int32)` | Yes | Not declared nullable | Numeric year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `color` | `string` | Yes | Not declared nullable | Color text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `plateNumber` | `string` | Yes | Not declared nullable | Country-specific vehicle registration plate; validate through the applicable country workflow. | No further constraint recorded |
| `vehicleCategoryId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related vehicle category record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `allowsPets` | `boolean` | No | Not declared nullable | Whether allows pets applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `childSeatCapacity` | `integer (int32)` | No | Not declared nullable | Numeric child seat capacity for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `isWheelchairAccessible` | `boolean` | No | Not declared nullable | Whether is wheelchair accessible applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `isAirportPickupEligible` | `boolean` | No | Not declared nullable | Whether is airport pickup eligible applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `interiorImageFileRef` | `string` | No | Explicitly allowed | Interior image file ref text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `frontExteriorImageFileRef` | `string` | No | Explicitly allowed | Front exterior image file ref text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UploadDocumentDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `type` | [DocumentType](d.md#documenttype) | Yes | Not declared nullable | Type represented by the `DocumentType` model or enum; use that definition's fields/values. | No further constraint recorded |
| `fileRef` | `string` | Yes | Not declared nullable | Private storage reference; not a permanent public URL or approval decision. | No further constraint recorded |
| `fileName` | `string` | Yes | Not declared nullable | Document/file display name; it is not a storage authorization or approved-document status. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `vehicleId` | `string (uuid)` | No | Explicitly allowed | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `driverLicenseNumber` | `string` | No | Explicitly allowed | Driver license number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `driverLicenseControlNumber` | `string` | No | Explicitly allowed | Driver license control number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `driverLicenseOriginalIssueDate` | `string (date)` | No | Explicitly allowed | Calendar date for driver license original issue date; preserve date-only semantics rather than shifting it through a timezone. | No further constraint recorded |
| `driverLicenseExpiresOn` | `string (date)` | No | Explicitly allowed | Calendar date for driver license expires on; preserve date-only semantics rather than shifting it through a timezone. | No further constraint recorded |
| `onboardingSubmission` | `boolean` | No | Not declared nullable | Whether onboarding submission applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpsertBusinessShippingMemberDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `userId` | `string (uuid)` | Yes | Not declared nullable | Related account identity; the server still proves the caller's ownership or permitted relationship. | No further constraint recorded |
| `role` | `string` | Yes | Not declared nullable | Role text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `canCreateOrders` | `boolean` | Yes | Not declared nullable | Whether can create orders applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `canViewBilling` | `boolean` | Yes | Not declared nullable | Whether can view billing applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `canManageMembers` | `boolean` | Yes | Not declared nullable | Whether can manage members applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpsertCorporateMemberDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `userId` | `string (uuid)` | Yes | Not declared nullable | Related account identity; the server still proves the caller's ownership or permitted relationship. | No further constraint recorded |
| `role` | [CorporateMemberRole](c.md#corporatememberrole) | Yes | Not declared nullable | Role represented by the `CorporateMemberRole` model or enum; use that definition's fields/values. | No further constraint recorded |
| `permissions` | [CorporateMemberPermission](c.md#corporatememberpermission) | Yes | Not declared nullable | Permissions represented by the `CorporateMemberPermission` model or enum; use that definition's fields/values. | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | No further constraint recorded |
| `authorityExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for authority expires at; parse strictly and localize only for display. | No further constraint recorded |
| `expectedAccountRevision` | `integer (int64)` | Yes | Not declared nullable | Expected account revision for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpsertHouseholdMemberDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `userId` | `string (uuid)` | Yes | Not declared nullable | Related account identity; the server still proves the caller's ownership or permitted relationship. | No further constraint recorded |
| `role` | [HouseholdMemberRole](h.md#householdmemberrole) | Yes | Not declared nullable | Role represented by the `HouseholdMemberRole` model or enum; use that definition's fields/values. | No further constraint recorded |
| `perTransactionLimitMinor` | `integer (int64)` | Yes | Not declared nullable | Per transaction limit in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `dailyLimitMinor` | `integer (int64)` | Yes | Not declared nullable | Daily limit in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `canBook` | `boolean` | Yes | Not declared nullable | Whether can book applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `canApprove` | `boolean` | Yes | Not declared nullable | Whether can approve applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `authorityExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for authority expires at; parse strictly and localize only for display. | No further constraint recorded |
| `expectedHouseholdRevision` | `integer (int64)` | Yes | Not declared nullable | Expected household revision for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UpsertRecurringRideDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `pickupLatitude` | `number (double)` | Yes | Not declared nullable | Pickup latitude in degrees; latitude is separate from address text. | No further constraint recorded |
| `pickupLongitude` | `number (double)` | Yes | Not declared nullable | Pickup longitude in degrees; preserve coordinate order. | No further constraint recorded |
| `pickupAddress` | `string` | Yes | Not declared nullable | Human pickup-address text accompanying the structured location. | No further constraint recorded |
| `dropoffLatitude` | `number (double)` | Yes | Not declared nullable | Destination latitude in degrees. | No further constraint recorded |
| `dropoffLongitude` | `number (double)` | Yes | Not declared nullable | Destination longitude in degrees. | No further constraint recorded |
| `dropoffAddress` | `string` | Yes | Not declared nullable | Human destination-address text accompanying the structured location. | No further constraint recorded |
| `distanceMeters` | `integer (int32)` | No | Explicitly allowed | Distance represented by this model, in metres; its source/assessment depends on the operation. | No further constraint recorded |
| `estimatedDurationSeconds` | `integer (int32)` | No | Explicitly allowed | Estimated duration in seconds; an estimate is not actual elapsed trip time. | No further constraint recorded |
| `weekdays` | [WeekdayFlags](w.md#weekdayflags) | Yes | Not declared nullable | Weekdays represented by the `WeekdayFlags` model or enum; use that definition's fields/values. | No further constraint recorded |
| `pickupTime` | `string (time)` | Yes | Not declared nullable | Pickup time text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `vehicleCategoryId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related vehicle category record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `proposedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Rider's proposed fare in currency minor units, subject to applicable quote and marketplace rules. | No further constraint recorded |
| `passengerCount` | `integer (int32)` | Yes | Not declared nullable | Number of passenger in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | No further constraint recorded |
| `pickupPlaceId` | `string` | No | Explicitly allowed | Identifier of the related pickup place record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `dropoffPlaceId` | `string` | No | Explicitly allowed | Identifier of the related dropoff place record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## User

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `friendlyUserId` | `string` | No | Explicitly allowed | Identifier of the related friendly user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `role` | [UserRole](u.md#userrole) | No | Not declared nullable | Role represented by the `UserRole` model or enum; use that definition's fields/values. | No further constraint recorded |
| `status` | [UserStatus](u.md#userstatus) | No | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `firstName` | `string` | No | Explicitly allowed | Person's given name as provided through the applicable profile/identity workflow. | No further constraint recorded |
| `lastName` | `string` | No | Explicitly allowed | Person's family name as provided through the applicable profile/identity workflow. | No further constraint recorded |
| `avatarStorageKey` | `string` | No | Explicitly allowed | Avatar storage key text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `dateOfBirth` | `string (date)` | No | Explicitly allowed | Calendar date for date of birth; preserve date-only semantics rather than shifting it through a timezone. | No further constraint recorded |
| `gender` | `string` | No | Explicitly allowed | Gender text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `identityVerifiedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for identity verified at; parse strictly and localize only for display. | No further constraint recorded |
| `email` | `string` | No | Explicitly allowed | Email address for this model's person/destination; its presence does not prove verification. | No further constraint recorded |
| `emailVerifiedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for email verified at; parse strictly and localize only for display. | No further constraint recorded |
| `loginEmailNotificationsEnabled` | `boolean` | No | Not declared nullable | Whether login email notifications enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `phoneNumber` | `string` | No | Explicitly allowed | Country-aware contact number; its presence does not prove verification or provider provisioning. | No further constraint recorded |
| `phoneVerifiedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for phone verified at; parse strictly and localize only for display. | No further constraint recorded |
| `riderOnboardingPolicyVersion` | `integer (int32)` | No | Not declared nullable | Rider onboarding policy version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `riderPhoneOnboardingDecision` | `string` | No | Explicitly allowed | Rider phone onboarding decision text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `riderPhoneOnboardingDecisionAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for rider phone onboarding decision at; parse strictly and localize only for display. | No further constraint recorded |
| `riderProfilePhotoOnboardingPolicyVersion` | `integer (int32)` | No | Not declared nullable | Rider profile photo onboarding policy version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `riderProfilePhotoSkippedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for rider profile photo skipped at; parse strictly and localize only for display. | No further constraint recorded |
| `countryCode` | `string` | No | Explicitly allowed | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |
| `currency` | `string` | No | Explicitly allowed | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `timezone` | `string` | No | Explicitly allowed | Timezone context used by this contract; apply documented IANA/display semantics. | No further constraint recorded |
| `preferredLanguage` | `string` | No | Explicitly allowed | Preferred language text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `passwordHash` | `string` | No | Explicitly allowed | Password hash text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `passwordSetDeadlineUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for password set deadline; parse strictly and localize only for display. | No further constraint recorded |
| `twoFactorEnabled` | `boolean` | No | Not declared nullable | Whether two factor enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `twoFactorRequired` | `boolean` | No | Not declared nullable | Whether two factor required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `twoFactorSecret` | `string` | No | Explicitly allowed | Private two factor secret used by this specific ceremony; never log, publish or substitute it for another proof. | No further constraint recorded |
| `twoFactorMethod` | `string` | No | Explicitly allowed | Two factor method text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `tokenVersion` | `integer (int32)` | No | Not declared nullable | Token version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `failedLoginCount` | `integer (int32)` | No | Not declared nullable | Number of failed login in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `lockoutUntilUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for lockout until; parse strictly and localize only for display. | No further constraint recorded |
| `lastLoginAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last login at; parse strictly and localize only for display. | No further constraint recorded |
| `deletedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for deleted at; parse strictly and localize only for display. | No further constraint recorded |
| `referralCode` | `string` | No | Explicitly allowed | Referral code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `referredByUserId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related referred by user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `membershipPlanId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related membership plan record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `membershipExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for membership expires at; parse strictly and localize only for display. | No further constraint recorded |
| `autoRenewMembership` | `boolean` | No | Not declared nullable | Whether auto renew membership applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `driverProfile` | [DriverProfile](d.md#driverprofile) | No | Not declared nullable | Driver profile represented by the `DriverProfile` model or enum; use that definition's fields/values. | No further constraint recorded |
| `wallet` | [Wallet](w.md#wallet) | No | Not declared nullable | Wallet represented by the `Wallet` model or enum; use that definition's fields/values. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UserActivityDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `activity` | `string` | Yes | Not declared nullable | Activity text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `outcome` | `string` | Yes | Not declared nullable | Result/recovery state of this operation; unknown or pending is not failed or successful. | No further constraint recorded |
| `dateUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for date; parse strictly and localize only for display. | No further constraint recorded |
| `source` | `string` | Yes | Not declared nullable | Source text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `deviceId` | `string` | No | Explicitly allowed | Identifier of the related device record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `deviceName` | `string` | No | Explicitly allowed | Device name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `deviceManufacturer` | `string` | No | Explicitly allowed | Device manufacturer text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `deviceModel` | `string` | No | Explicitly allowed | Device model text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `operatingSystem` | `string` | No | Explicitly allowed | Operating system text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `appVersion` | `string` | No | Explicitly allowed | App version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `ipAddress` | `string` | No | Explicitly allowed | Ip address text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `userAgent` | `string` | No | Explicitly allowed | User agent text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `authenticationMethod` | `string` | No | Explicitly allowed | Authentication method text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `countryCode` | `string` | No | Explicitly allowed | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |
| `tenantSlug` | `string` | No | Explicitly allowed | Tenant slug text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `correlationId` | `string` | No | Explicitly allowed | Safe request correlation reference; not an access token or proof of success. | No further constraint recorded |
| `riskLevel` | `string` | Yes | Not declared nullable | Risk level text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `detailsJson` | `string` | No | Explicitly allowed | Details json text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UserActivityDtoPagedResult

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `items` | [UserActivityDto](u.md#useractivitydto)[] | No | Explicitly allowed | Records returned in this collection/page, each using the referenced item model. | No further constraint recorded |
| `page` | `integer (int32)` | No | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | No further constraint recorded |
| `pageSize` | `integer (int32)` | No | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | No further constraint recorded |
| `totalCount` | `integer (int64)` | No | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | No further constraint recorded |
| `totalPages` | `integer (int32)` | No | Not declared nullable | Number of pages represented by this page-number model. | readOnly: `True` |
| `hasPreviousPage` | `boolean` | No | Not declared nullable | Whether has previous page applies in this model's context. This flag does not replace server permission or lifecycle checks. | readOnly: `True` |
| `hasNextPage` | `boolean` | No | Not declared nullable | Whether has next page applies in this model's context. This flag does not replace server permission or lifecycle checks. | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## UserBlockDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `blockId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related block record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `identifierType` | `string` | Yes | Not declared nullable | Identifier type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `identifierDisplay` | `string` | Yes | Not declared nullable | Identifier display text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `blockedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for blocked at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UserDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `role` | [UserRole](u.md#userrole) | Yes | Not declared nullable | Role represented by the `UserRole` model or enum; use that definition's fields/values. | No further constraint recorded |
| `firstName` | `string` | Yes | Not declared nullable | Person's given name as provided through the applicable profile/identity workflow. | No further constraint recorded |
| `lastName` | `string` | Yes | Not declared nullable | Person's family name as provided through the applicable profile/identity workflow. | No further constraint recorded |
| `email` | `string` | No | Explicitly allowed | Email address for this model's person/destination; its presence does not prove verification. | No further constraint recorded |
| `phoneNumber` | `string` | No | Explicitly allowed | Country-aware contact number; its presence does not prove verification or provider provisioning. | No further constraint recorded |
| `walletBalanceMinor` | `integer (int64)` | Yes | Not declared nullable | Wallet balance in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |
| `timezone` | `string` | Yes | Not declared nullable | Timezone context used by this contract; apply documented IANA/display semantics. | No further constraint recorded |
| `passwordSetDeadlineUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for password set deadline; parse strictly and localize only for display. | No further constraint recorded |
| `phoneVerified` | `boolean` | No | Not declared nullable | Whether phone verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `identityVerified` | `boolean` | No | Not declared nullable | Whether identity verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `friendlyUserId` | `string` | No | Explicitly allowed | Identifier of the related friendly user record in this model; ownership and scope are checked separately. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UserExternalExperienceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `source` | `string` | Yes | Not declared nullable | Source text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | No further constraint recorded |
| `reviewCount` | `integer (int32)` | Yes | Not declared nullable | Number of review in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `averageRating` | `number (double)` | No | Explicitly allowed | Numeric average rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `positivePercentage` | `number (double)` | No | Explicitly allowed | Numeric positive percentage for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `completedTripCount` | `integer (int32)` | No | Explicitly allowed | Number of completed trip in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `verifiedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for verified at; parse strictly and localize only for display. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `status` | [RatingImportStatus](r.md#ratingimportstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `confidence` | [ExternalEvidenceConfidenceLevel](e.md#externalevidenceconfidencelevel) | Yes | Not declared nullable | Confidence represented by the `ExternalEvidenceConfidenceLevel` model or enum; use that definition's fields/values. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UserReputationAchievementDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `evidence` | `string` | Yes | Not declared nullable | Evidence text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `evidenceCount` | `integer (int32)` | Yes | Not declared nullable | Number of evidence in this model's stated scope; not automatically a global/live total. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UserReputationCategoryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `average` | `number (double)` | Yes | Not declared nullable | Numeric average for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `count` | `integer (int32)` | Yes | Not declared nullable | Numeric count for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UserReputationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `averageStars` | `number (double)` | Yes | Not declared nullable | Numeric average stars for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `reviewCount` | `integer (int32)` | Yes | Not declared nullable | Number of review in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `verifiedCompletedTrips` | `integer (int32)` | Yes | Not declared nullable | Numeric verified completed trips for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `categories` | [UserReputationCategoryDto](u.md#userreputationcategorydto)[] | Yes | Not declared nullable | Collection of categories for this model; interpret each item through the declared item type. | No further constraint recorded |
| `achievements` | [UserReputationAchievementDto](u.md#userreputationachievementdto)[] | Yes | Not declared nullable | Collection of achievements for this model; interpret each item through the declared item type. | No further constraint recorded |
| `recentReviews` | [UserReputationReviewDto](u.md#userreputationreviewdto)[] | Yes | Not declared nullable | Collection of recent reviews for this model; interpret each item through the declared item type. | No further constraint recorded |
| `publicationPolicy` | `string` | Yes | Not declared nullable | Publication policy text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `subjectRole` | `string` | No | Explicitly allowed | Subject role text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `nativeAverageStars` | `number (double)` | No | Not declared nullable | Numeric native average stars for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `nativeReviewCount` | `integer (int32)` | No | Not declared nullable | Number of native review in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `importedAverageStars` | `number (double)` | No | Explicitly allowed | Numeric imported average stars for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `importedReviewCount` | `integer (int32)` | No | Not declared nullable | Number of imported review in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `latestReviewPublishedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for latest review published at; parse strictly and localize only for display. | No further constraint recorded |
| `recentReviewCount` | `integer (int32)` | No | Not declared nullable | Number of recent review in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `recencyWindowDays` | `integer (int32)` | No | Not declared nullable | Recency window, measured in days under this workflow's calendar rules. | No further constraint recorded |
| `verificationBadges` | [UserReputationVerificationBadgeDto](u.md#userreputationverificationbadgedto)[] | No | Explicitly allowed | Collection of verification badges for this model; interpret each item through the declared item type. | No further constraint recorded |
| `externalExperiences` | [UserExternalExperienceDto](u.md#userexternalexperiencedto)[] | No | Explicitly allowed | Collection of external experiences for this model; interpret each item through the declared item type. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UserReputationReviewDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | No further constraint recorded |
| `reviewerName` | `string` | Yes | Not declared nullable | Reviewer name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `stars` | `integer (int32)` | Yes | Not declared nullable | Numeric stars for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `comment` | `string` | No | Explicitly allowed | Comment text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `tags` | `string[]` | Yes | Not declared nullable | Collection of tags for this model; interpret each item through the declared item type. | No further constraint recorded |
| `tripCompletedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for trip completed at; parse strictly and localize only for display. | No further constraint recorded |
| `publishedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for published at; parse strictly and localize only for display. | No further constraint recorded |
| `reviewerRole` | `string` | No | Explicitly allowed | Reviewer role text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UserReputationVerificationBadgeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `verified` | `boolean` | Yes | Not declared nullable | Whether verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `verifiedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for verified at; parse strictly and localize only for display. | No further constraint recorded |
| `validUntilUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for valid until; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UserRole

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Passenger | Passenger state/choice in this specific enum. |
| `2` | Driver | Driver state/choice in this specific enum. |
| `3` | TenantAdmin | Tenant admin state/choice in this specific enum. |
| `4` | SystemAdmin | System admin state/choice in this specific enum. |

## UserSecurityEventDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `eventType` | `string` | Yes | Not declared nullable | Event type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `outcome` | `string` | Yes | Not declared nullable | Result/recovery state of this operation; unknown or pending is not failed or successful. | No further constraint recorded |
| `authenticationMethod` | `string` | No | Explicitly allowed | Authentication method text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `riskLevel` | `string` | Yes | Not declared nullable | Risk level text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `countryCode` | `string` | No | Explicitly allowed | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |
| `tenantSlug` | `string` | No | Explicitly allowed | Tenant slug text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `ipAddress` | `string` | No | Explicitly allowed | Ip address text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `deviceId` | `string` | No | Explicitly allowed | Identifier of the related device record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## UserStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Active | Active state/choice in this specific enum. |
| `2` | Suspended | Suspended state/choice in this specific enum. |
| `3` | Deleted | Deleted state/choice in this specific enum. |
