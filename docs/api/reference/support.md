# Support tickets and review appeals

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## POST `/api/v1/reviews/{kind}/{reviewId}/appeals`

**What it does:** Submit/create the documented record or action for reviews → appeals. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [CreateReviewAppealDto](../schemas/c.md#createreviewappealdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `kind` | path | Yes | `ReviewAggregateKind` | Kind represented by the `ReviewAggregateKind` model or enum; use that definition's fields/values. |
| `reviewId` | path | Yes | `string (uuid)` | Identifier of the related review record in this model; ownership and scope are checked separately. |
| `If-Match` | header | Yes | `integer (int64)` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [ReviewAppealDto](../schemas/r.md#reviewappealdto) | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/support/tickets`

**What it does:** Read the permitted records/state for support → tickets. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `status` | query | Conditional or optional | `SupportTicketStatus` | Current domain status; use this model's enum or documented string vocabulary. |
| `issueType` | query | Conditional or optional | `string` | Issue type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `subjectType` | query | Conditional or optional | `string` | Subject type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `subjectEntityId` | query | Conditional or optional | `string (uuid)` | Identifier of the related subject entity record in this model; ownership and scope are checked separately. |
| `createdFromUtc` | query | Conditional or optional | `string (date-time)` | UTC instant for created from; parse strictly and localize only for display. |
| `createdToUtc` | query | Conditional or optional | `string (date-time)` | UTC instant for created to; parse strictly and localize only for display. |
| `slaState` | query | Conditional or optional | `string` | Sla state text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |
| `page` | query | Conditional or optional | `integer (int32)` | Page-number context for this endpoint; not a universal zero-based offset. |
| `pageSize` | query | Conditional or optional | `integer (int32)` | Requested or returned page size, subject to this endpoint's server bounds. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SupportTicketDtoPagedResult](../schemas/s.md#supportticketdtopagedresult) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/support/tickets`

**What it does:** Submit/create the documented record or action for support → tickets. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [CreateSupportTicketDto](../schemas/c.md#createsupportticketdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SupportTicketDto](../schemas/s.md#supportticketdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## GET `/api/v1/support/tickets/catalog`

**What it does:** Read the permitted records/state for support → tickets → catalog. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `subjectType` | query | Conditional or optional | `string` | Subject type text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SupportCaseCatalogDto](../schemas/s.md#supportcasecatalogdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/support/tickets/operations/outcome`

**What it does:** Read the permitted records/state for support → tickets → operations → outcome. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SupportCommandOutcomeDto](../schemas/s.md#supportcommandoutcomedto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/support/tickets/{ticketId}`

**What it does:** Read the permitted records/state for support → tickets. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `ticketId` | path | Yes | `string (uuid)` | Identifier of the related ticket record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SupportTicketDetailsDto](../schemas/s.md#supportticketdetailsdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/support/tickets/{ticketId}/close`

**What it does:** Close the selected workflow where permitted in the support → tickets → close workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [CloseSupportCaseDto](../schemas/c.md#closesupportcasedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `ticketId` | path | Yes | `string (uuid)` | Identifier of the related ticket record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SupportTicketDto](../schemas/s.md#supportticketdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/support/tickets/{ticketId}/close/recoverable`

**What it does:** Submit/create the documented record or action for support → tickets → close → recoverable. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [CloseSupportCaseDto](../schemas/c.md#closesupportcasedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `ticketId` | path | Yes | `string (uuid)` | Identifier of the related ticket record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SupportTicketDto](../schemas/s.md#supportticketdto) | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## GET `/api/v1/support/tickets/{ticketId}/messages/{messageId}/attachments/{index}`

**What it does:** Read the permitted records/state for support → tickets → messages → attachments. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `ticketId` | path | Yes | `string (uuid)` | Identifier of the related ticket record in this model; ownership and scope are checked separately. |
| `messageId` | path | Yes | `string (uuid)` | Identifier of the related message record in this model; ownership and scope are checked separately. |
| `index` | path | Yes | `integer (int32)` | Numeric index for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. |

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

## PUT `/api/v1/support/tickets/{ticketId}/read`

**What it does:** Update the permitted configuration/record for support → tickets → read. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `ticketId` | path | Yes | `string (uuid)` | Identifier of the related ticket record in this model; ownership and scope are checked separately. |

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

## POST `/api/v1/support/tickets/{ticketId}/reopen`

**What it does:** Reopen the selected workflow where permitted in the support → tickets → reopen workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [ReopenSupportCaseDto](../schemas/r.md#reopensupportcasedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `ticketId` | path | Yes | `string (uuid)` | Identifier of the related ticket record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SupportTicketDto](../schemas/s.md#supportticketdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/support/tickets/{ticketId}/reopen/recoverable`

**What it does:** Submit/create the documented record or action for support → tickets → reopen → recoverable. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [ReopenSupportCaseDto](../schemas/r.md#reopensupportcasedto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `ticketId` | path | Yes | `string (uuid)` | Identifier of the related ticket record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SupportTicketDto](../schemas/s.md#supportticketdto) | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.

## POST `/api/v1/support/tickets/{ticketId}/reply`

**What it does:** Add a reply to the caller's authorized conversation/ticket in the support → tickets → reply workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required.

**Body:** [ReplySupportTicketDto](../schemas/r.md#replysupportticketdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `ticketId` | path | Yes | `string (uuid)` | Identifier of the related ticket record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SupportTicketDetailsDto](../schemas/s.md#supportticketdetailsdto) | `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
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

## POST `/api/v1/support/tickets/{ticketId}/reply/recoverable`

**What it does:** Submit/create the documented record or action for support → tickets → reply → recoverable. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required.

**Body:** [ReplySupportTicketDto](../schemas/r.md#replysupportticketdto); required; media types: `application/json`, `text/json`, `application/*+json`.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `ticketId` | path | Yes | `string (uuid)` | Identifier of the related ticket record in this model; ownership and scope are checked separately. |
| `Idempotency-Key` | header | Yes | `string` | Original stable key for this logical operation; retain it with the original payload/revision when reconciling a lost response. |
| `If-Match` | header | Yes | `string` | Strong resource ETag read before this logical edit; preserve the original value for uncertain-outcome replay. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [SupportTicketDetailsDto](../schemas/s.md#supportticketdetailsdto) | `ETag`, `X-Entity-Revision`, `Idempotent-Replayed`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After`, `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 428 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 422 | [ProblemDetails](../schemas/p.md#problemdetails) | `X-Operation-Reference`, `X-Recovery-Operation-Reference` |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

**Mutation handling:** Preserve the original idempotency key and payload through unknown outcomes. Preserve the original revision during outcome recovery; refresh before a new logical edit.
