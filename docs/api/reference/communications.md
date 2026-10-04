# Participant call workflows

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## POST `/api/v1/voice/call`

**What it does:** Submit/create the documented record or action for voice → call. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Driver, Passenger.

**Body:** [StartVoiceCallRequest](../schemas/s.md#startvoicecallrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [VoiceCallStartDto](../schemas/v.md#voicecallstartdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/voice/call/connected`

**What it does:** Record the call connection state in the voice → call → connected workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required; declared roles: Driver, Passenger.

**Body:** [VoiceCallLifecycleRequest](../schemas/v.md#voicecalllifecyclerequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [VoiceCallLifecycleDto](../schemas/v.md#voicecalllifecycledto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/voice/call/consent`

**What it does:** Submit/create the documented record or action for voice → call → consent. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Driver, Passenger.

**Body:** [VoiceCallLifecycleRequest](../schemas/v.md#voicecalllifecyclerequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [VoiceCallLifecycleDto](../schemas/v.md#voicecalllifecycledto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## POST `/api/v1/voice/call/end`

**What it does:** End the applicable call workflow in the voice → call → end workflow. The request and returned models below define the exact submitted evidence and result.

**Access:** Bearer required; declared roles: Driver, Passenger.

**Body:** [EndVoiceCallRequest](../schemas/e.md#endvoicecallrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

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

## POST `/api/v1/voice/call/gsm`

**What it does:** Submit/create the documented record or action for voice → call → gsm. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Driver, Passenger.

**Body:** [StartVoiceCallRequest](../schemas/s.md#startvoicecallrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

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

## GET `/api/v1/voice/call/incoming`

**What it does:** Read the permitted records/state for voice → call → incoming. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Driver, Passenger.

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [IncomingVoiceCallRecoveryDto](../schemas/i.md#incomingvoicecallrecoverydto) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/voice/call/{callId}`

**What it does:** Read the permitted records/state for voice → call. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Driver, Passenger.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `callId` | path | Yes | `string (uuid)` | Identifier of the related call record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [VoiceCallLifecycleDto](../schemas/v.md#voicecalllifecycledto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/voice/options`

**What it does:** Read the permitted records/state for voice → options. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Driver, Passenger.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `tripId` | query | Yes | `string (uuid)` | Accepted trip record, distinct from the originating ride request. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [VoiceCallOptionsDto](../schemas/v.md#voicecalloptionsdto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |

## GET `/api/v1/voice/token`

**What it does:** Read the permitted records/state for voice → token. Use the request/response fields below; server validation and the caller's resource relationship define the permitted effect.

**Access:** Bearer required; declared roles: Driver, Passenger.

| Parameter | Location | Required | Type | Meaning |
| --- | --- | --- | --- | --- |
| `tripId` | query | Yes | `string (uuid)` | Accepted trip record, distinct from the originating ride request. |
| `callId` | query | Conditional or optional | `string (uuid)` | Identifier of the related call record in this model; ownership and scope are checked separately. |

| Recorded status | Response schema | Response headers |
| --- | --- | --- |
| 200 | [VoiceSessionDto](../schemas/v.md#voicesessiondto) | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | None recorded |
