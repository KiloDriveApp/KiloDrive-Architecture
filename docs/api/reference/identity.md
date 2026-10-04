# Identity, account and installation lifecycle

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## DELETE `/api/v1/account`

**What it does:** Remove, archive or deactivate the selected record for account. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [DeleteAccountDto](../schemas/d.md#deleteaccountdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/account/activity`

**What it does:** Read the permitted records/state for account → activity. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `page` | query | Conditional or optional | `integer (int32)` | Page-number context for this endpoint; not a universal zero-based offset. |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. |
| `preset` | query | Conditional or optional | `string` | Named range/filter preset accepted by this endpoint; explicit date bounds have separate semantics. |
| `timezone` | query | Conditional or optional | `string` | Timezone context used by this contract; apply documented IANA/display semantics. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [UserActivityDtoPagedResult](../schemas/u.md#useractivitydtopagedresult) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/account/activity/settings`

**What it does:** Submit/create the documented record or action for account → activity → settings. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [RecordUserSettingChangeDto](../schemas/r.md#recordusersettingchangedto); required; media types: `application/json`, `text/json`, `application/*+json`.

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

## GET `/api/v1/account/avatar`

**What it does:** Read the permitted records/state for account → avatar. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/account/avatar`

**What it does:** Submit/create the documented record or action for account → avatar. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [SetAvatarDto](../schemas/s.md#setavatardto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## PUT `/api/v1/account/complete-profile`

**What it does:** Update the permitted configuration/record for account → complete profile. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [CompleteProfileDto](../schemas/c.md#completeprofiledto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/account/contact-details`

**What it does:** Read the permitted records/state for account → contact details. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ContactDetailsDto](../schemas/c.md#contactdetailsdto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## PUT `/api/v1/account/contact-details`

**What it does:** Update the permitted configuration/record for account → contact details. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [UpdateContactDetailsDto](../schemas/u.md#updatecontactdetailsdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ContactDetailsDto](../schemas/c.md#contactdetailsdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/account/contact-details/email/confirm`

**What it does:** Confirm the submitted evidence or pending decision in the account → contact details → email → confirm workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [ConfirmEmailVerificationDto](../schemas/c.md#confirmemailverificationdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/account/contact-details/email/request-code`

**What it does:** Request delivery of the applicable verification challenge in the account → contact details → email → request code workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ContactVerificationChallengeDto](../schemas/c.md#contactverificationchallengedto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/account/contact-details/phone/confirm`

**What it does:** Confirm the submitted evidence or pending decision in the account → contact details → phone → confirm workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [ConfirmPhoneContactVerificationDto](../schemas/c.md#confirmphonecontactverificationdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/account/contact-details/phone/request-code`

**What it does:** Request delivery of the applicable verification challenge in the account → contact details → phone → request code workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [RequestPhoneContactVerificationDto](../schemas/r.md#requestphonecontactverificationdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ContactVerificationChallengeDto](../schemas/c.md#contactverificationchallengedto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/account/deactivate`

**What it does:** Submit/create the documented record or action for account → deactivate. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/account/deactivate/recoverable`

**What it does:** Submit/create the documented record or action for account → deactivate → recoverable. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes.

## POST `/api/v1/account/deletion-request`

**What it does:** Submit/create the documented record or action for account → deletion request. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [RequestAccountDeletionDto](../schemas/r.md#requestaccountdeletiondto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

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

## GET `/api/v1/account/export`

**What it does:** Read the permitted records/state for account → export. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/account/identity-verification`

**What it does:** Read the permitted records/state for account → identity verification. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [IdentityVerificationDto](../schemas/i.md#identityverificationdto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/account/identity-verification`

**What it does:** Submit/create the documented record or action for account → identity verification. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [SubmitIdentityVerificationDto](../schemas/s.md#submitidentityverificationdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [IdentityVerificationDto](../schemas/i.md#identityverificationdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/account/identity-verification/operations/outcome`

**What it does:** Read the permitted records/state for account → identity verification → operations → outcome. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [IdentitySubmissionOutcomeDto](../schemas/i.md#identitysubmissionoutcomedto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/account/identity-verification/recoverable`

**What it does:** Submit/create the documented record or action for account → identity verification → recoverable. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [SubmitIdentityVerificationDto](../schemas/s.md#submitidentityverificationdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [IdentityVerificationDto](../schemas/i.md#identityverificationdto) | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/account/name-change-request`

**What it does:** Submit/create the documented record or action for account → name change request. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [RequestNameChangeDto](../schemas/r.md#requestnamechangedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [NameChangeRequestDto](../schemas/n.md#namechangerequestdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/account/onboarding/contact-proof`

**What it does:** Submit proof of the applicable contact ceremony in the account → onboarding → contact proof workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [TwoFactorStepUpDto](../schemas/t.md#twofactorstepupdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. The server can require recent authentication; local app unlock is not proof.

## POST `/api/v1/account/onboarding/phone-decision`

**What it does:** Submit/create the documented record or action for account → onboarding → phone decision. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [SetRiderPhoneOnboardingDecisionDto](../schemas/s.md#setriderphoneonboardingdecisiondto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RiderOnboardingDecisionDto](../schemas/r.md#rideronboardingdecisiondto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/account/onboarding/profile-photo-decision`

**What it does:** Submit/create the documented record or action for account → onboarding → profile photo decision. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [SetRiderProfilePhotoOnboardingDecisionDto](../schemas/s.md#setriderprofilephotoonboardingdecisiondto); required; media types: `application/json`, `text/json`, `application/*+json`.

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

## DELETE `/api/v1/account/recoverable`

**What it does:** Remove, archive or deactivate the selected record for account → recoverable. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [DeleteAccountDto](../schemas/d.md#deleteaccountdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

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

## GET `/api/v1/account/referrals`

**What it does:** Read the permitted records/state for account → referrals. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ReferralSummaryDto](../schemas/r.md#referralsummarydto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/account/reputation`

**What it does:** Read the permitted records/state for account → reputation. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [UserReputationDto](../schemas/u.md#userreputationdto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/account/security-events`

**What it does:** Read the permitted records/state for account → security events. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `take` | query | Conditional or optional | `integer (int32)` | Numeric take for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [UserSecurityEventDto](../schemas/u.md#usersecurityeventdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/account/security-preferences`

**What it does:** Read the permitted records/state for account → security preferences. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SecurityPreferencesDto](../schemas/s.md#securitypreferencesdto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## PUT `/api/v1/account/security-preferences/login-email-alerts`

**What it does:** Update the permitted configuration/record for account → security preferences → login email alerts. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [SetLoginEmailNotificationsDto](../schemas/s.md#setloginemailnotificationsdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SecurityPreferencesDto](../schemas/s.md#securitypreferencesdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/account/setup-progress`

**What it does:** Read the permitted records/state for account → setup progress. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [AccountSetupProgressDto](../schemas/a.md#accountsetupprogressdto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/2fa/confirm`

**What it does:** Confirm the submitted evidence or pending decision in the auth → 2fa → confirm workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [TwoFactorCodeRequest](../schemas/t.md#twofactorcoderequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [TwoFactorConfirmedDto](../schemas/t.md#twofactorconfirmeddto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/2fa/disable`

**What it does:** Disable the selected security method or setting through its protected ceremony in the auth → 2fa → disable workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [TwoFactorCodeRequest](../schemas/t.md#twofactorcoderequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [TwoFactorStatusDto](../schemas/t.md#twofactorstatusdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/2fa/enroll`

**What it does:** Start enrollment in the applicable security method in the auth → 2fa → enroll workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [TwoFactorEnrollmentDto](../schemas/t.md#twofactorenrollmentdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** The server can require recent authentication; local app unlock is not proof.

## POST `/api/v1/auth/2fa/enroll/contact/confirm`

**What it does:** Confirm the submitted evidence or pending decision in the auth → 2fa → enroll → contact → confirm workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [ConfirmContactTwoFactorEnrollmentRequest](../schemas/c.md#confirmcontacttwofactorenrollmentrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [TwoFactorConfirmedDto](../schemas/t.md#twofactorconfirmeddto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/2fa/enroll/contact/request-code`

**What it does:** Request delivery of the applicable verification challenge in the auth → 2fa → enroll → contact → request code workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [BeginContactTwoFactorEnrollmentRequest](../schemas/b.md#begincontacttwofactorenrollmentrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ContactTwoFactorEnrollmentDto](../schemas/c.md#contacttwofactorenrollmentdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** The server can require recent authentication; local app unlock is not proof.

## POST `/api/v1/auth/2fa/recovery-codes/regenerate`

**What it does:** Replace the applicable recovery material through the protected workflow in the auth → 2fa → recovery codes → regenerate workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [TwoFactorConfirmedDto](../schemas/t.md#twofactorconfirmeddto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/auth/2fa/status`

**What it does:** Read the permitted records/state for auth → 2fa → status. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [TwoFactorStatusDto](../schemas/t.md#twofactorstatusdto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/2fa/step-up`

**What it does:** Complete the additional server authentication ceremony in the auth → 2fa → step up workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [CreateTwoFactorStepUpDto](../schemas/c.md#createtwofactorstepupdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [TwoFactorStepUpDto](../schemas/t.md#twofactorstepupdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/2fa/step-up/request-code`

**What it does:** Request delivery of the applicable verification challenge in the auth → 2fa → step up → request code workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [RequestOutOfBandStepUpDto](../schemas/r.md#requestoutofbandstepupdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [OutOfBandStepUpChallengeDto](../schemas/o.md#outofbandstepupchallengedto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/auth/change-password`

**What it does:** Submit/create the documented record or action for auth → change password. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [SetPasswordRequest](../schemas/s.md#setpasswordrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** The server can require recent authentication; local app unlock is not proof.

## POST `/api/v1/auth/login`

**What it does:** Authenticate an identifier and password; return either the next security step or the final authenticated session.

**Access:** Anonymous bearer metadata.

**Body:** [LoginRequest](../schemas/l.md#loginrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [LoginResultDto](../schemas/l.md#loginresultdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/login/2fa`

**What it does:** Submit/create the documented record or action for auth → login → 2fa. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

**Body:** [VerifyTwoFactorLoginRequest](../schemas/v.md#verifytwofactorloginrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [LoginResultDto](../schemas/l.md#loginresultdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/login/2fa/passkey/begin`

**What it does:** Begin the applicable secure ceremony in the auth → login → 2fa → passkey → begin workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Anonymous bearer metadata.

**Body:** [PasskeyLoginBeginRequest](../schemas/p.md#passkeyloginbeginrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [PasskeyCeremonyDto](../schemas/p.md#passkeyceremonydto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/login/2fa/passkey/complete`

**What it does:** Complete the selected workflow after its required state/evidence checks in the auth → login → 2fa → passkey → complete workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Anonymous bearer metadata.

**Body:** [PasskeyLoginCompleteRequest](../schemas/p.md#passkeylogincompleterequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [LoginResultDto](../schemas/l.md#loginresultdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/login/2fa/request-code`

**What it does:** Request delivery of the applicable verification challenge in the auth → login → 2fa → request code workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Anonymous bearer metadata.

**Body:** [RequestTwoFactorLoginCodeRequest](../schemas/r.md#requesttwofactorlogincoderequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ContactTwoFactorEnrollmentDto](../schemas/c.md#contacttwofactorenrollmentdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/login/email/confirm`

**What it does:** Confirm the submitted evidence or pending decision in the auth → login → email → confirm workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Anonymous bearer metadata.

**Body:** [ConfirmEmailLoginDto](../schemas/c.md#confirmemaillogindto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [LoginResultDto](../schemas/l.md#loginresultdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/login/email/request`

**What it does:** Start the applicable request/challenge workflow in the auth → login → email → request workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Anonymous bearer metadata.

**Body:** [RequestEmailLoginDto](../schemas/r.md#requestemaillogindto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/login/phone/confirm`

**What it does:** Confirm the submitted evidence or pending decision in the auth → login → phone → confirm workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Anonymous bearer metadata.

**Body:** [ConfirmPhoneLoginDto](../schemas/c.md#confirmphonelogindto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [LoginResultDto](../schemas/l.md#loginresultdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/login/phone/request`

**What it does:** Start the applicable request/challenge workflow in the auth → login → phone → request workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Anonymous bearer metadata.

**Body:** [RequestPhoneLoginDto](../schemas/r.md#requestphonelogindto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/logout`

**What it does:** End the applicable authenticated session through the server logout workflow.

**Access:** Anonymous bearer metadata.

**Body:** [RefreshRequest](../schemas/r.md#refreshrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/auth/me`

**What it does:** Read the authenticated identity's user model.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [UserDto](../schemas/u.md#userdto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/auth/passkeys`

**What it does:** Read the permitted records/state for auth → passkeys. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [PasskeyDto](../schemas/p.md#passkeydto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/passkeys/register/begin`

**What it does:** Begin the applicable secure ceremony in the auth → passkeys → register → begin workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [PasskeyCeremonyDto](../schemas/p.md#passkeyceremonydto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** The server can require recent authentication; local app unlock is not proof.

## POST `/api/v1/auth/passkeys/register/complete`

**What it does:** Complete the selected workflow after its required state/evidence checks in the auth → passkeys → register → complete workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [PasskeyRegisterCompleteRequest](../schemas/p.md#passkeyregistercompleterequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [PasskeyDto](../schemas/p.md#passkeydto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** The server can require recent authentication; local app unlock is not proof.

## DELETE `/api/v1/auth/passkeys/{id}`

**What it does:** Remove, archive or deactivate the selected record for auth → passkeys. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `id` | path | Yes | `string (uuid)` | Opaque identifier of this model's record; knowing it does not grant access. |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

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

**Mutation handling:** The server can require recent authentication; local app unlock is not proof.

## POST `/api/v1/auth/password-reset/confirm`

**What it does:** Confirm valid reset evidence and set the new password through the established identity workflow.

**Access:** Anonymous bearer metadata.

**Body:** [ConfirmPasswordResetRequest](../schemas/c.md#confirmpasswordresetrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/password-reset/request`

**What it does:** Request the secure password-reset ceremony; the response must not expose a password or account-existence proof.

**Access:** Anonymous bearer metadata.

**Body:** [RequestPasswordResetRequest](../schemas/r.md#requestpasswordresetrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/password-strength`

**What it does:** Submit/create the documented record or action for auth → password strength. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Anonymous bearer metadata.

**Body:** [PasswordStrengthRequest](../schemas/p.md#passwordstrengthrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [PasswordStrengthDto](../schemas/p.md#passwordstrengthdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/phone-verification/confirm`

**What it does:** Confirm the submitted evidence or pending decision in the auth → phone verification → confirm workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [ConfirmPhoneVerificationRequest](../schemas/c.md#confirmphoneverificationrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/phone-verification/request`

**What it does:** Start the applicable request/challenge workflow in the auth → phone verification → request workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `deliveryMethod` | query | Conditional or optional | `string` | Delivery method text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/recent-authentication`

**What it does:** Obtain server-validated recent account proof for consequential operations that require it.

**Access:** Bearer required.

**Body:** [CreateRecentAuthenticationProofRequest](../schemas/c.md#createrecentauthenticationproofrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [RecentAuthenticationProofDto](../schemas/r.md#recentauthenticationproofdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/refresh`

**What it does:** Rotate an eligible refresh credential and obtain the current session; installation and session-family checks still apply.

**Access:** Anonymous bearer metadata.

**Body:** [RefreshRequest](../schemas/r.md#refreshrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [AuthResponse](../schemas/a.md#authresponse) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/register`

**What it does:** Create a consumer account and begin its country/contact/onboarding journey; this does not grant administrator authority.

**Access:** Anonymous bearer metadata.

**Body:** [RegisterRequest](../schemas/r.md#registerrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [AuthResponse](../schemas/a.md#authresponse) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/auth/session`

**What it does:** Read the current session's authoritative account/security state before resuming protected work.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 204 | No typed schema recorded | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/auth/sessions`

**What it does:** Read the permitted records/state for auth → sessions. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-Refresh-Token` | header | Conditional or optional | `string` | Private x refresh token used by this specific ceremony; never log, publish or substitute it for another proof. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SessionDto](../schemas/s.md#sessiondto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## DELETE `/api/v1/auth/sessions/{id}`

**What it does:** Remove, archive or deactivate the selected record for auth → sessions. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `id` | path | Yes | `string (uuid)` | Opaque identifier of this model's record; knowing it does not grant access. |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

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

**Mutation handling:** The server can require recent authentication; local app unlock is not proof.

## POST `/api/v1/auth/set-password`

**What it does:** Submit/create the documented record or action for auth → set password. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [SetPasswordRequest](../schemas/s.md#setpasswordrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

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

## POST `/api/v1/auth/social`

**What it does:** Validate provider sign-in evidence and return a session or the protected pending-link/verification ceremony.

**Access:** Anonymous bearer metadata.

**Body:** [SocialLoginRequest](../schemas/s.md#socialloginrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [LoginResultDto](../schemas/l.md#loginresultdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/auth/social-connections`

**What it does:** Read the permitted records/state for auth → social connections. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SocialLoginConnectionDto](../schemas/s.md#socialloginconnectiondto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/social-connections`

**What it does:** Submit/create the documented record or action for auth → social connections. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [LinkSocialLoginConnectionRequest](../schemas/l.md#linksocialloginconnectionrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SocialLoginConnectionDto](../schemas/s.md#socialloginconnectiondto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** The server can require recent authentication; local app unlock is not proof.

## DELETE `/api/v1/auth/social-connections/{id}`

**What it does:** Remove, archive or deactivate the selected record for auth → social connections. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `id` | path | Yes | `string (uuid)` | Opaque identifier of this model's record; knowing it does not grant access. |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

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

**Mutation handling:** The server can require recent authentication; local app unlock is not proof.

## POST `/api/v1/auth/social-link-intents/cancel`

**What it does:** Cancel the selected pending or active workflow where permitted in the auth → social link intents → cancel workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Anonymous bearer metadata.

**Body:** [PendingSocialLinkTokenRequest](../schemas/p.md#pendingsociallinktokenrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | No typed schema recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/auth/social-link-intents/confirm`

**What it does:** Confirm the submitted evidence or pending decision in the auth → social link intents → confirm workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [ConfirmPendingSocialLinkRequest](../schemas/c.md#confirmpendingsociallinkrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `X-KiloDrive-Recent-Authentication` | header | Conditional or optional | `string` | Private recent account proof when required by the server; local biometric/PIN unlock is insufficient. |
| `X-KiloDrive-Step-Up` | header | Conditional or optional | `string` | X kilo drive step up text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SocialLoginConnectionDto](../schemas/s.md#socialloginconnectiondto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** The server can require recent authentication; local app unlock is not proof.

## POST `/api/v1/auth/social-link-intents/review`

**What it does:** Submit/create the documented record or action for auth → social link intents → review. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [PendingSocialLinkTokenRequest](../schemas/p.md#pendingsociallinktokenrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [PendingSocialLinkDto](../schemas/p.md#pendingsociallinkdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/devices/heartbeat`

**What it does:** Update the current installation's reported metadata and return access state.

**Access:** Anonymous bearer metadata.

**Body:** [DeviceMetadataDto](../schemas/d.md#devicemetadatadto); requiredness not asserted in metadata; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [DeviceAccessStatusDto](../schemas/d.md#deviceaccessstatusdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/devices/register`

**What it does:** Register/admit an installation and return its private credential and access state; anonymous bearer metadata does not bypass app admission.

**Access:** Anonymous bearer metadata.

**Body:** [RegisterDeviceDto](../schemas/r.md#registerdevicedto); requiredness not asserted in metadata; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [DeviceRegistrationDto](../schemas/d.md#deviceregistrationdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/devices/status`

**What it does:** Read the current installation's allowed/restricted access state.

**Access:** Anonymous bearer metadata.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [DeviceAccessStatusDto](../schemas/d.md#deviceaccessstatusdto) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
