# Plugins, Providers, and Extension Points

KiloDrive uses dependency-injected interfaces and feature flags rather than
loading arbitrary third-party executable plugins into production.

## Implemented adapter boundaries

| Capability | Interface/abstraction style | Examples |
| --- | --- | --- |
| Payments | Payment gateway | Stripe, PayPal, bank transfer, test simulator |
| Notifications | Channel/provider adapters | FCM/APNs, AWS/Twilio SMS and WhatsApp, SES |
| Maps | Route/geocode provider | Google Maps; routing abstraction supports alternatives |
| Voice | Token, room, egress, object-store adapters | LiveKit and private S3 |
| Uploads | Object storage and scan adapters | S3, ClamAV/CDR-compatible boundary |
| Cache/realtime | Distributed cache and backplane | Valkey/Redis protocol |
| Dispatch bus | High-throughput publisher/consumer | EventBridge and SQS |
| Reports | Builder and renderer | Excel and PDF renderers |
| Telemetry | OpenTelemetry exporter and log sinks | OTLP and CloudWatch-compatible paths |

## Extension rules

1. The domain depends on a narrow interface, not a provider SDK.
2. Provider credentials come from protected configuration or workload identity.
3. Provider calls have explicit timeouts and sanitized errors.
4. Mutating retries require stable idempotency and reconciliation.
5. Health/readiness and protected canaries expose only provider ID, latency,
   sanitized status, and correlation ID.
6. The adapter has contract, timeout, partial-failure, and redaction tests.
7. A rollback path exists before the adapter can be enabled.

## Feature flags

Flags may enable an approved capability per deployment, tenant, country, plan,
or build. A flag is not authorization. All server-side access and financial rules
remain enforced when a client is modified or stale.

## Map engine portability

Map controller operations are isolated behind an application-facing abstraction
so regional Google Maps, Mapbox, Apple Maps, OSRM, or Valhalla adapters can be
introduced without changing ride/trip state or API DTOs. Current mobile rendering
still uses Google Maps unless an approved adapter is implemented and certified.
