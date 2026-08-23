# Geospatial degradation runbook

- **Owner:** Geospatial, dispatch, and maps-provider operations
- **Status:** Operational degradation procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Geospatial processing](../architecture/geospatial.md), [realtime and events](../architecture/realtime-and-events.md), and [observability](../architecture/observability.md)

## Purpose and scope

Use this runbook when any part of KiloDrive's location stack is slow, incorrect,
or unavailable. The stack includes place autocomplete/details, forward and
reverse geocoding, route and matrix calls, map tiles, driver telemetry, proximity
matching, OSRM map matching, route-deviation detection, and toll-plaza matching.

These are separate stages with different safety consequences. “Maps are down”
is not a useful diagnosis. A tile-rendering outage should not stop a text-based
trip status, while an untrusted distance result must not silently determine a
fare, toll, or receipt.

## Owners and roles

| Role | Responsibility |
| --- | --- |
| Incident lead | Coordinates scope, customer posture, mitigation, and recovery |
| Maps/provider owner | Checks quota, key restrictions, billing, provider status, and latency |
| Geospatial engineer | Evaluates route geometry, map-match confidence, spatial data, and thresholds |
| Dispatch owner | Protects driver visibility, telemetry freshness, and matching behavior |
| Financial/product owner | Decides whether quotes/tolls can be shown, withheld, or reviewed |
| Mobile/web owner | Confirms degraded UI, cached data, and safe retry behavior |

## Capability and truth map

| Capability | Typical authority | Safe degradation principle |
| --- | --- | --- |
| Place suggestion/details | configured places provider plus bounded cache | manual entry only where server contract can validate it |
| Route distance/duration | configured route provider | never invent a billable distance |
| Driver live location | fresh authenticated heartbeat in Valkey | stale telemetry makes the driver ineligible/explicitly offline |
| Historical breadcrumb | country-cell persistence | useful for audit/replay, not live dispatch |
| Map matching | OSRM/approved road-network service | expose confidence; ambiguity is not a toll traversal |
| Toll plaza/rate | reviewed country reference data and spatial/journey rules | explicit unavailable/incomplete beats a false charge |
| Map display | client tile/rendering provider | retain textual addresses and non-map controls |

## Preconditions

Operators need access to:

- stage-level traces and bounded metrics;
- provider console/status through approved roles;
- Valkey health and telemetry-freshness metrics;
- OSRM health, data-build version, and fixture endpoints;
- MySQL reference-data version/fingerprint and spatial-query diagnostics;
- dedicated public-landmark route fixtures for each active country; and
- feature controls that can disable a capability without weakening unrelated
  security or accounting checks.

Production diagnostics must not log raw customer addresses, coordinates, route
polylines, tokens, API keys, or user identities.

## Detection and alerting

Track each stage separately:

- application warm-cache p50/p95/p99 and error rate;
- provider time for autocomplete, place details, geocode, route, and matrix;
- cache hit rate, eviction, TTL expiry, and country-key correctness;
- OSRM match latency, confidence, unmatched points, and data version;
- toll candidate count, confirmed traversal count, anomaly rate, and unmatched
  known-route fixtures;
- driver heartbeat age, accuracy, rejected telemetry, and stale-online count;
- database spatial query latency and rows examined; and
- serialization and client rendering time.

Alert on the approved customer budget, including the warm application p95 gate
for two consecutive windows. Provider latency must be graphed separately so the
team does not “fix” a slow upstream service by hiding it in a larger timeout.

## Safety and stop conditions

Stop or disable the affected quote/dispatch/charge path when:

- route distance or geometry is missing, malformed, crosses an implausible
  boundary, or has insufficient map-match confidence;
- toll reference data contains unknown encoding, duplicate effective periods, or
  an incomplete pricing matrix for the route;
- a stale or low-quality driver position would make proximity unsafe;
- country cache keys could return another country's places, currency, tolls, or
  rules;
