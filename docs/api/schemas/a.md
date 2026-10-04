# Field dictionary: A

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

The explanation basis distinguishes model-specific meaning, shared conventions,
name-derived units and type-only entries awaiting semantic review. See the
[coverage report](../reference/coverage.md); field presence is not semantic completeness.

## Models on this page

- [AcceptBidDto](#acceptbiddto)
- [AcceptDeliveryBidAuthorizationDto](#acceptdeliverybidauthorizationdto)
- [AcceptLegalDocumentDto](#acceptlegaldocumentdto)
- [AcceptRentalTeamInvitationDto](#acceptrentalteaminvitationdto)
- [AcceptTravelInvitationDto](#accepttravelinvitationdto)
- [AccountSetupItemDto](#accountsetupitemdto)
- [AccountSetupProgressDto](#accountsetupprogressdto)
- [AddFavoriteDto](#addfavoritedto)
- [AddOdometerReadingDto](#addodometerreadingdto)
- [AddRentalVehicleImageDto](#addrentalvehicleimagedto)
- [AddTravelMemberDto](#addtravelmemberdto)
- [AddTravelMemberResultDto](#addtravelmemberresultdto)
- [AddVehicleBrakeDto](#addvehiclebrakedto)
- [AddVehicleExpenseDto](#addvehicleexpensedto)
- [AddVehicleTyreDto](#addvehicletyredto)
- [AddWalletRecipientDto](#addwalletrecipientdto)
- [AmortizationPdfRowDto](#amortizationpdfrowdto)
- [AppReleaseCorrectionNoticeDto](#appreleasecorrectionnoticedto)
- [AppReleaseDetailDto](#appreleasedetaildto)
- [AppReleaseImprovementDto](#appreleaseimprovementdto)
- [AppReleaseListDto](#appreleaselistdto)
- [AppReleaseSummaryDto](#appreleasesummarydto)
- [AppVersionPolicyDto](#appversionpolicydto)
- [AuthResponse](#authresponse)
- [AuthorizeRentalBookingPaymentDto](#authorizerentalbookingpaymentdto)

## AcceptBidDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `bidId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related bid record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `paymentMethod` | [PaymentMethod](p.md#paymentmethod) | No | Not declared nullable | Payment method enum; availability and settlement rules are checked separately. | Shared convention | No further constraint recorded |
| `promoCode` | `string` | No | Explicitly allowed | Promotion code supplied for server validation; it is not a guaranteed discount or credit. | Shared convention | No further constraint recorded |
| `expectedAuthorizationMinor` | `integer (int64)` | No | Explicitly allowed | Expected authorization in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `expectedAuthorizationFingerprint` | `string` | No | Explicitly allowed | Fingerprint of the authorization/quote the caller reviewed; used to detect a changed financial precondition. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AcceptDeliveryBidAuthorizationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `paymentMethod` | [PaymentMethod](p.md#paymentmethod) | Yes | Not declared nullable | Payment method enum; availability and settlement rules are checked separately. | Shared convention | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | Yes | Not declared nullable | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | Shared convention | No further constraint recorded |
| `expectedAuthorizationMinor` | `integer (int64)` | Yes | Not declared nullable | Expected authorization in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `expectedAuthorizationFingerprint` | `string` | Yes | Not declared nullable | Fingerprint of the authorization/quote the caller reviewed; used to detect a changed financial precondition. | Shared convention | No further constraint recorded |
| `promoCode` | `string` | No | Explicitly allowed | Promotion code supplied for server validation; it is not a guaranteed discount or credit. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AcceptLegalDocumentDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `documentKey` | `string` | No | Explicitly allowed | Stable key of the legal/document definition whose version is being accepted or read. | Shared convention | No further constraint recorded |
| `version` | `string` | No | Explicitly allowed | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `language` | `string` | No | Explicitly allowed | Language selector/content language; use the endpoint's supported values and fallback rules. | Shared convention | No further constraint recorded |
| `countryCode` | `string` | No | Explicitly allowed | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `role` | `string` | No | Explicitly allowed | Role text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `channel` | `string` | No | Explicitly allowed | Channel text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `applicationVersion` | `string` | No | Explicitly allowed | Application version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AcceptRentalTeamInvitationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `token` | `string` | Yes | Not declared nullable | Token for this specific contract, such as push registration; sensitive values must not be logged or reused in another ceremony. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AcceptTravelInvitationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `invitationCode` | `string` | Yes | Not declared nullable | Invitation code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AccountSetupItemDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `action` | `string` | Yes | Not declared nullable | Action text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `isComplete` | `boolean` | Yes | Not declared nullable | Whether is complete applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `isRequired` | `boolean` | No | Not declared nullable | Whether is required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AccountSetupProgressDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `role` | `string` | Yes | Not declared nullable | Role text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `completedSteps` | `integer (int32)` | Yes | Not declared nullable | Numeric completed steps for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `totalSteps` | `integer (int32)` | Yes | Not declared nullable | Numeric total steps for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `percentComplete` | `integer (int32)` | Yes | Not declared nullable | Numeric percent complete for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `steps` | [AccountSetupItemDto](a.md#accountsetupitemdto)[] | Yes | Not declared nullable | Collection of steps for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `riderOnboarding` | [RiderOnboardingDecisionDto](r.md#rideronboardingdecisiondto) | No | Not declared nullable | Rider onboarding represented by the `RiderOnboardingDecisionDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AddFavoriteDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `address` | `string` | Yes | Not declared nullable | Address text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `latitude` | `number (double)` | No | Explicitly allowed | Latitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `longitude` | `number (double)` | No | Explicitly allowed | Longitude in degrees for the location represented by this model. | Shared convention | No further constraint recorded |
| `placeId` | `string` | No | Explicitly allowed | Identifier of the related place record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AddOdometerReadingDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `reading` | `number (double)` | Yes | Not declared nullable | Numeric reading for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `unitCode` | `string` | Yes | Not declared nullable | Unit code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `observedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for observed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `sourceCode` | `string` | Yes | Not declared nullable | Source code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `notes` | `string` | No | Explicitly allowed | Human notes for this record; keep them within the authorized data scope. | Shared convention | No further constraint recorded |
| `dashboardImageFileRef` | `string` | No | Explicitly allowed | Dashboard image file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `clientOperationId` | `string` | Yes | Not declared nullable | Client's stable identity for this logical operation; preserve it through interrupted responses. | Shared convention | No further constraint recorded |
| `correctsReadingId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related corrects reading record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `correctionReason` | `string` | No | Explicitly allowed | Correction reason text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AddRentalVehicleImageDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `fileRef` | `string` | Yes | Not declared nullable | Private storage reference; not a permanent public URL or approval decision. | Shared convention | No further constraint recorded |
| `altText` | `string` | Yes | Not declared nullable | Alt text text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isPrimary` | `boolean` | Yes | Not declared nullable | Whether the vehicle is designated primary in this account context; work eligibility is assessed separately. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AddTravelMemberDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
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

**Additional object properties:** not allowed by the schema.

## AddTravelMemberResultDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `member` | [TravelMemberDto](t.md#travelmemberdto) | Yes | Not declared nullable | Member represented by the `TravelMemberDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `invitationCode` | `string` | No | Explicitly allowed | Invitation code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `invitationExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for invitation expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AddVehicleBrakeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `inspectedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for inspected at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `odometer` | `number (double)` | No | Explicitly allowed | Numeric odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `componentCode` | `string` | Yes | Not declared nullable | Component code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `conditionCode` | `string` | Yes | Not declared nullable | Condition code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `measurementMillimeters` | `number (double)` | No | Explicitly allowed | Numeric measurement millimeters for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `recommendedAction` | `string` | No | Explicitly allowed | Recommended action text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `costMinor` | `integer (int64)` | Yes | Not declared nullable | Cost in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `attachmentFileRef` | `string` | No | Explicitly allowed | Attachment file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `notes` | `string` | No | Explicitly allowed | Human notes for this record; keep them within the authorized data scope. | Shared convention | No further constraint recorded |
| `clientOperationId` | `string` | Yes | Not declared nullable | Client's stable identity for this logical operation; preserve it through interrupted responses. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AddVehicleExpenseDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `categoryCode` | `string` | Yes | Not declared nullable | Category code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `incurredAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for incurred at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `vendor` | `string` | No | Explicitly allowed | Vendor text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `notes` | `string` | No | Explicitly allowed | Human notes for this record; keep them within the authorized data scope. | Shared convention | No further constraint recorded |
| `receiptFileRef` | `string` | No | Explicitly allowed | Receipt file ref text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `clientOperationId` | `string` | Yes | Not declared nullable | Client's stable identity for this logical operation; preserve it through interrupted responses. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AddVehicleTyreDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `positionCode` | `string` | Yes | Not declared nullable | Position code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `brand` | `string` | No | Explicitly allowed | Brand text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `model` | `string` | No | Explicitly allowed | Model in the owning domain; for vehicle contracts, the vehicle model associated with the manufacturer. | Shared convention | No further constraint recorded |
| `size` | `string` | No | Explicitly allowed | Size text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `observedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for observed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `odometer` | `number (double)` | No | Explicitly allowed | Numeric odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `treadDepthMillimeters` | `number (double)` | No | Explicitly allowed | Numeric tread depth millimeters for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `pressurePsi` | `number (double)` | No | Explicitly allowed | Numeric pressure psi for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `conditionCode` | `string` | Yes | Not declared nullable | Condition code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | Shared convention | No further constraint recorded |
| `costMinor` | `integer (int64)` | Yes | Not declared nullable | Cost in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `notes` | `string` | No | Explicitly allowed | Human notes for this record; keep them within the authorized data scope. | Shared convention | No further constraint recorded |
| `clientOperationId` | `string` | Yes | Not declared nullable | Client's stable identity for this logical operation; preserve it through interrupted responses. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AddWalletRecipientDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `identifier` | `string` | Yes | Not declared nullable | Sign-in identifier accepted by this identity contract; validation and privacy rules still apply. | Shared convention | No further constraint recorded |
| `alias` | `string` | No | Explicitly allowed | Alias text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AmortizationPdfRowDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `period` | `integer (int32)` | Yes | Not declared nullable | Numeric period for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `payment` | `string` | Yes | Not declared nullable | Payment text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `principal` | `string` | Yes | Not declared nullable | Principal text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `interest` | `string` | Yes | Not declared nullable | Interest text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `balance` | `string` | Yes | Not declared nullable | Balance text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `date` | `string` | No | Explicitly allowed | Date text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AppReleaseCorrectionNoticeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `kind` | `string` | Yes | Not declared nullable | Kind text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `relatedReleaseVersion` | `string` | Yes | Not declared nullable | Related release version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `relatedReleasePath` | `string` | Yes | Not declared nullable | Related release path text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `message` | `string` | Yes | Not declared nullable | Message text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AppReleaseDetailDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `productSurface` | `string` | Yes | Not declared nullable | Product surface text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `platform` | `string` | Yes | Not declared nullable | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | Shared convention | No further constraint recorded |
| `version` | `string` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `language` | `string` | Yes | Not declared nullable | Language selector/content language; use the endpoint's supported values and fallback rules. | Shared convention | No further constraint recorded |
| `simpleSummary` | `string` | Yes | Not declared nullable | Simple summary text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `detailedDescription` | `string` | Yes | Not declared nullable | Detailed description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `releasedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for released at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `publishedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for published at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `isPublished` | `boolean` | Yes | Not declared nullable | Whether is published applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `improvements` | [AppReleaseImprovementDto](a.md#appreleaseimprovementdto)[] | Yes | Not declared nullable | Collection of improvements for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `buildNumber` | `integer (int32)` | No | Not declared nullable | Numeric build number for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `revision` | `integer (int32)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |
| `translationStatus` | `string` | No | Explicitly allowed | Translation status text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `legalReviewStatus` | `string` | No | Explicitly allowed | Legal review status text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `fallbackPolicy` | `string` | No | Explicitly allowed | Fallback policy text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isMachineGenerated` | `boolean` | No | Not declared nullable | Whether is machine generated applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `translationSourceId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related translation source record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `sourceRevision` | `integer (int32)` | No | Not declared nullable | Source revision for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `translationReviewedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for translation reviewed at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `translationReviewNotes` | `string` | No | Explicitly allowed | Translation review notes text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `correctsReleaseId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related corrects release record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `supersedesReleaseId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related supersedes release record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `correctionNotice` | [AppReleaseCorrectionNoticeDto](a.md#appreleasecorrectionnoticedto) | No | Not declared nullable | Correction notice represented by the `AppReleaseCorrectionNoticeDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AppReleaseImprovementDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `category` | `string` | Yes | Not declared nullable | Category text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `detail` | `string` | Yes | Not declared nullable | Detail text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `improvementDate` | `string (date)` | Yes | Not declared nullable | Calendar date for improvement date; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |
| `endUserBenefit` | `string` | Yes | Not declared nullable | End user benefit text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `sortOrder` | `integer (int32)` | Yes | Not declared nullable | Numeric sort order for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AppReleaseListDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `items` | [AppReleaseSummaryDto](a.md#appreleasesummarydto)[] | Yes | Not declared nullable | Records returned in this collection/page, each using the referenced item model. | Shared convention | No further constraint recorded |
| `totalCount` | `integer (int32)` | Yes | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | Shared convention | No further constraint recorded |
| `page` | `integer (int32)` | Yes | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | Shared convention | No further constraint recorded |
| `pageSize` | `integer (int32)` | Yes | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AppReleaseSummaryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `productSurface` | `string` | Yes | Not declared nullable | Product surface text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `platform` | `string` | Yes | Not declared nullable | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | Shared convention | No further constraint recorded |
| `version` | `string` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `language` | `string` | Yes | Not declared nullable | Language selector/content language; use the endpoint's supported values and fallback rules. | Shared convention | No further constraint recorded |
| `simpleSummary` | `string` | Yes | Not declared nullable | Simple summary text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `releasedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for released at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `publishedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for published at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `isPublished` | `boolean` | Yes | Not declared nullable | Whether is published applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `improvementCount` | `integer (int32)` | Yes | Not declared nullable | Number of improvement in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `translationStatus` | `string` | No | Explicitly allowed | Translation status text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `legalReviewStatus` | `string` | No | Explicitly allowed | Legal review status text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `fallbackPolicy` | `string` | No | Explicitly allowed | Fallback policy text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isMachineGenerated` | `boolean` | No | Not declared nullable | Whether is machine generated applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `isStale` | `boolean` | No | Not declared nullable | Whether is stale applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AppVersionPolicyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `platform` | `string` | Yes | Not declared nullable | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | Shared convention | No further constraint recorded |
| `installedVersion` | `string` | Yes | Not declared nullable | Installed version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `minimumRequiredVersion` | `string` | Yes | Not declared nullable | Minimum required version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `currentVersion` | `string` | Yes | Not declared nullable | Current version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `updateRequired` | `boolean` | Yes | Not declared nullable | Whether update required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `storeUrl` | `string` | Yes | Not declared nullable | URL for store; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `changelogUrl` | `string` | Yes | Not declared nullable | URL for changelog; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `currentRelease` | [AppReleaseSummaryDto](a.md#appreleasesummarydto) | No | Not declared nullable | Current release represented by the `AppReleaseSummaryDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `optionalPromptCooldownHours` | `integer (int32)` | No | Not declared nullable | Numeric optional prompt cooldown hours for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `optionalUpdateMessage` | `string` | No | Explicitly allowed | Optional update message text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `requiredUpdateMessage` | `string` | No | Explicitly allowed | Required update message text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AuthResponse

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `accessToken` | `string` | Yes | Not declared nullable | Sensitive bearer access credential for the issued session. | Shared convention | No further constraint recorded |
| `accessTokenExpiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for access token expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `refreshToken` | `string` | Yes | Not declared nullable | Sensitive rotating refresh credential; preserve secure-store and session-family rules. | Shared convention | No further constraint recorded |
| `user` | [UserDto](u.md#userdto) | Yes | Not declared nullable | User represented by the `UserDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `isNewAccount` | `boolean` | No | Not declared nullable | Whether is new account applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## AuthorizeRentalBookingPaymentDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `providerReference` | `string` | Yes | Not declared nullable | Provider reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
