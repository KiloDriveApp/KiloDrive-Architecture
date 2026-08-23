# AWS integration guide

KiloDrive uses AWS as a collection of narrowly scoped infrastructure services,
not as a place to hide application correctness. The country database remains the
durable source of truth for a ride, payment, notification intent, or recording
request. EventBridge, SQS, S3, SES, CloudWatch, and LiveKit infrastructure help us
move, store, and observe that work safely.

That distinction matters. A queue may redeliver a message. A provider may accept
a request and time out before replying. An instance may restart halfway through a
deployment. Good application design assumes all three will eventually happen.

## Implementation status

The public source tree contains provider adapters, configuration validation,
health checks, tests, and deployment assets for the capabilities below. Whether a
provider is enabled, approved for a particular country, or provisioned in a given
environment is deployment-specific. Empty example values are not proof that a
service is unavailable, and code support is not proof that production access has
been granted.

| AWS capability | KiloDrive responsibility | Where to continue |
| --- | --- | --- |
| EventBridge and SQS | Buffer bursty ride-dispatch work while SQL remains the recovery ledger | [Event-driven dispatch](eventbridge-sqs.md) |
| S3 and KMS controls | Store private documents, reports, thumbnails, and consented recordings | [Storage and encryption](storage.md) |
| IAM and STS | Give each workload only the actions it needs | [IAM](iam.md) |
| End User Messaging and SES | Send transactional SMS, voice OTP, WhatsApp, and email | [Messaging](messaging.md) |
| CloudWatch, SNS, and ADOT | Collect sanitized telemetry and notify operators | [Monitoring](monitoring.md) |
| Compute, networking, and S3 | Host LiveKit, TURN, and recording egress when enabled | [LiveKit](livekit.md) |

## The shape of a safe integration

Most KiloDrive integrations follow the same six-part pattern:

1. A user-facing command commits its domain change and a durable outbox intent in
   one country-cell transaction.
2. A worker reads that intent after commit. The request thread does not wait for
   email, SMS, push, or recording startup.
3. The adapter calls AWS with an explicit timeout and a stable provider reference
   where the provider supports idempotency.
4. Only a bounded result is persisted: provider name, safe provider ID, status,
   latency, attempt count, and correlation ID.
5. Unknown outcomes are reconciled before retrying a mutating operation.
6. Dashboards and alarms point to a runbook; they do not include the payload that
   caused the event.

This pattern prevents a common production lie: returning an HTTP failure after
the business transaction actually committed because an email provider was slow.

## Credentials and configuration

Prefer the standard AWS credential chain and workload identity. An instance role
or assumed role is easier to rotate and harder to copy accidentally than a static
access key. A local development profile may be appropriate for a developer, but
it must not be copied into an application settings file or committed to Git.

Configuration should identify a capability and its non-secret routing values.
Secrets belong in a protected secret source. Public documentation deliberately
omits account IDs, ARNs, resource names, IP addresses, hostnames, ports chosen for
private networks, key identifiers, and alarm destinations.

When onboarding a new AWS integration, answer these questions before enabling it:

- Which application component assumes the role?
- Which exact API actions and resource prefixes are required?
- Can the provider return an unknown result after accepting the request?
- What is the stable idempotency or reconciliation key?
- Which health check proves configuration, and which canary proves delivery?
- What happens to the user when AWS is unavailable?
- Which metric will alert us, and which runbook owns the response?
- How are credentials revoked without rebuilding the application?

## A practical local-to-production path

1. Develop against a fake or sandbox adapter and add contract tests.
2. Provision a dedicated non-user canary destination.
3. Create a least-privilege workload policy and validate denied actions as well
   as allowed ones.
4. Enable the adapter in a non-production environment.
5. Exercise timeout, throttling, duplicate delivery, malformed response, and
   credential-revocation cases.
6. Confirm that logs, traces, metrics, and database rows contain no destination,
   token, secret, message body, or object content.
7. Enable production behind a reversible feature flag.
8. Watch the first legitimate traffic window before changing thresholds.

## Lessons learned

### “Authenticated” does not mean “authorized”

We once reached AWS successfully but received `AccessDenied` for event
publication. The access key was valid; the identity simply lacked permission on
the selected bus. Diagnose those as IAM/resource-policy problems, not as network
failures, and do not respond by granting broad administrator access.

### A healthy provider is not a healthy product flow

SES can accept mail while the notification outbox is stuck. SQS can be empty
because EventBridge publication is failing. LiveKit signalling can be healthy
while TURN is unreachable from a mobile carrier. Dashboards therefore show the
whole chain, not a single green provider check.

### Canary destinations are operational credentials

A device registration token or test telephone number may look harmless, but it
can identify a device or person. Keep destinations outside source control, use
dedicated non-user endpoints, and store only sanitized results.

### Optional infrastructure must degrade deliberately

Turning off a canary, broker, or cache must not silently turn off core business
rules. The SQL outbox remains available when the dispatch broker is disabled;
private uploads remain quarantined when the scanner is unavailable; security
ceremonies fail closed if their distributed single-use store is unavailable.

## Related guidance

- [Hosting topology](../architecture/hosting.md)
- [Realtime and asynchronous processing](../architecture/realtime-and-events.md)
- [Observability](../architecture/observability.md)
- [Provider outage runbook](../runbooks/provider-outage.md)
- [Security posture](../security/README.md)