- provider credentials or restrictions may have been compromised;
- a fallback would change a financial result without explicit disclosure; or
- the operator cannot identify which stage produced the value.

Do not disable TLS, broaden an API key to all origins/IPs, expose coordinates in
logs, remove telemetry freshness, or charge a guessed toll to make the flow
“work.”

## First ten minutes

1. Capture UTC time, affected feature/country/client, correlation ID, deployment,
   provider, cache state, and stage timings. Use a dedicated fixture, not a
   customer's route.
2. Determine scope: one user, one node, one API key/project, one country, one
   route class, or global.
3. Check recent releases, country-reference updates, provider key/quotas/billing,
   DNS/network, certificates, Valkey ACL/latency, OSRM health/data version, and
   database query saturation.
4. Run the fixture ladder: autocomplete → details → reverse geocode → route →
   map match → spatial toll match → final quote/serialization.
5. Compare cold and warm runs. Record provider and application time separately.
6. Apply the narrowest safe degraded mode and tell support what the user will see.

## Diagnosis by stage

### Autocomplete and place details

Check debounce/cancellation generations, country bounds, locale, session token,
provider response code, quota, and cache key. A superseded request must not
replace a newer query. Place-details cache entries should be short-lived,
country/provider scoped, and invalidated when reference context changes.

If autocomplete is unavailable, allow manual structured input only where the API
can validate coordinates/address. Give a localized retry message; do not leave an
infinite spinner.

### Current and reverse-geocoded location

Separate coordinate acquisition from address lookup. A last-known fix is usable
only if age and accuracy meet policy. Start a fresh bounded-accuracy request in
parallel, show “Finding your location…,” populate valid coordinates immediately,
then reverse-geocode asynchronously. If reverse geocoding fails, retain bounded
coordinates with a retry rather than pretending an old address is current.

### Route, distance, duration, and fare input

Verify start, destination, all supported intermediate stops/diversions, return
option, vehicle/category, accessibility options, and route preferences are
identical between preview and creation. Compare provider geometry and totals.

If no trusted route is available, return a stable unavailable result or an
approved clearly labelled estimate. Never submit a different hidden route input
than the one the rider previewed.

### Driver telemetry and proximity matching

Check authentication, driver online state, heartbeat age, accuracy, speed,
country/cell, assigned vehicle, compliance, active assignment, trust level, and
blocked relationships. “Online” is a lease supported by fresh telemetry, not a
permanent Boolean.

If the platform cannot maintain genuine background heartbeats, expire online
status clearly and notify the driver. Do not keep a stale driver visible for a
selling point.

### OSRM map matching and route anomaly detection

Confirm the OSRM service is healthy and uses the intended regional data build.
Inspect point sampling, timestamp ordering, radiuses/accuracy, match confidence,
gaps, and implausible jumps. GPS noise, tunnels, and parallel frontage roads can
make a fixed geometric corridor look like a route change.

During low confidence, record a degraded anomaly and ask for rider confirmation
where appropriate; do not automatically accuse the driver or trigger a toll.
Emergency actions remain explicit and available.

### Toll detection and pricing

Verify the calculation uses start, destination, no more than the supported stops,
diversions, return option, vehicle class, cost-per-distance input, and selected
historical rate period. Distinguish journey-level entry/exit matrices from
separately priced plaza crossings.

Candidate plazas should come from database spatial indexes or an approved H3
index; traversal confirmation should use matched road geometry and travel order.
A fixed 2.5 km Haversine corridor alone can charge a parallel road.

Known-route fixtures must assert:

- ordered plaza/entry/exit encounters;
- direction and re-entry behavior;
- vehicle-class and effective-period rate;
- per-leg distance and additional distance cost;
- return-trip multiplication/rules; and
- grand total equals the sum of displayed components.

Reject U+FFFD replacement characters and verify stable UTF-8 names through
MySQL, API JSON, Portal, Website, and Flutter.

