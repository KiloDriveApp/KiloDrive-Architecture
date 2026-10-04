# Field dictionary: S

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

The explanation basis distinguishes model-specific meaning, shared conventions,
name-derived units and type-only entries awaiting semantic review. See the
[coverage report](../reference/coverage.md); field presence is not semantic completeness.

## Models on this page

- [SafetyCaseSeverity](#safetycaseseverity)
- [SafetyEscalationChannel](#safetyescalationchannel)
- [SafetyEventPassengerResponse](#safetyeventpassengerresponse)
- [SafetyEventSeverity](#safetyeventseverity)
- [SafetyEventStatus](#safetyeventstatus)
- [SafetyEventType](#safetyeventtype)
- [SafetyEventViewDto](#safetyeventviewdto)
- [SafetyPreferencesDto](#safetypreferencesdto)
- [SaveCalculationDto](#savecalculationdto)
- [SaveDriverOnboardingProgressDto](#savedriveronboardingprogressdto)
- [SaveFamilySafetyPolicyDto](#savefamilysafetypolicydto)
- [SaveTravelCostCenterDto](#savetravelcostcenterdto)
- [SaveTravelPolicyDto](#savetravelpolicydto)
- [SavedCalculationDto](#savedcalculationdto)
- [ScheduledReportDto](#scheduledreportdto)
- [ScheduledRideGuaranteeStatus](#scheduledrideguaranteestatus)
- [ScheduledRideOperatingStatusDto](#scheduledrideoperatingstatusdto)
- [ScheduledRideRiderCheckInDto](#scheduledrideridercheckindto)
- [SecurityPreferencesDto](#securitypreferencesdto)
- [SendChatMessageRequest](#sendchatmessagerequest)
- [SendRideInquiryMessageDto](#sendrideinquirymessagedto)
- [SendSupervisedMessageDto](#sendsupervisedmessagedto)
- [SessionDto](#sessiondto)
- [SetAutoRenewRequest](#setautorenewrequest)
- [SetAvatarDto](#setavatardto)
- [SetCorporateBudgetDto](#setcorporatebudgetdto)
- [SetHouseholdConsentDto](#sethouseholdconsentdto)
- [SetLoginEmailNotificationsDto](#setloginemailnotificationsdto)
- [SetPasswordRequest](#setpasswordrequest)
- [SetRentalProviderProtectionDto](#setrentalproviderprotectiondto)
- [SetRiderPhoneOnboardingDecisionDto](#setriderphoneonboardingdecisiondto)
- [SetRiderProfilePhotoOnboardingDecisionDto](#setriderprofilephotoonboardingdecisiondto)
- [SetTravelTrackingConsentDto](#settraveltrackingconsentdto)
- [SettleRentalDepositDto](#settlerentaldepositdto)
- [SignRentalAgreementDto](#signrentalagreementdto)
- [SkipTripStopRequest](#skiptripstoprequest)
- [SocialLoginConnectionDto](#socialloginconnectiondto)
- [SocialLoginRequest](#socialloginrequest)
- [StartTripRequest](#starttriprequest)
- [StartVoiceCallRequest](#startvoicecallrequest)
- [StoreEntitlementDto](#storeentitlementdto)
- [StoreMembershipBenefitDto](#storemembershipbenefitdto)
- [StoreProductDto](#storeproductdto)
- [StorePurchaseOperationDto](#storepurchaseoperationdto)
- [StorePurchaseOpportunityDto](#storepurchaseopportunitydto)
- [StorePurchasePreparationDto](#storepurchasepreparationdto)
- [StorePurchaseQuoteDto](#storepurchasequotedto)
- [SubmitIdentityVerificationDto](#submitidentityverificationdto)
- [SubmitWebsiteContactDto](#submitwebsitecontactdto)
- [SubscribeMembershipRequest](#subscribemembershiprequest)
- [SupervisedConversationDto](#supervisedconversationdto)
- [SupervisedMessageDto](#supervisedmessagedto)
- [SupervisedParticipantDto](#supervisedparticipantdto)
- [SupportCaseActionPolicyDto](#supportcaseactionpolicydto)
- [SupportCaseCatalogDto](#supportcasecatalogdto)
- [SupportCaseSubjectDto](#supportcasesubjectdto)
- [SupportCommandOutcomeDto](#supportcommandoutcomedto)
- [SupportContractOptionDto](#supportcontractoptiondto)
- [SupportIssueTypeDto](#supportissuetypedto)
- [SupportLifecycleContractDto](#supportlifecyclecontractdto)
- [SupportTicketDetailsDto](#supportticketdetailsdto)
- [SupportTicketDto](#supportticketdto)
- [SupportTicketDtoPagedResult](#supportticketdtopagedresult)
- [SupportTicketEventDto](#supportticketeventdto)
- [SupportTicketMessageDto](#supportticketmessagedto)
- [SupportTicketStatus](#supportticketstatus)

## SafetyCaseSeverity

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Low | Low state/choice in this specific enum. |
| `2` | Moderate | Moderate state/choice in this specific enum. |
| `3` | High | High state/choice in this specific enum. |
| `4` | Critical | Critical state/choice in this specific enum. |

## SafetyEscalationChannel

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | InApp | In app state/choice in this specific enum. |
| `2` | Phone | Phone state/choice in this specific enum. |
| `3` | Sms | Sms state/choice in this specific enum. |
| `4` | Email | Email state/choice in this specific enum. |
| `5` | EmergencyServices | Emergency services state/choice in this specific enum. |

## SafetyEventPassengerResponse

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | None | None state/choice in this specific enum. |
| `1` | RouteAllowed | Route allowed state/choice in this specific enum. |
| `2` | EmergencyRequested | Emergency requested state/choice in this specific enum. |

## SafetyEventSeverity

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Unknown | Unknown state/choice in this specific enum. |
| `1` | Informational | Informational state/choice in this specific enum. |
| `2` | Attention | Attention state/choice in this specific enum. |
| `3` | SuspectedIncident | Suspected incident state/choice in this specific enum. |
| `4` | Emergency | Emergency state/choice in this specific enum. |

## SafetyEventStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Open | Open state/choice in this specific enum. |
| `2` | AwaitingCheckIn | Awaiting check in state/choice in this specific enum. |
| `3` | Escalated | Escalated state/choice in this specific enum. |
| `4` | Resolved | Resolved state/choice in this specific enum. |

## SafetyEventType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Sos | Sos state/choice in this specific enum. |
| `2` | RouteDeviation | Route deviation state/choice in this specific enum. |
| `3` | UnexpectedStop | Unexpected stop state/choice in this specific enum. |
| `4` | CollisionSuspected | Collision suspected state/choice in this specific enum. |
| `5` | CheckIn | Check in state/choice in this specific enum. |
| `6` | TelemetryGap | Telemetry gap state/choice in this specific enum. |

## SafetyEventViewDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `safetyEventId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related safety event record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `type` | [SafetyEventType](s.md#safetyeventtype) | Yes | Not declared nullable | Type represented by the `SafetyEventType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `status` | [SafetyEventStatus](s.md#safetyeventstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `passengerResponse` | [SafetyEventPassengerResponse](s.md#safetyeventpassengerresponse) | Yes | Not declared nullable | Passenger response represented by the `SafetyEventPassengerResponse` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `version` | `integer (int64)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `atUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `severity` | [SafetyEventSeverity](s.md#safetyeventseverity) | Yes | Not declared nullable | Severity represented by the `SafetyEventSeverity` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `isConnectivityIssue` | `boolean` | Yes | Not declared nullable | Whether is connectivity issue applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `connectivityReason` | `string` | No | Explicitly allowed | Connectivity reason text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `deviationMeters` | `integer (int32)` | No | Explicitly allowed | Deviation, measured in metres. | Naming convention | No further constraint recorded |
| `detectionAccuracyMeters` | `number (double)` | No | Explicitly allowed | Detection accuracy, measured in metres. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SafetyPreferencesDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `driverTrustLevel` | [DriverTrustLevel](d.md#drivertrustlevel) | Yes | Not declared nullable | Driver trust level represented by the `DriverTrustLevel` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `rideCheckEnabled` | `boolean` | Yes | Not declared nullable | Whether ride check enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `pickupConfirmationEnabled` | `boolean` | No | Not declared nullable | Whether pickup confirmation enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SaveCalculationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `calculatorType` | `string` | Yes | Not declared nullable | Calculator type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `inputs` | `schema` | Yes | Not declared nullable | Inputs text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `results` | `schema` | Yes | Not declared nullable | Results text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SaveDriverOnboardingProgressDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `currentPage` | `integer (int32)` | Yes | Not declared nullable | Numeric current page for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `devicePlatform` | `string` | No | Explicitly allowed | Device platform text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SaveFamilySafetyPolicyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `policyVersion` | `string` | Yes | Not declared nullable | Policy revision used for this assessment; not the mobile app build number. | Shared convention | No further constraint recorded |
| `isEnabled` | `boolean` | Yes | Not declared nullable | Whether is enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `minimumTravelerAge` | `integer (int32)` | Yes | Not declared nullable | Numeric minimum traveler age for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `maximumTravelerAge` | `integer (int32)` | Yes | Not declared nullable | Numeric maximum traveler age for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `consentValidityDays` | `integer (int32)` | Yes | Not declared nullable | Consent validity, measured in days under this workflow's calendar rules. | Naming convention | No further constraint recorded |
| `consentRenewalWarningDays` | `integer (int32)` | Yes | Not declared nullable | Consent renewal warning, measured in days under this workflow's calendar rules. | Naming convention | No further constraint recorded |
| `requireLiveTrackingConsent` | `boolean` | Yes | Not declared nullable | Whether require live tracking consent applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requireThreeWayCommunicationConsent` | `boolean` | Yes | Not declared nullable | Whether require three way communication consent applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requireEmergencyContactConfirmation` | `boolean` | Yes | Not declared nullable | Whether require emergency contact confirmation applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `allowCash` | `boolean` | Yes | Not declared nullable | Whether allow cash applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `allowedWeekdaysMask` | `integer (int32)` | Yes | Not declared nullable | Numeric allowed weekdays mask for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `earliestMinuteLocal` | `integer (int32)` | Yes | Not declared nullable | Numeric earliest minute local for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `latestMinuteLocal` | `integer (int32)` | Yes | Not declared nullable | Numeric latest minute local for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `minimumDriverTrustLevel` | `integer (int32)` | Yes | Not declared nullable | Numeric minimum driver trust level for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `requirePickupGuardianConfirmation` | `boolean` | Yes | Not declared nullable | Whether require pickup guardian confirmation applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requireDropoffGuardianConfirmation` | `boolean` | Yes | Not declared nullable | Whether require dropoff guardian confirmation applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | Yes | Not declared nullable | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SaveTravelCostCenterDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `monthlyBudgetMinor` | `integer (int64)` | Yes | Not declared nullable | Monthly budget in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `isActive` | `boolean` | No | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SaveTravelPolicyDto

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

## SavedCalculationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `calculatorType` | `string` | Yes | Not declared nullable | Calculator type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `inputs` | `schema` | Yes | Not declared nullable | Inputs text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `results` | `schema` | Yes | Not declared nullable | Results text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `version` | `integer (int32)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ScheduledReportDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `reportType` | `string` | Yes | Not declared nullable | Report type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `cadence` | `string` | Yes | Not declared nullable | Cadence text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `format` | `string` | Yes | Not declared nullable | Output/file format selector; use the operation's supported media rather than guessing an extension. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `lastGeneratedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last generated at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ScheduledRideGuaranteeStatus

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | NotApplicable | Not applicable state/choice in this specific enum. |
| `1` | Searching | Searching state/choice in this specific enum. |
| `2` | DriverReserved | Driver reserved state/choice in this specific enum. |
| `3` | ConfirmationRequired | Confirmation required state/choice in this specific enum. |
| `4` | Guaranteed | Guaranteed state/choice in this specific enum. |
| `5` | ReplacementSearching | Replacement searching state/choice in this specific enum. |
| `6` | NotGuaranteed | Not guaranteed state/choice in this specific enum. |
| `7` | Cancelled | Cancelled state/choice in this specific enum. |
| `8` | Scheduled | Scheduled state/choice in this specific enum. |

## ScheduledRideOperatingStatusDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `stateCode` | `string` | Yes | Not declared nullable | State code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `riskLevel` | `string` | Yes | Not declared nullable | Risk level text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `promiseCode` | `string` | Yes | Not declared nullable | Promise code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `nextAction` | `string` | Yes | Not declared nullable | Suggested next workflow step returned by the server; it does not override authorization. | Shared convention | No further constraint recorded |
| `riderActions` | `string[]` | Yes | Not declared nullable | Collection of rider actions for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `driverActions` | `string[]` | Yes | Not declared nullable | Collection of driver actions for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `driverActionRequired` | `boolean` | Yes | Not declared nullable | Whether driver action required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `supportRecommended` | `boolean` | Yes | Not declared nullable | Whether support recommended applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `confirmationOpensAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for confirmation opens at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `confirmationDeadlineUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for confirmation deadline; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `supportResponseDueAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for support response due at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `replacementAttemptCount` | `integer (int32)` | Yes | Not declared nullable | Number of replacement attempt in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `policyVersion` | `string` | No | Explicitly allowed | Policy revision used for this assessment; not the mobile app build number. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ScheduledRideRiderCheckInDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `isCheckedIn` | `boolean` | Yes | Not declared nullable | Whether is checked in applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canCheckIn` | `boolean` | Yes | Not declared nullable | Whether can check in applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `state` | `string` | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `nextAction` | `string` | Yes | Not declared nullable | Suggested next workflow step returned by the server; it does not override authorization. | Shared convention | No further constraint recorded |
| `scheduledForUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for scheduled for; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `opensAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for opens at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `closesAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for closes at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `checkedInAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for checked in at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `tripLifecycleVersion` | `integer (int64)` | Yes | Not declared nullable | Trip lifecycle version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `rideLifecycleVersion` | `integer (int64)` | Yes | Not declared nullable | Ride lifecycle version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SecurityPreferencesDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `loginEmailNotificationsEnabled` | `boolean` | Yes | Not declared nullable | Whether login email notifications enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `emailVerified` | `boolean` | Yes | Not declared nullable | Whether email verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `email` | `string` | No | Explicitly allowed | Email address for this model's person/destination; its presence does not prove verification. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SendChatMessageRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `string` | Yes | Not declared nullable | Message/content body in this model; privacy and rendering rules depend on the operation. | Shared convention | No further constraint recorded |
| `clientMessageId` | `string` | No | Explicitly allowed | Stable client message identity used for deduplication or reconciliation after a lost chat response. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SendRideInquiryMessageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `body` | `string` | Yes | Not declared nullable | Message/content body in this model; privacy and rendering rules depend on the operation. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SendSupervisedMessageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `clientMessageId` | `string (uuid)` | Yes | Not declared nullable | Stable client message identity used for deduplication or reconciliation after a lost chat response. | Shared convention | No further constraint recorded |
| `body` | `string` | Yes | Not declared nullable | Message/content body in this model; privacy and rendering rules depend on the operation. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SessionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `deviceName` | `string` | No | Explicitly allowed | Device name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `ipAddress` | `string` | No | Explicitly allowed | Ip address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `userAgent` | `string` | No | Explicitly allowed | User agent text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `deviceManufacturer` | `string` | No | Explicitly allowed | Device manufacturer text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `deviceModel` | `string` | No | Explicitly allowed | Device model text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `operatingSystem` | `string` | No | Explicitly allowed | Operating system text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `appVersion` | `string` | No | Explicitly allowed | App version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `installationId` | `string` | No | Explicitly allowed | Identifier of the related installation record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `isCurrent` | `boolean` | Yes | Not declared nullable | Whether is current applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SetAutoRenewRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `enabled` | `boolean` | Yes | Not declared nullable | Whether enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SetAvatarDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `fileRef` | `string` | Yes | Not declared nullable | Private storage reference; not a permanent public URL or approval decision. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SetCorporateBudgetDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `costCenterCode` | `string` | Yes | Not declared nullable | Cost center code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `periodStartsAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for period starts at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `periodEndsAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for period ends at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `limitMinor` | `integer (int64)` | Yes | Not declared nullable | Limit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | Yes | Not declared nullable | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SetHouseholdConsentDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `consentState` | [HouseholdConsentState](h.md#householdconsentstate) | Yes | Not declared nullable | Consent state represented by the `HouseholdConsentState` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `expectedMemberRevision` | `integer (int64)` | Yes | Not declared nullable | Expected member revision for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `expectedHouseholdRevision` | `integer (int64)` | Yes | Not declared nullable | Expected household revision for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SetLoginEmailNotificationsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `enabled` | `boolean` | Yes | Not declared nullable | Whether enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SetPasswordRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `newPassword` | `string` | Yes | Not declared nullable | Private new password used by this specific ceremony; never log, publish or substitute it for another proof. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SetRentalProviderProtectionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `expectedVersion` | `integer (int32)` | Yes | Not declared nullable | Expected version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `isOffered` | `boolean` | Yes | Not declared nullable | Whether is offered applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `kind` | `string` | Yes | Not declared nullable | Kind text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `issuerName` | `string` | Yes | Not declared nullable | Issuer name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `policyReference` | `string` | Yes | Not declared nullable | Policy reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `policyVersion` | `string` | Yes | Not declared nullable | Policy revision used for this assessment; not the mobile app build number. | Shared convention | No further constraint recorded |
| `coverageStartsAt` | `string (date-time)` | Yes | Not declared nullable | Coverage starts at text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `coverageEndsAt` | `string (date-time)` | Yes | Not declared nullable | Coverage ends at text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `coverageSummary` | `string` | Yes | Not declared nullable | Coverage summary text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `exclusions` | `string[]` | Yes | Not declared nullable | Collection of exclusions for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `excessMinor` | `integer (int64)` | Yes | Not declared nullable | Excess in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `permittedDriverTerms` | `string` | Yes | Not declared nullable | Permitted driver terms text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `claimsInstructions` | `string` | Yes | Not declared nullable | Claims instructions text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `providerResponsibilityConfirmed` | `boolean` | Yes | Not declared nullable | Whether provider responsibility confirmed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `evidenceUploadId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related evidence upload record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SetRiderPhoneOnboardingDecisionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `policyVersion` | `integer (int32)` | Yes | Not declared nullable | Policy revision used for this assessment; not the mobile app build number. | Shared convention | No further constraint recorded |
| `skip` | `boolean` | Yes | Not declared nullable | Whether skip applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SetRiderProfilePhotoOnboardingDecisionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `skip` | `boolean` | Yes | Not declared nullable | Whether skip applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SetTravelTrackingConsentDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `granted` | `boolean` | Yes | Not declared nullable | Whether granted applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SettleRentalDepositDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `capturedMinor` | `integer (int64)` | Yes | Not declared nullable | Captured in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `releasedMinor` | `integer (int64)` | Yes | Not declared nullable | Released in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `providerReference` | `string` | Yes | Not declared nullable | Provider reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `expectedBookingVersion` | `integer (int32)` | Yes | Not declared nullable | Expected booking version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SignRentalAgreementDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `expectedBookingVersion` | `integer (int32)` | Yes | Not declared nullable | Expected booking version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SkipTripStopRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `expectedLifecycleVersion` | `integer (int64)` | Yes | Not declared nullable | Expected lifecycle version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `reasonCode` | `string` | Yes | Not declared nullable | Stable reason code; map through the applicable reason catalog instead of displaying an unrelated enum. | Shared convention | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SocialLoginConnectionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `provider` | `string` | Yes | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SocialLoginRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `provider` | `string` | Yes | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | Shared convention | No further constraint recorded |
| `idToken` | `string` | No | Explicitly allowed | Private id token used by this specific ceremony; never log, publish or substitute it for another proof. | Naming convention | No further constraint recorded |
| `accessToken` | `string` | No | Explicitly allowed | Sensitive bearer access credential for the issued session. | Shared convention | No further constraint recorded |
| `role` | [UserRole](u.md#userrole) | Yes | Not declared nullable | Role represented by the `UserRole` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `firstName` | `string` | No | Explicitly allowed | Person's given name as provided through the applicable profile/identity workflow. | Shared convention | No further constraint recorded |
| `lastName` | `string` | No | Explicitly allowed | Person's family name as provided through the applicable profile/identity workflow. | Shared convention | No further constraint recorded |
| `nonce` | `string` | No | Explicitly allowed | Nonce text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `createAccount` | `boolean` | No | Not declared nullable | Whether create account applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `countryCode` | `string` | No | Explicitly allowed | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `driverAccountType` | [DriverAccountType](d.md#driveraccounttype) | No | Not declared nullable | Driver account type represented by the `DriverAccountType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `createRentalOrganization` | `boolean` | No | Not declared nullable | Whether create rental organization applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `phoneNumber` | `string` | No | Explicitly allowed | Country-aware contact number; its presence does not prove verification or provider provisioning. | Shared convention | No further constraint recorded |
| `businessLegalName` | `string` | No | Explicitly allowed | Business legal name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `businessTradingName` | `string` | No | Explicitly allowed | Business trading name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `businessRegistrationNumber` | `string` | No | Explicitly allowed | Business registration number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `businessTaxNumber` | `string` | No | Explicitly allowed | Business tax number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `businessRegisteredAddress` | `string` | No | Explicitly allowed | Business registered address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `authorizationCode` | `string` | No | Explicitly allowed | Authorization code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## StartTripRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `riderPin` | `string` | No | Explicitly allowed | Rider pin text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `challengeId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related challenge record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `qrPayload` | `string` | No | Explicitly allowed | Qr payload text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## StartVoiceCallRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## StoreEntitlementDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `purchaseId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related purchase record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `planId` | `string (uuid)` | Yes | Not declared nullable | Membership catalog record; it does not itself prove a user entitlement. | Shared convention | No further constraint recorded |
| `planName` | `string` | Yes | Not declared nullable | Human plan name; use plan/entitlement records for identity and authority. | Shared convention | No further constraint recorded |
| `audience` | `string` | Yes | Not declared nullable | Applicable product/client audience, distinct from verified security authority. | Shared convention | No further constraint recorded |
| `productId` | `string` | Yes | Not declared nullable | Identifier of the related product record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `platform` | `string` | Yes | Not declared nullable | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | Shared convention | Allowed wire values: `apple`, `google` |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `restored` | `boolean` | Yes | Not declared nullable | Whether restored applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `willAutoRenew` | `boolean` | Yes | Not declared nullable | Whether will auto renew applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `gracePeriodExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for grace period expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `acknowledgementPending` | `boolean` | No | Not declared nullable | Whether acknowledgement pending applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `reconciliationStatus` | `string` | No | Explicitly allowed | Reconciliation status text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `lastReconciledAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last reconciled at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `nextReconciliationAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for next reconciliation at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `reconciliationErrorCode` | `string` | No | Explicitly allowed | Reconciliation error code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## StoreMembershipBenefitDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `priceEvidence` | `string` | Yes | Not declared nullable | Price evidence text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `commissionEffect` | `string` | Yes | Not declared nullable | Commission effect text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `maxBidsPerDay` | `integer (int32)` | Yes | Not declared nullable | Plan allotment for new bids in the server-defined daily usage period; re-bid rules are separate. | Shared convention | No further constraint recorded |
| `maxAcceptedTripsPerWeek` | `integer (int32)` | No | Explicitly allowed | Catalog allotment for accepted trips in the applicable weekly period; use authoritative usage/readiness checks. | Shared convention | No further constraint recorded |
| `maxVehiclesEligibleForBidding` | `integer (int32)` | Yes | Not declared nullable | Numeric max vehicles eligible for bidding for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `maxVehicleChangesPerPeriod` | `integer (int32)` | Yes | Not declared nullable | Plan's vehicle-change allotment for its usage period; assignment and verification checks still apply. | Shared convention | No further constraint recorded |
| `maxFavorites` | `integer (int32)` | Yes | Not declared nullable | Plan's applicable saved-favorite allotment; ownership and feature policy still apply. | Shared convention | No further constraint recorded |
| `bidsUsedToday` | `integer (int32)` | No | Explicitly allowed | Numeric bids used today for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `acceptedTripsUsedThisWeek` | `integer (int32)` | No | Explicitly allowed | Numeric accepted trips used this week for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `registeredVehicles` | `integer (int32)` | No | Explicitly allowed | Numeric registered vehicles for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `favoritesUsed` | `integer (int32)` | No | Explicitly allowed | Numeric favorites used for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `renewalTermsCode` | `string` | Yes | Not declared nullable | Renewal terms code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `cancellationTermsCode` | `string` | Yes | Not declared nullable | Cancellation terms code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `estimatedBreakEvenTrips` | `integer (int32)` | No | Explicitly allowed | Numeric estimated break even trips for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `breakEvenAssumptionsCode` | `string` | Yes | Not declared nullable | Break even assumptions code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `opportunity` | [StorePurchaseOpportunityDto](s.md#storepurchaseopportunitydto) | Yes | Not declared nullable | Opportunity represented by the `StorePurchaseOpportunityDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## StoreProductDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `planId` | `string (uuid)` | Yes | Not declared nullable | Membership catalog record; it does not itself prove a user entitlement. | Shared convention | No further constraint recorded |
| `audience` | `string` | Yes | Not declared nullable | Applicable product/client audience, distinct from verified security authority. | Shared convention | No further constraint recorded |
| `planName` | `string` | Yes | Not declared nullable | Human plan name; use plan/entitlement records for identity and authority. | Shared convention | No further constraint recorded |
| `platform` | `string` | Yes | Not declared nullable | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | Shared convention | Allowed wire values: `apple`, `google` |
| `productId` | `string` | Yes | Not declared nullable | Exact native store product identifier in the reviewed mapping; not the membership plan UUID. | Model-specific | No further constraint recorded |
| `termDays` | `integer (int32)` | Yes | Not declared nullable | Requested/applicable membership term in days; only configured valid terms are allowed. | Shared convention | No further constraint recorded |
| `basePriceMinor` | `integer (int64)` | Yes | Not declared nullable | Base price in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `baseCurrency` | `string` | Yes | Not declared nullable | Currency of the catalog/quote's base amount, distinct from the displayed local currency. | Shared convention | No further constraint recorded |
| `appleSubscriptionGroupReference` | `string` | No | Explicitly allowed | Apple subscription group reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `googleBasePlanId` | `string` | No | Explicitly allowed | Google subscription base-plan identifier where the mapping uses one. | Model-specific | No further constraint recorded |
| `googleOfferId` | `string` | No | Explicitly allowed | Google offer identifier where an offer applies; it is distinct from the base plan. | Model-specific | No further constraint recorded |
| `description` | `string` | No | Explicitly allowed | Human-readable store-product description; the mapped plan and native offer establish the actual purchase. | Model-specific | No further constraint recorded |
| `countryCode` | `string` | No | Explicitly allowed | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `currency` | `string` | No | Explicitly allowed | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `mappingVersion` | `string` | No | Explicitly allowed | Mapping version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `canPurchase` | `boolean` | No | Not declared nullable | Server eligibility result for this mapping/context; the native storefront must still return the matching offer. | Model-specific | No further constraint recorded |
| `planPriceMinor` | `integer (int64)` | No | Explicitly allowed | Plan price in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `planCurrency` | `string` | No | Explicitly allowed | Plan currency text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `benefits` | [StoreMembershipBenefitDto](s.md#storemembershipbenefitdto) | No | Not declared nullable | Benefits represented by the `StoreMembershipBenefitDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `purchaseDisabledReason` | `string` | No | Explicitly allowed | Purchase disabled reason text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `exactLocalizedPrice` | `string` | No | Explicitly allowed | Localized store-price evidence when available; absence must not be replaced with an invented payable store price. | Model-specific | No further constraint recorded |
| `priceEvidenceId` | `string` | No | Explicitly allowed | Identifier of the related price evidence record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## StorePurchaseOperationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `operationId` | `string (uuid)` | Yes | Not declared nullable | Durable operation reference used for applicable outcome discovery. | Shared convention | No further constraint recorded |
| `state` | `string` | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `membershipPlanId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related membership plan record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `planName` | `string` | No | Explicitly allowed | Human plan name; use plan/entitlement records for identity and authority. | Shared convention | No further constraint recorded |
| `transactionId` | `string` | No | Explicitly allowed | Identifier of the related transaction record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `safeRetryAllowed` | `boolean` | Yes | Not declared nullable | Whether safe retry allowed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `safeInstructionCode` | `string` | Yes | Not declared nullable | Safe instruction code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `supportReference` | `string` | Yes | Not declared nullable | Support reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `lastProviderCheckAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last provider check at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `entitlementExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for entitlement expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## StorePurchaseOpportunityDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `required` | `boolean` | Yes | Not declared nullable | Whether required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `eligible` | `boolean` | Yes | Not declared nullable | Whether eligible applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `windowDays` | `integer (int32)` | Yes | Not declared nullable | Window, measured in days under this workflow's calendar rules. | Naming convention | No further constraint recorded |
| `recentRequests` | `integer (int32)` | Yes | Not declared nullable | Numeric recent requests for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `eligibleDrivers` | `integer (int32)` | Yes | Not declared nullable | Numeric eligible drivers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `requiredRequests` | `integer (int32)` | Yes | Not declared nullable | Numeric required requests for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `evidenceCode` | `string` | Yes | Not declared nullable | Evidence code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## StorePurchasePreparationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `operationId` | `string (uuid)` | Yes | Not declared nullable | Durable operation reference used for applicable outcome discovery. | Shared convention | No further constraint recorded |
| `state` | `string` | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `quoteExpiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for quote expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `googleObfuscatedAccountId` | `string` | No | Explicitly allowed | Identifier of the related google obfuscated account record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `googleObfuscatedProfileId` | `string` | No | Explicitly allowed | Identifier of the related google obfuscated profile record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## StorePurchaseQuoteDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `planId` | `string (uuid)` | Yes | Not declared nullable | Membership catalog record; it does not itself prove a user entitlement. | Shared convention | No further constraint recorded |
| `platform` | `string` | Yes | Not declared nullable | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | Shared convention | No further constraint recorded |
| `productId` | `string` | Yes | Not declared nullable | Identifier of the related product record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `termDays` | `integer (int32)` | Yes | Not declared nullable | Requested/applicable membership term in days; only configured valid terms are allowed. | Shared convention | No further constraint recorded |
| `googleBasePlanId` | `string` | No | Explicitly allowed | Identifier of the related google base plan record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `googleOfferId` | `string` | No | Explicitly allowed | Identifier of the related google offer record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `localizedPrice` | `string` | Yes | Not declared nullable | Localized price text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `priceMinor` | `integer (int64)` | Yes | Not declared nullable | Price in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `mappingVersion` | `string` | Yes | Not declared nullable | Mapping version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `quoteToken` | `string` | Yes | Not declared nullable | Server-owned quote evidence; preserve currency/amount/expiry binding and treat it as private. | Shared convention | No further constraint recorded |
| `googleTransition` | [GoogleSubscriptionTransitionDto](g.md#googlesubscriptiontransitiondto) | No | Not declared nullable | Google transition represented by the `GoogleSubscriptionTransitionDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SubmitIdentityVerificationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `dateOfBirth` | `string (date)` | Yes | Not declared nullable | Calendar date for date of birth; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |
| `gender` | `string` | Yes | Not declared nullable | Gender text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `documentType` | [DocumentType](d.md#documenttype) | Yes | Not declared nullable | Document type represented by the `DocumentType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `frontFileRef` | `string` | Yes | Not declared nullable | Front file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `backFileRef` | `string` | No | Explicitly allowed | Back file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `driverLicenseNumber` | `string` | No | Explicitly allowed | Driver license number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `driverLicenseControlNumber` | `string` | No | Explicitly allowed | Driver license control number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `driverLicenseOriginalIssueDate` | `string (date)` | No | Explicitly allowed | Calendar date for driver license original issue date; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |
| `driverLicenseExpiresOn` | `string (date)` | No | Explicitly allowed | Calendar date for driver license expires on; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |
| `onboardingSubmission` | `boolean` | No | Not declared nullable | Whether onboarding submission applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SubmitWebsiteContactDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `email` | `string` | No | Explicitly allowed | Email address for this model's person/destination; its presence does not prove verification. | Shared convention | No further constraint recorded |
| `phone` | `string` | No | Explicitly allowed | Phone text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `subject` | `string` | Yes | Not declared nullable | Subject text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `message` | `string` | Yes | Not declared nullable | Message text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `clientIpAddress` | `string` | No | Explicitly allowed | Client ip address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `browserDetails` | `string` | No | Explicitly allowed | Browser details text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SubscribeMembershipRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `planId` | `string (uuid)` | Yes | Not declared nullable | Membership catalog record; it does not itself prove a user entitlement. | Shared convention | No further constraint recorded |
| `termDays` | `integer (int32)` | No | Not declared nullable | Requested/applicable membership term in days; only configured valid terms are allowed. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupervisedConversationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `conversationKind` | `string` | Yes | Not declared nullable | Conversation kind text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `state` | `string` | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |
| `conversationClosesAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for conversation closes at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `retainUntilUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for retain until; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `currentUserRole` | `string` | Yes | Not declared nullable | Current user role text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `canSend` | `boolean` | Yes | Not declared nullable | Whether can send applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `participants` | [SupervisedParticipantDto](s.md#supervisedparticipantdto)[] | Yes | Not declared nullable | Collection of participants for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `messages` | [SupervisedMessageDto](s.md#supervisedmessagedto)[] | Yes | Not declared nullable | Collection of messages for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupervisedMessageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `clientMessageId` | `string (uuid)` | Yes | Not declared nullable | Stable client message identity used for deduplication or reconciliation after a lost chat response. | Shared convention | No further constraint recorded |
| `senderUserId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related sender user record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `senderRole` | `string` | Yes | Not declared nullable | Sender role text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `body` | `string` | Yes | Not declared nullable | Message/content body in this model; privacy and rendering rules depend on the operation. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupervisedParticipantDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `string (uuid)` | Yes | Not declared nullable | Related account identity; the server still proves the caller's ownership or permitted relationship. | Shared convention | No further constraint recorded |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | Shared convention | No further constraint recorded |
| `role` | `string` | Yes | Not declared nullable | Role text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `canRead` | `boolean` | Yes | Not declared nullable | Whether can read applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canSend` | `boolean` | Yes | Not declared nullable | Whether can send applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupportCaseActionPolicyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `canReply` | `boolean` | Yes | Not declared nullable | Whether can reply applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canClose` | `boolean` | Yes | Not declared nullable | Whether can close applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canReopen` | `boolean` | Yes | Not declared nullable | Whether can reopen applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canEscalate` | `boolean` | Yes | Not declared nullable | Whether can escalate applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `reopenUntilUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for reopen until; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `reopenPolicy` | `string` | Yes | Not declared nullable | Reopen policy text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `escalationPolicy` | `string` | Yes | Not declared nullable | Escalation policy text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `reopenPolicyCode` | `string` | No | Explicitly allowed | Reopen policy code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `escalationPolicyCode` | `string` | No | Explicitly allowed | Escalation policy code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupportCaseCatalogDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `subjects` | [SupportCaseSubjectDto](s.md#supportcasesubjectdto)[] | Yes | Not declared nullable | Collection of subjects for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `issueTypes` | [SupportIssueTypeDto](s.md#supportissuetypedto)[] | Yes | Not declared nullable | Collection of issue types for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `contract` | [SupportLifecycleContractDto](s.md#supportlifecyclecontractdto) | No | Not declared nullable | Contract represented by the `SupportLifecycleContractDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupportCaseSubjectDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `subjectType` | `string` | Yes | Not declared nullable | Subject type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `label` | `string` | Yes | Not declared nullable | Label text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `amountMinor` | `integer (int64)` | No | Explicitly allowed | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `currency` | `string` | No | Explicitly allowed | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupportCommandOutcomeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `schemaVersion` | `integer (int32)` | Yes | Not declared nullable | Schema version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `outcome` | `string` | Yes | Not declared nullable | Result/recovery state of this operation; unknown or pending is not failed or successful. | Shared convention | No further constraint recorded |
| `path` | `string` | Yes | Not declared nullable | Path text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `action` | `string` | Yes | Not declared nullable | Action text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `keySha256` | `string` | Yes | Not declared nullable | Key sha256 text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `payloadSha256` | `string` | Yes | Not declared nullable | Payload sha256 text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `ticketId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related ticket record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `messageId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related message record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `expectedCaseVersion` | `integer (int64)` | No | Explicitly allowed | Expected case version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `resultCaseVersion` | `integer (int64)` | Yes | Not declared nullable | Result case version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupportContractOptionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `localizationKey` | `string` | Yes | Not declared nullable | Localization key text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `wireValue` | `integer (int32)` | No | Explicitly allowed | Numeric wire value for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `subjectType` | `string` | No | Explicitly allowed | Subject type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupportIssueTypeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `subjectType` | `string` | Yes | Not declared nullable | Subject type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `localizationKey` | `string` | No | Explicitly allowed | Localization key text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupportLifecycleContractDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `version` | `integer (int32)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `statuses` | [SupportContractOptionDto](s.md#supportcontractoptiondto)[] | Yes | Not declared nullable | Collection of statuses for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `priorities` | [SupportContractOptionDto](s.md#supportcontractoptiondto)[] | Yes | Not declared nullable | Collection of priorities for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `nextActions` | [SupportContractOptionDto](s.md#supportcontractoptiondto)[] | Yes | Not declared nullable | Collection of next actions for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `reopenPolicyCode` | `string` | Yes | Not declared nullable | Reopen policy code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `escalationPolicyCode` | `string` | Yes | Not declared nullable | Escalation policy code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `issueTypes` | [SupportIssueTypeDto](s.md#supportissuetypedto)[] | No | Explicitly allowed | Collection of issue types for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `subjectTypes` | [SupportContractOptionDto](s.md#supportcontractoptiondto)[] | No | Explicitly allowed | Collection of subject types for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupportTicketDetailsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `ticket` | [SupportTicketDto](s.md#supportticketdto) | Yes | Not declared nullable | Ticket represented by the `SupportTicketDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `messages` | [SupportTicketMessageDto](s.md#supportticketmessagedto)[] | Yes | Not declared nullable | Collection of messages for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `timeline` | [SupportTicketEventDto](s.md#supportticketeventdto)[] | No | Explicitly allowed | Collection of timeline for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `actions` | [SupportCaseActionPolicyDto](s.md#supportcaseactionpolicydto) | No | Not declared nullable | Actions represented by the `SupportCaseActionPolicyDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupportTicketDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `referenceCode` | `string` | Yes | Not declared nullable | Reference code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `ticketType` | `string` | Yes | Not declared nullable | Ticket type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `subject` | `string` | Yes | Not declared nullable | Subject text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `body` | `string` | Yes | Not declared nullable | Message/content body in this model; privacy and rendering rules depend on the operation. | Shared convention | No further constraint recorded |
| `status` | [SupportTicketStatus](s.md#supportticketstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `adminNote` | `string` | No | Explicitly allowed | Admin note text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `attachmentFileRefs` | `string[]` | Yes | Not declared nullable | Collection of attachment file refs for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `answeredAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for answered at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `slaDueAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for sla due at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `slaPriority` | `string` | No | Explicitly allowed | Sla priority text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `subjectType` | `string` | No | Explicitly allowed | Subject type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `subjectEntityId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related subject entity record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `subjectLabel` | `string` | No | Explicitly allowed | Subject label text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `issueType` | `string` | No | Explicitly allowed | Issue type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `assignedToUserId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related assigned to user record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `resolutionCode` | `string` | No | Explicitly allowed | Resolution code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `resolutionSummary` | `string` | No | Explicitly allowed | Resolution summary text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `lastUserMessageAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last user message at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `lastSupportMessageAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last support message at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `hasUnreadSupportReply` | `boolean` | No | Not declared nullable | Whether has unread support reply applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `caseVersion` | `integer (int64)` | No | Not declared nullable | Case version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `ownerDisplayName` | `string` | No | Explicitly allowed | Owner display name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `nextAction` | `string` | No | Explicitly allowed | Suggested next workflow step returned by the server; it does not override authorization. | Shared convention | No further constraint recorded |
| `ageHours` | `integer (int64)` | No | Not declared nullable | Numeric age hours for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `slaBreached` | `boolean` | No | Not declared nullable | Whether sla breached applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `statusCode` | `string` | No | Explicitly allowed | Status code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `priorityCode` | `string` | No | Explicitly allowed | Priority code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `issueCode` | `string` | No | Explicitly allowed | Issue code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `contractVersion` | `integer (int32)` | No | Not declared nullable | Contract version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupportTicketDtoPagedResult

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `items` | [SupportTicketDto](s.md#supportticketdto)[] | No | Explicitly allowed | Records returned in this collection/page, each using the referenced item model. | Shared convention | No further constraint recorded |
| `page` | `integer (int32)` | No | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | Shared convention | No further constraint recorded |
| `pageSize` | `integer (int32)` | No | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | Shared convention | No further constraint recorded |
| `totalCount` | `integer (int64)` | No | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | Shared convention | No further constraint recorded |
| `totalPages` | `integer (int32)` | No | Not declared nullable | Number of pages represented by this page-number model. | Shared convention | readOnly: `True` |
| `hasPreviousPage` | `boolean` | No | Not declared nullable | Whether has previous page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |
| `hasNextPage` | `boolean` | No | Not declared nullable | Whether has next page applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | readOnly: `True` |

**Additional object properties:** not allowed by the schema.

## SupportTicketEventDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `eventType` | `string` | Yes | Not declared nullable | Event type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `fromStatus` | [SupportTicketStatus](s.md#supportticketstatus) | No | Not declared nullable | From status represented by the `SupportTicketStatus` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `toStatus` | [SupportTicketStatus](s.md#supportticketstatus) | No | Not declared nullable | To status represented by the `SupportTicketStatus` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `reasonCode` | `string` | No | Explicitly allowed | Stable reason code; map through the applicable reason catalog instead of displaying an unrelated enum. | Shared convention | No further constraint recorded |
| `actorType` | `string` | Yes | Not declared nullable | Actor type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupportTicketMessageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `authorUserId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related author user record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `authorType` | `string` | Yes | Not declared nullable | Author type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `body` | `string` | Yes | Not declared nullable | Message/content body in this model; privacy and rendering rules depend on the operation. | Shared convention | No further constraint recorded |
| `attachmentFileRefs` | `string[]` | Yes | Not declared nullable | Collection of attachment file refs for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `authorName` | `string` | No | Explicitly allowed | Author name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `authorFriendlyUserId` | `string` | No | Explicitly allowed | Identifier of the related author friendly user record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## SupportTicketStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `10`, `20`, `30`, `40`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Open | Open state/choice in this specific enum. |
| `2` | Answered | Answered state/choice in this specific enum. |
| `3` | Closed | Closed state/choice in this specific enum. |
| `10` | Received | Received state/choice in this specific enum. |
| `20` | Reviewing | Reviewing state/choice in this specific enum. |
| `30` | WaitingForInformation | Waiting for information state/choice in this specific enum. |
| `40` | Resolved | Resolved state/choice in this specific enum. |
