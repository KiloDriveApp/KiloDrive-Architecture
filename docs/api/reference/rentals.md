# Rental bookings and organization workflows

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## GET `/api/v1/rental-partner/organizations`

**What it does:** Read the permitted records/state for rental partner → organizations. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalOrganizationDto](../schemas/r.md#rentalorganizationdto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/rental-partner/organizations`

**What it does:** Submit/create the documented record or action for rental partner → organizations. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [CreateRentalOrganizationDto](../schemas/c.md#createrentalorganizationdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalOrganizationDto](../schemas/r.md#rentalorganizationdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## DELETE `/api/v1/rental-partner/organizations/{organizationId}`

**What it does:** Remove, archive or deactivate the selected record for rental partner → organizations. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## PUT `/api/v1/rental-partner/organizations/{organizationId}`

**What it does:** Update the permitted configuration/record for rental partner → organizations. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [UpdateRentalOrganizationSettingsDto](../schemas/u.md#updaterentalorganizationsettingsdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalOrganizationDto](../schemas/r.md#rentalorganizationdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rental-partner/organizations/{organizationId}/analytics`

**What it does:** Read the permitted records/state for rental partner → organizations → analytics. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `from` | query | Yes | `string (date-time)` | From text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `to` | query | Yes | `string (date-time)` | To text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalOwnerAnalyticsDto](../schemas/r.md#rentalowneranalyticsdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/rental-partner/organizations/{organizationId}/availability-blocks`

**What it does:** Submit/create the documented record or action for rental partner → organizations → availability blocks. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [CreateRentalAvailabilityBlockDto](../schemas/c.md#createrentalavailabilityblockdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalAvailabilityBlockDto](../schemas/r.md#rentalavailabilityblockdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## DELETE `/api/v1/rental-partner/organizations/{organizationId}/availability-blocks/{blockId}`

**What it does:** Remove, archive or deactivate the selected record for rental partner → organizations → availability blocks. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `blockId` | path | Yes | `string (uuid)` | Identifier of the related block record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rental-partner/organizations/{organizationId}/billing`

**What it does:** Read the permitted records/state for rental partner → organizations → billing. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ProviderBillingDto](../schemas/p.md#providerbillingdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/rental-partner/organizations/{organizationId}/billing/membership`

**What it does:** Submit/create the documented record or action for rental partner → organizations → billing → membership. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [RentalMembershipPurchaseDto](../schemas/r.md#rentalmembershippurchasedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ProviderBillingDto](../schemas/p.md#providerbillingdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## PUT `/api/v1/rental-partner/organizations/{organizationId}/billing/membership/auto-renew`

**What it does:** Update the permitted configuration/record for rental partner → organizations → billing → membership → auto renew. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [SetAutoRenewRequest](../schemas/s.md#setautorenewrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ProviderBillingDto](../schemas/p.md#providerbillingdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rental-partner/organizations/{organizationId}/billing/membership/checkout`

**What it does:** Start the applicable payment checkout; checkout creation is not settlement in the rental partner → organizations → billing → membership → checkout workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [MembershipCheckoutRequest](../schemas/m.md#membershipcheckoutrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [MembershipCheckoutDto](../schemas/m.md#membershipcheckoutdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## PUT `/api/v1/rental-partner/organizations/{organizationId}/billing/mode`

**What it does:** Update the permitted configuration/record for rental partner → organizations → billing → mode. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [BillingModeDto](../schemas/b.md#billingmodedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ProviderBillingDto](../schemas/p.md#providerbillingdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rental-partner/organizations/{organizationId}/bookings`

**What it does:** Read the permitted records/state for rental partner → organizations → bookings. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalPartnerBookingDto](../schemas/r.md#rentalpartnerbookingdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/agreement`

**What it does:** Submit/create the documented record or action for rental partner → organizations → bookings → agreement. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [IssueRentalAgreementDto](../schemas/i.md#issuerentalagreementdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalAgreementDto](../schemas/r.md#rentalagreementdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/agreement/sign`

**What it does:** Submit signature/acceptance evidence for the selected agreement in the rental partner → organizations → bookings → agreement → sign workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [SignRentalAgreementDto](../schemas/s.md#signrentalagreementdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalAgreementDto](../schemas/r.md#rentalagreementdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/damage-claims`

**What it does:** Submit/create the documented record or action for rental partner → organizations → bookings → damage claims. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [CreateRentalDamageClaimDto](../schemas/c.md#createrentaldamageclaimdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalDamageClaimDto](../schemas/r.md#rentaldamageclaimdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/deposit/settle`

**What it does:** Request the applicable settlement under the current financial state in the rental partner → organizations → bookings → deposit → settle workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [SettleRentalDepositDto](../schemas/s.md#settlerentaldepositdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/inspections`

**What it does:** Submit/create the documented record or action for rental partner → organizations → bookings → inspections. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [CreateRentalInspectionDto](../schemas/c.md#createrentalinspectiondto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalInspectionDto](../schemas/r.md#rentalinspectiondto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/late-return/assess`

**What it does:** Submit/create the documented record or action for rental partner → organizations → bookings → late return → assess. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [RentalExpectedVersionDto](../schemas/r.md#rentalexpectedversiondto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## PUT `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/status`

**What it does:** Update the permitted configuration/record for rental partner → organizations → bookings → status. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [UpdateRentalBookingStatusDto](../schemas/u.md#updaterentalbookingstatusdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rental-partner/organizations/{organizationId}/branches`

**What it does:** Read the permitted records/state for rental partner → organizations → branches. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalPartnerBranchDto](../schemas/r.md#rentalpartnerbranchdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/rental-partner/organizations/{organizationId}/branches`

**What it does:** Submit/create the documented record or action for rental partner → organizations → branches. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [CreateRentalBranchDto](../schemas/c.md#createrentalbranchdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## PUT `/api/v1/rental-partner/organizations/{organizationId}/extensions/{extensionId}`

**What it does:** Update the permitted configuration/record for rental partner → organizations → extensions. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [ReviewRentalExtensionDto](../schemas/r.md#reviewrentalextensiondto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `extensionId` | path | Yes | `string (uuid)` | Identifier of the related extension record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalExtensionDto](../schemas/r.md#rentalextensiondto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rental-partner/organizations/{organizationId}/fleet/reminders`

**What it does:** Read the permitted records/state for rental partner → organizations → fleet → reminders. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `from` | query | Conditional or optional | `string (date-time)` | From text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `to` | query | Conditional or optional | `string (date-time)` | To text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalFleetReminderDto](../schemas/r.md#rentalfleetreminderdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## PUT `/api/v1/rental-partner/organizations/{organizationId}/profile-image`

**What it does:** Update the permitted configuration/record for rental partner → organizations → profile image. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [UpdateRentalOrganizationProfileImageDto](../schemas/u.md#updaterentalorganizationprofileimagedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rental-partner/organizations/{organizationId}/team`

**What it does:** Read the permitted records/state for rental partner → organizations → team. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalTeamDto](../schemas/r.md#rentalteamdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/rental-partner/organizations/{organizationId}/team/invitations`

**What it does:** Submit/create the documented record or action for rental partner → organizations → team → invitations. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [InviteRentalTeamMemberDto](../schemas/i.md#inviterentalteammemberdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalTeamInvitationDto](../schemas/r.md#rentalteaminvitationdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## DELETE `/api/v1/rental-partner/organizations/{organizationId}/team/invitations/{invitationId}`

**What it does:** Remove, archive or deactivate the selected record for rental partner → organizations → team → invitations. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `invitationId` | path | Yes | `string (uuid)` | Identifier of the related invitation record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## PUT `/api/v1/rental-partner/organizations/{organizationId}/team/{userId}`

**What it does:** Update the permitted configuration/record for rental partner → organizations → team. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [UpdateRentalTeamMemberDto](../schemas/u.md#updaterentalteammemberdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `userId` | path | Yes | `string (uuid)` | Related account identity; the server still proves the caller's ownership or permitted relationship. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rental-partner/organizations/{organizationId}/vehicles`

**What it does:** Read the permitted records/state for rental partner → organizations → vehicles. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalPartnerVehicleDto](../schemas/r.md#rentalpartnervehicledto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/rental-partner/organizations/{organizationId}/vehicles`

**What it does:** Submit/create the documented record or action for rental partner → organizations → vehicles. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [CreateRentalVehicleDto](../schemas/c.md#createrentalvehicledto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## DELETE `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}`

**What it does:** Remove, archive or deactivate the selected record for rental partner → organizations → vehicles. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## PUT `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}`

**What it does:** Update the permitted configuration/record for rental partner → organizations → vehicles. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [UpdateRentalVehicleDto](../schemas/u.md#updaterentalvehicledto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/availability`

**What it does:** Read the permitted records/state for rental partner → organizations → vehicles → availability. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |
| `from` | query | Yes | `string (date-time)` | From text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `to` | query | Yes | `string (date-time)` | To text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalAvailabilityCalendarDto](../schemas/r.md#rentalavailabilitycalendardto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## DELETE `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/images/{imageId}`

**What it does:** Remove, archive or deactivate the selected record for rental partner → organizations → vehicles → images. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |
| `imageId` | path | Yes | `string (uuid)` | Identifier of the related image record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## PUT `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/images/{imageId}/primary`

**What it does:** Update the permitted configuration/record for rental partner → organizations → vehicles → images → primary. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |
| `imageId` | path | Yes | `string (uuid)` | Identifier of the related image record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## PUT `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/protection`

**What it does:** Update the permitted configuration/record for rental partner → organizations → vehicles → protection. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [SetRentalProviderProtectionDto](../schemas/s.md#setrentalproviderprotectiondto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rental-partner/team/invitations/accept`

**What it does:** Accept the selected offer/request in the rental partner → team → invitations → accept workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [AcceptRentalTeamInvitationDto](../schemas/a.md#acceptrentalteaminvitationdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/rental-partner/vehicles/{vehicleId}/images`

**What it does:** Submit/create the documented record or action for rental partner → vehicles → images. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [AddRentalVehicleImageDto](../schemas/a.md#addrentalvehicleimagedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rentals/booking-status-contract`

**What it does:** Read the permitted records/state for rentals → booking status contract. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalBookingStatusContractDto](../schemas/r.md#rentalbookingstatuscontractdto) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/rentals/bookings`

**What it does:** Submit/create the documented record or action for rentals → bookings. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [CreateRentalBookingDto](../schemas/c.md#createrentalbookingdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalBookingDto](../schemas/r.md#rentalbookingdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/rentals/bookings/mine`

**What it does:** Read the permitted records/state for rentals → bookings → mine. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalBookingDto](../schemas/r.md#rentalbookingdto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/rentals/bookings/{bookingId}/agreement/sign`

**What it does:** Submit signature/acceptance evidence for the selected agreement in the rentals → bookings → agreement → sign workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [SignRentalAgreementDto](../schemas/s.md#signrentalagreementdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalAgreementDto](../schemas/r.md#rentalagreementdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rentals/bookings/{bookingId}/cancel`

**What it does:** Cancel the selected pending or active workflow where permitted in the rentals → bookings → cancel workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [CancelRentalBookingDto](../schemas/c.md#cancelrentalbookingdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rentals/bookings/{bookingId}/checkout`

**What it does:** Start the applicable payment checkout; checkout creation is not settlement in the rentals → bookings → checkout workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [CreateRentalCheckoutDto](../schemas/c.md#createrentalcheckoutdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalCheckoutDto](../schemas/r.md#rentalcheckoutdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rentals/bookings/{bookingId}/damage-evidence/{evidenceId}`

**What it does:** Read the permitted records/state for rentals → bookings → damage evidence. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `evidenceId` | path | Yes | `string (uuid)` | Identifier of the related evidence record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/rentals/bookings/{bookingId}/dispute-evidence/{evidenceId}`

**What it does:** Read the permitted records/state for rentals → bookings → dispute evidence. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `evidenceId` | path | Yes | `string (uuid)` | Identifier of the related evidence record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/rentals/bookings/{bookingId}/disputes`

**What it does:** Submit/create the documented record or action for rentals → bookings → disputes. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [OpenRentalDisputeDto](../schemas/o.md#openrentaldisputedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalDisputeDto](../schemas/r.md#rentaldisputedto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rentals/bookings/{bookingId}/extensions`

**What it does:** Submit/create the documented record or action for rentals → bookings → extensions. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [RequestRentalExtensionDto](../schemas/r.md#requestrentalextensiondto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalExtensionDto](../schemas/r.md#rentalextensiondto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/rentals/bookings/{bookingId}/extensions/{extensionId}/checkout`

**What it does:** Start the applicable payment checkout; checkout creation is not settlement in the rentals → bookings → extensions → checkout workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required; declared roles: Passenger.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `extensionId` | path | Yes | `string (uuid)` | Identifier of the related extension record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalCheckoutDto](../schemas/r.md#rentalcheckoutdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rentals/bookings/{bookingId}/inspection-evidence/{evidenceId}`

**What it does:** Read the permitted records/state for rentals → bookings → inspection evidence. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `evidenceId` | path | Yes | `string (uuid)` | Identifier of the related evidence record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/rentals/bookings/{bookingId}/operations`

**What it does:** Read the permitted records/state for rentals → bookings → operations. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalBookingOperationsDto](../schemas/r.md#rentalbookingoperationsdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/rentals/bookings/{bookingId}/payment-authorized`

**What it does:** Submit/create the documented record or action for rentals → bookings → payment authorized. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [AuthorizeRentalBookingPaymentDto](../schemas/a.md#authorizerentalbookingpaymentdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalBookingDto](../schemas/r.md#rentalbookingdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## GET `/api/v1/rentals/bookings/{bookingId}/protection`

**What it does:** Read the permitted records/state for rentals → bookings → protection. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalProviderProtectionDto](../schemas/r.md#rentalproviderprotectiondto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/rentals/bookings/{bookingId}/rating`

**What it does:** Submit the caller's permitted rating for the selected completed service in the rentals → bookings → rating workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required; declared roles: Passenger.

**Body:** [CreateRentalRatingDto](../schemas/c.md#createrentalratingdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `bookingId` | path | Yes | `string (uuid)` | Identifier of the related booking record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## DELETE `/api/v1/rentals/favorites/{vehicleId}`

**What it does:** Remove, archive or deactivate the selected record for rentals → favorites. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## PUT `/api/v1/rentals/favorites/{vehicleId}`

**What it does:** Update the permitted configuration/record for rentals → favorites. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/rentals/filters`

**What it does:** Read the permitted records/state for rentals → filters. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalMarketplaceFiltersDto](../schemas/r.md#rentalmarketplacefiltersdto) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/rentals/organizations`

**What it does:** Read the permitted records/state for rentals → organizations. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Search` | query | Conditional or optional | `string` | Search text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `Page` | query | Conditional or optional | `integer (int32)` | Numeric page for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |
| `PageSize` | query | Conditional or optional | `integer (int32)` | Numeric page size for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalOrganizationCardDtoPagedResult](../schemas/r.md#rentalorganizationcarddtopagedresult) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/rentals/organizations/{organizationId}`

**What it does:** Read the permitted records/state for rentals → organizations. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalOrganizationPublicDto](../schemas/r.md#rentalorganizationpublicdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/rentals/organizations/{organizationId}/profile-image`

**What it does:** Read the permitted records/state for rentals → organizations → profile image. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `organizationId` | path | Yes | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/rentals/vehicles`

**What it does:** Read the permitted records/state for rentals → vehicles. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Category` | query | Conditional or optional | `string` | Category text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `PickupAt` | query | Conditional or optional | `string (date-time)` | Pickup at text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `ReturnAt` | query | Conditional or optional | `string (date-time)` | Return at text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `Latitude` | query | Conditional or optional | `number (double)` | Numeric latitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |
| `Longitude` | query | Conditional or optional | `number (double)` | Numeric longitude for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |
| `Page` | query | Conditional or optional | `integer (int32)` | Numeric page for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |
| `PageSize` | query | Conditional or optional | `integer (int32)` | Numeric page size for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |
| `Search` | query | Conditional or optional | `string` | Search text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `OrganizationId` | query | Conditional or optional | `string (uuid)` | Identifier of the related organization record in this model; ownership and scope are checked separately. |
| `Make` | query | Conditional or optional | `string` | Make text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `Model` | query | Conditional or optional | `string` | Model text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `MinYear` | query | Conditional or optional | `integer (int32)` | Numeric min year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |
| `MaxYear` | query | Conditional or optional | `integer (int32)` | Numeric max year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |
| `VehicleType` | query | Conditional or optional | `string` | Vehicle type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `Transmission` | query | Conditional or optional | `string` | Transmission text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `MinimumSeats` | query | Conditional or optional | `integer (int32)` | Numeric minimum seats for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |
| `BookingMode` | query | Conditional or optional | `RentalBookingMode` | Booking mode represented by the `RentalBookingMode` model or enum; use that definition's fields/values. |
| `Sort` | query | Conditional or optional | `string` | Sort text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `RadiusKilometers` | query | Conditional or optional | `number (double)` | Numeric radius kilometers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalVehicleCardDtoPagedResult](../schemas/r.md#rentalvehiclecarddtopagedresult) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/rentals/vehicles/{vehicleId}`

**What it does:** Read the permitted records/state for rentals → vehicles. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalVehicleDetailDto](../schemas/r.md#rentalvehicledetaildto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/rentals/vehicles/{vehicleId}/availability`

**What it does:** Read the permitted records/state for rentals → vehicles → availability. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |
| `from` | query | Yes | `string (date-time)` | From text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `to` | query | Yes | `string (date-time)` | To text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalAvailabilityCalendarDto](../schemas/r.md#rentalavailabilitycalendardto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/rentals/vehicles/{vehicleId}/images/{imageId}`

**What it does:** Read the permitted records/state for rentals → vehicles → images. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |
| `imageId` | path | Yes | `string (uuid)` | Identifier of the related image record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/rentals/vehicles/{vehicleId}/protection`

**What it does:** Read the permitted records/state for rentals → vehicles → protection. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |
| `pickupAt` | query | Yes | `string (date-time)` | Pickup at text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `returnAt` | query | Yes | `string (date-time)` | Return at text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalProviderProtectionDto](../schemas/r.md#rentalproviderprotectiondto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/rentals/vehicles/{vehicleId}/quote`

**What it does:** Read the permitted records/state for rentals → vehicles → quote. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `vehicleId` | path | Yes | `string (uuid)` | Account vehicle record associated with this operation or result. |
| `PickupAt` | query | Conditional or optional | `string (date-time)` | Pickup at text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `ReturnAt` | query | Conditional or optional | `string (date-time)` | Return at text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `HandoverMode` | query | Conditional or optional | `RentalVehicleHandoverMode` | Handover mode represented by the `RentalVehicleHandoverMode` model or enum; use that definition's fields/values. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RentalQuoteDto](../schemas/r.md#rentalquotedto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
