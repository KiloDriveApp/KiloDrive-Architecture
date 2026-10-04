# Field dictionary: B

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

The explanation basis distinguishes model-specific meaning, shared conventions,
name-derived units and type-only entries awaiting semantic review. See the
[coverage report](../reference/coverage.md); field presence is not semantic completeness.

## Models on this page

- [BankBranchReferenceDto](#bankbranchreferencedto)
- [BankReferenceDto](#bankreferencedto)
- [BankTransferTopUpDto](#banktransfertopupdto)
- [BeginContactTwoFactorEnrollmentRequest](#begincontacttwofactorenrollmentrequest)
- [BidStatus](#bidstatus)
- [BidType](#bidtype)
- [BillingHistoryItemDto](#billinghistoryitemdto)
- [BillingModeDto](#billingmodedto)
- [BillingPaymentMethodDto](#billingpaymentmethoddto)
- [BlockDriverByIdentifierDto](#blockdriverbyidentifierdto)
- [BlogCatalogDto](#blogcatalogdto)
- [BlogPostDto](#blogpostdto)
- [BlogPostSummaryDto](#blogpostsummarydto)
- [BlogTaxonomyDto](#blogtaxonomydto)
- [BlogTocItemDto](#blogtocitemdto)
- [BulkDeliveryItemResultDto](#bulkdeliveryitemresultdto)
- [BulkDeliveryRequestDto](#bulkdeliveryrequestdto)
- [BulkDeliveryResultDto](#bulkdeliveryresultdto)
- [BusinessShippingAccountDto](#businessshippingaccountdto)
- [BusinessShippingAccountStatus](#businessshippingaccountstatus)
- [BusinessShippingMemberDto](#businessshippingmemberdto)

## BankBranchReferenceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `branchCode` | `string` | Yes | Not declared nullable | Branch code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `routingCode` | `string` | No | Explicitly allowed | Routing code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | Shared convention | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BankReferenceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `institutionCode` | `string` | Yes | Not declared nullable | Institution code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `swiftBic` | `string` | No | Explicitly allowed | Swift bic text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | Shared convention | No further constraint recorded |
| `branches` | [BankBranchReferenceDto](b.md#bankbranchreferencedto)[] | Yes | Not declared nullable | Collection of branches for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BankTransferTopUpDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `instructions` | `string` | No | Explicitly allowed | Instructions text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `failureReason` | `string` | No | Explicitly allowed | Failure reason text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BeginContactTwoFactorEnrollmentRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `method` | `string` | Yes | Not declared nullable | Method text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BidStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`, `5`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Accepted | Accepted state/choice in this specific enum. |
| `3` | Rejected | Rejected state/choice in this specific enum. |
| `4` | Withdrawn | Withdrawn state/choice in this specific enum. |
| `5` | Expired | Expired state/choice in this specific enum. |

## BidType

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Accept | Accept state/choice in this specific enum. |
| `2` | Counter | Counter state/choice in this specific enum. |

## BillingHistoryItemDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `description` | `string` | Yes | Not declared nullable | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `amountMinor` | `integer (int64)` | Yes | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | Shared convention | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `status` | [PaymentStatus](p.md#paymentstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `method` | [PaymentMethod](p.md#paymentmethod) | Yes | Not declared nullable | Method represented by the `PaymentMethod` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `termDays` | `integer (int32)` | No | Explicitly allowed | Requested/applicable membership term in days; only configured valid terms are allowed. | Shared convention | No further constraint recorded |
| `periodStartUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for period start; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `periodEndUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for period end; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BillingModeDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `mode` | `string` | Yes | Not declared nullable | Mode text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BillingPaymentMethodDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | Shared convention | No further constraint recorded |
| `label` | `string` | Yes | Not declared nullable | Label text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `available` | `boolean` | Yes | Not declared nullable | Whether available applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `note` | `string` | No | Explicitly allowed | Human note for this operation; do not include secrets or treat text as executable instructions. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BlockDriverByIdentifierDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `identifierType` | `string` | Yes | Not declared nullable | Identifier type text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `identifier` | `string` | Yes | Not declared nullable | Sign-in identifier accepted by this identity contract; validation and privacy rules still apply. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BlogCatalogDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `posts` | [BlogPostSummaryDto](b.md#blogpostsummarydto)[] | Yes | Not declared nullable | Collection of posts for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `categories` | [BlogTaxonomyDto](b.md#blogtaxonomydto)[] | Yes | Not declared nullable | Collection of categories for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `tags` | [BlogTaxonomyDto](b.md#blogtaxonomydto)[] | Yes | Not declared nullable | Collection of tags for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `page` | `integer (int32)` | Yes | Not declared nullable | Page-number context for this endpoint; not a universal zero-based offset. | Shared convention | No further constraint recorded |
| `pageSize` | `integer (int32)` | Yes | Not declared nullable | Requested or returned page size, subject to this endpoint's server bounds. | Shared convention | No further constraint recorded |
| `totalCount` | `integer (int32)` | Yes | Not declared nullable | Total count defined by this page model; not automatically a live aggregate. | Shared convention | No further constraint recorded |
| `totalPages` | `integer (int32)` | Yes | Not declared nullable | Number of pages represented by this page-number model. | Shared convention | No further constraint recorded |
| `activeCategory` | `string` | No | Explicitly allowed | Active category text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `activeTag` | `string` | No | Explicitly allowed | Active tag text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `search` | `string` | No | Explicitly allowed | Search text applied within this endpoint's authorized collection; it does not widen account/tenant scope. | Shared convention | No further constraint recorded |
| `hasMore` | `boolean` | No | Explicitly allowed | Whether the seek-paged result indicates more records after this page. | Shared convention | No further constraint recorded |
| `nextCursor` | `string` | No | Explicitly allowed | Opaque, scope-bound continuation token; preserve it unchanged and reset it when filters/context change. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BlogPostDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `slug` | `string` | Yes | Not declared nullable | Slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `language` | `string` | Yes | Not declared nullable | Language selector/content language; use the endpoint's supported values and fallback rules. | Shared convention | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `excerpt` | `string` | Yes | Not declared nullable | Excerpt text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `bodyHtml` | `string` | Yes | Not declared nullable | Body html text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `heroImageUrl` | `string` | No | Explicitly allowed | URL for hero image; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `heroImageAlt` | `string` | No | Explicitly allowed | Hero image alt text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `seoTitle` | `string` | Yes | Not declared nullable | Seo title text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `metaDescription` | `string` | Yes | Not declared nullable | Meta description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `canonicalUrl` | `string` | No | Explicitly allowed | URL for canonical; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `authorName` | `string` | Yes | Not declared nullable | Author name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `category` | [BlogTaxonomyDto](b.md#blogtaxonomydto) | No | Not declared nullable | Category represented by the `BlogTaxonomyDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `tags` | [BlogTaxonomyDto](b.md#blogtaxonomydto)[] | Yes | Not declared nullable | Collection of tags for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `tableOfContents` | [BlogTocItemDto](b.md#blogtocitemdto)[] | Yes | Not declared nullable | Collection of table of contents for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `readingMinutes` | `integer (int32)` | Yes | Not declared nullable | Reading, measured in minutes. | Naming convention | No further constraint recorded |
| `isPublished` | `boolean` | Yes | Not declared nullable | Whether is published applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `isFeatured` | `boolean` | Yes | Not declared nullable | Whether is featured applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `publishedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for published at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `scheduledForUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for scheduled for; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `version` | `integer (int32)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `editableBodyHtml` | `string` | No | Explicitly allowed | Editable body html text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BlogPostSummaryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `slug` | `string` | Yes | Not declared nullable | Slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `language` | `string` | Yes | Not declared nullable | Language selector/content language; use the endpoint's supported values and fallback rules. | Shared convention | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `excerpt` | `string` | Yes | Not declared nullable | Excerpt text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `heroImageUrl` | `string` | No | Explicitly allowed | URL for hero image; validate the intended origin/access and never assume private links are public. | Naming convention | No further constraint recorded |
| `heroImageAlt` | `string` | No | Explicitly allowed | Hero image alt text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `authorName` | `string` | Yes | Not declared nullable | Author name text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `category` | [BlogTaxonomyDto](b.md#blogtaxonomydto) | No | Not declared nullable | Category represented by the `BlogTaxonomyDto` model or enum; use that definition's fields/values. | Type only; meaning review open | No further constraint recorded |
| `tags` | [BlogTaxonomyDto](b.md#blogtaxonomydto)[] | Yes | Not declared nullable | Collection of tags for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |
| `readingMinutes` | `integer (int32)` | Yes | Not declared nullable | Reading, measured in minutes. | Naming convention | No further constraint recorded |
| `isFeatured` | `boolean` | Yes | Not declared nullable | Whether is featured applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `publishedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for published at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `scheduledForUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for scheduled for; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `version` | `integer (int32)` | Yes | Not declared nullable | Version in this model's domain; not automatically an API major version. | Shared convention | No further constraint recorded |
| `isPublished` | `boolean` | No | Not declared nullable | Whether is published applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `readingEstimateAvailable` | `boolean` | No | Not declared nullable | Whether reading estimate available applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BlogTaxonomyDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `slug` | `string` | Yes | Not declared nullable | Slug text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `language` | `string` | Yes | Not declared nullable | Language selector/content language; use the endpoint's supported values and fallback rules. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `description` | `string` | No | Explicitly allowed | Description text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `articleCount` | `integer (int32)` | No | Not declared nullable | Number of article in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `browsePath` | `string` | No | Explicitly allowed | Browse path text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BlogTocItemDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `title` | `string` | Yes | Not declared nullable | Human-readable title for the record/content, distinct from its ID. | Shared convention | No further constraint recorded |
| `level` | `integer (int32)` | Yes | Not declared nullable | Numeric level for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `href` | `string` | Yes | Not declared nullable | Href text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `parentId` | `string` | No | Explicitly allowed | Identifier of the related parent record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BulkDeliveryItemResultDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `index` | `integer (int32)` | Yes | Not declared nullable | Numeric index for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | Type only; meaning review open | No further constraint recorded |
| `deliveryRequestId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related delivery request record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `errorCode` | `string` | No | Explicitly allowed | Error code text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BulkDeliveryRequestDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `businessShippingAccountId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related business shipping account record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `orders` | [CreateDeliveryRequestDto](c.md#createdeliveryrequestdto)[] | Yes | Not declared nullable | Collection of orders for this model; interpret each item through the declared item type. | Type only; meaning review open | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BulkDeliveryResultDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `batchId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related batch record in this model; ownership and scope are checked separately. | Naming convention | No further constraint recorded |
| `status` | [DeliveryBulkOrderStatus](d.md#deliverybulkorderstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `createdCount` | `integer (int32)` | Yes | Not declared nullable | Number of created in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `failedCount` | `integer (int32)` | Yes | Not declared nullable | Number of failed in this model's stated scope; not automatically a global/live total. | Naming convention | No further constraint recorded |
| `items` | [BulkDeliveryItemResultDto](b.md#bulkdeliveryitemresultdto)[] | Yes | Not declared nullable | Records returned in this collection/page, each using the referenced item model. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BusinessShippingAccountDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `billingEmail` | `string` | Yes | Not declared nullable | Billing email text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `currency` | `string` | Yes | Not declared nullable | ISO currency code for the accompanying monetary amounts. | Shared convention | No further constraint recorded |
| `status` | [BusinessShippingAccountStatus](b.md#businessshippingaccountstatus) | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | Shared convention | No further constraint recorded |
| `monthlyCreditLimitMinor` | `integer (int64)` | Yes | Not declared nullable | Monthly credit limit in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `currentExposureMinor` | `integer (int64)` | Yes | Not declared nullable | Current exposure in the accompanying currency's integer minor units; do not send a formatted money string. | Naming convention | No further constraint recorded |
| `requireDeliveryOtp` | `boolean` | Yes | Not declared nullable | Whether require delivery otp applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `requireProofPhoto` | `boolean` | Yes | Not declared nullable | Whether require proof photo applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `verifiedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for verified at; parse strictly and localize only for display. | Naming convention | No further constraint recorded |
| `requireSignature` | `boolean` | No | Not declared nullable | Whether require signature applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## BusinessShippingAccountStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`, `4`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Active | Active state/choice in this specific enum. |
| `3` | Suspended | Suspended state/choice in this specific enum. |
| `4` | Closed | Closed state/choice in this specific enum. |

## BusinessShippingMemberDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Explanation basis | Additional constraints |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | Shared convention | No further constraint recorded |
| `userId` | `string (uuid)` | Yes | Not declared nullable | Related account identity; the server still proves the caller's ownership or permitted relationship. | Shared convention | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | Shared convention | No further constraint recorded |
| `role` | `string` | Yes | Not declared nullable | Role text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | Type only; meaning review open | No further constraint recorded |
| `canCreateOrders` | `boolean` | Yes | Not declared nullable | Whether can create orders applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canViewBilling` | `boolean` | Yes | Not declared nullable | Whether can view billing applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `canManageMembers` | `boolean` | Yes | Not declared nullable | Whether can manage members applies in this model's context. This flag does not replace server permission or lifecycle checks. | Type only; meaning review open | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | Shared convention | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
