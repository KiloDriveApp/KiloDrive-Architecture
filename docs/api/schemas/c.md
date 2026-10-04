# Field dictionary: C

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

The explanation basis distinguishes model-specific meaning, shared conventions,
name-derived units and type-only entries awaiting semantic review. See the
[coverage report](../reference/coverage.md); field presence is not semantic completeness.

## Models on this page

- [CalculatorPdfRequest](#calculatorpdfrequest)
- [CalculatorPdfRowDto](#calculatorpdfrowdto)
- [CampaignChannel](#campaignchannel)
- [CampaignInboxItemDto](#campaigninboxitemdto)
- [CancelPendingMembershipChangeRequest](#cancelpendingmembershipchangerequest)
- [CancelRentalBookingDto](#cancelrentalbookingdto)
- [CancelRequest](#cancelrequest)
- [CashoutDto](#cashoutdto)
- [CashoutLimitsDto](#cashoutlimitsdto)
- [CashoutReconciliationState](#cashoutreconciliationstate)
- [CashoutSettlementState](#cashoutsettlementstate)
- [CashoutStatus](#cashoutstatus)
- [CashoutStatusHistoryEntryDto](#cashoutstatushistoryentrydto)
- [CashoutStatusResourceDto](#cashoutstatusresourcedto)
- [ChatMessageCommitOutcome](#chatmessagecommitoutcome)
- [ChatMessageDto](#chatmessagedto)
- [CloseSupportCaseDto](#closesupportcasedto)
- [CompleteDriverOnboardingDto](#completedriveronboardingdto)
- [CompleteProfileDto](#completeprofiledto)
- [CompleteTripRequest](#completetriprequest)
- [CompleteVehicleServiceDto](#completevehicleservicedto)
- [ConfigureFareSplitDto](#configurefaresplitdto)
- [ConfirmContactTwoFactorEnrollmentRequest](#confirmcontacttwofactorenrollmentrequest)
- [ConfirmDeliveryVerificationDto](#confirmdeliveryverificationdto)
- [ConfirmDriverOnboardingStepDto](#confirmdriveronboardingstepdto)
- [ConfirmEmailLoginDto](#confirmemaillogindto)
- [ConfirmEmailVerificationDto](#confirmemailverificationdto)
- [ConfirmPasswordResetRequest](#confirmpasswordresetrequest)
- [ConfirmPendingSocialLinkRequest](#confirmpendingsociallinkrequest)
- [ConfirmPhoneContactVerificationDto](#confirmphonecontactverificationdto)
- [ConfirmPhoneLoginDto](#confirmphonelogindto)
- [ConfirmPhoneVerificationRequest](#confirmphoneverificationrequest)
- [ConfirmSupervisedHandoffDto](#confirmsupervisedhandoffdto)
- [ContactDetailsDto](#contactdetailsdto)
- [ContactTwoFactorEnrollmentDto](#contacttwofactorenrollmentdto)
- [ContactVerificationChallengeDto](#contactverificationchallengedto)
- [ContentPageDto](#contentpagedto)
- [CorporateAccountDto](#corporateaccountdto)
- [CorporateAccountStatus](#corporateaccountstatus)
- [CorporateBudgetDto](#corporatebudgetdto)
- [CorporateMemberPermission](#corporatememberpermission)
- [CorporateMemberRole](#corporatememberrole)
- [CountryReferenceDto](#countryreferencedto)
- [CourierProductSettingsDto](#courierproductsettingsdto)
- [CreateBusinessShippingAccountDto](#createbusinessshippingaccountdto)
- [CreateCorporateAccountDto](#createcorporateaccountdto)
- [CreateDelegatedRideDto](#createdelegatedridedto)
- [CreateDeliveryQuoteDto](#createdeliveryquotedto)
- [CreateDeliveryRequestDto](#createdeliveryrequestdto)
- [CreateDependentTravelDto](#createdependenttraveldto)
- [CreateGeneratedExportRequest](#creategeneratedexportrequest)
- [CreateHouseholdAccountDto](#createhouseholdaccountdto)
- [CreateMaintenanceScheduleDto](#createmaintenancescheduledto)
- [CreateParcelProtectionClaimDto](#createparcelprotectionclaimdto)
- [CreatePayoutMethodDto](#createpayoutmethoddto)
- [CreateRecentAuthenticationProofRequest](#createrecentauthenticationproofrequest)
- [CreateRentalAvailabilityBlockDto](#createrentalavailabilityblockdto)
- [CreateRentalBookingDto](#createrentalbookingdto)
- [CreateRentalBranchDto](#createrentalbranchdto)
- [CreateRentalCheckoutDto](#createrentalcheckoutdto)
- [CreateRentalDamageClaimDto](#createrentaldamageclaimdto)
- [CreateRentalInspectionDto](#createrentalinspectiondto)
- [CreateRentalOrganizationDto](#createrentalorganizationdto)
- [CreateRentalRatingDto](#createrentalratingdto)
- [CreateRentalVehicleDto](#createrentalvehicledto)
- [CreateReviewAppealDto](#createreviewappealdto)
- [CreateRideRequestDto](#createriderequestdto)
- [CreateSafetyCaseRequest](#createsafetycaserequest)
- [CreateSafetyEventRequest](#createsafetyeventrequest)
- [CreateScheduledReportCommand](#createscheduledreportcommand)
- [CreateStorePurchaseQuoteDto](#createstorepurchasequotedto)
- [CreateSupportTicketDto](#createsupportticketdto)
- [CreateTravelProfileDto](#createtravelprofiledto)
- [CreateTripTipDto](#createtriptipdto)
- [CreateTwoFactorStepUpDto](#createtwofactorstepupdto)

## CalculatorPdfRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `calculatorType` | `string` | Yes | Not declared nullable | Calculator type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `inputs` | [CalculatorPdfRowDto](c.md#calculatorpdfrowdto)[] | Yes | Not declared nullable | Collection of inputs for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `results` | [CalculatorPdfRowDto](c.md#calculatorpdfrowdto)[] | Yes | Not declared nullable | Collection of results for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `amortization` | [AmortizationPdfRowDto](a.md#amortizationpdfrowdto)[] | No | Explicitly allowed | Collection of amortization for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `disclaimer` | `string` | No | Explicitly allowed | Disclaimer text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CalculatorPdfRowDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `label` | `string` | Yes | Not declared nullable | Label text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `value` | `string` | Yes | Not declared nullable | Value text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CampaignChannel

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `4`, `8`, `16`, `32`, `64`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | None | None state/choice in this specific enum. |
| `1` | Email | Email state/choice in this specific enum. |
| `2` | Sms | Sms state/choice in this specific enum. |
| `4` | Push | Push state/choice in this specific enum. |
| `8` | WhatsApp | Whatsapp state/choice in this specific enum. |
| `16` | InAppInbox | In app inbox state/choice in this specific enum. |
| `32` | InAppBanner | In app banner state/choice in this specific enum. |
| `64` | MandatoryOperationalNotice | Mandatory operational notice state/choice in this specific enum. |

## CampaignInboxItemDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |
| `channel` | [CampaignChannel](c.md#campaignchannel) | Yes | Not declared nullable | Channel represented by the `CampaignChannel` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `language` | `string` | Yes | Not declared nullable | Language selector/content language; use the endpoint's supported values and fallback rules. | Shared convention | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `body` | `string` | Yes | Not declared nullable | Message/content body in this model; privacy and rendering rules depend on the operation. | Shared convention | No further constraint recorded |
| `deepLink` | `string` | No | Explicitly allowed | Deep link text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `visibleFromUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for visible from; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `readAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for read at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `acknowledgedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for acknowledged at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CancelPendingMembershipChangeRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `changeId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related change record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CancelRentalBookingDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `reasonCode` | [RentalCancellationReason](r.md#rentalcancellationreason) | Yes | Not declared nullable | Stable reason code; map through the applicable reason catalog instead of displaying an unrelated enum. | Shared convention | No further constraint recorded |
| `reasonDetail` | `string` | No | Explicitly allowed | Reason detail text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `expectedVersion` | `integer (int32)` | Yes | Not declared nullable | Expected version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CancelRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `reason` | `string` | No | Explicitly allowed | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CashoutDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `status` | [CashoutStatus](c.md#cashoutstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `reviewedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for reviewed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `reviewNote` | `string` | No | Explicitly allowed | Human-readable reviewer explanation, including remediation where applicable. | Shared convention | No further constraint recorded |
| `payoutMethod` | `string` | No | Explicitly allowed | Payout method text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `payoutStatus` | [PayoutTransferStatus](p.md#payouttransferstatus) | No | Not declared nullable | Payout status represented by the `PayoutTransferStatus` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `processingLabel` | `string` | No | Explicitly allowed | Processing label text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `estimatedArrivalMinutesMin` | `integer (int32)` | No | Not declared nullable | Numeric estimated arrival minutes min for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `estimatedArrivalMinutesMax` | `integer (int32)` | No | Not declared nullable | Numeric estimated arrival minutes max for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `kiloDriveFeeMinor` | `integer (int64)` | No | Not declared nullable | Kilo drive fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `providerFeeMinor` | `integer (int64)` | No | Explicitly allowed | Provider fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `externalFeesMayApply` | `boolean` | No | Not declared nullable | Whether external fees may apply applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CashoutLimitsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `minAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Min amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `maxAmountMinor` | `integer (int64)` | No | Explicitly allowed | Max amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `balanceMinor` | `integer (int64)` | Yes | Not declared nullable | Wallet balance in integer minor units; use the full wallet breakdown to interpret spendable funds. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `planName` | `string` | No | Explicitly allowed | Human plan name; use plan/entitlement records for identity and authority. | Shared convention | No further constraint recorded |
| `dailyLimitMinor` | `integer (int64)` | No | Explicitly allowed | Daily limit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `weeklyLimitMinor` | `integer (int64)` | No | Explicitly allowed | Weekly limit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `processingLabel` | `string` | No | Explicitly allowed | Processing label text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `estimatedArrivalMinutesMin` | `integer (int32)` | No | Not declared nullable | Numeric estimated arrival minutes min for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `estimatedArrivalMinutesMax` | `integer (int32)` | No | Not declared nullable | Numeric estimated arrival minutes max for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `kiloDriveFeeMinor` | `integer (int64)` | No | Not declared nullable | Kilo drive fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `externalFeesMayApply` | `boolean` | No | Not declared nullable | Whether external fees may apply applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `feeBasisPoints` | `integer (int32)` | No | Not declared nullable | Numeric fee basis points for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CashoutReconciliationState

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Settled | Settled state/choice in this specific enum. |
| `3` | CheckingOutcome | Checking outcome state/choice in this specific enum. |
| `4` | NeedsReview | Needs review state/choice in this specific enum. |

## CashoutSettlementState

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`, `4`, `5`, `6`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Unknown | Unknown state/choice in this specific enum. |
| `1` | Queued | Queued state/choice in this specific enum. |
| `2` | Submitted | Submitted state/choice in this specific enum. |
| `3` | Paid | Paid state/choice in this specific enum. |
| `4` | Failed | Failed state/choice in this specific enum. |
| `5` | Returned | Returned state/choice in this specific enum. |
| `6` | Reversed | Reversed state/choice in this specific enum. |

## CashoutStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Approved | Approved state/choice in this specific enum. |
| `3` | Rejected | Rejected state/choice in this specific enum. |
| `4` | Completed | Completed state/choice in this specific enum. |
| `5` | Returned | Returned state/choice in this specific enum. |
| `6` | Reversed | Reversed state/choice in this specific enum. |

## CashoutStatusHistoryEntryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `state` | [CashoutSettlementState](c.md#cashoutsettlementstate) | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `occurredAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for occurred at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `statusCode` | `string` | Yes | Not declared nullable | Status code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CashoutStatusResourceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `cashoutId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related cashout record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `state` | [CashoutSettlementState](c.md#cashoutsettlementstate) | Yes | Not declared nullable | State in this model's workflow; do not map it with another domain's status registry. | Shared convention | No further constraint recorded |
| `reconciliationState` | [CashoutReconciliationState](c.md#cashoutreconciliationstate) | Yes | Not declared nullable | Reconciliation state represented by the `CashoutReconciliationState` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `statusCode` | `string` | Yes | Not declared nullable | Status code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `providerCode` | `string` | No | Explicitly allowed | Provider code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `providerTraceReference` | `string` | No | Explicitly allowed | Provider trace reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `failureCode` | `string` | No | Explicitly allowed | Failure code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `remediationCode` | `string` | Yes | Not declared nullable | Remediation code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `safeNextAction` | `string` | Yes | Not declared nullable | Safe next action text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `observedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for observed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `isStale` | `boolean` | Yes | Not declared nullable | Whether is stale applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `nextRefreshAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for next refresh at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `blocksDuplicateSubmission` | `boolean` | Yes | Not declared nullable | Whether blocks duplicate submission applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `history` | [CashoutStatusHistoryEntryDto](c.md#cashoutstatushistoryentrydto)[] | Yes | Not declared nullable | Collection of history for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ChatMessageCommitOutcome

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | NotApplicable | Not applicable state/choice in this specific enum. |
| `1` | CommittedPendingFanout | Committed pending fanout state/choice in this specific enum. |
| `2` | AlreadyCommittedPendingFanout | Already committed pending fanout state/choice in this specific enum. |

## ChatMessageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `senderId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related sender record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `senderName` | `string` | Yes | Not declared nullable | Sender name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `body` | `string` | Yes | Not declared nullable | Message/content body in this model; privacy and rendering rules depend on the operation. | Shared convention | No further constraint recorded |
| `readAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for read at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `lifecycleVersion` | `integer (int64)` | Yes | Not declared nullable | Lifecycle version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `clientMessageId` | `string` | No | Explicitly allowed | Stable client message identity used for deduplication or reconciliation after a lost chat response. | Shared convention | No further constraint recorded |
| `commitOutcome` | [ChatMessageCommitOutcome](c.md#chatmessagecommitoutcome) | No | Not declared nullable | Commit outcome represented by the `ChatMessageCommitOutcome` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `messageSequence` | `integer (int64)` | No | Not declared nullable | Numeric message sequence for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CloseSupportCaseDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `reason` | `string` | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CompleteDriverOnboardingDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `privacyAccepted` | `boolean` | No | Not declared nullable | Whether privacy accepted applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `termsAccepted` | `boolean` | No | Not declared nullable | Whether terms accepted applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CompleteProfileDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `firstName` | `string` | Yes | Not declared nullable | Person's given name as provided through the applicable profile/identity workflow. | Shared convention | No further constraint recorded |
| `lastName` | `string` | Yes | Not declared nullable | Person's family name as provided through the applicable profile/identity workflow. | Shared convention | No further constraint recorded |
| `email` | `string` | No | Explicitly allowed | Email address for this model's person/destination; its presence does not prove verification. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CompleteTripRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `actualDistanceMeters` | `integer (int32)` | No | Explicitly allowed | Actual distance, measured in metres. | Naming convention | No further constraint recorded |
| `actualDurationSeconds` | `integer (int32)` | No | Explicitly allowed | Actual duration, measured in seconds. | Naming convention | No further constraint recorded |
| `completionExceptionReasonCode` | `string` | No | Explicitly allowed | Completion exception reason code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `completionExceptionNote` | `string` | No | Explicitly allowed | Completion exception note text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CompleteVehicleServiceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `scheduleId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related schedule record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `categoryCode` | `string` | Yes | Not declared nullable | Category code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `completedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for completed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `completedOdometer` | `number (double)` | No | Explicitly allowed | Numeric completed odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `workshop` | `string` | No | Explicitly allowed | Workshop text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `workPerformed` | `string` | Yes | Not declared nullable | Work performed text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `partsJson` | `string` | No | Explicitly allowed | Parts json text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `labourCostMinor` | `integer (int64)` | Yes | Not declared nullable | Labour cost in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `partsCostMinor` | `integer (int64)` | Yes | Not declared nullable | Parts cost in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `taxMinor` | `integer (int64)` | Yes | Not declared nullable | Tax in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `discountMinor` | `integer (int64)` | Yes | Not declared nullable | Discount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `totalMinor` | `integer (int64)` | Yes | Not declared nullable | Total in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `warrantyNotes` | `string` | No | Explicitly allowed | Warranty notes text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `notes` | `string` | No | Explicitly allowed | Human notes for this record; keep them within the authorized data scope. | Shared convention | No further constraint recorded |
| `receiptFileRef` | `string` | No | Explicitly allowed | Receipt file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `evidenceFileRefsJson` | `string` | No | Explicitly allowed | Evidence file refs json text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `nextRecommendedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for next recommended at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `nextRecommendedOdometer` | `number (double)` | No | Explicitly allowed | Numeric next recommended odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `clientOperationId` | `string` | Yes | Not declared nullable | Client's stable identity for this logical operation; preserve it through interrupted responses. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ConfigureFareSplitDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `shares` | [FareSplitShareInputDto](f.md#faresplitshareinputdto)[] | Yes | Not declared nullable | Collection of shares for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ConfirmContactTwoFactorEnrollmentRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `method` | `string` | Yes | Not declared nullable | Method text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ConfirmDeliveryVerificationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `challengeId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related challenge record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `code` | `string` | No | Explicitly allowed | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `qrPayload` | `string` | No | Explicitly allowed | Qr payload text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `evidence` | [DeliveryEvidenceInputDto](d.md#deliveryevidenceinputdto) | No | Not declared nullable | Evidence represented by the `DeliveryEvidenceInputDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `recipientName` | `string` | No | Explicitly allowed | Recipient name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `signatureFileRef` | `string` | No | Explicitly allowed | Signature file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | No | Explicitly allowed | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ConfirmDriverOnboardingStepDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `stepCode` | `string` | Yes | Not declared nullable | Step code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `defer` | `boolean` | No | Not declared nullable | Whether defer applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `applicationVersion` | `string` | No | Explicitly allowed | Application version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ConfirmEmailLoginDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `email` | `string` | Yes | Not declared nullable | Email address for this model's person/destination; its presence does not prove verification. | Shared convention | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ConfirmEmailVerificationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ConfirmPasswordResetRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `identifier` | `string` | Yes | Not declared nullable | Sign-in identifier accepted by this identity contract; validation and privacy rules still apply. | Shared convention | No further constraint recorded |
| `lastName` | `string` | Yes | Not declared nullable | Person's family name as provided through the applicable profile/identity workflow. | Shared convention | No further constraint recorded |
| `ownershipConfirmed` | `boolean` | Yes | Not declared nullable | Whether ownership confirmed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `newPassword` | `string` | Yes | Not declared nullable | Private new password used by this specific ceremony; never log, publish or substitute it for another proof. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ConfirmPendingSocialLinkRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `intentToken` | `string` | Yes | Not declared nullable | Private intent token used by this specific ceremony; never log, publish or substitute it for another proof. | Naming convention | No further constraint recorded |
| `provider` | `string` | Yes | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ConfirmPhoneContactVerificationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ConfirmPhoneLoginDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `phoneNumber` | `string` | Yes | Not declared nullable | Country-aware contact number; its presence does not prove verification or provider provisioning. | Shared convention | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ConfirmPhoneVerificationRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ConfirmSupervisedHandoffDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `handoff` | `string` | Yes | Not declared nullable | Handoff text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | Yes | Not declared nullable | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ContactDetailsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `email` | `string` | No | Explicitly allowed | Email address for this model's person/destination; its presence does not prove verification. | Shared convention | No further constraint recorded |
| `phoneNumber` | `string` | No | Explicitly allowed | Country-aware contact number; its presence does not prove verification or provider provisioning. | Shared convention | No further constraint recorded |
| `emailVerified` | `boolean` | Yes | Not declared nullable | Whether email verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `phoneVerified` | `boolean` | Yes | Not declared nullable | Whether phone verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ContactTwoFactorEnrollmentDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `method` | `string` | Yes | Not declared nullable | Method text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `maskedDestination` | `string` | Yes | Not declared nullable | Privacy-reduced contact display for the ceremony; not the raw credential or full destination. | Shared convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ContactVerificationChallengeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `issuedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for issued at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `serverTimeUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for server time; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ContentPageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `slug` | `string` | Yes | Not declared nullable | Slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `language` | `string` | Yes | Not declared nullable | Language selector/content language; use the endpoint's supported values and fallback rules. | Shared convention | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `summary` | `string` | Yes | Not declared nullable | Summary text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `bodyHtml` | `string` | Yes | Not declared nullable | Body html text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isPublished` | `boolean` | Yes | Not declared nullable | Whether is published applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `sortOrder` | `integer (int32)` | Yes | Not declared nullable | Numeric sort order for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `legalVersion` | `string` | No | Explicitly allowed | Legal version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `legalEffectiveAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for legal effective at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `legalChangeSummary` | `string` | No | Explicitly allowed | Legal change summary text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isVersionControlled` | `boolean` | No | Not declared nullable | Whether is version controlled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CorporateAccountDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `legalName` | `string` | Yes | Not declared nullable | Legal name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `status` | [CorporateAccountStatus](c.md#corporateaccountstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `availableCreditMinor` | `integer (int64)` | Yes | Not declared nullable | Available credit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `heldCreditMinor` | `integer (int64)` | Yes | Not declared nullable | Held credit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `version` | `integer (int64)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CorporateAccountStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Active | Active state/choice in this specific enum. |
| `3` | Suspended | Suspended state/choice in this specific enum. |
| `4` | Closed | Closed state/choice in this specific enum. |

## CorporateBudgetDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `corporateAccountId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related corporate account record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `costCenterCode` | `string` | Yes | Not declared nullable | Cost center code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `periodStartsAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for period starts at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `periodEndsAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for period ends at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `limitMinor` | `integer (int64)` | Yes | Not declared nullable | Limit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `spentMinor` | `integer (int64)` | Yes | Not declared nullable | Spent in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `heldMinor` | `integer (int64)` | Yes | Not declared nullable | Held in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `version` | `integer (int64)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CorporateMemberPermission

**Wire type:** `integer (int64)`. Allowed wire values: `0`, `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `255`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | None | None state/choice in this specific enum. |
| `1` | ManageMembers | Manage members state/choice in this specific enum. |
| `2` | ManagePolicy | Manage policy state/choice in this specific enum. |
| `4` | ManageBudgets | Manage budgets state/choice in this specific enum. |
| `8` | BookTravel | Book travel state/choice in this specific enum. |
| `16` | ApproveTravel | Approve travel state/choice in this specific enum. |
| `32` | ViewFinance | View finance state/choice in this specific enum. |
| `64` | ManageBilling | Manage billing state/choice in this specific enum. |
| `128` | ViewAudit | View audit state/choice in this specific enum. |
| `255` | All | All state/choice in this specific enum. |

## CorporateMemberRole

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`, `6`, `7`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Owner | Owner state/choice in this specific enum. |
| `2` | Administrator | Administrator state/choice in this specific enum. |
| `3` | Approver | Approver state/choice in this specific enum. |
| `4` | Booker | Booker state/choice in this specific enum. |
| `5` | Traveler | Traveler state/choice in this specific enum. |
| `6` | Finance | Finance state/choice in this specific enum. |
| `7` | Auditor | Auditor state/choice in this specific enum. |

## CountryReferenceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `currencyCode` | `string` | Yes | Not declared nullable | ISO currency code; do not infer it from a dollar symbol. | Shared convention | No further constraint recorded |
| `currencySymbol` | `string` | Yes | Not declared nullable | Currency symbol text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `timezone` | `string` | Yes | Not declared nullable | Timezone context used by this contract; apply documented IANA/display semantics. | Shared convention | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | Shared convention | No further constraint recorded |
| `sortOrder` | `integer (int32)` | Yes | Not declared nullable | Numeric sort order for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `driverLicensePattern` | `string` | No | Explicitly allowed | Driver license pattern text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `vehiclePlatePattern` | `string` | No | Explicitly allowed | Vehicle plate pattern text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `driverLicenseMinLength` | `integer (int32)` | No | Not declared nullable | Numeric driver license min length for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `driverLicenseMaxLength` | `integer (int32)` | No | Not declared nullable | Numeric driver license max length for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `vehiclePlateMinLength` | `integer (int32)` | No | Not declared nullable | Numeric vehicle plate min length for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `vehiclePlateMaxLength` | `integer (int32)` | No | Not declared nullable | Numeric vehicle plate max length for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `riderIdentityVerificationRequired` | `boolean` | No | Not declared nullable | Whether rider identity verification required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `launchReady` | `boolean` | No | Not declared nullable | Whether launch ready applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `launchIssues` | `string[]` | No | Explicitly allowed | Collection of launch issues for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CourierProductSettingsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `otpExpiryMinutes` | `integer (int32)` | Yes | Not declared nullable | Otp expiry, measured in minutes. | Naming convention | No further constraint recorded |
| `otpMaximumAttempts` | `integer (int32)` | Yes | Not declared nullable | Numeric otp maximum attempts for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `maximumFailedAttempts` | `integer (int32)` | Yes | Not declared nullable | Numeric maximum failed attempts for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `parcelProtectionAvailable` | `boolean` | Yes | Not declared nullable | Whether parcel protection available applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `parcelProtectionRateBasisPoints` | `integer (int32)` | Yes | Not declared nullable | Numeric parcel protection rate basis points for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `parcelProtectionMaximumCoverageMinor` | `integer (int64)` | Yes | Not declared nullable | Parcel protection maximum coverage in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `parcelProtectionTermsVersion` | `string` | No | Explicitly allowed | Parcel protection terms version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `parcelProtectionTermsUrl` | `string` | No | Explicitly allowed | URL for parcel protection terms; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `parcelProtectionClaimWindowDays` | `integer (int32)` | No | Not declared nullable | Parcel protection claim window, measured in days under this workflow's calendar rules. | Naming convention | No further constraint recorded |
| `deliveryWindowEarlyToleranceMinutes` | `integer (int32)` | No | Not declared nullable | Delivery window early tolerance, measured in minutes. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateBusinessShippingAccountDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `billingEmail` | `string` | Yes | Not declared nullable | Billing email text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `requireDeliveryOtp` | `boolean` | No | Not declared nullable | Whether require delivery otp applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requireProofPhoto` | `boolean` | No | Not declared nullable | Whether require proof photo applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requireSignature` | `boolean` | No | Not declared nullable | Whether require signature applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateCorporateAccountDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `legalName` | `string` | Yes | Not declared nullable | Legal name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateDelegatedRideDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `memberId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related member record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `costCenterId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related cost center record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `ride` | [CreateRideRequestDto](c.md#createriderequestdto) | Yes | Not declared nullable | Ride represented by the `CreateRideRequestDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateDeliveryQuoteDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `vehicleCategoryId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related vehicle category record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `stops` | [DeliveryStopInputDto](d.md#deliverystopinputdto)[] | Yes | Not declared nullable | Ordered journey/delivery stops in the referenced stop model. | Shared convention | No further constraint recorded |
| `parcels` | [ParcelInputDto](p.md#parcelinputdto)[] | Yes | Not declared nullable | Collection of parcels for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `requestProtection` | `boolean` | No | Not declared nullable | Whether request protection applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `protectionTermsVersion` | `string` | No | Explicitly allowed | Protection terms version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `businessShippingAccountId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related business shipping account record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `pickupWindowStart` | `string (date-time)` | No | Explicitly allowed | Pickup window start text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `pickupWindowEnd` | `string (date-time)` | No | Explicitly allowed | Pickup window end text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `deliveryWindowStart` | `string (date-time)` | No | Explicitly allowed | Delivery window start text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `deliveryWindowEnd` | `string (date-time)` | No | Explicitly allowed | Delivery window end text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateDeliveryRequestDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `vehicleCategoryId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related vehicle category record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `proposedPriceMinor` | `integer (int64)` | Yes | Not declared nullable | Proposed price in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | Shared convention | No further constraint recorded |
| `stops` | [DeliveryStopInputDto](d.md#deliverystopinputdto)[] | Yes | Not declared nullable | Ordered journey/delivery stops in the referenced stop model. | Shared convention | No further constraint recorded |
| `parcels` | [ParcelInputDto](p.md#parcelinputdto)[] | Yes | Not declared nullable | Collection of parcels for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `pickupWindowStart` | `string (date-time)` | No | Explicitly allowed | Pickup window start text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `pickupWindowEnd` | `string (date-time)` | No | Explicitly allowed | Pickup window end text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `deliveryWindowStart` | `string (date-time)` | No | Explicitly allowed | Delivery window start text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `deliveryWindowEnd` | `string (date-time)` | No | Explicitly allowed | Delivery window end text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `pickupVerificationRequired` | `boolean` | No | Not declared nullable | Whether pickup verification required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `recipientVerificationRequired` | `boolean` | No | Not declared nullable | Whether recipient verification required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `proofPhotoRequired` | `boolean` | No | Not declared nullable | Whether proof photo required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requestProtection` | `boolean` | No | Not declared nullable | Whether request protection applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `protectionTermsVersion` | `string` | No | Explicitly allowed | Protection terms version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `businessShippingAccountId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related business shipping account record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `externalReference` | `string` | No | Explicitly allowed | External reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `signatureRequired` | `boolean` | No | Not declared nullable | Whether signature required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `returnPolicy` | [DeliveryReturnPolicy](d.md#deliveryreturnpolicy) | No | Not declared nullable | Return policy represented by the `DeliveryReturnPolicy` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `maximumFailedAttempts` | `integer (int32)` | No | Explicitly allowed | Numeric maximum failed attempts for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `returnVerificationRequired` | `boolean` | No | Not declared nullable | Whether return verification required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `returnEvidenceRequired` | `boolean` | No | Not declared nullable | Whether return evidence required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `quoteId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related quote record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `quoteRevision` | `integer (int64)` | No | Explicitly allowed | Quote revision for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `quoteFingerprint` | `string` | No | Explicitly allowed | Quote fingerprint text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateDependentTravelDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | Shared convention | No further constraint recorded |
| `email` | `string` | No | Explicitly allowed | Email address for this model's person/destination; its presence does not prove verification. | Shared convention | No further constraint recorded |
| `phoneNumber` | `string` | No | Explicitly allowed | Country-aware contact number; its presence does not prove verification or provider provisioning. | Shared convention | No further constraint recorded |
| `dateOfBirth` | `string (date)` | Yes | Not declared nullable | Calendar date for date of birth; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `relationship` | `string` | Yes | Not declared nullable | Relationship text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `consentPolicyVersion` | `string` | Yes | Not declared nullable | Consent policy version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `consentEvidenceReference` | `string` | Yes | Not declared nullable | Consent evidence reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `guardianAuthorityConfirmed` | `boolean` | Yes | Not declared nullable | Whether guardian authority confirmed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `allowCash` | `boolean` | No | Not declared nullable | Whether allow cash applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `allowedWeekdaysMask` | `integer (int32)` | No | Not declared nullable | Numeric allowed weekdays mask for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `earliestMinuteLocal` | `integer (int32)` | No | Not declared nullable | Numeric earliest minute local for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `latestMinuteLocal` | `integer (int32)` | No | Not declared nullable | Numeric latest minute local for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `minimumDriverTrustLevel` | `integer (int32)` | No | Not declared nullable | Numeric minimum driver trust level for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `requirePickupGuardianConfirmation` | `boolean` | No | Not declared nullable | Whether require pickup guardian confirmation applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requireDropoffGuardianConfirmation` | `boolean` | No | Not declared nullable | Whether require dropoff guardian confirmation applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `guardianAuthorityType` | `string` | No | Explicitly allowed | Guardian authority type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `liveTrackingConsentGranted` | `boolean` | No | Not declared nullable | Whether live tracking consent granted applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `threeWayCommunicationConsentGranted` | `boolean` | No | Not declared nullable | Whether three way communication consent granted applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `emergencyContactConfirmed` | `boolean` | No | Not declared nullable | Whether emergency contact confirmed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateGeneratedExportRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `reportType` | `string` | Yes | Not declared nullable | Report type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `format` | `string` | No | Explicitly allowed | Output/file format selector; use the operation's supported media rather than guessing an extension. | Shared convention | No further constraint recorded |
| `preset` | `string` | No | Explicitly allowed | Named range/filter preset accepted by this endpoint; explicit date bounds have separate semantics. | Shared convention | No further constraint recorded |
| `fromUtc` | `string (date-time)` | No | Explicitly allowed | UTC start of the requested range; apply this endpoint's inclusion/validation rules. | Shared convention | No further constraint recorded |
| `toUtc` | `string (date-time)` | No | Explicitly allowed | UTC end of the requested range; apply this endpoint's inclusion/validation rules. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateHouseholdAccountDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateMaintenanceScheduleDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `categoryCode` | `string` | Yes | Not declared nullable | Category code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `description` | `string` | No | Explicitly allowed | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `trigger` | [VehicleMaintenanceTrigger](v.md#vehiclemaintenancetrigger) | Yes | Not declared nullable | Trigger represented by the `VehicleMaintenanceTrigger` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `severity` | [VehicleMaintenanceSeverity](v.md#vehiclemaintenanceseverity) | Yes | Not declared nullable | Severity represented by the `VehicleMaintenanceSeverity` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `nextDueAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for next due at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `nextDueOdometer` | `number (double)` | No | Explicitly allowed | Numeric next due odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `recurrenceDays` | `integer (int32)` | No | Explicitly allowed | Recurrence, measured in days under this workflow's calendar rules. | Naming convention | No further constraint recorded |
| `recurrenceDistance` | `number (double)` | No | Explicitly allowed | Numeric recurrence distance for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `dueSoonDays` | `integer (int32)` | Yes | Not declared nullable | Due soon, measured in days under this workflow's calendar rules. | Naming convention | No further constraint recorded |
| `dueSoonDistance` | `number (double)` | Yes | Not declared nullable | Numeric due soon distance for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `remindersEnabled` | `boolean` | Yes | Not declared nullable | Whether reminders enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `clientOperationId` | `string` | Yes | Not declared nullable | Client's stable identity for this logical operation; preserve it through interrupted responses. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateParcelProtectionClaimDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `reason` | [ParcelProtectionClaimReason](p.md#parcelprotectionclaimreason) | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |
| `description` | `string` | Yes | Not declared nullable | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `claimedAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Claimed amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `evidence` | [DeliveryEvidenceInputDto](d.md#deliveryevidenceinputdto)[] | Yes | Not declared nullable | Collection of evidence for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreatePayoutMethodDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `type` | [PayoutMethodType](p.md#payoutmethodtype) | Yes | Not declared nullable | Type represented by the `PayoutMethodType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `bankName` | `string` | No | Explicitly allowed | Bank name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `accountNumber` | `string` | No | Explicitly allowed | Account number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `email` | `string` | No | Explicitly allowed | Email address for this model's person/destination; its presence does not prove verification. | Shared convention | No further constraint recorded |
| `bankBranchId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related bank branch record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `accountType` | `string` | No | Explicitly allowed | Account type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `currencyCode` | `string` | No | Explicitly allowed | ISO currency code; do not infer it from a dollar symbol. | Shared convention | No further constraint recorded |
| `confirmedDetails` | `boolean` | No | Not declared nullable | Whether confirmed details applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateRecentAuthenticationProofRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `password` | `string` | No | Not declared nullable | Secret password input for the established secure identity ceremony; never echo or log it. | Shared convention | minLength: `1`; maxLength: `1024`; pattern: `\S` |
| `provider` | `string` | No | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | Shared convention | minLength: `1`; maxLength: `8`; pattern: `\S`; Allowed wire values: `google`, `facebook`, `apple` |
| `idToken` | `string` | No | Not declared nullable | Private id token used by this specific ceremony; never log, publish or substitute it for another proof. | Naming convention | minLength: `1`; maxLength: `16384`; pattern: `\S` |
| `accessToken` | `string` | No | Not declared nullable | Sensitive bearer access credential for the issued session. | Shared convention | minLength: `1`; maxLength: `16384`; pattern: `\S` |
| `nonce` | `string` | No | Not declared nullable | Nonce text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | minLength: `1`; maxLength: `512`; pattern: `\S` |

**Composition (oneOf):** .

**Additional object properties:** not allowed by the schema.

## CreateRentalAvailabilityBlockDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `vehicleId` | `string (uuid)` | Yes | Not declared nullable | Account vehicle record associated with this operation or result. | Shared convention | No further constraint recorded |
| `type` | [RentalAvailabilityBlockType](r.md#rentalavailabilityblocktype) | Yes | Not declared nullable | Type represented by the `RentalAvailabilityBlockType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `startsAt` | `string (date-time)` | Yes | Not declared nullable | Starts at text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `endsAt` | `string (date-time)` | Yes | Not declared nullable | Ends at text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `reason` | `string` | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateRentalBookingDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `vehicleId` | `string (uuid)` | Yes | Not declared nullable | Account vehicle record associated with this operation or result. | Shared convention | No further constraint recorded |
| `pickupAt` | `string (date-time)` | Yes | Not declared nullable | Pickup at text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `returnAt` | `string (date-time)` | Yes | Not declared nullable | Return at text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `handoverMode` | [RentalVehicleHandoverMode](r.md#rentalvehiclehandovermode) | Yes | Not declared nullable | Handover mode represented by the `RentalVehicleHandoverMode` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `acceptedPolicyVersion` | `integer (int32)` | Yes | Not declared nullable | Accepted policy version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `policyConfirmed` | `boolean` | Yes | Not declared nullable | Whether policy confirmed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `pickupAddress` | `string` | No | Explicitly allowed | Human pickup-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `returnAddress` | `string` | No | Explicitly allowed | Return address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `protectionAcceptance` | [RentalProtectionAcceptanceDto](r.md#rentalprotectionacceptancedto) | No | Not declared nullable | Protection acceptance represented by the `RentalProtectionAcceptanceDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateRentalBranchDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `address` | `string` | Yes | Not declared nullable | Address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `latitude` | `number (double)` | Yes | Not declared nullable | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | Yes | Not declared nullable | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `timezone` | `string` | Yes | Not declared nullable | Timezone context used by this contract; apply documented IANA/display semantics. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateRentalCheckoutDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `provider` | `string` | No | Explicitly allowed | Configured provider selector for this operation; a named provider is not proof of readiness. | Shared convention | No further constraint recorded |
| `expectedBookingVersion` | `integer (int32)` | No | Not declared nullable | Expected booking version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateRentalDamageClaimDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `reason` | [RentalDamageReason](r.md#rentaldamagereason) | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | Shared convention | No further constraint recorded |
| `description` | `string` | Yes | Not declared nullable | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `claimedAmountMinor` | `integer (int64)` | Yes | Not declared nullable | Claimed amount in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `evidence` | [RentalEvidenceInput](r.md#rentalevidenceinput)[] | Yes | Not declared nullable | Collection of evidence for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `expectedBookingVersion` | `integer (int32)` | Yes | Not declared nullable | Expected booking version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateRentalInspectionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `phase` | [RentalInspectionPhase](r.md#rentalinspectionphase) | Yes | Not declared nullable | Phase represented by the `RentalInspectionPhase` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `odometerKilometers` | `integer (int32)` | Yes | Not declared nullable | Numeric odometer kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `fuelPercent` | `number (double)` | Yes | Not declared nullable | Numeric fuel percent for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `notes` | `string` | Yes | Not declared nullable | Human notes for this record; keep them within the authorized data scope. | Shared convention | No further constraint recorded |
| `photos` | [RentalInspectionPhotoInput](r.md#rentalinspectionphotoinput)[] | Yes | Not declared nullable | Collection of photos for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `checklist` | [RentalInspectionChecklistInput](r.md#rentalinspectionchecklistinput)[] | Yes | Not declared nullable | Requirement-by-requirement setup/readiness state. | Shared convention | No further constraint recorded |
| `expectedBookingVersion` | `integer (int32)` | Yes | Not declared nullable | Expected booking version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateRentalOrganizationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `providerType` | [RentalProviderType](r.md#rentalprovidertype) | Yes | Not declared nullable | Provider type represented by the `RentalProviderType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `legalName` | `string` | Yes | Not declared nullable | Legal name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `tradingName` | `string` | No | Explicitly allowed | Trading name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `slug` | `string` | Yes | Not declared nullable | Slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `timezone` | `string` | Yes | Not declared nullable | Timezone context used by this contract; apply documented IANA/display semantics. | Shared convention | No further constraint recorded |
| `registrationNumber` | `string` | No | Explicitly allowed | Registration number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `taxNumber` | `string` | No | Explicitly allowed | Tax number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `contactEmail` | `string` | Yes | Not declared nullable | Contact email text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `contactPhone` | `string` | Yes | Not declared nullable | Contact phone text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `description` | `string` | No | Explicitly allowed | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `websiteUrl` | `string` | No | Explicitly allowed | URL for website; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateRentalRatingDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `rating` | `integer (int32)` | Yes | Not declared nullable | Numeric rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `comment` | `string` | No | Explicitly allowed | Comment text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `vehicleRating` | `integer (int32)` | No | Explicitly allowed | Numeric vehicle rating for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `vehicleCondition` | `integer (int32)` | No | Explicitly allowed | Numeric vehicle condition for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `providerService` | `integer (int32)` | No | Explicitly allowed | Numeric provider service for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `communication` | `integer (int32)` | No | Explicitly allowed | Numeric communication for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `cleanliness` | `integer (int32)` | No | Explicitly allowed | Numeric cleanliness for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `valueForMoney` | `integer (int32)` | No | Explicitly allowed | Numeric value for money for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateRentalVehicleDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `branchId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related branch record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
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
| `extraKilometerRateMinor` | `integer (int64)` | Yes | Not declared nullable | Extra kilometer rate in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `handoverMode` | [RentalVehicleHandoverMode](r.md#rentalvehiclehandovermode) | Yes | Not declared nullable | Handover mode represented by the `RentalVehicleHandoverMode` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `pickupFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Pickup fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `deliveryFeeMinor` | `integer (int64)` | Yes | Not declared nullable | Delivery fee in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `serviceRadius` | `integer (int32)` | Yes | Not declared nullable | Numeric service radius for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `lateGraceMinutes` | `integer (int32)` | Yes | Not declared nullable | Late grace, measured in minutes. | Naming convention | No further constraint recorded |
| `lateFeePerHourMinor` | `integer (int64)` | Yes | Not declared nullable | Late fee per hour in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `registrationExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for registration expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `insuranceExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for insurance expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `fitnessExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for fitness expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `complianceReminderDays` | `integer (int32)` | Yes | Not declared nullable | Compliance reminder, measured in days under this workflow's calendar rules. | Naming convention | No further constraint recorded |
| `policyConfirmed` | `boolean` | Yes | Not declared nullable | Whether policy confirmed applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateReviewAppealDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `reasonCode` | `string` | Yes | Not declared nullable | Stable reason code; map through the applicable reason catalog instead of displaying an unrelated enum. | Shared convention | No further constraint recorded |
| `detail` | `string` | Yes | Not declared nullable | Detail text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateRideRequestDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `vehicleCategoryId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related vehicle category record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `pickupLatitude` | `number (double)` | Yes | Not declared nullable | Pickup latitude in degrees; latitude is separate from address text. | Shared convention | No further constraint recorded |
| `pickupLongitude` | `number (double)` | Yes | Not declared nullable | Pickup longitude in degrees; preserve coordinate order. | Shared convention | No further constraint recorded |
| `pickupAddress` | `string` | Yes | Not declared nullable | Human pickup-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `dropoffLatitude` | `number (double)` | Yes | Not declared nullable | Destination latitude in degrees. | Shared convention | No further constraint recorded |
| `dropoffLongitude` | `number (double)` | Yes | Not declared nullable | Destination longitude in degrees. | Shared convention | No further constraint recorded |
| `dropoffAddress` | `string` | Yes | Not declared nullable | Human destination-address text accompanying the structured location. | Shared convention | No further constraint recorded |
| `distanceMeters` | `integer (int32)` | No | Explicitly allowed | Distance represented by this model, in metres; its source/assessment depends on the operation. | Shared convention | No further constraint recorded |
| `estimatedDurationSeconds` | `integer (int32)` | No | Explicitly allowed | Estimated duration in seconds; an estimate is not actual elapsed trip time. | Shared convention | No further constraint recorded |
| `proposedFareMinor` | `integer (int64)` | Yes | Not declared nullable | Rider's proposed fare in currency minor units, subject to applicable quote and marketplace rules. | Shared convention | No further constraint recorded |
| `passengerCount` | `integer (int32)` | Yes | Not declared nullable | Number of passenger in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | Shared convention | No further constraint recorded |
| `scheduledForUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for scheduled for; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `pickupPlaceId` | `string` | No | Explicitly allowed | Identifier of the related pickup place record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `dropoffPlaceId` | `string` | No | Explicitly allowed | Identifier of the related dropoff place record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `paymentMethod` | [PaymentMethod](p.md#paymentmethod) | No | Not declared nullable | Payment method enum; availability and settlement rules are checked separately. | Shared convention | No further constraint recorded |
| `stops` | [RideStopInputDto](r.md#ridestopinputdto)[] | No | Explicitly allowed | Ordered journey/delivery stops in the referenced stop model. | Shared convention | No further constraint recorded |
| `petFriendlyRequired` | `boolean` | No | Not declared nullable | Whether pet friendly required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `childSeatRequired` | `boolean` | No | Not declared nullable | Whether child seat required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `childSeatCount` | `integer (int32)` | No | Not declared nullable | Number of child seat in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `wheelchairAccessibleRequired` | `boolean` | No | Not declared nullable | Whether wheelchair accessible required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `airportPickup` | `boolean` | No | Not declared nullable | Whether airport pickup applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `flightNumber` | `string` | No | Explicitly allowed | Flight number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `dispatchMode` | [RideDispatchMode](r.md#ridedispatchmode) | No | Not declared nullable | Dispatch mode represented by the `RideDispatchMode` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `autoAcceptExactFare` | `boolean` | No | Not declared nullable | Whether auto accept exact fare applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `productType` | [RideProductType](r.md#rideproducttype) | No | Not declared nullable | Product type represented by the `RideProductType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `bookedHourlyMinutes` | `integer (int32)` | No | Not declared nullable | Booked hourly, measured in minutes. | Naming convention | No further constraint recorded |
| `roundTripWaitSeconds` | `integer (int32)` | No | Not declared nullable | Round trip wait, measured in seconds. | Naming convention | No further constraint recorded |
| `useAssistanceProfile` | `boolean` | No | Not declared nullable | Whether use assistance profile applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `acknowledgeEstimatedRouteVariance` | `boolean` | No | Not declared nullable | Whether acknowledge estimated route variance applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateSafetyCaseRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `tripId` | `string (uuid)` | No | Explicitly allowed | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `severity` | [SafetyCaseSeverity](s.md#safetycaseseverity) | Yes | Not declared nullable | Severity represented by the `SafetyCaseSeverity` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `escalationChannel` | [SafetyEscalationChannel](s.md#safetyescalationchannel) | Yes | Not declared nullable | Escalation channel represented by the `SafetyEscalationChannel` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `evidenceBundleJson` | `string` | No | Explicitly allowed | Evidence bundle json text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateSafetyEventRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `type` | [SafetyEventType](s.md#safetyeventtype) | Yes | Not declared nullable | Type represented by the `SafetyEventType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `consentCaptured` | `boolean` | Yes | Not declared nullable | Whether consent captured applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `silentEscalation` | `boolean` | Yes | Not declared nullable | Whether silent escalation applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `latitude` | `number (double)` | No | Explicitly allowed | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | No | Explicitly allowed | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `deviationMeters` | `integer (int32)` | No | Explicitly allowed | Deviation, measured in metres. | Naming convention | No further constraint recorded |
| `stationarySeconds` | `integer (int32)` | No | Explicitly allowed | Stationary, measured in seconds. | Naming convention | No further constraint recorded |
| `voiceCallSessionId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related voice call session record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateScheduledReportCommand

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `reportType` | `string` | Yes | Not declared nullable | Report type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `cadence` | `string` | Yes | Not declared nullable | Cadence text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `format` | `string` | Yes | Not declared nullable | Output/file format selector; use the operation's supported media rather than guessing an extension. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateStorePurchaseQuoteDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `platform` | `string` | Yes | Not declared nullable | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | Shared convention | No further constraint recorded |
| `planId` | `string (uuid)` | Yes | Not declared nullable | Membership catalog record; it does not itself prove a user entitlement. | Shared convention | No further constraint recorded |
| `productId` | `string` | Yes | Not declared nullable | Identifier of the related product record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `termDays` | `integer (int32)` | Yes | Not declared nullable | Requested/applicable membership term in days; only configured valid terms are allowed. | Shared convention | No further constraint recorded |
| `googleBasePlanId` | `string` | No | Explicitly allowed | Identifier of the related google base plan record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `googleOfferId` | `string` | No | Explicitly allowed | Identifier of the related google offer record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `mappingVersion` | `string` | Yes | Not declared nullable | Mapping version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `localizedPrice` | `string` | Yes | Not declared nullable | Localized price text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `nativePriceMinor` | `integer (int64)` | Yes | Not declared nullable | Native price in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateSupportTicketDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `ticketType` | `string` | Yes | Not declared nullable | Ticket type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `subject` | `string` | Yes | Not declared nullable | Subject text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `body` | `string` | Yes | Not declared nullable | Message/content body in this model; privacy and rendering rules depend on the operation. | Shared convention | No further constraint recorded |
| `attachmentFileRefs` | `string[]` | No | Explicitly allowed | Collection of attachment file refs for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `subjectType` | `string` | No | Explicitly allowed | Subject type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `subjectEntityId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related subject entity record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `issueType` | `string` | No | Explicitly allowed | Issue type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `priority` | `string` | No | Explicitly allowed | Priority text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateTravelProfileDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `type` | `string` | Yes | Not declared nullable | Type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `centralBillingEnabled` | `boolean` | Yes | Not declared nullable | Whether central billing enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `monthlyBudgetMinor` | `integer (int64)` | No | Not declared nullable | Monthly budget in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateTripTipDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## CreateTwoFactorStepUpDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `action` | `string` | Yes | Not declared nullable | Action text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `channel` | `string` | No | Explicitly allowed | Channel text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