## Degraded-mode matrix

| Failure | User-facing behavior | Operational action |
| --- | --- | --- |
| Autocomplete unavailable | manual validated entry plus retry | disable provider-specific suggestion only |
| Reverse geocode slow | coordinates/locating state, asynchronous address retry | preserve coordinate age/accuracy diagnostics |
| Route provider unavailable | explicit quote unavailable or approved disclosed fallback | disable final billable quote if distance is untrusted |
| OSRM unavailable | route shown without confident map-match-dependent claims | suspend automatic toll/anomaly decision |
| Toll reference incomplete | explicit incomplete/unavailable toll result | flag reviewed data repair; do not return zero as certainty |
| Valkey/telemetry stale | driver becomes ineligible/offline | preserve durable state; restore cache/backplane |
| Map tiles fail | textual route, addresses, status, and actions remain | treat as rendering-only unless route service also fails |

## Recovery procedure

1. Correct the narrow cause: provider quota/restriction, network, cache, OSRM data,
   spatial index/reference seed, or code release.
2. Reproduce the correction in an isolated environment or with dedicated
   fixtures before production promotion.
3. Clear only affected bounded cache keys. Do not flush all Valkey data when a
   place-details cache is stale.
4. Warm public reference/cache entries gradually; never warm with customer
   addresses or routes.
5. Run the complete fixture ladder twice and compare cold/warm stage timings.
6. Verify known toll routes, no-toll routes, frontage-road ambiguity, stops,
   diversions, return, and historical pricing.
7. Verify stale drivers remain offline until a new permitted heartbeat arrives.
8. Observe at least two healthy windows before removing degraded-mode messaging.
9. Identify quotes/tolls produced during the affected period and route any
   correction through an approved audited financial process.

## Rollback

If a code or reference-data change caused the incident, disable the affected
feature or return to the previous immutable package/reference version. Preserve
new evidence and do not delete calculations. A reference rollback must respect
effective periods; never rewrite historical prices to today's values.

If the previous version produced unsafe or wrong charges, keep the capability
unavailable while fixing forward rather than restoring a known defect.

## Verification criteria

Recovery requires:

- stage-level success and latency within approved budgets for two windows;
- cache keys/TTLs correctly scoped and a healthy warm hit rate;
- valid current-location age/accuracy behavior;
- fresh driver telemetry and matching eligibility consistency;
- OSRM match confidence and data version as expected;
- known toll and no-toll fixtures with correct component/grand totals;
- UI retry, empty, degraded, and map-rendering fallbacks on supported clients;
- no raw coordinates, addresses, polylines, keys, or tokens in logs; and
- alerts/dashboards still active.

## Evidence to retain

Retain sanitized correlation IDs, country/fixture name, stage timings, provider
ID/status, cache state, OSRM/reference versions, before/after known-route results,
deployment or seed hash, degraded-mode interval, affected calculation count,
reviewer, and monitoring outcome.

Use approved public landmarks in evidence. Do not retain customer routes,
precise coordinates, addresses, driver identities, or provider credentials.

## Escalation

Escalate immediately when wrong geospatial output affected a fare, toll, receipt,
driver assignment, safety alert, emergency response, or cross-country boundary.
Financial and safety owners decide customer remediation; the maps operator does
not silently alter historical results.

## Common pitfalls

- Looking only at total API latency and missing the slow provider stage.
- Increasing timeouts before measuring quota, cache, and upstream time.
- Treating zero matched tolls as zero cost rather than an incomplete match.
- Iterating every plaza in application memory under load instead of narrowing
  candidates spatially.
- Using one fixed corridor for noisy GPS and frontage roads.
- Letting a last-known position create a fare without age/accuracy limits.
- Pausing background telemetry while continuing to display the driver as online.
- Flushing all Valkey keys to repair one cache namespace.
- Storing customer coordinates in traces because they are useful for debugging.
