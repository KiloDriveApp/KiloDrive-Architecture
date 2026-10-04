# Field dictionary: R

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

The explanation basis distinguishes model-specific meaning, shared conventions,
name-derived units and type-only entries awaiting semantic review. See the
[coverage report](../reference/coverage.md); field presence is not semantic completeness.

## Models on this page

- [RateTripDto](#ratetripdto)
- [RatingBreakdownDto](#ratingbreakdowndto)
- [RatingImportDto](#ratingimportdto)
- [RatingImportStatus](#ratingimportstatus)
- [RecentAuthenticationProofDto](#recentauthenticationproofdto)
- [RecentRideLocationDto](#recentridelocationdto)
- [RecordUserSettingChangeDto](#recordusersettingchangedto)
- [RecurringRideDto](#recurringridedto)
- [RecurringRideDtoPagedResult](#recurringridedtopagedresult)
- [RecurringRideOccurrenceDto](#recurringrideoccurrencedto)
- [ReferralSummaryDto](#referralsummarydto)
- [RefreshRequest](#refreshrequest)
- [RegisterDeviceDto](#registerdevicedto)
- [RegisterPushTokenRequest](#registerpushtokenrequest)
- [RegisterRequest](#registerrequest)
- [RegisterVehicleDto](#registervehicledto)
- [RenameSavedCalculationDto](#renamesavedcalculationdto)
- [RenewGuardianConsentDto](#renewguardianconsentdto)
- [RentalAgreementDto](#rentalagreementdto)
- [RentalAgreementStatus](#rentalagreementstatus)
- [RentalAllowedActionDto](#rentalallowedactiondto)
- [RentalAuthorizationEvidence](#rentalauthorizationevidence)
- [RentalAuthorizationState](#rentalauthorizationstate)
- [RentalAvailabilityBlockDto](#rentalavailabilityblockdto)
- [RentalAvailabilityBlockType](#rentalavailabilityblocktype)
- [RentalAvailabilityCalendarDto](#rentalavailabilitycalendardto)
- [RentalAvailabilityPolicyDto](#rentalavailabilitypolicydto)
- [RentalBookingDto](#rentalbookingdto)
- [RentalBookingMode](#rentalbookingmode)
- [RentalBookingOperationsDto](#rentalbookingoperationsdto)
- [RentalBookingStatus](#rentalbookingstatus)
- [RentalBookingStatusContractDto](#rentalbookingstatuscontractdto)
- [RentalBookingStatusDefinitionDto](#rentalbookingstatusdefinitiondto)
- [RentalBranchPublicDto](#rentalbranchpublicdto)
- [RentalCancellationReason](#rentalcancellationreason)
- [RentalCheckoutDto](#rentalcheckoutdto)
- [RentalDamageClaimDto](#rentaldamageclaimdto)
- [RentalDamageClaimStatus](#rentaldamageclaimstatus)
- [RentalDamageReason](#rentaldamagereason)
- [RentalDisputeDto](#rentaldisputedto)
- [RentalDisputeStatus](#rentaldisputestatus)
- [RentalEvidenceInput](#rentalevidenceinput)
- [RentalEvidencePreviewDto](#rentalevidencepreviewdto)
- [RentalExpectedVersionDto](#rentalexpectedversiondto)
- [RentalExtensionDto](#rentalextensiondto)
- [RentalExtensionStatus](#rentalextensionstatus)
- [RentalFleetReminderDto](#rentalfleetreminderdto)
- [RentalInspectionChecklistInput](#rentalinspectionchecklistinput)
- [RentalInspectionChecklistItemDto](#rentalinspectionchecklistitemdto)
- [RentalInspectionDto](#rentalinspectiondto)
- [RentalInspectionPhase](#rentalinspectionphase)
- [RentalInspectionPhotoDto](#rentalinspectionphotodto)
- [RentalInspectionPhotoInput](#rentalinspectionphotoinput)
- [RentalInventoryHoldDto](#rentalinventoryholddto)
- [RentalInventoryHoldState](#rentalinventoryholdstate)
- [RentalLifecycleDto](#rentallifecycledto)
- [RentalLifecycleRequirementDto](#rentallifecyclerequirementdto)
- [RentalMakeModelsDto](#rentalmakemodelsdto)
- [RentalMarketplaceFiltersDto](#rentalmarketplacefiltersdto)
- [RentalMembershipPurchaseDto](#rentalmembershippurchasedto)
- [RentalOrganizationCardDto](#rentalorganizationcarddto)
- [RentalOrganizationCardDtoPagedResult](#rentalorganizationcarddtopagedresult)
- [RentalOrganizationDto](#rentalorganizationdto)
- [RentalOrganizationPermission](#rentalorganizationpermission)
- [RentalOrganizationPublicDto](#rentalorganizationpublicdto)
- [RentalOrganizationRole](#rentalorganizationrole)
- [RentalOrganizationStatus](#rentalorganizationstatus)
- [RentalOwnerAnalyticsDto](#rentalowneranalyticsdto)
- [RentalPartnerBookingDto](#rentalpartnerbookingdto)
- [RentalPartnerBranchDto](#rentalpartnerbranchdto)
- [RentalPartnerVehicleDto](#rentalpartnervehicledto)
- [RentalPartnerVehicleImageDto](#rentalpartnervehicleimagedto)
- [RentalPolicyDto](#rentalpolicydto)
- [RentalPolicySnapshot](#rentalpolicysnapshot)
- [RentalProtectionAcceptanceDto](#rentalprotectionacceptancedto)
- [RentalProviderProtectionDto](#rentalproviderprotectiondto)
- [RentalProviderType](#rentalprovidertype)
- [RentalQuoteDto](#rentalquotedto)
- [RentalTeamDto](#rentalteamdto)
- [RentalTeamInvitationDto](#rentalteaminvitationdto)
- [RentalTeamInvitationStatus](#rentalteaminvitationstatus)
- [RentalTeamMemberDto](#rentalteammemberdto)
- [RentalVehicleCardDto](#rentalvehiclecarddto)
- [RentalVehicleCardDtoPagedResult](#rentalvehiclecarddtopagedresult)
- [RentalVehicleDetailDto](#rentalvehicledetaildto)
- [RentalVehicleHandoverMode](#rentalvehiclehandovermode)
- [RentalVehicleImageDto](#rentalvehicleimagedto)
- [RentalVehicleStatus](#rentalvehiclestatus)
- [ReopenSupportCaseDto](#reopensupportcasedto)
- [ReplySupportTicketDto](#replysupportticketdto)
- [ReportVehicleDefectDto](#reportvehicledefectdto)
- [ReputationCategoryDto](#reputationcategorydto)
- [RequestAccountDeletionDto](#requestaccountdeletiondto)
- [RequestCashoutDto](#requestcashoutdto)
- [RequestEmailLoginDto](#requestemaillogindto)
- [RequestNameChangeDto](#requestnamechangedto)
- [RequestOutOfBandStepUpDto](#requestoutofbandstepupdto)
- [RequestPasswordResetRequest](#requestpasswordresetrequest)
- [RequestPhoneContactVerificationDto](#requestphonecontactverificationdto)
- [RequestPhoneLoginDto](#requestphonelogindto)
- [RequestRatingImportDto](#requestratingimportdto)
- [RequestRentalExtensionDto](#requestrentalextensiondto)
- [RequestRouteAlterationDto](#requestroutealterationdto)
- [RequestTwoFactorLoginCodeRequest](#requesttwofactorlogincoderequest)
- [ResolveVehicleDefectDto](#resolvevehicledefectdto)
- [RespondFareSplitRequest](#respondfaresplitrequest)
- [ReviewAggregateKind](#reviewaggregatekind)
- [ReviewAppealDto](#reviewappealdto)
- [ReviewAppealStatus](#reviewappealstatus)
- [ReviewRentalExtensionDto](#reviewrentalextensiondto)
- [RevokeDependentConsentDto](#revokedependentconsentdto)
- [RideAssistanceDto](#rideassistancedto)
- [RideBidDto](#ridebiddto)
- [RideDispatchMode](#ridedispatchmode)
- [RideFareRouteSource](#ridefareroutesource)
- [RideInquiryMessageDto](#rideinquirymessagedto)
- [RideInquiryThreadDto](#rideinquirythreaddto)
- [RideNoDriverRecoveryAction](#ridenodriverrecoveryaction)
- [RideNoDriverRecoveryActionDecision](#ridenodriverrecoveryactiondecision)
- [RideNoDriverRecoveryProjection](#ridenodriverrecoveryprojection)
- [RideNoDriverRecoveryState](#ridenodriverrecoverystate)
- [RideProductType](#rideproducttype)
- [RideRecoveryExecutionKind](#riderecoveryexecutionkind)
- [RideRequestDto](#riderequestdto)
- [RideRequestDtoPagedResult](#riderequestdtopagedresult)
- [RideRequestStatus](#riderequeststatus)
- [RideSearchMapDto](#ridesearchmapdto)
- [RideStopDto](#ridestopdto)
- [RideStopInputDto](#ridestopinputdto)
- [RideStopStatus](#ridestopstatus)
- [RideStopType](#ridestoptype)
- [RiderAssistanceProfileDto](#riderassistanceprofiledto)
- [RiderEntitlementsDto](#riderentitlementsdto)
- [RiderOnboardingDecisionDto](#rideronboardingdecisiondto)
- [RiderVerificationPolicyDto](#riderverificationpolicydto)
- [RiderVerificationState](#riderverificationstate)
- [RouteDeviationAlertDto](#routedeviationalertdto)
- [RouteDeviationResponseRequest](#routedeviationresponserequest)

## RateTripDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `stars` | `integer (int32)` | Yes | Not declared nullable | Numeric stars for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `comment` | `string` | No | Explicitly allowed | Comment text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `driving` | `integer (int32)` | No | Explicitly allowed | Numeric driving for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `courtesy` | `integer (int32)` | No | Explicitly allowed | Numeric courtesy for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `cleanliness` | `integer (int32)` | No | Explicitly allowed | Numeric cleanliness for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `punctuality` | `integer (int32)` | No | Explicitly allowed | Numeric punctuality for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `tags` | `string[]` | No | Explicitly allowed | Collection of tags for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `communication` | `integer (int32)` | No | Explicitly allowed | Numeric communication for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `respect` | `integer (int32)` | No | Explicitly allowed | Numeric respect for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `pickupReadiness` | `integer (int32)` | No | Explicitly allowed | Numeric pickup readiness for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `vehicleCare` | `integer (int32)` | No | Explicitly allowed | Numeric vehicle care for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RatingBreakdownDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `overall` | `number (double)` | Yes | Not declared nullable | Numeric overall for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `count` | `integer (int32)` | Yes | Not declared nullable | Numeric count for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `driving` | `number (double)` | Yes | Not declared nullable | Numeric driving for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `courtesy` | `number (double)` | Yes | Not declared nullable | Numeric courtesy for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `cleanliness` | `number (double)` | Yes | Not declared nullable | Numeric cleanliness for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `punctuality` | `number (double)` | Yes | Not declared nullable | Numeric punctuality for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `nativeCount` | `integer (int32)` | Yes | Not declared nullable | Number of native in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `importedCount` | `integer (int32)` | Yes | Not declared nullable | Number of imported in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `importedSources` | [ImportedRatingSourceDto](i.md#importedratingsourcedto)[] | Yes | Not declared nullable | Collection of imported sources for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RatingImportDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `driverProfileId` | `string (uuid)` | Yes | Not declared nullable | Driver-profile record associated with this operation or result. | Shared convention | No further constraint recorded |
| `driverName` | `string` | Yes | Not declared nullable | Driver name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `source` | `string` | Yes | Not declared nullable | Source text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `profileRef` | `string` | Yes | Not declared nullable | Profile ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `inDriveUsername` | `string` | No | Explicitly allowed | In drive username text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `profileUrl` | `string` | No | Explicitly allowed | URL for profile; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `evidenceFileRef` | `string` | No | Explicitly allowed | Evidence file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `evidenceFileRefs` | `string[]` | Yes | Not declared nullable | Collection of evidence file refs for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `supportTicketId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related support ticket record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `status` | [RatingImportStatus](r.md#ratingimportstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `importedAverage` | `number (double)` | No | Explicitly allowed | Numeric imported average for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `importedCount` | `integer (int32)` | No | Explicitly allowed | Number of imported in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `error` | `string` | No | Explicitly allowed | Error text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `resolutionNote` | `string` | No | Explicitly allowed | Resolution note text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `confidenceScore` | `integer (int32)` | No | Explicitly allowed | Numeric confidence score for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `scanNote` | `string` | No | Explicitly allowed | Scan note text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `resolvedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for resolved at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |
| `evidenceObservedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for evidence observed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `evidenceExpiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for evidence expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `evidenceType` | `string` | Yes | Not declared nullable | Evidence type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `evidenceVersion` | `integer (int32)` | Yes | Not declared nullable | Evidence version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `verificationMethod` | `string` | Yes | Not declared nullable | Verification method text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `confidenceLevel` | [ExternalEvidenceConfidenceLevel](e.md#externalevidenceconfidencelevel) | Yes | Not declared nullable | Confidence level represented by the `ExternalEvidenceConfidenceLevel` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `verifiedCompletedTripCount` | `integer (int32)` | No | Explicitly allowed | Number of verified completed trip in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `positivePercentage` | `number (double)` | No | Explicitly allowed | Numeric positive percentage for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `evidenceSha256` | `string` | Yes | Not declared nullable | Evidence sha256 text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `evidenceHashKind` | `string` | Yes | Not declared nullable | Evidence hash kind text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `retainUntilUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for retain until; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `legalHoldActive` | `boolean` | Yes | Not declared nullable | Whether legal hold active applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `firstReviewedByUserId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related first reviewed by user record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `secondApprovedByUserId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related second approved by user record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `revokedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for revoked at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `revocationReason` | `string` | No | Explicitly allowed | Revocation reason text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RatingImportStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Completed | Completed state/choice in this specific enum. |
| `3` | Failed | Failed state/choice in this specific enum. |
| `4` | Rejected | Rejected state/choice in this specific enum. |
| `5` | Superseded | Superseded state/choice in this specific enum. |
| `6` | AwaitingSecondApproval | Awaiting second approval state/choice in this specific enum. |
| `7` | Expired | Expired state/choice in this specific enum. |
| `8` | Revoked | Revoked state/choice in this specific enum. |

## RecentAuthenticationProofDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `token` | `string` | Yes | Not declared nullable | Token for this specific contract, such as push registration; sensitive values must not be logged or reused in another ceremony. | Shared convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RecentRideLocationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `address` | `string` | Yes | Not declared nullable | Address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `placeId` | `string` | No | Explicitly allowed | Identifier of the related place record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `kind` | `string` | Yes | Not declared nullable | Kind text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `lastUsedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for last used at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RecordUserSettingChangeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `settingKey` | `string` | Yes | Not declared nullable | Setting key text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `change` | `string` | Yes | Not declared nullable | Change text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RecurringRideDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `pickupLatitude` | `number (double)` | Yes | Not declared nullable | Pickup latitude in degrees; latitude is separate from address text. | Shared convention | No further constraint recorded |
| `pickupLongitude` | `number (double)` | Yes | Not declared nullable | Pickup longitude in degrees; preserve coordinate order. | Shared convention | No further constraint recorded |
| `pickupAddress` | `string` | Yes | Not declared nullable | Human pickup-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `dropoffLatitude` | `number (double)` | Yes | Not declared nullable | Destination latitude in degrees. | Shared convention | No further constraint recorded |
| `dropoffLongitude` | `number (double)` | Yes | Not declared nullable | Destination longitude in degrees. | Shared convention | No further constraint recorded |
| `dropoffAddress` | `string` | Yes | Not declared nullable | Human destination-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `distanceMeters` | `integer (int32)` | Yes | Not declared nullable | Distance represented by this model, in metres; its source/assessment depends on the operation. | Shared convention | No further constraint recorded |
| `estimatedDurationSeconds` | `integer (int32)` | Yes | Not declared nullable | Estimated duration in seconds; an estimate is not actual elapsed trip time. | Shared convention | No further constraint recorded |
| `weekdays` | [WeekdayFlags](w.md#weekdayflags) | Yes | Not declared nullable | Weekdays represented by the `WeekdayFlags` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `pickupTime` | `string (time)` | Yes | Not declared nullable | Pickup time text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `timezone` | `string` | Yes | Not declared nullable | Timezone context used by this contract; apply documented IANA/display semantics. | Shared convention | No further constraint recorded |
| `vehicleCategoryId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related vehicle category record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `vehicleCategoryName` | `string` | Yes | Not declared nullable | Vehicle category name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `proposedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Rider's proposed fare in currency minor units, subject to applicable quote and marketplace rules. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `passengerCount` | `integer (int32)` | Yes | Not declared nullable | Number of passenger in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | Shared convention | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `nextOccurrenceUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for next occurrence; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RecurringRideDtoPagedResult

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `items` | [RecurringRideDto](r.md#recurringridedto)[] | No | Explicitly allowed | Records returned in this collection/page, each using the referenced item model. | Shared convention | No further constraint recorded |
| `page` | `integer (int32)` | No | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | Shared convention | No further constraint recorded |
| `pageSize` | `integer (int32)` | No | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | Shared convention | No further constraint recorded |
| `totalCount` | `integer (int64)` | No | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | Shared convention | No further constraint recorded |
| `totalPages` | `integer (int32)` | No | Not declared nullable | Number of pages represented by this page-number model. | Shared convention | readOnly: `True` |
| `hasPreviousPage` | `boolean` | No | Not declared nullable | Whether has previous page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |
| `hasNextPage` | `boolean` | No | Not declared nullable | Whether has next page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## RecurringRideOccurrenceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `rideRequestId` | `string (uuid)` | Yes | Not declared nullable | Rider request record, distinct from an accepted trip. | Shared convention | No further constraint recorded |
| `scheduledForUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for scheduled for; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `status` | [RideRequestStatus](r.md#riderequeststatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `bidCount` | `integer (int32)` | Yes | Not declared nullable | Number of bid in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `tripId` | `string (uuid)` | No | Explicitly allowed | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ReferralSummaryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `referralCode` | `string` | Yes | Not declared nullable | Referral code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `referredUsers` | `integer (int32)` | Yes | Not declared nullable | Numeric referred users for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `completedTrips` | `integer (int32)` | Yes | Not declared nullable | Numeric completed trips for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `earningsMinor` | `integer (int64)` | Yes | Not declared nullable | Earnings in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RefreshRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `refreshToken` | `string` | Yes | Not declared nullable | Sensitive rotating refresh credential; preserve secure-store and session-family rules. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RegisterDeviceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `installationId` | `string` | Yes | Not declared nullable | Identifier of the related installation record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `platform` | `string` | Yes | Not declared nullable | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | Shared convention | No further constraint recorded |
| `manufacturer` | `string` | Yes | Not declared nullable | Manufacturer text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `brand` | `string` | Yes | Not declared nullable | Brand text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `model` | `string` | Yes | Not declared nullable | Model in the owning domain; for vehicle contracts, the vehicle model associated with the manufacturer. | Shared convention | No further constraint recorded |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | Shared convention | No further constraint recorded |
| `operatingSystem` | `string` | Yes | Not declared nullable | Operating system text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `osVersion` | `string` | Yes | Not declared nullable | Os version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `appVersion` | `string` | Yes | Not declared nullable | App version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `buildNumber` | `integer (int32)` | Yes | Not declared nullable | Numeric build number for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `locale` | `string` | Yes | Not declared nullable | Locale text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RegisterPushTokenRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `token` | `string` | No | Explicitly allowed | Native push-registration token for this installation; distinct from the admitted-device credential and bearer access token. | Model-specific | No further constraint recorded |
| `platform` | [PushPlatform](p.md#pushplatform) | Yes | Not declared nullable | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | Shared convention | No further constraint recorded |
| `notificationPermission` | `string` | No | Explicitly allowed | Reported native notification permission state. | Shared convention | No further constraint recorded |
| `channelCapabilities` | [PushChannelCapabilitiesDto](p.md#pushchannelcapabilitiesdto) | No | Not declared nullable | Reported native delivery capabilities for applicable notification behavior. | Shared convention | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | No | Explicitly allowed | Previously read installation binding revision; prevents a stale callback from overwriting newer opt-out or ownership state. | Model-specific | No further constraint recorded |
| `explicitOptIn` | `boolean` | No | Not declared nullable | Explicit user request to enable this installation's notifications; token refresh alone is not renewed consent. | Model-specific | No further constraint recorded |
| `mutationId` | `string (uuid)` | No | Explicitly allowed | Identity of this binding change, retained for replay/reconciliation after a lost response. | Model-specific | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RegisterRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `firstName` | `string` | Yes | Not declared nullable | Person's given name as provided through the applicable profile/identity workflow. | Shared convention | No further constraint recorded |
| `lastName` | `string` | Yes | Not declared nullable | Person's family name as provided through the applicable profile/identity workflow. | Shared convention | No further constraint recorded |
| `email` | `string` | No | Explicitly allowed | Email address for this model's person/destination; its presence does not prove verification. | Shared convention | No further constraint recorded |
| `phoneNumber` | `string` | No | Explicitly allowed | Country-aware contact number; its presence does not prove verification or provider provisioning. | Shared convention | No further constraint recorded |
| `password` | `string` | Yes | Not declared nullable | Secret password input for the established secure identity ceremony; never echo or log it. | Shared convention | No further constraint recorded |
| `role` | [UserRole](u.md#userrole) | Yes | Not declared nullable | Requested consumer role. The shared UserRole enum also contains administrative values, but self-registration does not grant those roles. | Model-specific | No further constraint recorded |
| `referralCode` | `string` | No | Explicitly allowed | Referral code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `countryCode` | `string` | No | Explicitly allowed | Country selected in the immutable registration intent; the server must accept it as an active, provisioned signup country. | Model-specific | No further constraint recorded |
| `driverAccountType` | [DriverAccountType](d.md#driveraccounttype) | No | Not declared nullable | Individual/business driver choice carried from registration intent into the driver profile. | Model-specific | No further constraint recorded |
| `businessLegalName` | `string` | No | Explicitly allowed | Business legal name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `businessTradingName` | `string` | No | Explicitly allowed | Business trading name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `businessRegistrationNumber` | `string` | No | Explicitly allowed | Business registration number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `businessTaxNumber` | `string` | No | Explicitly allowed | Business tax number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `businessEmail` | `string` | No | Explicitly allowed | Business email text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `businessPhone` | `string` | No | Explicitly allowed | Business phone text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `businessRegisteredAddress` | `string` | No | Explicitly allowed | Business registered address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `createRentalOrganization` | `boolean` | No | Not declared nullable | Whether this signup requests the rental-organization onboarding path; it does not make the organization operationally approved. | Model-specific | No further constraint recorded |
| `allowWeakPassword` | `boolean` | No | Not declared nullable | Client acknowledgement field for a password-policy choice; it does not override server validation. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RegisterVehicleDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `make` | `string` | Yes | Not declared nullable | Vehicle manufacturer name/catalog selection. | Shared convention | No further constraint recorded |
| `model` | `string` | Yes | Not declared nullable | Model in the owning domain; for vehicle contracts, the vehicle model associated with the manufacturer. | Shared convention | No further constraint recorded |
| `year` | `integer (int32)` | No | Explicitly allowed | Numeric year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `color` | `string` | Yes | Not declared nullable | Color text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `plateNumber` | `string` | Yes | Not declared nullable | Country-specific vehicle registration plate; validate through the applicable country workflow. | Shared convention | No further constraint recorded |
| `vehicleCategoryId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related vehicle category record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `registrationFileRef` | `string` | No | Explicitly allowed | Registration file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `registrationFileName` | `string` | No | Explicitly allowed | Registration file name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `allowsPets` | `boolean` | No | Not declared nullable | Whether allows pets applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `childSeatCapacity` | `integer (int32)` | No | Not declared nullable | Numeric child seat capacity for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `isWheelchairAccessible` | `boolean` | No | Not declared nullable | Whether is wheelchair accessible applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `isAirportPickupEligible` | `boolean` | No | Not declared nullable | Whether is airport pickup eligible applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `conditionCode` | `string` | No | Explicitly allowed | Condition code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `vinChassis` | `string` | No | Explicitly allowed | Vehicle VIN/chassis identification data; keep the actual value private and within authorized views. | Shared convention | No further constraint recorded |
| `registrationExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for registration expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `fitnessExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for fitness expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `insuranceExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for insurance expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `interiorImageFileRef` | `string` | No | Explicitly allowed | Interior image file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `frontExteriorImageFileRef` | `string` | No | Explicitly allowed | Front exterior image file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `insuranceFileRef` | `string` | No | Explicitly allowed | Insurance file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `insuranceFileName` | `string` | No | Explicitly allowed | Insurance file name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `insuranceProviderId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related insurance provider record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `insuranceProvider` | `string` | No | Explicitly allowed | Insurance provider text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `setAsPrimary` | `boolean` | No | Not declared nullable | Whether set as primary applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `onboardingSubmission` | `boolean` | No | Not declared nullable | Whether onboarding submission applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RenameSavedCalculationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RenewGuardianConsentDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `consentPolicyVersion` | `string` | Yes | Not declared nullable | Consent policy version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `consentEvidenceReference` | `string` | Yes | Not declared nullable | Consent evidence reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `guardianAuthorityType` | `string` | Yes | Not declared nullable | Guardian authority type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `guardianAuthorityConfirmed` | `boolean` | Yes | Not declared nullable | Whether guardian authority confirmed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `liveTrackingConsentGranted` | `boolean` | Yes | Not declared nullable | Whether live tracking consent granted applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `threeWayCommunicationConsentGranted` | `boolean` | Yes | Not declared nullable | Whether three way communication consent granted applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `emergencyContactConfirmed` | `boolean` | Yes | Not declared nullable | Whether emergency contact confirmed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `expectedAuthorizationRevision` | `integer (int64)` | Yes | Not declared nullable | Expected authorization revision for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `expectedSafetyPolicyRevision` | `integer (int64)` | Yes | Not declared nullable | Expected safety policy revision for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalAgreementDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `bookingId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related booking record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `agreementVersion` | `integer (int32)` | Yes | Not declared nullable | Agreement version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `status` | [RentalAgreementStatus](r.md#rentalagreementstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `termsVersion` | `string` | Yes | Not declared nullable | Terms version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `termsSha256` | `string` | Yes | Not declared nullable | Terms sha256 text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `renterSignedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for renter signed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `providerSignedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for provider signed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `executedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for executed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalAgreementStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | AwaitingRenter | Awaiting renter state/choice in this specific enum. |
| `2` | AwaitingProvider | Awaiting provider state/choice in this specific enum. |
| `3` | Executed | Executed state/choice in this specific enum. |
| `4` | Voided | Voided state/choice in this specific enum. |

## RentalAllowedActionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `actor` | `string` | Yes | Not declared nullable | Actor text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `expectedBookingVersion` | `integer (int32)` | Yes | Not declared nullable | Expected booking version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `requiresReason` | `boolean` | Yes | Not declared nullable | Whether requires reason applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requiresEvidence` | `boolean` | Yes | Not declared nullable | Whether requires evidence applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requiredPermission` | `string` | No | Explicitly allowed | Required permission text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `requiredChecklistCodes` | `string[]` | Yes | Not declared nullable | Collection of required checklist codes for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalAuthorizationEvidence

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `state` | [RentalAuthorizationState](r.md#rentalauthorizationstate) | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `observedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for observed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `captureBeforeUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for capture before; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `authorizedMinor` | `integer (int64)` | No | Explicitly allowed | Authorized in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | No | Explicitly allowed | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `network` | `string` | No | Explicitly allowed | Network text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `extendedAuthorization` | `boolean` | No | Explicitly allowed | Whether extended authorization applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `incrementalAuthorization` | `boolean` | No | Explicitly allowed | Whether incremental authorization applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalAuthorizationState

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Unavailable | Unavailable state/choice in this specific enum. |
| `1` | Valid | Valid state/choice in this specific enum. |
| `2` | Expiring | Expiring state/choice in this specific enum. |
| `3` | Expired | Expired state/choice in this specific enum. |
| `4` | Released | Released state/choice in this specific enum. |
| `5` | Captured | Captured state/choice in this specific enum. |
| `6` | Declined | Declined state/choice in this specific enum. |
| `7` | Mismatch | Mismatch state/choice in this specific enum. |

## RentalAvailabilityBlockDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `vehicleId` | `string (uuid)` | Yes | Not declared nullable | Account vehicle record associated with this operation or result. | Shared convention | No further constraint recorded |
| `type` | [RentalAvailabilityBlockType](r.md#rentalavailabilityblocktype) | Yes | Not declared nullable | Type represented by the `RentalAvailabilityBlockType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `startsAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for starts at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `endsAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for ends at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `reason` | `string` | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalAvailabilityBlockType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Maintenance | Maintenance state/choice in this specific enum. |
| `2` | Repair | Repair state/choice in this specific enum. |
| `3` | OwnerUse | Owner use state/choice in this specific enum. |
| `4` | Inspection | Inspection state/choice in this specific enum. |
| `5` | Other | Other state/choice in this specific enum. |

## RentalAvailabilityCalendarDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `vehicleId` | `string (uuid)` | Yes | Not declared nullable | Account vehicle record associated with this operation or result. | Shared convention | No further constraint recorded |
| `fromUtc` | `string (date-time)` | Yes | Not declared nullable | UTC start of the requested range; apply this endpoint's inclusion/validation rules. | Shared convention | No further constraint recorded |
| `toUtc` | `string (date-time)` | Yes | Not declared nullable | UTC end of the requested range; apply this endpoint's inclusion/validation rules. | Shared convention | No further constraint recorded |
| `occupiedDays` | `string (date)[]` | Yes | Not declared nullable | Occupied, measured in days under this workflow's calendar rules. | Naming convention | No further constraint recorded |
| `blocks` | [RentalAvailabilityBlockDto](r.md#rentalavailabilityblockdto)[] | Yes | Not declared nullable | Collection of blocks for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `availabilityPolicy` | [RentalAvailabilityPolicyDto](r.md#rentalavailabilitypolicydto) | No | Not declared nullable | Availability policy represented by the `RentalAvailabilityPolicyDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalAvailabilityPolicyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `version` | `string` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `basis` | `string` | Yes | Not declared nullable | Basis text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `turnaroundMinutes` | `integer (int32)` | Yes | Not declared nullable | Turnaround, measured in minutes. | Naming convention | No further constraint recorded |
| `legacyUtcDayRestriction` | `boolean` | Yes | Not declared nullable | Whether legacy utc day restriction applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalBookingDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `vehicleId` | `string (uuid)` | Yes | Not declared nullable | Account vehicle record associated with this operation or result. | Shared convention | No further constraint recorded |
| `pickupAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for pickup at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `returnAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for return at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `status` | [RentalBookingStatus](r.md#rentalbookingstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `baseAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Base amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `securityDepositMinor` | `integer (int64)` | Yes | Not declared nullable | Security deposit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `totalAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Total amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `version` | `integer (int32)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `vehicle` | `string` | Yes | Not declared nullable | Vehicle text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `providerName` | `string` | Yes | Not declared nullable | Provider name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalBookingMode

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | RequestToBook | Request to book state/choice in this specific enum. |
| `2` | InstantBook | Instant book state/choice in this specific enum. |

## RentalBookingOperationsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `booking` | [RentalBookingDto](r.md#rentalbookingdto) | Yes | Not declared nullable | Booking represented by the `RentalBookingDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `handoverMode` | [RentalVehicleHandoverMode](r.md#rentalvehiclehandovermode) | Yes | Not declared nullable | Handover mode represented by the `RentalVehicleHandoverMode` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `pickupAddress` | `string` | No | Explicitly allowed | Human pickup-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `returnAddress` | `string` | No | Explicitly allowed | Return address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `handoverFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Handover fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `depositAuthorizedMinor` | `integer (int64)` | Yes | Not declared nullable | Deposit authorized in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `depositCapturedMinor` | `integer (int64)` | Yes | Not declared nullable | Deposit captured in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `depositReleasedMinor` | `integer (int64)` | Yes | Not declared nullable | Deposit released in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `lateFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Late fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `extensionAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Extension amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `distanceDrivenKilometers` | `integer (int32)` | No | Explicitly allowed | Numeric distance driven kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `startFuelPercent` | `number (double)` | No | Explicitly allowed | Numeric start fuel percent for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `endFuelPercent` | `number (double)` | No | Explicitly allowed | Numeric end fuel percent for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `agreement` | [RentalAgreementDto](r.md#rentalagreementdto) | No | Not declared nullable | Agreement represented by the `RentalAgreementDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `inspections` | [RentalInspectionDto](r.md#rentalinspectiondto)[] | Yes | Not declared nullable | Collection of inspections for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `extensions` | [RentalExtensionDto](r.md#rentalextensiondto)[] | Yes | Not declared nullable | Collection of extensions for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `damageClaims` | [RentalDamageClaimDto](r.md#rentaldamageclaimdto)[] | Yes | Not declared nullable | Collection of damage claims for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `disputes` | [RentalDisputeDto](r.md#rentaldisputedto)[] | Yes | Not declared nullable | Collection of disputes for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `rentalPolicyVersion` | `integer (int32)` | Yes | Not declared nullable | Rental policy version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `acceptedPolicy` | [RentalPolicySnapshot](r.md#rentalpolicysnapshot) | No | Not declared nullable | Accepted policy represented by the `RentalPolicySnapshot` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `lifecycle` | [RentalLifecycleDto](r.md#rentallifecycledto) | Yes | Not declared nullable | Lifecycle represented by the `RentalLifecycleDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `authorization` | [RentalAuthorizationEvidence](r.md#rentalauthorizationevidence) | No | Not declared nullable | Authorization represented by the `RentalAuthorizationEvidence` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `inventoryHold` | [RentalInventoryHoldDto](r.md#rentalinventoryholddto) | No | Not declared nullable | Inventory hold represented by the `RentalInventoryHoldDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `protection` | [RentalProviderProtectionDto](r.md#rentalproviderprotectiondto) | No | Not declared nullable | Protection represented by the `RentalProviderProtectionDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalBookingStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Requested | Requested state/choice in this specific enum. |
| `2` | Approved | Approved state/choice in this specific enum. |
| `3` | Declined | Declined state/choice in this specific enum. |
| `4` | Confirmed | Confirmed state/choice in this specific enum. |
| `5` | CheckedOut | Checked out state/choice in this specific enum. |
| `6` | Returned | Returned state/choice in this specific enum. |
| `7` | Completed | Completed state/choice in this specific enum. |
| `8` | Cancelled | Cancelled state/choice in this specific enum. |
| `9` | Disputed | Disputed state/choice in this specific enum. |
| `10` | Quote | Quote state/choice in this specific enum. |
| `11` | PaymentAuthorized | Payment authorized state/choice in this specific enum. |
| `12` | CheckedIn | Checked in state/choice in this specific enum. |
| `13` | Active | Active state/choice in this specific enum. |
| `14` | Settled | Settled state/choice in this specific enum. |

## RentalBookingStatusContractDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `version` | `integer (int32)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `unknownName` | `string` | Yes | Not declared nullable | Unknown name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `statuses` | [RentalBookingStatusDefinitionDto](r.md#rentalbookingstatusdefinitiondto)[] | Yes | Not declared nullable | Collection of statuses for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalBookingStatusDefinitionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `value` | `integer (int32)` | Yes | Not declared nullable | Numeric value for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `isTerminal` | `boolean` | Yes | Not declared nullable | Whether is terminal applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `allowedTransitions` | `integer (int32)[]` | Yes | Not declared nullable | Collection of allowed transitions for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalBranchPublicDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `address` | `string` | Yes | Not declared nullable | Address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalCancellationReason

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | PlansChanged | Plans changed state/choice in this specific enum. |
| `2` | PriceOrDeposit | Price or deposit state/choice in this specific enum. |
| `3` | VehicleOrProvider | Vehicle or provider state/choice in this specific enum. |
| `4` | TravelDisruption | Travel disruption state/choice in this specific enum. |
| `5` | DuplicateBooking | Duplicate booking state/choice in this specific enum. |
| `6` | ProviderCancelled | Provider cancelled state/choice in this specific enum. |
| `7` | NoShow | No show state/choice in this specific enum. |
| `8` | Other | Other state/choice in this specific enum. |

## RentalCheckoutDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `paymentId` | `string (uuid)` | Yes | Not declared nullable | Server-owned payment record used for state/reconciliation. | Shared convention | No further constraint recorded |
| `provider` | `string` | Yes | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | Shared convention | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `checkoutUrl` | `string` | No | Explicitly allowed | URL for checkout; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalDamageClaimDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `bookingId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related booking record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `status` | [RentalDamageClaimStatus](r.md#rentaldamageclaimstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `reason` | [RentalDamageReason](r.md#rentaldamagereason) | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |
| `description` | `string` | Yes | Not declared nullable | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `claimedAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Claimed amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `approvedAmountMinor` | `integer (int64)` | No | Explicitly allowed | Approved amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `reviewNote` | `string` | No | Explicitly allowed | Human-readable reviewer explanation, including remediation where applicable. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `reviewedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for reviewed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `settlementReference` | `string` | No | Explicitly allowed | Settlement reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `evidence` | [RentalEvidencePreviewDto](r.md#rentalevidencepreviewdto)[] | Yes | Not declared nullable | Collection of evidence for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalDamageClaimStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Submitted | Submitted state/choice in this specific enum. |
| `2` | UnderReview | Under review state/choice in this specific enum. |
| `3` | Approved | Approved state/choice in this specific enum. |
| `4` | Rejected | Rejected state/choice in this specific enum. |
| `5` | Settled | Settled state/choice in this specific enum. |
| `6` | Withdrawn | Withdrawn state/choice in this specific enum. |

## RentalDamageReason

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | ExteriorDamage | Exterior damage state/choice in this specific enum. |
| `2` | InteriorDamage | Interior damage state/choice in this specific enum. |
| `3` | GlassOrLighting | Glass or lighting state/choice in this specific enum. |
| `4` | TireOrWheel | Tire or wheel state/choice in this specific enum. |
| `5` | Mechanical | Mechanical state/choice in this specific enum. |
| `6` | FuelShortfall | Fuel shortfall state/choice in this specific enum. |
| `7` | ExcessMileage | Excess mileage state/choice in this specific enum. |
| `8` | Cleaning | Cleaning state/choice in this specific enum. |
| `9` | LostItemOrKey | Lost item or key state/choice in this specific enum. |
| `10` | Other | Other state/choice in this specific enum. |

## RentalDisputeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `bookingId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related booking record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `reasonCode` | `string` | Yes | Not declared nullable | Stable reason code; map through the applicable reason catalog instead of displaying an unrelated enum. | Shared convention | No further constraint recorded |
| `detail` | `string` | Yes | Not declared nullable | Detail text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `status` | [RentalDisputeStatus](r.md#rentaldisputestatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `resolutionReason` | `string` | No | Explicitly allowed | Resolution reason text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `reviewedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for reviewed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `evidence` | [RentalEvidencePreviewDto](r.md#rentalevidencepreviewdto)[] | Yes | Not declared nullable | Collection of evidence for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalDisputeStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Submitted | Submitted state/choice in this specific enum. |
| `2` | UnderReview | Under review state/choice in this specific enum. |
| `3` | Resolved | Resolved state/choice in this specific enum. |
| `4` | Rejected | Rejected state/choice in this specific enum. |

## RentalEvidenceInput

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `fileRef` | `string` | Yes | Not declared nullable | Private storage reference; not a permanent public URL or approval decision. | Shared convention | No further constraint recorded |
| `label` | `string` | Yes | Not declared nullable | Label text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalEvidencePreviewDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `label` | `string` | Yes | Not declared nullable | Label text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `previewPath` | `string` | Yes | Not declared nullable | Preview path text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalExpectedVersionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `expectedVersion` | `integer (int32)` | Yes | Not declared nullable | Expected version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalExtensionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `bookingId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related booking record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `requestedReturnAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for requested return at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `quotedAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Quoted amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `status` | [RentalExtensionStatus](r.md#rentalextensionstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `decisionReason` | `string` | No | Explicitly allowed | Decision reason text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `reviewedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for reviewed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalExtensionStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Approved | Approved state/choice in this specific enum. |
| `3` | Rejected | Rejected state/choice in this specific enum. |
| `4` | Cancelled | Cancelled state/choice in this specific enum. |
| `5` | PaymentPending | Payment pending state/choice in this specific enum. |

## RentalFleetReminderDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `vehicleId` | `string (uuid)` | Yes | Not declared nullable | Account vehicle record associated with this operation or result. | Shared convention | No further constraint recorded |
| `vehicle` | `string` | Yes | Not declared nullable | Vehicle text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `plateNumber` | `string` | Yes | Not declared nullable | Country-specific vehicle registration plate; validate through the applicable country workflow. | Shared convention | No further constraint recorded |
| `kind` | `string` | Yes | Not declared nullable | Kind text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `dueAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for due at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `daysRemaining` | `integer (int32)` | Yes | Not declared nullable | Numeric days remaining for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `state` | `string` | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalInspectionChecklistInput

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `isSatisfied` | `boolean` | Yes | Not declared nullable | Whether is satisfied applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalInspectionChecklistItemDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `isSatisfied` | `boolean` | Yes | Not declared nullable | Whether is satisfied applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalInspectionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `bookingId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related booking record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `phase` | [RentalInspectionPhase](r.md#rentalinspectionphase) | Yes | Not declared nullable | Phase represented by the `RentalInspectionPhase` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `odometerKilometers` | `integer (int32)` | Yes | Not declared nullable | Numeric odometer kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `fuelPercent` | `number (double)` | Yes | Not declared nullable | Numeric fuel percent for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `notes` | `string` | Yes | Not declared nullable | Human notes for this record; keep them within the authorized data scope. | Shared convention | No further constraint recorded |
| `completedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for completed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `photos` | [RentalInspectionPhotoDto](r.md#rentalinspectionphotodto)[] | Yes | Not declared nullable | Collection of photos for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `checklist` | [RentalInspectionChecklistItemDto](r.md#rentalinspectionchecklistitemdto)[] | Yes | Not declared nullable | Requirement-by-requirement setup/readiness state. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalInspectionPhase

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | PreRental | Pre rental state/choice in this specific enum. |
| `2` | PostRental | Post rental state/choice in this specific enum. |

## RentalInspectionPhotoDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `area` | `string` | Yes | Not declared nullable | Area text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `damageObserved` | `boolean` | Yes | Not declared nullable | Whether damage observed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `previewPath` | `string` | Yes | Not declared nullable | Preview path text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalInspectionPhotoInput

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `fileRef` | `string` | Yes | Not declared nullable | Private storage reference; not a permanent public URL or approval decision. | Shared convention | No further constraint recorded |
| `area` | `string` | Yes | Not declared nullable | Area text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `damageObserved` | `boolean` | Yes | Not declared nullable | Whether damage observed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalInventoryHoldDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Explicitly allowed | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `state` | [RentalInventoryHoldState](r.md#rentalinventoryholdstate) | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `version` | `integer (int64)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `ownerUserId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related owner user record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `tenantId` | `string (uuid)` | Yes | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | Shared convention | No further constraint recorded |
| `country` | `string` | No | Explicitly allowed | Country text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `paymentId` | `string (uuid)` | No | Explicitly allowed | Server-owned payment record used for state/reconciliation. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalInventoryHoldState

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`, `4`, `5`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Legacy | Legacy state/choice in this specific enum. |
| `1` | Holding | Holding state/choice in this specific enum. |
| `2` | Reserved | Reserved state/choice in this specific enum. |
| `3` | Expired | Expired state/choice in this specific enum. |
| `4` | Released | Released state/choice in this specific enum. |
| `5` | PaymentReview | Payment review state/choice in this specific enum. |

## RentalLifecycleDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `currentStep` | `string` | Yes | Not declared nullable | Current step text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `bookingVersion` | `integer (int32)` | Yes | Not declared nullable | Booking version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `requirements` | [RentalLifecycleRequirementDto](r.md#rentallifecyclerequirementdto)[] | Yes | Not declared nullable | Collection of requirements for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `allowedActions` | [RentalAllowedActionDto](r.md#rentalallowedactiondto)[] | Yes | Not declared nullable | Collection of allowed actions for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalLifecycleRequirementDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `satisfied` | `boolean` | Yes | Not declared nullable | Whether satisfied applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `message` | `string` | Yes | Not declared nullable | Message text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalMakeModelsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `make` | `string` | Yes | Not declared nullable | Vehicle manufacturer name/catalog selection. | Shared convention | No further constraint recorded |
| `models` | `string[]` | Yes | Not declared nullable | Collection of models for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalMarketplaceFiltersDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `makes` | `string[]` | Yes | Not declared nullable | Collection of makes for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `models` | `string[]` | Yes | Not declared nullable | Collection of models for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `vehicleTypes` | `string[]` | Yes | Not declared nullable | Collection of vehicle types for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `transmissions` | `string[]` | Yes | Not declared nullable | Collection of transmissions for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `minimumYear` | `integer (int32)` | No | Explicitly allowed | Numeric minimum year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `maximumYear` | `integer (int32)` | No | Explicitly allowed | Numeric maximum year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `makeModels` | [RentalMakeModelsDto](r.md#rentalmakemodelsdto)[] | No | Explicitly allowed | Collection of make models for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalMembershipPurchaseDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `planId` | `string (uuid)` | Yes | Not declared nullable | Membership catalog record; it does not itself prove a user entitlement. | Shared convention | No further constraint recorded |
| `termDays` | `integer (int32)` | No | Not declared nullable | Requested/applicable membership term in days; only configured valid terms are allowed. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalOrganizationCardDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `tradingName` | `string` | Yes | Not declared nullable | Trading name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `providerType` | [RentalProviderType](r.md#rentalprovidertype) | Yes | Not declared nullable | Provider type represented by the `RentalProviderType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `rating` | `number (double)` | No | Explicitly allowed | Numeric rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `vehicleCount` | `integer (int32)` | Yes | Not declared nullable | Number of vehicle in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `hasProfileImage` | `boolean` | Yes | Not declared nullable | Whether has profile image applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `vehicleTypes` | `string[]` | Yes | Not declared nullable | Collection of vehicle types for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalOrganizationCardDtoPagedResult

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `items` | [RentalOrganizationCardDto](r.md#rentalorganizationcarddto)[] | No | Explicitly allowed | Records returned in this collection/page, each using the referenced item model. | Shared convention | No further constraint recorded |
| `page` | `integer (int32)` | No | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | Shared convention | No further constraint recorded |
| `pageSize` | `integer (int32)` | No | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | Shared convention | No further constraint recorded |
| `totalCount` | `integer (int64)` | No | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | Shared convention | No further constraint recorded |
| `totalPages` | `integer (int32)` | No | Not declared nullable | Number of pages represented by this page-number model. | Shared convention | readOnly: `True` |
| `hasPreviousPage` | `boolean` | No | Not declared nullable | Whether has previous page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |
| `hasNextPage` | `boolean` | No | Not declared nullable | Whether has next page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## RentalOrganizationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `providerType` | [RentalProviderType](r.md#rentalprovidertype) | Yes | Not declared nullable | Provider type represented by the `RentalProviderType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `legalName` | `string` | Yes | Not declared nullable | Legal name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `tradingName` | `string` | Yes | Not declared nullable | Trading name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `slug` | `string` | Yes | Not declared nullable | Slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `timezone` | `string` | Yes | Not declared nullable | Timezone context used by this contract; apply documented IANA/display semantics. | Shared convention | No further constraint recorded |
| `status` | [RentalOrganizationStatus](r.md#rentalorganizationstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `rating` | `number (double)` | No | Explicitly allowed | Numeric rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `myRole` | [RentalOrganizationRole](r.md#rentalorganizationrole) | Yes | Not declared nullable | My role represented by the `RentalOrganizationRole` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `myPermissions` | [RentalOrganizationPermission](r.md#rentalorganizationpermission) | Yes | Not declared nullable | My permissions represented by the `RentalOrganizationPermission` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `description` | `string` | No | Explicitly allowed | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `websiteUrl` | `string` | No | Explicitly allowed | URL for website; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `contactEmail` | `string` | No | Explicitly allowed | Contact email text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `contactPhone` | `string` | No | Explicitly allowed | Contact phone text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `registrationNumber` | `string` | No | Explicitly allowed | Registration number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `taxNumber` | `string` | No | Explicitly allowed | Tax number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `hasProfileImage` | `boolean` | No | Not declared nullable | Whether has profile image applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalOrganizationPermission

**Wire type:** `integer (int64)`. Allowed wire values: `0`, `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `256`, `511`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | None | None state/choice in this specific enum. |
| `1` | ManageTeam | Manage team state/choice in this specific enum. |
| `2` | ManageBranches | Manage branches state/choice in this specific enum. |
| `4` | ManageVehicles | Manage vehicles state/choice in this specific enum. |
| `8` | ManageVehicleImages | Manage vehicle images state/choice in this specific enum. |
| `16` | ManageBookings | Manage bookings state/choice in this specific enum. |
| `32` | ViewFinance | View finance state/choice in this specific enum. |
| `64` | ManagePayouts | Manage payouts state/choice in this specific enum. |
| `128` | PerformInspections | Perform inspections state/choice in this specific enum. |
| `256` | ViewAudit | View audit state/choice in this specific enum. |
| `511` | All | All state/choice in this specific enum. |

## RentalOrganizationPublicDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `tradingName` | `string` | Yes | Not declared nullable | Trading name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `providerType` | [RentalProviderType](r.md#rentalprovidertype) | Yes | Not declared nullable | Provider type represented by the `RentalProviderType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `rating` | `number (double)` | No | Explicitly allowed | Numeric rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `ratingCount` | `integer (int32)` | Yes | Not declared nullable | Number of rating in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `hasProfileImage` | `boolean` | Yes | Not declared nullable | Whether has profile image applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `branches` | [RentalBranchPublicDto](r.md#rentalbranchpublicdto)[] | Yes | Not declared nullable | Collection of branches for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `vehicleTypes` | `string[]` | Yes | Not declared nullable | Collection of vehicle types for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `vehicleCount` | `integer (int32)` | Yes | Not declared nullable | Number of vehicle in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalOrganizationRole

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Owner | Owner state/choice in this specific enum. |
| `2` | FleetManager | Fleet manager state/choice in this specific enum. |
| `3` | BookingAgent | Booking agent state/choice in this specific enum. |
| `4` | FinanceOfficer | Finance officer state/choice in this specific enum. |
| `5` | VehicleInspector | Vehicle inspector state/choice in this specific enum. |
| `6` | Auditor | Auditor state/choice in this specific enum. |

## RentalOrganizationStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Active | Active state/choice in this specific enum. |
| `3` | Suspended | Suspended state/choice in this specific enum. |
| `4` | Closed | Closed state/choice in this specific enum. |

## RentalOwnerAnalyticsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `activeFleet` | `integer (int32)` | Yes | Not declared nullable | Numeric active fleet for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `bookedToday` | `integer (int32)` | Yes | Not declared nullable | Numeric booked today for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `completedBookings` | `integer (int32)` | Yes | Not declared nullable | Numeric completed bookings for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `grossBookedMinor` | `integer (int64)` | Yes | Not declared nullable | Gross booked in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `depositsHeldMinor` | `integer (int64)` | Yes | Not declared nullable | Deposits held in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `lateFeesMinor` | `integer (int64)` | Yes | Not declared nullable | Late fees in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `damageClaimsApprovedMinor` | `integer (int64)` | Yes | Not declared nullable | Damage claims approved in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `utilizationPercent` | `number (double)` | Yes | Not declared nullable | Numeric utilization percent for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `averageRating` | `number (double)` | No | Explicitly allowed | Numeric average rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalPartnerBookingDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `vehicleId` | `string (uuid)` | Yes | Not declared nullable | Account vehicle record associated with this operation or result. | Shared convention | No further constraint recorded |
| `vehicle` | `string` | Yes | Not declared nullable | Vehicle text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `renterName` | `string` | Yes | Not declared nullable | Renter name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `pickupAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for pickup at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `returnAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for return at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `status` | [RentalBookingStatus](r.md#rentalbookingstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `totalAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Total amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `declineReason` | `string` | No | Explicitly allowed | Decline reason text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `version` | `integer (int32)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalPartnerBranchDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `address` | `string` | Yes | Not declared nullable | Address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `timezone` | `string` | Yes | Not declared nullable | Timezone context used by this contract; apply documented IANA/display semantics. | Shared convention | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalPartnerVehicleDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `branchId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related branch record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | Shared convention | No further constraint recorded |
| `make` | `string` | Yes | Not declared nullable | Vehicle manufacturer name/catalog selection. | Shared convention | No further constraint recorded |
| `model` | `string` | Yes | Not declared nullable | Model in the owning domain; for vehicle contracts, the vehicle model associated with the manufacturer. | Shared convention | No further constraint recorded |
| `year` | `integer (int32)` | Yes | Not declared nullable | Numeric year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `category` | `string` | Yes | Not declared nullable | Category text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `transmission` | `string` | Yes | Not declared nullable | Transmission text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `fuelType` | `string` | Yes | Not declared nullable | Fuel type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `seats` | `integer (int32)` | Yes | Not declared nullable | Numeric seats for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `color` | `string` | Yes | Not declared nullable | Color text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `plateNumber` | `string` | Yes | Not declared nullable | Country-specific vehicle registration plate; validate through the applicable country workflow. | Shared convention | No further constraint recorded |
| `description` | `string` | Yes | Not declared nullable | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `dailyRateMinor` | `integer (int64)` | Yes | Not declared nullable | Daily rate in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `weeklyRateMinor` | `integer (int64)` | No | Explicitly allowed | Weekly rate in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `securityDepositMinor` | `integer (int64)` | Yes | Not declared nullable | Security deposit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `bookingMode` | [RentalBookingMode](r.md#rentalbookingmode) | Yes | Not declared nullable | Booking mode represented by the `RentalBookingMode` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `distanceUnit` | `string` | Yes | Not declared nullable | Distance unit text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `includedDistancePerDay` | `integer (int32)` | Yes | Not declared nullable | Numeric included distance per day for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `includedKilometersPerDay` | `integer (int32)` | Yes | Not declared nullable | Numeric included kilometers per day for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `extraKilometerRateMinor` | `integer (int64)` | Yes | Not declared nullable | Extra kilometer rate in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `handoverMode` | [RentalVehicleHandoverMode](r.md#rentalvehiclehandovermode) | Yes | Not declared nullable | Handover mode represented by the `RentalVehicleHandoverMode` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `pickupFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Pickup fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `deliveryFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Delivery fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `serviceRadius` | `integer (int32)` | Yes | Not declared nullable | Numeric service radius for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `serviceRadiusKilometers` | `integer (int32)` | Yes | Not declared nullable | Numeric service radius kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `lateGraceMinutes` | `integer (int32)` | Yes | Not declared nullable | Late grace, measured in minutes. | Naming convention | No further constraint recorded |
| `lateFeePerHourMinor` | `integer (int64)` | Yes | Not declared nullable | Late fee per hour in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `registrationExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for registration expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `insuranceExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for insurance expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `fitnessExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for fitness expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `complianceReminderDays` | `integer (int32)` | Yes | Not declared nullable | Compliance reminder, measured in days under this workflow's calendar rules. | Naming convention | No further constraint recorded |
| `policyVersion` | `integer (int32)` | Yes | Not declared nullable | Policy revision used for this assessment; not the mobile app build number. | Shared convention | No further constraint recorded |
| `policyAcceptedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for policy accepted at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `status` | [RentalVehicleStatus](r.md#rentalvehiclestatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `images` | [RentalPartnerVehicleImageDto](r.md#rentalpartnervehicleimagedto)[] | Yes | Not declared nullable | Collection of images for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalPartnerVehicleImageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `fileRef` | `string` | Yes | Not declared nullable | Private storage reference; not a permanent public URL or approval decision. | Shared convention | No further constraint recorded |
| `altText` | `string` | Yes | Not declared nullable | Alt text text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isPrimary` | `boolean` | Yes | Not declared nullable | Whether the vehicle is designated primary in this account context; work eligibility is assessed separately. | Shared convention | No further constraint recorded |
| `sortOrder` | `integer (int32)` | Yes | Not declared nullable | Numeric sort order for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalPolicyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `bookingApproval` | `string` | Yes | Not declared nullable | Booking approval text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `mileage` | `string` | Yes | Not declared nullable | Mileage text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `securityDeposit` | `string` | Yes | Not declared nullable | Security deposit text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `lateReturn` | `string` | Yes | Not declared nullable | Late return text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `handover` | `string` | Yes | Not declared nullable | Handover text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `cancellation` | `string` | Yes | Not declared nullable | Cancellation text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalPolicySnapshot

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `schemaVersion` | `integer (int32)` | Yes | Not declared nullable | Schema version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `policyVersion` | `integer (int32)` | Yes | Not declared nullable | Policy revision used for this assessment; not the mobile app build number. | Shared convention | No further constraint recorded |
| `acceptedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for accepted at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `bookingMode` | [RentalBookingMode](r.md#rentalbookingmode) | Yes | Not declared nullable | Booking mode represented by the `RentalBookingMode` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `distanceUnit` | `string` | Yes | Not declared nullable | Distance unit text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `includedDistancePerDay` | `integer (int32)` | Yes | Not declared nullable | Numeric included distance per day for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `includedKilometersPerDay` | `integer (int32)` | Yes | Not declared nullable | Numeric included kilometers per day for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `extraKilometerRateMinor` | `integer (int64)` | Yes | Not declared nullable | Extra kilometer rate in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `offeredHandoverMode` | [RentalVehicleHandoverMode](r.md#rentalvehiclehandovermode) | Yes | Not declared nullable | Offered handover mode represented by the `RentalVehicleHandoverMode` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `selectedHandoverMode` | [RentalVehicleHandoverMode](r.md#rentalvehiclehandovermode) | Yes | Not declared nullable | Selected handover mode represented by the `RentalVehicleHandoverMode` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `pickupFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Pickup fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `deliveryFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Delivery fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `selectedHandoverFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Selected handover fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `serviceRadius` | `integer (int32)` | Yes | Not declared nullable | Numeric service radius for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `serviceRadiusKilometers` | `integer (int32)` | Yes | Not declared nullable | Numeric service radius kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `lateGraceMinutes` | `integer (int32)` | Yes | Not declared nullable | Late grace, measured in minutes. | Naming convention | No further constraint recorded |
| `lateFeePerHourMinor` | `integer (int64)` | Yes | Not declared nullable | Late fee per hour in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `complianceReminderDays` | `integer (int32)` | Yes | Not declared nullable | Compliance reminder, measured in days under this workflow's calendar rules. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalProtectionAcceptanceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `version` | `integer (int32)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `termsSha256` | `string` | Yes | Not declared nullable | Terms sha256 text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `accepted` | `boolean` | Yes | Not declared nullable | Whether accepted applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalProviderProtectionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `version` | `integer (int32)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `state` | `string` | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `country` | `string` | Yes | Not declared nullable | Country text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `kind` | `string` | No | Explicitly allowed | Kind text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `issuerName` | `string` | No | Explicitly allowed | Issuer name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `policyReference` | `string` | No | Explicitly allowed | Policy reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `policyVersion` | `string` | No | Explicitly allowed | Policy revision used for this assessment; not the mobile app build number. | Shared convention | No further constraint recorded |
| `coverageStartsAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for coverage starts at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `coverageEndsAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for coverage ends at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `coverageSummary` | `string` | No | Explicitly allowed | Coverage summary text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `exclusions` | `string[]` | Yes | Not declared nullable | Collection of exclusions for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `excessMinor` | `integer (int64)` | No | Explicitly allowed | Excess in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | No | Explicitly allowed | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `permittedDriverTerms` | `string` | No | Explicitly allowed | Permitted driver terms text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `claimsInstructions` | `string` | No | Explicitly allowed | Claims instructions text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `termsSha256` | `string` | No | Explicitly allowed | Terms sha256 text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `acceptedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for accepted at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `namedDriverCount` | `integer (int32)` | Yes | Not declared nullable | Number of named driver in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalProviderType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Individual | Individual state/choice in this specific enum. |
| `2` | Organization | Organization state/choice in this specific enum. |

## RentalQuoteDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `vehicleId` | `string (uuid)` | Yes | Not declared nullable | Account vehicle record associated with this operation or result. | Shared convention | No further constraint recorded |
| `pickupAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for pickup at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `returnAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for return at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `billableDays` | `integer (int32)` | Yes | Not declared nullable | Billable, measured in days under this workflow's calendar rules. | Naming convention | No further constraint recorded |
| `weeklyBlocks` | `integer (int32)` | Yes | Not declared nullable | Numeric weekly blocks for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `dailyBlocks` | `integer (int32)` | Yes | Not declared nullable | Numeric daily blocks for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `dailyRateMinor` | `integer (int64)` | Yes | Not declared nullable | Daily rate in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `weeklyRateMinor` | `integer (int64)` | No | Explicitly allowed | Weekly rate in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `baseAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Base amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `handoverFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Handover fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `securityDepositMinor` | `integer (int64)` | Yes | Not declared nullable | Security deposit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `totalAuthorizationMinor` | `integer (int64)` | Yes | Not declared nullable | Total authorization in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `isAvailable` | `boolean` | Yes | Not declared nullable | Whether is available applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `availabilityStatus` | `string` | Yes | Not declared nullable | Availability status text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `availabilityPolicy` | [RentalAvailabilityPolicyDto](r.md#rentalavailabilitypolicydto) | No | Not declared nullable | Availability policy represented by the `RentalAvailabilityPolicyDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalTeamDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `members` | [RentalTeamMemberDto](r.md#rentalteammemberdto)[] | Yes | Not declared nullable | Collection of members for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `invitations` | [RentalTeamInvitationDto](r.md#rentalteaminvitationdto)[] | Yes | Not declared nullable | Collection of invitations for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalTeamInvitationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `email` | `string` | Yes | Not declared nullable | Email address for this model's person/destination; its presence does not prove verification. | Shared convention | No further constraint recorded |
| `role` | [RentalOrganizationRole](r.md#rentalorganizationrole) | Yes | Not declared nullable | Role represented by the `RentalOrganizationRole` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `permissions` | [RentalOrganizationPermission](r.md#rentalorganizationpermission) | Yes | Not declared nullable | Permissions represented by the `RentalOrganizationPermission` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `status` | [RentalTeamInvitationStatus](r.md#rentalteaminvitationstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalTeamInvitationStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Accepted | Accepted state/choice in this specific enum. |
| `3` | Revoked | Revoked state/choice in this specific enum. |
| `4` | Expired | Expired state/choice in this specific enum. |

## RentalTeamMemberDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `string (uuid)` | Yes | Not declared nullable | Related account identity; the server still proves the caller's ownership or permitted relationship. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `email` | `string` | No | Explicitly allowed | Email address for this model's person/destination; its presence does not prove verification. | Shared convention | No further constraint recorded |
| `role` | [RentalOrganizationRole](r.md#rentalorganizationrole) | Yes | Not declared nullable | Role represented by the `RentalOrganizationRole` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `permissions` | [RentalOrganizationPermission](r.md#rentalorganizationpermission) | Yes | Not declared nullable | Permissions represented by the `RentalOrganizationPermission` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | Shared convention | No further constraint recorded |
| `joinedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for joined at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalVehicleCardDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `organizationId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related organization record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `companyName` | `string` | Yes | Not declared nullable | Company name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `make` | `string` | Yes | Not declared nullable | Vehicle manufacturer name/catalog selection. | Shared convention | No further constraint recorded |
| `model` | `string` | Yes | Not declared nullable | Model in the owning domain; for vehicle contracts, the vehicle model associated with the manufacturer. | Shared convention | No further constraint recorded |
| `year` | `integer (int32)` | Yes | Not declared nullable | Numeric year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `category` | `string` | Yes | Not declared nullable | Category text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `seats` | `integer (int32)` | Yes | Not declared nullable | Numeric seats for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `transmission` | `string` | Yes | Not declared nullable | Transmission text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `dailyRateMinor` | `integer (int64)` | Yes | Not declared nullable | Daily rate in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `primaryImageId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related primary image record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `bookingMode` | [RentalBookingMode](r.md#rentalbookingmode) | Yes | Not declared nullable | Booking mode represented by the `RentalBookingMode` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `hasProviderProfileImage` | `boolean` | No | Not declared nullable | Whether has provider profile image applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `providerRating` | `number (double)` | No | Explicitly allowed | Numeric provider rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `distanceKilometers` | `number (double)` | No | Explicitly allowed | Numeric distance kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalVehicleCardDtoPagedResult

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `items` | [RentalVehicleCardDto](r.md#rentalvehiclecarddto)[] | No | Explicitly allowed | Records returned in this collection/page, each using the referenced item model. | Shared convention | No further constraint recorded |
| `page` | `integer (int32)` | No | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | Shared convention | No further constraint recorded |
| `pageSize` | `integer (int32)` | No | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | Shared convention | No further constraint recorded |
| `totalCount` | `integer (int64)` | No | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | Shared convention | No further constraint recorded |
| `totalPages` | `integer (int32)` | No | Not declared nullable | Number of pages represented by this page-number model. | Shared convention | readOnly: `True` |
| `hasPreviousPage` | `boolean` | No | Not declared nullable | Whether has previous page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |
| `hasNextPage` | `boolean` | No | Not declared nullable | Whether has next page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## RentalVehicleDetailDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `organizationId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related organization record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `companyName` | `string` | Yes | Not declared nullable | Company name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `branchId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related branch record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `branchName` | `string` | Yes | Not declared nullable | Branch name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `branchAddress` | `string` | Yes | Not declared nullable | Branch address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `make` | `string` | Yes | Not declared nullable | Vehicle manufacturer name/catalog selection. | Shared convention | No further constraint recorded |
| `model` | `string` | Yes | Not declared nullable | Model in the owning domain; for vehicle contracts, the vehicle model associated with the manufacturer. | Shared convention | No further constraint recorded |
| `year` | `integer (int32)` | Yes | Not declared nullable | Numeric year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `category` | `string` | Yes | Not declared nullable | Category text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `seats` | `integer (int32)` | Yes | Not declared nullable | Numeric seats for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `transmission` | `string` | Yes | Not declared nullable | Transmission text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `fuelType` | `string` | Yes | Not declared nullable | Fuel type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `color` | `string` | Yes | Not declared nullable | Color text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `description` | `string` | Yes | Not declared nullable | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `dailyRateMinor` | `integer (int64)` | Yes | Not declared nullable | Daily rate in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `weeklyRateMinor` | `integer (int64)` | No | Explicitly allowed | Weekly rate in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `securityDepositMinor` | `integer (int64)` | Yes | Not declared nullable | Security deposit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `includedKilometersPerDay` | `integer (int32)` | Yes | Not declared nullable | Numeric included kilometers per day for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `extraKilometerRateMinor` | `integer (int64)` | Yes | Not declared nullable | Extra kilometer rate in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `bookingMode` | [RentalBookingMode](r.md#rentalbookingmode) | Yes | Not declared nullable | Booking mode represented by the `RentalBookingMode` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `images` | [RentalVehicleImageDto](r.md#rentalvehicleimagedto)[] | Yes | Not declared nullable | Collection of images for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `handoverMode` | [RentalVehicleHandoverMode](r.md#rentalvehiclehandovermode) | Yes | Not declared nullable | Handover mode represented by the `RentalVehicleHandoverMode` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `pickupFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Pickup fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `deliveryFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Delivery fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `serviceRadiusKilometers` | `integer (int32)` | Yes | Not declared nullable | Numeric service radius kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `lateGraceMinutes` | `integer (int32)` | Yes | Not declared nullable | Late grace, measured in minutes. | Naming convention | No further constraint recorded |
| `lateFeePerHourMinor` | `integer (int64)` | Yes | Not declared nullable | Late fee per hour in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `hasProviderProfileImage` | `boolean` | No | Not declared nullable | Whether has provider profile image applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `providerRating` | `number (double)` | No | Explicitly allowed | Numeric provider rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `policies` | [RentalPolicyDto](r.md#rentalpolicydto) | No | Not declared nullable | Policies represented by the `RentalPolicyDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `isFavorite` | `boolean` | No | Not declared nullable | Whether is favorite applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `distanceUnit` | `string` | No | Explicitly allowed | Distance unit text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `includedDistancePerDay` | `integer (int32)` | No | Not declared nullable | Numeric included distance per day for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `serviceRadius` | `integer (int32)` | No | Not declared nullable | Numeric service radius for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `policyVersion` | `integer (int32)` | No | Not declared nullable | Policy revision used for this assessment; not the mobile app build number. | Shared convention | No further constraint recorded |
| `policyAcceptedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for policy accepted at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalVehicleHandoverMode

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | BranchOnly | Branch only state/choice in this specific enum. |
| `2` | Pickup | Pickup state/choice in this specific enum. |
| `3` | Delivery | Delivery state/choice in this specific enum. |
| `4` | PickupAndDelivery | Pickup and delivery state/choice in this specific enum. |

## RentalVehicleImageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `altText` | `string` | Yes | Not declared nullable | Alt text text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isPrimary` | `boolean` | Yes | Not declared nullable | Whether the vehicle is designated primary in this account context; work eligibility is assessed separately. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RentalVehicleStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Draft | Draft state/choice in this specific enum. |
| `2` | PendingReview | Pending review state/choice in this specific enum. |
| `3` | Available | Available state/choice in this specific enum. |
| `4` | Reserved | Reserved state/choice in this specific enum. |
| `5` | Rented | Rented state/choice in this specific enum. |
| `6` | Maintenance | Maintenance state/choice in this specific enum. |
| `7` | Suspended | Suspended state/choice in this specific enum. |
| `8` | Archived | Archived state/choice in this specific enum. |

## ReopenSupportCaseDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `reason` | `string` | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ReplySupportTicketDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `string` | Yes | Not declared nullable | Message/content body in this model; privacy and rendering rules depend on the operation. | Shared convention | No further constraint recorded |
| `attachmentFileRefs` | `string[]` | No | Explicitly allowed | Collection of attachment file refs for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ReportVehicleDefectDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `componentCode` | `string` | Yes | Not declared nullable | Component code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `description` | `string` | Yes | Not declared nullable | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `severity` | [VehicleMaintenanceSeverity](v.md#vehiclemaintenanceseverity) | Yes | Not declared nullable | Severity represented by the `VehicleMaintenanceSeverity` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `observedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for observed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `odometer` | `number (double)` | No | Explicitly allowed | Numeric odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `reporterBelievesSafeToDrive` | `boolean` | Yes | Not declared nullable | Whether reporter believes safe to drive applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `evidenceFileRefsJson` | `string` | No | Explicitly allowed | Evidence file refs json text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `clientOperationId` | `string` | Yes | Not declared nullable | Client's stable identity for this logical operation; preserve it through interrupted responses. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ReputationCategoryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `average` | `number (double)` | Yes | Not declared nullable | Numeric average for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `count` | `integer (int32)` | Yes | Not declared nullable | Numeric count for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RequestAccountDeletionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `reason` | `string` | No | Explicitly allowed | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RequestCashoutDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `payoutMethodId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related payout method record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RequestEmailLoginDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `email` | `string` | Yes | Not declared nullable | Email address for this model's person/destination; its presence does not prove verification. | Shared convention | No further constraint recorded |
| `password` | `string` | No | Explicitly allowed | Secret password input for the established secure identity ceremony; never echo or log it. | Shared convention | No further constraint recorded |
| `countryCode` | `string` | No | Explicitly allowed | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `role` | [UserRole](u.md#userrole) | No | Not declared nullable | Role represented by the `UserRole` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RequestNameChangeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `firstName` | `string` | Yes | Not declared nullable | Person's given name as provided through the applicable profile/identity workflow. | Shared convention | No further constraint recorded |
| `lastName` | `string` | Yes | Not declared nullable | Person's family name as provided through the applicable profile/identity workflow. | Shared convention | No further constraint recorded |
| `identityFileRef` | `string` | Yes | Not declared nullable | Identity file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `reason` | `string` | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RequestOutOfBandStepUpDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `action` | `string` | Yes | Not declared nullable | Action text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `channel` | `string` | Yes | Not declared nullable | Channel text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RequestPasswordResetRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `identifier` | `string` | Yes | Not declared nullable | Sign-in identifier accepted by this identity contract; validation and privacy rules still apply. | Shared convention | No further constraint recorded |
| `lastName` | `string` | Yes | Not declared nullable | Person's family name as provided through the applicable profile/identity workflow. | Shared convention | No further constraint recorded |
| `ownershipConfirmed` | `boolean` | Yes | Not declared nullable | Whether ownership confirmed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RequestPhoneContactVerificationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `deliveryMethod` | `string` | Yes | Not declared nullable | Delivery method text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RequestPhoneLoginDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `phoneNumber` | `string` | Yes | Not declared nullable | Country-aware contact number; its presence does not prove verification or provider provisioning. | Shared convention | No further constraint recorded |
| `deliveryChannel` | `string` | Yes | Not declared nullable | Delivery channel text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `appSignature` | `string` | No | Explicitly allowed | App signature text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `countryCode` | `string` | No | Explicitly allowed | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `role` | [UserRole](u.md#userrole) | No | Not declared nullable | Role represented by the `UserRole` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RequestRatingImportDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `source` | `string` | Yes | Not declared nullable | Source text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `profileRef` | `string` | No | Explicitly allowed | Profile ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `inDriveUsername` | `string` | No | Explicitly allowed | In drive username text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `profileUrl` | `string` | No | Explicitly allowed | URL for profile; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `evidenceFileRef` | `string` | No | Explicitly allowed | Evidence file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `evidenceFileRefs` | `string[]` | No | Explicitly allowed | Collection of evidence file refs for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RequestRentalExtensionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `requestedReturnAt` | `string (date-time)` | Yes | Not declared nullable | Requested return at text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `expectedBookingVersion` | `integer (int32)` | Yes | Not declared nullable | Expected booking version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RequestRouteAlterationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `address` | `string` | Yes | Not declared nullable | Address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `placeId` | `string` | No | Explicitly allowed | Identifier of the related place record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `expectedRouteVersion` | `integer (int32)` | Yes | Not declared nullable | Expected route version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RequestTwoFactorLoginCodeRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket` | `string` | Yes | Not declared nullable | Ticket text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ResolveVehicleDefectDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `resolutionNotes` | `string` | Yes | Not declared nullable | Resolution notes text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `serviceRecordId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related service record record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | Yes | Not declared nullable | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RespondFareSplitRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `accept` | `boolean` | Yes | Not declared nullable | Whether accept applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ReviewAggregateKind

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | TripRating | Trip rating state/choice in this specific enum. |
| `2` | RentalRating | Rental rating state/choice in this specific enum. |

## ReviewAppealDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `reviewKind` | [ReviewAggregateKind](r.md#reviewaggregatekind) | Yes | Not declared nullable | Review kind represented by the `ReviewAggregateKind` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `reviewId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related review record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `status` | [ReviewAppealStatus](r.md#reviewappealstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `reasonCode` | `string` | Yes | Not declared nullable | Stable reason code; map through the applicable reason catalog instead of displaying an unrelated enum. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ReviewAppealStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Submitted | Submitted state/choice in this specific enum. |
| `2` | UnderReview | Under review state/choice in this specific enum. |
| `3` | Upheld | Upheld state/choice in this specific enum. |
| `4` | Reversed | Reversed state/choice in this specific enum. |
| `5` | Closed | Closed state/choice in this specific enum. |

## ReviewRentalExtensionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `approve` | `boolean` | Yes | Not declared nullable | Whether approve applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `reason` | `string` | No | Explicitly allowed | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |
| `expectedBookingVersion` | `integer (int32)` | Yes | Not declared nullable | Expected booking version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RevokeDependentConsentDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `reason` | `string` | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | Yes | Not declared nullable | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RideAssistanceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `mobilityCode` | `string` | Yes | Not declared nullable | Mobility code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `wheelchairWidthMillimeters` | `integer (int32)` | No | Explicitly allowed | Numeric wheelchair width millimeters for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `wheelchairLengthMillimeters` | `integer (int32)` | No | Explicitly allowed | Numeric wheelchair length millimeters for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `wheelchairCombinedWeightKilograms` | `integer (int32)` | No | Explicitly allowed | Numeric wheelchair combined weight kilograms for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `serviceAnimal` | `boolean` | Yes | Not declared nullable | Whether service animal applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `hearingCommunicationCode` | `string` | Yes | Not declared nullable | Hearing communication code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `visionCommunicationCode` | `string` | Yes | Not declared nullable | Vision communication code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `communicationCode` | `string` | Yes | Not declared nullable | Communication code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `extraBoardingMinutes` | `integer (int32)` | Yes | Not declared nullable | Extra boarding, measured in minutes. | Naming convention | No further constraint recorded |
| `profileRevision` | `integer (int64)` | Yes | Not declared nullable | Profile revision for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RideBidDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `driverProfileId` | `string (uuid)` | Yes | Not declared nullable | Driver-profile record associated with this operation or result. | Shared convention | No further constraint recorded |
| `driverName` | `string` | Yes | Not declared nullable | Driver name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `driverRating` | `number (double)` | Yes | Not declared nullable | Numeric driver rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `driverTotalTrips` | `integer (int32)` | Yes | Not declared nullable | Numeric driver total trips for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `vehicleDescription` | `string` | No | Explicitly allowed | Vehicle description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `plateNumber` | `string` | No | Explicitly allowed | Country-specific vehicle registration plate; validate through the applicable country workflow. | Shared convention | No further constraint recorded |
| `driverAvatarRef` | `string` | No | Explicitly allowed | Driver avatar ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `vehicleYear` | `integer (int32)` | Yes | Not declared nullable | Numeric vehicle year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `positiveRatingCount` | `integer (int32)` | Yes | Not declared nullable | Number of positive rating in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `negativeRatingCount` | `integer (int32)` | Yes | Not declared nullable | Number of negative rating in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `importedRatings` | [ImportedRatingBadgeDto](i.md#importedratingbadgedto)[] | Yes | Not declared nullable | Collection of imported ratings for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `isPreferredDriver` | `boolean` | Yes | Not declared nullable | Whether is preferred driver applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `type` | [BidType](b.md#bidtype) | Yes | Not declared nullable | Type represented by the `BidType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `message` | `string` | No | Explicitly allowed | Message text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `status` | [BidStatus](b.md#bidstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `version` | `integer (int64)` | No | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `trustBadges` | `string[]` | No | Explicitly allowed | Collection of trust badges for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `ratingCategories` | [ReputationCategoryDto](r.md#reputationcategorydto)[] | No | Explicitly allowed | Collection of rating categories for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `trustAchievements` | `string[]` | No | Explicitly allowed | Collection of trust achievements for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `vehicleId` | `string (uuid)` | No | Explicitly allowed | Account vehicle record associated with this operation or result. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RideDispatchMode

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Proximity | Proximity state/choice in this specific enum. |
| `2` | CountrywideHall | Countrywide hall state/choice in this specific enum. |

## RideFareRouteSource

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Provider | Provider state/choice in this specific enum. |
| `1` | GeodesicEstimate | Geodesic estimate state/choice in this specific enum. |

## RideInquiryMessageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `rideRequestId` | `string (uuid)` | Yes | Not declared nullable | Rider request record, distinct from an accepted trip. | Shared convention | No further constraint recorded |
| `driverProfileId` | `string (uuid)` | Yes | Not declared nullable | Driver-profile record associated with this operation or result. | Shared convention | No further constraint recorded |
| `senderUserId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related sender user record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `senderRole` | `string` | Yes | Not declared nullable | Sender role text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `body` | `string` | Yes | Not declared nullable | Message/content body in this model; privacy and rendering rules depend on the operation. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `readAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for read at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `version` | `integer (int64)` | No | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RideInquiryThreadDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `driverProfileId` | `string (uuid)` | Yes | Not declared nullable | Driver-profile record associated with this operation or result. | Shared convention | No further constraint recorded |
| `driverName` | `string` | Yes | Not declared nullable | Driver name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `lastMessageAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for last message at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `messageCount` | `integer (int32)` | Yes | Not declared nullable | Number of message in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `unreadCount` | `integer (int32)` | Yes | Not declared nullable | Current unread count in the applicable notification/chat model. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RideNoDriverRecoveryAction

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | WaitOrExtend | Wait or extend state/choice in this specific enum. |
| `2` | AdjustPickup | Adjust pickup state/choice in this specific enum. |
| `3` | Reschedule | Reschedule state/choice in this specific enum. |
| `4` | ReviseFare | Revise fare state/choice in this specific enum. |
| `5` | ChangeCategory | Change category state/choice in this specific enum. |
| `6` | Cancel | Cancel state/choice in this specific enum. |

## RideNoDriverRecoveryActionDecision

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `action` | [RideNoDriverRecoveryAction](r.md#ridenodriverrecoveryaction) | Yes | Not declared nullable | Action represented by the `RideNoDriverRecoveryAction` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `isAvailable` | `boolean` | Yes | Not declared nullable | Whether is available applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `execution` | [RideRecoveryExecutionKind](r.md#riderecoveryexecutionkind) | Yes | Not declared nullable | Execution represented by the `RideRecoveryExecutionKind` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `expectedRideVersion` | `integer (int64)` | No | Explicitly allowed | Expected ride version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `constraintImpact` | `string` | Yes | Not declared nullable | Constraint impact text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `unavailableReason` | `string` | No | Explicitly allowed | Unavailable reason text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `resultingExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for resulting expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RideNoDriverRecoveryProjection

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `state` | [RideNoDriverRecoveryState](r.md#ridenodriverrecoverystate) | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `expectedRideVersion` | `integer (int64)` | No | Explicitly allowed | Expected ride version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `actions` | [RideNoDriverRecoveryActionDecision](r.md#ridenodriverrecoveryactiondecision)[] | Yes | Not declared nullable | Collection of actions for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RideNoDriverRecoveryState

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | ActiveSearchNoBids | Active search no bids state/choice in this specific enum. |
| `2` | ActiveSearchWithBids | Active search with bids state/choice in this specific enum. |
| `3` | SearchExpired | Search expired state/choice in this specific enum. |
| `4` | Closed | Closed state/choice in this specific enum. |

## RideProductType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | PointToPoint | Point to point state/choice in this specific enum. |
| `2` | RoundTrip | Round trip state/choice in this specific enum. |
| `3` | Hourly | Hourly state/choice in this specific enum. |

## RideRecoveryExecutionKind

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Unavailable | Unavailable state/choice in this specific enum. |
| `1` | PassiveWait | Passive wait state/choice in this specific enum. |
| `2` | ExistingMutation | Existing mutation state/choice in this specific enum. |

## RideRequestDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `status` | [RideRequestStatus](r.md#riderequeststatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `vehicleCategoryId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related vehicle category record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `vehicleCategoryName` | `string` | Yes | Not declared nullable | Vehicle category name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `pickupLatitude` | `number (double)` | Yes | Not declared nullable | Pickup latitude in degrees; latitude is separate from address text. | Shared convention | No further constraint recorded |
| `pickupLongitude` | `number (double)` | Yes | Not declared nullable | Pickup longitude in degrees; preserve coordinate order. | Shared convention | No further constraint recorded |
| `pickupAddress` | `string` | Yes | Not declared nullable | Human pickup-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `dropoffLatitude` | `number (double)` | Yes | Not declared nullable | Destination latitude in degrees. | Shared convention | No further constraint recorded |
| `dropoffLongitude` | `number (double)` | Yes | Not declared nullable | Destination longitude in degrees. | Shared convention | No further constraint recorded |
| `dropoffAddress` | `string` | Yes | Not declared nullable | Human destination-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `distanceMeters` | `integer (int32)` | Yes | Not declared nullable | Distance represented by this model, in metres; its source/assessment depends on the operation. | Shared convention | No further constraint recorded |
| `estimatedDurationSeconds` | `integer (int32)` | Yes | Not declared nullable | Estimated duration in seconds; an estimate is not actual elapsed trip time. | Shared convention | No further constraint recorded |
| `suggestedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Suggested fare in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `surgeMultiplier` | `number (double)` | Yes | Not declared nullable | Numeric surge multiplier for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `proposedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Rider's proposed fare in currency minor units, subject to applicable quote and marketplace rules. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `paymentMethod` | [PaymentMethod](p.md#paymentmethod) | Yes | Not declared nullable | Payment method enum; availability and settlement rules are checked separately. | Shared convention | No further constraint recorded |
| `finalFareMinor` | `integer (int64)` | No | Explicitly allowed | Final fare in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `passengerCount` | `integer (int32)` | Yes | Not declared nullable | Number of passenger in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | Shared convention | No further constraint recorded |
| `scheduledForUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for scheduled for; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `bidCount` | `integer (int32)` | Yes | Not declared nullable | Number of bid in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `tripId` | `string (uuid)` | No | Explicitly allowed | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `stops` | [RideStopDto](r.md#ridestopdto)[] | No | Explicitly allowed | Ordered journey/delivery stops in the referenced stop model. | Shared convention | No further constraint recorded |
| `petFriendlyRequired` | `boolean` | No | Not declared nullable | Whether pet friendly required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `childSeatRequired` | `boolean` | No | Not declared nullable | Whether child seat required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `childSeatCount` | `integer (int32)` | No | Not declared nullable | Number of child seat in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `wheelchairAccessibleRequired` | `boolean` | No | Not declared nullable | Whether wheelchair accessible required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `airportPickup` | `boolean` | No | Not declared nullable | Whether airport pickup applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `flightNumber` | `string` | No | Explicitly allowed | Flight number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `dispatchMode` | [RideDispatchMode](r.md#ridedispatchmode) | No | Not declared nullable | Dispatch mode represented by the `RideDispatchMode` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `autoAcceptExactFare` | `boolean` | No | Not declared nullable | Whether auto accept exact fare applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `lifecycleVersion` | `integer (int64)` | No | Not declared nullable | Lifecycle version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `scheduledGuaranteeStatus` | [ScheduledRideGuaranteeStatus](s.md#scheduledrideguaranteestatus) | No | Not declared nullable | Scheduled guarantee status represented by the `ScheduledRideGuaranteeStatus` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `reservationAssignedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for reservation assigned at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `driverConfirmationOpensAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for driver confirmation opens at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `driverConfirmationDeadlineUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for driver confirmation deadline; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `driverConfirmedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for driver confirmed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `replacementAttemptCount` | `integer (int32)` | No | Not declared nullable | Number of replacement attempt in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `guaranteeStatusReason` | `string` | No | Explicitly allowed | Guarantee status reason text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `productType` | [RideProductType](r.md#rideproducttype) | No | Not declared nullable | Product type represented by the `RideProductType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `bookedHourlyMinutes` | `integer (int32)` | No | Not declared nullable | Booked hourly, measured in minutes. | Naming convention | No further constraint recorded |
| `plannedWaitingSeconds` | `integer (int32)` | No | Not declared nullable | Planned waiting, measured in seconds. | Naming convention | No further constraint recorded |
| `routeFareMinor` | `integer (int64)` | No | Not declared nullable | Route fare in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `stopChargeMinor` | `integer (int64)` | No | Not declared nullable | Stop charge in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `waitingChargeMinor` | `integer (int64)` | No | Not declared nullable | Waiting charge in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `hourlyChargeMinor` | `integer (int64)` | No | Not declared nullable | Hourly charge in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `fareLastChangedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for fare last changed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `guaranteePolicyVersion` | `string` | No | Explicitly allowed | Guarantee policy version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `guaranteeTermsUrl` | `string` | No | Explicitly allowed | URL for guarantee terms; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `guaranteeSupportPolicy` | `string` | No | Explicitly allowed | Guarantee support policy text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `guaranteeSupportSlaMinutes` | `integer (int32)` | No | Explicitly allowed | Guarantee support sla, measured in minutes. | Naming convention | No further constraint recorded |
| `guaranteeCompensationMinor` | `integer (int64)` | No | Explicitly allowed | Guarantee compensation in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `assistance` | [RideAssistanceDto](r.md#rideassistancedto) | No | Not declared nullable | Assistance represented by the `RideAssistanceDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `consistencyState` | `string` | No | Explicitly allowed | Consistency state text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RideRequestDtoPagedResult

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `items` | [RideRequestDto](r.md#riderequestdto)[] | No | Explicitly allowed | Records returned in this collection/page, each using the referenced item model. | Shared convention | No further constraint recorded |
| `page` | `integer (int32)` | No | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | Shared convention | No further constraint recorded |
| `pageSize` | `integer (int32)` | No | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | Shared convention | No further constraint recorded |
| `totalCount` | `integer (int64)` | No | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | Shared convention | No further constraint recorded |
| `totalPages` | `integer (int32)` | No | Not declared nullable | Number of pages represented by this page-number model. | Shared convention | readOnly: `True` |
| `hasPreviousPage` | `boolean` | No | Not declared nullable | Whether has previous page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |
| `hasNextPage` | `boolean` | No | Not declared nullable | Whether has next page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## RideRequestStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Requested | Requested state/choice in this specific enum. |
| `2` | Assigned | Assigned state/choice in this specific enum. |
| `3` | InProgress | In progress state/choice in this specific enum. |
| `4` | Completed | Completed state/choice in this specific enum. |
| `5` | Cancelled | Cancelled state/choice in this specific enum. |
| `6` | Expired | Expired state/choice in this specific enum. |

## RideSearchMapDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `radiusMeters` | `number (double)` | Yes | Not declared nullable | Radius, measured in metres. | Naming convention | No further constraint recorded |
| `isExpanded` | `boolean` | Yes | Not declared nullable | Whether is expanded applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `viewerCount` | `integer (int32)` | Yes | Not declared nullable | Number of viewer in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `drivers` | [NearbyDriverDto](n.md#nearbydriverdto)[] | Yes | Not declared nullable | Collection of drivers for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `serverTimeUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for server time; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `dispatchScope` | `string` | Yes | Not declared nullable | Dispatch scope text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `pickupEstimate` | [MarketplacePickupEstimateDto](m.md#marketplacepickupestimatedto) | Yes | Not declared nullable | Pickup estimate represented by the `MarketplacePickupEstimateDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `estimateFreshForSeconds` | `integer (int32)` | Yes | Not declared nullable | Estimate fresh for, measured in seconds. | Naming convention | No further constraint recorded |
| `activeViewerDefinition` | `string` | Yes | Not declared nullable | Active viewer definition text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `backgroundBehavior` | `string` | Yes | Not declared nullable | Background behavior text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isGuaranteed` | `boolean` | No | Not declared nullable | Whether is guaranteed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RideStopDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `sequence` | `integer (int32)` | Yes | Not declared nullable | Numeric sequence for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `address` | `string` | Yes | Not declared nullable | Address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `placeId` | `string` | No | Explicitly allowed | Identifier of the related place record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `arrivedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for arrived at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `type` | [RideStopType](r.md#ridestoptype) | No | Not declared nullable | Type represented by the `RideStopType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `status` | [RideStopStatus](r.md#ridestopstatus) | No | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `plannedWaitSeconds` | `integer (int32)` | No | Not declared nullable | Planned wait, measured in seconds. | Naming convention | No further constraint recorded |
| `waitingStartedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for waiting started at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `departedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for departed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `actualWaitSeconds` | `integer (int32)` | No | Not declared nullable | Actual wait, measured in seconds. | Naming convention | No further constraint recorded |
| `skippedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for skipped at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `skipReasonCode` | `string` | No | Explicitly allowed | Skip reason code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `skipReason` | `string` | No | Explicitly allowed | Skip reason text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RideStopInputDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `address` | `string` | Yes | Not declared nullable | Address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `placeId` | `string` | No | Explicitly allowed | Identifier of the related place record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `plannedWaitSeconds` | `integer (int32)` | No | Not declared nullable | Planned wait, measured in seconds. | Naming convention | No further constraint recorded |
| `type` | [RideStopType](r.md#ridestoptype) | No | Not declared nullable | Type represented by the `RideStopType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RideStopStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Arrived | Arrived state/choice in this specific enum. |
| `3` | Waiting | Waiting state/choice in this specific enum. |
| `4` | Completed | Completed state/choice in this specific enum. |
| `5` | Skipped | Skipped state/choice in this specific enum. |

## RideStopType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Intermediate | Intermediate state/choice in this specific enum. |
| `2` | Turnaround | Turnaround state/choice in this specific enum. |

## RiderAssistanceProfileDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `isEnabled` | `boolean` | Yes | Not declared nullable | Whether is enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `mobilityCode` | `string` | Yes | Not declared nullable | Mobility code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `wheelchairWidthMillimeters` | `integer (int32)` | No | Explicitly allowed | Numeric wheelchair width millimeters for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `wheelchairLengthMillimeters` | `integer (int32)` | No | Explicitly allowed | Numeric wheelchair length millimeters for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `wheelchairCombinedWeightKilograms` | `integer (int32)` | No | Explicitly allowed | Numeric wheelchair combined weight kilograms for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `serviceAnimal` | `boolean` | Yes | Not declared nullable | Whether service animal applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `hearingCommunicationCode` | `string` | Yes | Not declared nullable | Hearing communication code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `visionCommunicationCode` | `string` | Yes | Not declared nullable | Vision communication code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `communicationCode` | `string` | Yes | Not declared nullable | Communication code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `extraBoardingMinutes` | `integer (int32)` | Yes | Not declared nullable | Extra boarding, measured in minutes. | Naming convention | No further constraint recorded |
| `caregiverName` | `string` | No | Explicitly allowed | Caregiver name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `caregiverContactMasked` | `string` | No | Explicitly allowed | Caregiver contact masked text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `caregiverTripNotificationsEnabled` | `boolean` | Yes | Not declared nullable | Whether caregiver trip notifications enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |
| `consentGrantedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for consent granted at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `consentRevokedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for consent revoked at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RiderEntitlementsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `planName` | `string` | Yes | Not declared nullable | Human plan name; use plan/entitlement records for identity and authority. | Shared convention | No further constraint recorded |
| `isPaid` | `boolean` | Yes | Not declared nullable | Whether is paid applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `canUseBlockList` | `boolean` | Yes | Not declared nullable | Whether can use block list applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canUseFavorites` | `boolean` | Yes | Not declared nullable | Whether can use favorites applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canRepeatRides` | `boolean` | Yes | Not declared nullable | Whether can repeat rides applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canManageWallet` | `boolean` | Yes | Not declared nullable | Whether can manage wallet applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `monthlyRideRequestLimit` | `integer (int32)` | No | Explicitly allowed | Numeric monthly ride request limit for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RiderOnboardingDecisionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `policyVersion` | `integer (int32)` | Yes | Not declared nullable | Policy revision used for this assessment; not the mobile app build number. | Shared convention | No further constraint recorded |
| `phoneDecision` | `string` | Yes | Not declared nullable | Phone decision text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `decidedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for decided at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `phoneRequiredForOnboarding` | `boolean` | Yes | Not declared nullable | Whether phone required for onboarding applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RiderVerificationPolicyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `state` | [RiderVerificationState](r.md#riderverificationstate) | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `required` | `boolean` | Yes | Not declared nullable | Whether required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canSubmit` | `boolean` | Yes | Not declared nullable | Whether can submit applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `evaluatedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for evaluated at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RiderVerificationState

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`, `4`, `5`, `6`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | NotRequired | Not required state/choice in this specific enum. |
| `1` | NotStarted | Not started state/choice in this specific enum. |
| `2` | Pending | Pending state/choice in this specific enum. |
| `3` | Verified | Verified state/choice in this specific enum. |
| `4` | Rejected | Rejected state/choice in this specific enum. |
| `5` | Expired | Expired state/choice in this specific enum. |
| `6` | Unavailable | Unavailable state/choice in this specific enum. |

## RouteDeviationAlertDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `safetyCaseId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related safety case record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `version` | `integer (int64)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `status` | [SafetyEventStatus](s.md#safetyeventstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `passengerResponse` | [SafetyEventPassengerResponse](s.md#safetyeventpassengerresponse) | Yes | Not declared nullable | Passenger response represented by the `SafetyEventPassengerResponse` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `deviationMeters` | `integer (int32)` | No | Explicitly allowed | Deviation, measured in metres. | Naming convention | No further constraint recorded |
| `detectionSampleCount` | `integer (int32)` | Yes | Not declared nullable | Number of detection sample in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `detectionWindowSeconds` | `integer (int32)` | No | Explicitly allowed | Detection window, measured in seconds. | Naming convention | No further constraint recorded |
| `worstAccuracyMeters` | `number (double)` | No | Explicitly allowed | Worst accuracy, measured in metres. | Naming convention | No further constraint recorded |
| `alertCount` | `integer (int32)` | Yes | Not declared nullable | Number of alert in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `detectedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for detected at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `lastAlertedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last alerted at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `respondedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for responded at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `routeRejoinedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for route rejoined at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## RouteDeviationResponseRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `action` | `string` | Yes | Not declared nullable | Action text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `expectedVersion` | `integer (int64)` | Yes | Not declared nullable | Expected version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
