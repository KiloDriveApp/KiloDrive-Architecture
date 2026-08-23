# LiveKit on AWS

## Topology

KiloDrive can self-host LiveKit and TURN on an approved Linux compute instance,
with a separately managed Egress service for recordings. Public DNS and TLS
front the signalling endpoints; media uses the documented LiveKit UDP/TCP/TURN
ports allowed by tightly scoped security groups.

## API integration

The KiloDrive API authenticates both trip participants and issues short-lived,
trip/role-scoped LiveKit tokens. The mobile app joins audio-only rooms and uses
platform call presentation for incoming calls. A call remains bound to the trip
lifecycle and expires after closure.

## Egress

When recording is enabled and all required consent/policy checks pass, an outbox
handler starts or reconciles audio egress. Output is encrypted in private S3.
Retries inspect existing egress state before creating another recording.

## Capacity and recovery

Monitor CPU, memory, network packets, egress bandwidth, packet loss, jitter,
TURN allocation, room count, participant count, and recording queue. Recovery
prioritizes active call continuity, token reissue, orphan cleanup, and explicit
recording state reconciliation.

Credentials, endpoints, media ranges, security groups, and instance sizing are
kept in restricted infrastructure documentation.
