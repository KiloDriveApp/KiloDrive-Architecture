# Participant call workflows

[Reference index](README.md) · [API guide](../README.md)

Access shown here describes bearer metadata only. Anonymous operations can still
require installation admission, application attestation, contact proof or country
context. A bearer token does not replace ownership, feature gates or role checks.

Each entry lists recorded schemas, parameters, status codes and mutation guards.
Response metadata is not a complete list of runtime business outcomes; read the
[contract limitations](../coverage-and-limitations.md).

## Operations on this page

- [POST `/api/v1/voice/call`](#post-apiv1voicecall)
- [POST `/api/v1/voice/call/connected`](#post-apiv1voicecallconnected)
- [POST `/api/v1/voice/call/consent`](#post-apiv1voicecallconsent)
- [POST `/api/v1/voice/call/end`](#post-apiv1voicecallend)
- [POST `/api/v1/voice/call/gsm`](#post-apiv1voicecallgsm)
- [GET `/api/v1/voice/call/incoming`](#get-apiv1voicecallincoming)
- [GET `/api/v1/voice/call/{callId}`](#get-apiv1voicecallcallid)
- [GET `/api/v1/voice/options`](#get-apiv1voiceoptions)
- [GET `/api/v1/voice/token`](#get-apiv1voicetoken)

## POST `/api/v1/voice/call`

**What it does:** Submit/create the documented record or action for voice / call. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver, Passenger.

**Body:** [StartVoiceCallRequest](../schemas/s.md#startvoicecallrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [VoiceCallStartDto](../schemas/v.md#voicecallstartdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/voice/call/connected`

**What it does:** Record the call connection state in the voice / call / connected workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver, Passenger.

**Body:** [VoiceCallLifecycleRequest](../schemas/v.md#voicecalllifecyclerequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [VoiceCallLifecycleDto](../schemas/v.md#voicecalllifecycledto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/voice/call/consent`

**What it does:** Submit/create the documented record or action for voice / call / consent. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver, Passenger.

**Body:** [VoiceCallLifecycleRequest](../schemas/v.md#voicecalllifecyclerequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [VoiceCallLifecycleDto](../schemas/v.md#voicecalllifecycledto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/voice/call/end`

**What it does:** End the applicable call workflow in the voice / call / end workflow. The request and returned models below define the exact submitted evidence and result.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver, Passenger.

**Body:** [EndVoiceCallRequest](../schemas/e.md#endvoicecallrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## POST `/api/v1/voice/call/gsm`

**What it does:** Submit/create the documented record or action for voice / call / gsm. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver, Passenger.

**Body:** [StartVoiceCallRequest](../schemas/s.md#startvoicecallrequest); required; media types: `application/json`, `text/json`, `application/*+json`.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | No typed schema recorded | None recorded | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 409 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 415 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/voice/call/incoming`

**What it does:** Read incoming call state for the authenticated participant. Stop polling when the protected session is unavailable.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver, Passenger.

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [IncomingVoiceCallRecoveryDto](../schemas/i.md#incomingvoicecallrecoverydto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/voice/call/{callId}`

**What it does:** Read an authorized participant call's state and permitted connection information.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver, Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `callId` | path | Yes | `string (uuid)` | Identifier of the related call record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [VoiceCallLifecycleDto](../schemas/v.md#voicecalllifecycledto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 404 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/voice/options`

**What it does:** Read available calling options for this context; provider configuration and trip relationship determine actual availability.

**Explanation basis:** Operation-specific explanation.

**Access:** Bearer required; declared roles: Driver, Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `tripId` | query | Yes | `string (uuid)` | Accepted trip record, distinct from the originating ride request. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [VoiceCallOptionsDto](../schemas/v.md#voicecalloptionsdto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |

## GET `/api/v1/voice/token`

**What it does:** Read the permitted records/state for voice / token. This route-derived summary does not establish additional lifecycle rules.

**Explanation basis:** Route-derived summary; detailed behavior review remains open.

**Access:** Bearer required; declared roles: Driver, Passenger.

| Parameter | Location | Required | Type | Meaning | Constraints |
| --- | --- | --- | --- | --- | --- |
| `tripId` | query | Yes | `string (uuid)` | Accepted trip record, distinct from the originating ride request. | No further constraint recorded |
| `callId` | query | Conditional or optional | `string (uuid)` | Identifier of the related call record in this model; ownership and scope are checked separately. | No further constraint recorded |

| Recorded status | Response schema | Media types | Response headers |
| --- | --- | --- | --- |
| 200 | [VoiceSessionDto](../schemas/v.md#voicesessiondto) | `text/plain`, `application/json`, `text/json` | None recorded |
| 400 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 401 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 403 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 426 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
| 429 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | `Retry-After` |
| 500 | [ProblemDetails](../schemas/p.md#problemdetails) | `application/problem+json` | None recorded |
