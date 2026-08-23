# System Context

## Purpose

KiloDrive connects riders, drivers, rental organizations, operations staff, and
external providers through one versioned API. It supports ride proposals and
bids, trips, deliveries, memberships, wallet operations, vehicle and driver
verification, rentals, support, reports, safety workflows, and communications.

## Runtime components

| Component | Responsibility | Trust level |
| --- | --- | --- |
| Flutter mobile app | Rider, driver, rental, tools-only, and System Admin experiences | Untrusted client |
| ASP.NET Core portal | Browser operations and account workflows | Untrusted browser with server session |
| Corporate website | Public content and calculators backed by approved API data | Public client |
| ASP.NET Core API | Authentication, authorization, business rules, orchestration, contracts | Trusted application boundary |
| Identity control database | Global credentials, security state, country memberships, support/privacy coordination | Restricted data tier |
| Country databases | Operational, financial, trip, delivery, rental, audit, and outbox records | Restricted data tier |
| Valkey | Ephemeral/distributed state and realtime scale-out | Restricted infrastructure tier |
| Provider adapters | Maps, messaging, payments, push, voice, storage, and telemetry | External trust boundaries |

## Principal flows

1. A client authenticates against the global identity control plane.
2. Claims and authorized country memberships select a country workspace.
3. Tenant resolution binds the request to one authorized marketplace boundary.
4. A handler validates and executes the domain operation in the owning database.
5. Side effects are staged in an outbox and delivered after commit.
6. Realtime updates are broadcast through SignalR and its Valkey backplane;
   durable events and polling remain recovery paths.
7. Correlation IDs connect sanitized request, audit, telemetry, and provider
   attempt records.

## Architectural priorities

- fail closed at identity, tenant, money, verification, and document boundaries;
- preserve country-level financial and operational sovereignty;
- make mutation retries safe with idempotency and conditional state changes;
- keep provider failures outside short database transactions;
- prevent payloads, tokens, contact details, and document contents from entering
  operational logs;
- preserve degraded operation only where doing so is safe and truthful; and
- keep deployment evidence private while publishing architecture openly.

## Availability model

MySQL is authoritative. Valkey and providers improve latency and connectivity but
do not replace durable domain state. Some functions intentionally fail closed
when a dependency is security-critical (for example, production upload scanning
or schema compatibility). Other paths degrade safely (for example, a provider
notification can retry from the outbox without rolling back an already committed
business transaction).
