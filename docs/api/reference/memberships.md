# Membership and store entitlement workflows

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## Operations on this page

- [GET `/api/v1/driver/billing`](#get-apiv1driverbilling)
- [PUT `/api/v1/driver/billing/mode`](#put-apiv1driverbillingmode)
- [GET `/api/v1/driver/membership`](#get-apiv1drivermembership)
- [POST `/api/v1/driver/membership`](#post-apiv1drivermembership)
- [PUT `/api/v1/driver/membership/auto-renew`](#put-apiv1drivermembershipauto-renew)
- [POST `/api/v1/driver/membership/checkout`](#post-apiv1drivermembershipcheckout)
- [POST `/api/v1/driver/membership/pending-change/cancel`](#post-apiv1drivermembershippending-changecancel)
- [GET `/api/v1/driver/membership/store-status`](#get-apiv1drivermembershipstore-status)
- [GET `/api/v1/membership/plans`](#get-apiv1membershipplans)
- [GET `/api/v1/rental-partner/membership/plans`](#get-apiv1rental-partnermembershipplans)
- [GET `/api/v1/store-billing/operations/{operationId}`](#get-apiv1store-billingoperationsoperationid)
- [POST `/api/v1/store-billing/prepare`](#post-apiv1store-billingprepare)
- [GET `/api/v1/store-billing/products`](#get-apiv1store-billingproducts)
- [POST `/api/v1/store-billing/quote`](#post-apiv1store-billingquote)
- [POST `/api/v1/store-billing/restore`](#post-apiv1store-billingrestore)
- [POST `/api/v1/store-billing/verify`](#post-apiv1store-billingverify)

## GET `/api/v1/driver/billing`

**What it does:** Read the driver's billing mode, payment choices, billing history and store reconciliation facts. Use membership/store-status for the unified entitlement decision.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [ProviderBillingDto](../schemas/p.md#providerbillingdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## PUT `/api/v1/driver/billing/mode`

**What it does:** Change the driver's requested billing mode against the current revision; this does not by itself purchase or activate a plan.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

**Body:** [BillingModeDto](../schemas/b.md#billingmodedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | pattern: `^\"[1-9][0-9]*\"$` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [ProviderBillingDto](../schemas/p.md#providerbillingdto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/driver/membership`

**What it does:** Read the driver's current membership, usage period, pending plan change and renewal preference.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [MyMembershipDto](../schemas/m.md#mymembershipdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/driver/membership`

**What it does:** Purchase an eligible driver plan through the wallet workflow with server-owned pricing/proration and revision checks.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

**Body:** [SubscribeMembershipRequest](../schemas/s.md#subscribemembershiprequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | pattern: `^\"[1-9][0-9]*\"$` |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. | minLength: `1`; maxLength: `256` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [MyMembershipDto](../schemas/m.md#mymembershipdto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit. The server can require recent authentication; local app unlock is not proof.

## PUT `/api/v1/driver/membership/auto-renew`

**What it does:** Change the server-managed membership renewal preference. Native-store subscription management remains a separate provider workflow.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

**Body:** [SetAutoRenewRequest](../schemas/s.md#setautorenewrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | pattern: `^\"[1-9][0-9]*\"$` |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value. Detailed meaning and accepted vocabulary are not yet documented for this model. | minLength: `1`; maxLength: `256` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [MyMembershipDto](../schemas/m.md#mymembershipdto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## POST `/api/v1/driver/membership/checkout`

**What it does:** Create a membership checkout for a plan, term and supported provider; a checkout response is not proof of entitlement.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

**Body:** [MembershipCheckoutRequest](../schemas/m.md#membershipcheckoutrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. | minLength: `1`; maxLength: `256` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [MembershipCheckoutDto](../schemas/m.md#membershipcheckoutdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. The server can require recent authentication; local app unlock is not proof.

## POST `/api/v1/driver/membership/pending-change/cancel`

**What it does:** Cancel the identified pending membership change using the original membership revision; retain the currently effective entitlement facts.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

**Body:** [CancelPendingMembershipChangeRequest](../schemas/c.md#cancelpendingmembershipchangerequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. | pattern: `^\"[1-9][0-9]*\"$` |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. | minLength: `1`; maxLength: `256` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [MyMembershipDto](../schemas/m.md#mymembershipdto) | `text/plain`, `application/json`, `text/json` | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit. The server can require recent authentication; local app unlock is not proof.

## GET `/api/v1/driver/membership/store-status`

**What it does:** Read the single authoritative driver membership workspace snapshot, including entitlement and billing/recovery state.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [MembershipStoreStatusDto](../schemas/m.md#membershipstorestatusdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/membership/plans`

**What it does:** List driver membership catalog plans, term prices and benefit limits for the resolved country context.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [MembershipPlanDto](../schemas/m.md#membershipplandto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/rental-partner/membership/plans`

**What it does:** List membership plans for rental partners; organization access and purchase readiness are checked separately.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [MembershipPlanDto](../schemas/m.md#membershipplandto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/store-billing/operations/{operationId}`

**What it does:** Read the caller's prepared store purchase operation and recovery state without starting another native purchase.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `operationId` | path | Yes | `string (uuid)` | Durable operation reference used for applicable outcome discovery. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [StorePurchaseOperationDto](../schemas/s.md#storepurchaseoperationdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/store-billing/prepare`

**What it does:** Persist the applicable purchase preparation before native checkout; preparation does not grant entitlement.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

**Body:** [PrepareStorePurchaseDto](../schemas/p.md#preparestorepurchasedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [StorePurchasePreparationDto](../schemas/s.md#storepurchasepreparationdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/store-billing/products`

**What it does:** Read the reviewed platform/audience product mapping for comparison with actual native localized offers.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `platform` | query | Yes | `string` | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | Allowed wire values: `apple`, `google` |
| `audience` | query | Conditional or optional | `string` | Applicable product/client audience, distinct from verified security authority. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | Array of [StoreProductDto](../schemas/s.md#storeproductdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/store-billing/quote`

**What it does:** Validate the exact mapped plan and native offer and create the applicable server-owned purchase quote.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

**Body:** [CreateStorePurchaseQuoteDto](../schemas/c.md#createstorepurchasequotedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [StorePurchaseQuoteDto](../schemas/s.md#storepurchasequotedto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/store-billing/restore`

**What it does:** Reconcile eligible existing store purchases with the authenticated account; restoration is not a new sale.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

**Body:** [VerifyStorePurchaseDto](../schemas/v.md#verifystorepurchasedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [StoreEntitlementDto](../schemas/s.md#storeentitlementdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/store-billing/verify`

**What it does:** Validate store transaction evidence on the server and reconcile/grant the mapped entitlement once.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required.

**Body:** [VerifyStorePurchaseDto](../schemas/v.md#verifystorepurchasedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. | minLength: `1`; maxLength: `128` |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [StoreEntitlementDto](../schemas/s.md#storeentitlementdto) | `text/plain`, `application/json`, `text/json` | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.
