# Membership and store entitlement workflows

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## GET `/api/v1/driver/billing`

**What it does:** Read the permitted records/state for driver → billing. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ProviderBillingDto](../schemas/p.md#providerbillingdto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## PUT `/api/v1/driver/billing/mode`

**What it does:** Update the permitted configuration/record for driver → billing → mode. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Driver.

**Body:** [BillingModeDto](../schemas/b.md#billingmodedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ProviderBillingDto](../schemas/p.md#providerbillingdto) | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/driver/membership`

**What it does:** Read the permitted records/state for driver → membership. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [MyMembershipDto](../schemas/m.md#mymembershipdto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/driver/membership`

**What it does:** Purchase an eligible driver plan through the wallet workflow with server-owned pricing/proration and revision checks.

**Access:** Bearer required; declared roles: Driver.

**Body:** [SubscribeMembershipRequest](../schemas/s.md#subscribemembershiprequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [MyMembershipDto](../schemas/m.md#mymembershipdto) | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit. The server can require recent authentication; local app unlock is not proof.

## PUT `/api/v1/driver/membership/auto-renew`

**What it does:** Update the permitted configuration/record for driver → membership → auto renew. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Driver.

**Body:** [SetAutoRenewRequest](../schemas/s.md#setautorenewrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [MyMembershipDto](../schemas/m.md#mymembershipdto) | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## POST `/api/v1/driver/membership/checkout`

**What it does:** Start the applicable payment checkout; checkout creation is not settlement in the driver → membership → checkout workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required; declared roles: Driver.

**Body:** [MembershipCheckoutRequest](../schemas/m.md#membershipcheckoutrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [MembershipCheckoutDto](../schemas/m.md#membershipcheckoutdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. The server can require recent authentication; local app unlock is not proof.

## POST `/api/v1/driver/membership/pending-change/cancel`

**What it does:** Cancel the selected pending or active workflow where permitted in the driver → membership → pending change → cancel workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required; declared roles: Driver.

**Body:** [CancelPendingMembershipChangeRequest](../schemas/c.md#cancelpendingmembershipchangerequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [MyMembershipDto](../schemas/m.md#mymembershipdto) | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit. The server can require recent authentication; local app unlock is not proof.

## GET `/api/v1/driver/membership/store-status`

**What it does:** Read the single authoritative driver membership workspace snapshot, including entitlement and billing/recovery state.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [MembershipStoreStatusDto](../schemas/m.md#membershipstorestatusdto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/membership/plans`

**What it does:** Read the permitted records/state for membership → plans. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Driver.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [MembershipPlanDto](../schemas/m.md#membershipplandto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/rental-partner/membership/plans`

**What it does:** Read the permitted records/state for rental partner → membership → plans. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [MembershipPlanDto](../schemas/m.md#membershipplandto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/store-billing/operations/{operationId}`

**What it does:** Read the permitted records/state for store billing → operations. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `operationId` | path | Yes | `string (uuid)` | Durable operation reference used for applicable outcome discovery. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [StorePurchaseOperationDto](../schemas/s.md#storepurchaseoperationdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/store-billing/prepare`

**What it does:** Persist the applicable purchase preparation before native checkout; preparation does not grant entitlement.

**Access:** Bearer required.

**Body:** [PrepareStorePurchaseDto](../schemas/p.md#preparestorepurchasedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [StorePurchasePreparationDto](../schemas/s.md#storepurchasepreparationdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/store-billing/products`

**What it does:** Read the reviewed platform/audience product mapping for comparison with actual native localized offers.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `platform` | query | Yes | `string` | Platform selector in this contract; numeric enums and string selectors are not interchangeable. |
| `audience` | query | Conditional or optional | `string` | Applicable product/client audience, distinct from verified security authority. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [StoreProductDto](../schemas/s.md#storeproductdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/store-billing/quote`

**What it does:** Validate the exact mapped plan and native offer and create the applicable server-owned purchase quote.

**Access:** Bearer required.

**Body:** [CreateStorePurchaseQuoteDto](../schemas/c.md#createstorepurchasequotedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [StorePurchaseQuoteDto](../schemas/s.md#storepurchasequotedto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/store-billing/restore`

**What it does:** Reconcile eligible existing store purchases with the authenticated account; restoration is not a new sale.

**Access:** Bearer required.

**Body:** [VerifyStorePurchaseDto](../schemas/v.md#verifystorepurchasedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [StoreEntitlementDto](../schemas/s.md#storeentitlementdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/store-billing/verify`

**What it does:** Validate store transaction evidence on the server and reconcile/grant the mapped entitlement once.

**Access:** Bearer required.

**Body:** [VerifyStorePurchaseDto](../schemas/v.md#verifystorepurchasedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [StoreEntitlementDto](../schemas/s.md#storeentitlementdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.
