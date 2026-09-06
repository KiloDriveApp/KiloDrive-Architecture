# Architecture Guide

KiloDrive is easiest to understand as a set of ownership boundaries rather than
as a list of technologies. The database that owns a password is not the same
database that owns a trip. The system that announces a bid is not the system
that proves who won it. The cache that knows where a driver was seconds ago is
not the permanent trip record.

## The chapters

| Chapter | Question it answers |
| --- | --- |
| [System context](system-context.md) | Who uses KiloDrive and what sits inside or outside the trust boundary? |
| [Capability status](capability-status.md) | What is implemented, incremental, or planned in source, and what is configurable, uncertified, certified, active, or unavailable in deployment? |
| [Product and operational doctrine](../governance/product-and-operational-doctrine.md) | Which product, failure, safety, wording, and evidence rules apply across every architecture chapter? |
| [API](api.md) | How does the API turn a request into authorized, validated, idempotent domain work? |
| [Tenancy and country cells](tenancy-and-country-cells.md) | Which database owns each class of data, and why? |
| [Entity identification](entity-identification.md) | How are internal, external, and human support identifiers designed? |
| [Realtime and events](realtime-and-events.md) | How does fast delivery coexist with durable recovery? |
| [Geospatial](geospatial.md) | How are noisy locations turned into useful matching and safety signals? |
| [Rider and driver safety](rider-driver-safety.md) | How do prevention, trip protection, RideCheck, emergency actions, evidence, and human response protect both marketplace participants? |
| [Marketplace product lifecycles](marketplace-product-lifecycles.md) | How do scheduled/multi-stop rides, intelligence, driver tools, family/business travel, courier, rentals, reputation, and support remain durable and recoverable? |
| [Jurisdictional compliance](jurisdictional-compliance.md) | How do country dossiers, shard controls, effective rules, approvals, and evidence support lawful country operations? |
| [Financial systems](financial-systems.md) | How are wallet balances, holds, journals, and provider settlements kept explainable? |
| [Rental marketplace](rental-marketplace.md) | How do organizations, compliant fleets, bookings, deposits, evidence, settlement, and disputes stay consistent? |
| [Documents, media, and voice](documents-media-voice.md) | How are private uploads and call media authorized, scanned, retained, and audited? |
| [Mobile](mobile.md) | How do Flutter workspaces, repositories, state, offline behavior, and native services fit together? |
| [Portal and website](portal-and-website.md) | How do browser applications preserve API authorization and presentation parity? |
| [System Administration](system-administration.md) | How do capabilities, country workspaces, work queues, investigations, step-up, audit, and recovery stay inside the control-plane boundary? |
| [Runtime boundaries and certification](runtime-boundaries-and-certification.md) | How are anonymous tenancy, public endpoints, response hardening, typed clients, negotiated fares, realtime recovery, and capacity evidence certified together? |
| [Hosting](hosting.md) | How are edge, IIS, MySQL, Valkey, routing, and media failure domains separated? |
| [Observability](observability.md) | How are requests, queues, providers, and customer symptoms correlated safely? |
| [Scaling and capacity](scaling-and-capacity.md) | How do we model load, find the first bottleneck, and scale without guessing? |
| [Plugins and extension points](plugins-and-extension-points.md) | Where can providers change without leaking SDK details into business logic? |

The [1.0.0 build 97 release update](release-1.0.0-97.md) captures the latest
vehicle/onboarding, typed-state and schema-alignment changes and explains which
claims still require live production or provider evidence.

## Three mental models worth keeping

### 1. Ownership before access

Ask “which component owns this truth?” before asking “how do I query it?” A
cross-cell join may be technically possible and still be architecturally wrong.
The owner determines transaction boundaries, retention, authorization, and
recovery.

### 2. Durable core, replaceable edges

Trips, bids, wallet movements, memberships, and audit evidence are durable.
Cache entries, websocket connections, provider requests, map tiles, and push
delivery are replaceable. The application should recover replaceable edges from
durable state, never invent durable state from a stale edge.

### 3. Commands are conditional state transitions

“Accept bid” is not a blind update. It is a conditional transition that must
prove the ride is open, the bid is actionable, the driver remains eligible, the
vehicle is compliant, and the expected entity version still matches. The
database lock and condition make competing accepts deterministic.

These models are repeated throughout the documentation because they explain
many of the failure modes documented in this repository.
