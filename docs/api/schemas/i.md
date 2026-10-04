# Field dictionary: I

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

The explanation basis distinguishes model-specific meaning, shared conventions,
name-derived units and type-only entries awaiting semantic review. See the
[coverage report](../reference/coverage.md); field presence is not semantic completeness.

## Models on this page

- [IdentitySubmissionOutcomeDto](#identitysubmissionoutcomedto)
- [IdentityVerificationDto](#identityverificationdto)
- [ImportedRatingBadgeDto](#importedratingbadgedto)
- [ImportedRatingSourceDto](#importedratingsourcedto)
- [IncomingVoiceCallDto](#incomingvoicecalldto)
- [IncomingVoiceCallRecoveryDto](#incomingvoicecallrecoverydto)
- [InsuranceStatus](#insurancestatus)
- [InviteRentalTeamMemberDto](#inviterentalteammemberdto)
- [IssueRentalAgreementDto](#issuerentalagreementdto)

## IdentitySubmissionOutcomeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `schemaVersion` | `integer (int32)` | Yes | Not declared nullable | Schema version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `outcome` | `string` | Yes | Not declared nullable | Result/recovery state of this operation; unknown or pending is not failed or successful. | Shared convention | No further constraint recorded |
| `path` | `string` | Yes | Not declared nullable | Path text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `action` | `string` | Yes | Not declared nullable | Action text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `keySha256` | `string` | Yes | Not declared nullable | Key sha256 text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `payloadSha256` | `string` | Yes | Not declared nullable | Payload sha256 text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `caseId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related case record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `documentId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related document record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `driverProfileId` | `string (uuid)` | No | Explicitly allowed | Driver-profile record associated with this operation or result. | Shared convention | No further constraint recorded |
| `sourceDriverDocumentId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related source driver document record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `expectedRevision` | `integer (int64)` | Yes | Not declared nullable | Revision the caller read for this logical update; retain the original during uncertain-outcome recovery. | Shared convention | No further constraint recorded |
| `resultRevision` | `integer (int64)` | Yes | Not declared nullable | Result revision for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `originalDriverRevision` | `integer (int64)` | No | Explicitly allowed | Original driver revision for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `resultDriverRevision` | `integer (int64)` | No | Explicitly allowed | Result driver revision for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `submittedStatus` | `string` | Yes | Not declared nullable | Submitted status text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `canResume` | `boolean` | No | Not declared nullable | Whether can resume applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## IdentityVerificationDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `dateOfBirth` | `string (date)` | No | Explicitly allowed | Calendar date for date of birth; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |
| `gender` | `string` | No | Explicitly allowed | Gender text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `caseId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related case record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `documentId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related document record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `reviewNote` | `string` | No | Explicitly allowed | Human-readable reviewer explanation, including remediation where applicable. | Shared convention | No further constraint recorded |
| `verifiedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for verified at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `documentType` | [DocumentType](d.md#documenttype) | No | Not declared nullable | Document type represented by the `DocumentType` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `hasBackImage` | `boolean` | No | Not declared nullable | Whether has back image applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `driverLicenseNumber` | `string` | No | Explicitly allowed | Driver license number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `driverLicenseControlNumber` | `string` | No | Explicitly allowed | Driver license control number text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `driverLicenseOriginalIssueDate` | `string (date)` | No | Explicitly allowed | Calendar date for driver license original issue date; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |
| `driverLicenseExpiresOn` | `string (date)` | No | Explicitly allowed | Calendar date for driver license expires on; preserve date-only semantics rather than shifting it through a timezone. | Naming convention | No further constraint recorded |
| `riderPolicy` | [RiderVerificationPolicyDto](r.md#riderverificationpolicydto) | No | Not declared nullable | Rider policy represented by the `RiderVerificationPolicyDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ImportedRatingBadgeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `source` | `string` | Yes | Not declared nullable | Source text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | Shared convention | No further constraint recorded |
| `average` | `number (double)` | Yes | Not declared nullable | Numeric average for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `count` | `integer (int32)` | Yes | Not declared nullable | Numeric count for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `verifiedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for verified at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## ImportedRatingSourceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `source` | `string` | Yes | Not declared nullable | Source text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `displayName` | `string` | Yes | Not declared nullable | Human-readable display label; do not use it as a stable identifier. | Shared convention | No further constraint recorded |
| `average` | `number (double)` | Yes | Not declared nullable | Numeric average for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `count` | `integer (int32)` | Yes | Not declared nullable | Numeric count for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `verifiedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for verified at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `verificationMethod` | `string` | No | Explicitly allowed | Verification method text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `confidenceLevel` | [ExternalEvidenceConfidenceLevel](e.md#externalevidenceconfidencelevel) | No | Not declared nullable | Confidence level represented by the `ExternalEvidenceConfidenceLevel` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## IncomingVoiceCallDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `callId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related call record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | Shared convention | No further constraint recorded |
| `callerName` | `string` | Yes | Not declared nullable | Caller name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `callerHasAvatar` | `boolean` | Yes | Not declared nullable | Whether caller has avatar applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `recordingEnabled` | `boolean` | Yes | Not declared nullable | Whether recording enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `recordingRequired` | `boolean` | Yes | Not declared nullable | Whether recording required applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `recordingDisclosureVersion` | `string` | No | Explicitly allowed | Recording disclosure version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `ringExpiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for ring expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## IncomingVoiceCallRecoveryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `call` | [IncomingVoiceCallDto](i.md#incomingvoicecalldto) | No | Not declared nullable | Call represented by the `IncomingVoiceCallDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## InsuranceStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Unconfirmed | Unconfirmed state/choice in this specific enum. |
| `2` | Confirmed | Confirmed state/choice in this specific enum. |

## InviteRentalTeamMemberDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `email` | `string` | Yes | Not declared nullable | Email address for this model's person/destination; its presence does not prove verification. | Shared convention | No further constraint recorded |
| `role` | [RentalOrganizationRole](r.md#rentalorganizationrole) | Yes | Not declared nullable | Role represented by the `RentalOrganizationRole` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `permissions` | [RentalOrganizationPermission](r.md#rentalorganizationpermission) | Yes | Not declared nullable | Permissions represented by the `RentalOrganizationPermission` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## IssueRentalAgreementDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `termsVersion` | `string` | Yes | Not declared nullable | Terms version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `expectedBookingVersion` | `integer (int32)` | Yes | Not declared nullable | Expected booking version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `termsSnapshot` | `string` | No | Explicitly allowed | Terms snapshot text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
