# Field dictionary: L

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

The explanation basis distinguishes model-specific meaning, shared conventions,
name-derived units and type-only entries awaiting semantic review. See the
[coverage report](../reference/coverage.md); field presence is not semantic completeness.

## Models on this page

- [LegalDocumentAcceptanceDto](#legaldocumentacceptancedto)
- [LegalDocumentCatalogueDto](#legaldocumentcataloguedto)
- [LegalDocumentCatalogueItemDto](#legaldocumentcatalogueitemdto)
- [LegalDocumentVersionDto](#legaldocumentversiondto)
- [LegalDocumentVersionSummaryDto](#legaldocumentversionsummarydto)
- [LinkSocialLoginConnectionRequest](#linksocialloginconnectionrequest)
- [LoginRequest](#loginrequest)
- [LoginResultDto](#loginresultdto)

## LegalDocumentAcceptanceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `documentKey` | `string` | Yes | Not declared nullable | Stable key of the legal/document definition whose version is being accepted or read. | Shared convention | No further constraint recorded |
| `version` | `string` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `contentHash` | `string` | Yes | Not declared nullable | Content hash text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `language` | `string` | Yes | Not declared nullable | Language selector/content language; use the endpoint's supported values and fallback rules. | Shared convention | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `userRole` | `string` | Yes | Not declared nullable | User role text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `channel` | `string` | Yes | Not declared nullable | Channel text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `applicationVersion` | `string` | No | Explicitly allowed | Application version for this model's state or policy; do not substitute a timestamp or mobile build. | Naming convention | No further constraint recorded |
| `acceptedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for accepted at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## LegalDocumentCatalogueDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `requestedLanguage` | `string` | Yes | Not declared nullable | Requested language text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `resolvedLanguage` | `string` | Yes | Not declared nullable | Resolved language text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isLanguageFallback` | `boolean` | Yes | Not declared nullable | Whether is language fallback applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `audience` | `string` | Yes | Not declared nullable | Applicable product/client audience, distinct from verified security authority. | Shared convention | No further constraint recorded |
| `acceptanceVerified` | `boolean` | Yes | Not declared nullable | Whether acceptance verified applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requiredAcceptanceSatisfied` | `boolean` | Yes | Not declared nullable | Whether required acceptance satisfied applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `verifiedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for verified at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `documents` | [LegalDocumentCatalogueItemDto](l.md#legaldocumentcatalogueitemdto)[] | Yes | Not declared nullable | Collection of documents for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `recoveryHash` | `string` | No | Explicitly allowed | Recovery hash text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `recoveryExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for recovery expires at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `recoveryToken` | `string` | No | Explicitly allowed | Private recovery token used by this specific ceremony; never log, publish or substitute it for another proof. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## LegalDocumentCatalogueItemDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `documentKey` | `string` | Yes | Not declared nullable | Stable key of the legal/document definition whose version is being accepted or read. | Shared convention | No further constraint recorded |
| `category` | `string` | Yes | Not declared nullable | Category text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `routeSlug` | `string` | Yes | Not declared nullable | Route slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `publicPath` | `string` | Yes | Not declared nullable | Public path text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `language` | `string` | Yes | Not declared nullable | Language selector/content language; use the endpoint's supported values and fallback rules. | Shared convention | No further constraint recorded |
| `isLanguageFallback` | `boolean` | Yes | Not declared nullable | Whether is language fallback applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `jurisdictionCode` | `string` | Yes | Not declared nullable | Jurisdiction code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `serviceScope` | `string` | Yes | Not declared nullable | Service scope text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `audience` | `string` | Yes | Not declared nullable | Applicable product/client audience, distinct from verified security authority. | Shared convention | No further constraint recorded |
| `version` | `string` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `contentHash` | `string` | Yes | Not declared nullable | Content hash text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `changeSummary` | `string` | Yes | Not declared nullable | Change summary text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `materialChangeClassification` | `string` | Yes | Not declared nullable | Material change classification text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `requiresAcceptance` | `boolean` | Yes | Not declared nullable | Whether requires acceptance applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requiresNotice` | `boolean` | Yes | Not declared nullable | Whether requires notice applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `publicationState` | `string` | Yes | Not declared nullable | Publication state text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `acceptanceState` | `string` | Yes | Not declared nullable | Acceptance state text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `acceptedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for accepted at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `effectiveAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for effective at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `publishedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for published at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## LegalDocumentVersionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `documentKey` | `string` | Yes | Not declared nullable | Stable key of the legal/document definition whose version is being accepted or read. | Shared convention | No further constraint recorded |
| `routeSlug` | `string` | Yes | Not declared nullable | Route slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `language` | `string` | Yes | Not declared nullable | Language selector/content language; use the endpoint's supported values and fallback rules. | Shared convention | No further constraint recorded |
| `jurisdictionCode` | `string` | Yes | Not declared nullable | Jurisdiction code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `serviceScope` | `string` | Yes | Not declared nullable | Service scope text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `audience` | `string` | Yes | Not declared nullable | Applicable product/client audience, distinct from verified security authority. | Shared convention | No further constraint recorded |
| `version` | `string` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `contentHash` | `string` | Yes | Not declared nullable | Content hash text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `summary` | `string` | Yes | Not declared nullable | Summary text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `bodyHtml` | `string` | Yes | Not declared nullable | Body html text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `changeSummary` | `string` | Yes | Not declared nullable | Change summary text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `materialChangeClassification` | `string` | Yes | Not declared nullable | Material change classification text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `requiresAcceptance` | `boolean` | Yes | Not declared nullable | Whether requires acceptance applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requiresNotice` | `boolean` | Yes | Not declared nullable | Whether requires notice applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `issuedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for issued at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `effectiveAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for effective at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `approvedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for approved at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `publishedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for published at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `supersededAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for superseded at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `withdrawnAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for withdrawn at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `approvalRole` | `string` | No | Explicitly allowed | Approval role text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `approvalReference` | `string` | No | Explicitly allowed | Approval reference text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `revision` | `integer (int64)` | Yes | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## LegalDocumentVersionSummaryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `documentKey` | `string` | Yes | Not declared nullable | Stable key of the legal/document definition whose version is being accepted or read. | Shared convention | No further constraint recorded |
| `routeSlug` | `string` | Yes | Not declared nullable | Route slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `language` | `string` | Yes | Not declared nullable | Language selector/content language; use the endpoint's supported values and fallback rules. | Shared convention | No further constraint recorded |
| `jurisdictionCode` | `string` | Yes | Not declared nullable | Jurisdiction code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `serviceScope` | `string` | Yes | Not declared nullable | Service scope text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `audience` | `string` | Yes | Not declared nullable | Applicable product/client audience, distinct from verified security authority. | Shared convention | No further constraint recorded |
| `version` | `string` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `contentHash` | `string` | Yes | Not declared nullable | Content hash text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `changeSummary` | `string` | Yes | Not declared nullable | Change summary text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `materialChangeClassification` | `string` | Yes | Not declared nullable | Material change classification text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `requiresAcceptance` | `boolean` | Yes | Not declared nullable | Whether requires acceptance applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requiresNotice` | `boolean` | Yes | Not declared nullable | Whether requires notice applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `effectiveAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for effective at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `publishedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for published at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## LinkSocialLoginConnectionRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `provider` | `string` | Yes | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | Shared convention | No further constraint recorded |
| `idToken` | `string` | No | Explicitly allowed | Private id token used by this specific ceremony; never log, publish or substitute it for another proof. | Naming convention | No further constraint recorded |
| `accessToken` | `string` | No | Explicitly allowed | Sensitive bearer access credential for the issued session. | Shared convention | No further constraint recorded |
| `nonce` | `string` | No | Explicitly allowed | Nonce text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `authorizationCode` | `string` | No | Explicitly allowed | Authorization code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## LoginRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `identifier` | `string` | Yes | Not declared nullable | Sign-in identifier accepted by this identity contract; validation and privacy rules still apply. | Shared convention | No further constraint recorded |
| `password` | `string` | Yes | Not declared nullable | Secret password input for the established secure identity ceremony; never echo or log it. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## LoginResultDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `requiresTwoFactor` | `boolean` | Yes | Not declared nullable | Whether login needs its next second-factor step before a final authenticated session exists. | Shared convention | No further constraint recorded |
| `twoFactorTicket` | `string` | No | Explicitly allowed | Sensitive temporary ceremony ticket; it is not a bearer access token. | Shared convention | No further constraint recorded |
| `auth` | [AuthResponse](a.md#authresponse) | No | Not declared nullable | Final authentication/session model when the ceremony actually completes. | Shared convention | No further constraint recorded |
| `pendingSocialLink` | [PendingSocialLinkDto](p.md#pendingsociallinkdto) | No | Not declared nullable | Protected pending account-link decision; email equality alone must not finalize it. | Shared convention | No further constraint recorded |
| `twoFactorMethod` | `string` | No | Explicitly allowed | Two factor method text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `maskedDestination` | `string` | No | Explicitly allowed | Privacy-reduced contact display for the ceremony; not the raw credential or full destination. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
