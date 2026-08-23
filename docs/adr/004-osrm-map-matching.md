# ADR 004: Road-network map matching for route evidence

- **Status:** Accepted/Incremental
- **Date:** 2026-08-23
- **Decision owners:** Architecture, Geospatial, Safety, and Operations
- **Related systems:** Routing, toll calculation, trip replay, RideCheck,
  location telemetry, OSRM, and country reference data

## Context

A phone reports coordinates, not roads. Two roads may run only a few metres
apart while having very different consequences: one may be a tolled motorway
and the other an untolled frontage road; one may follow the planned trip while
the other is a genuine route deviation. A fixed Haversine corridor around a
polyline cannot reliably tell them apart.

KiloDrive still needs inexpensive geometric checks. They are useful for
discarding obviously distant candidates and for operating in an explicitly
degraded mode. They are not strong enough to become financial or safety proof
on their own. The platform therefore needs a road-aware step between noisy GPS
or provider geometry and decisions such as “this vehicle crossed this toll
plaza.”

The team already operates OpenStreetMap-based OSRM services for route and table
work. OSRM's `/match` endpoint can align a bounded trace to the road graph and
return a confidence value and matched geometry. It is not perfect evidence—map
data can be stale and sparse traces can be ambiguous—but it is materially more
defensible than proximity alone.

## Decision drivers

- Avoid false toll charges on parallel or frontage roads.
- Reduce false route-deviation alarms caused by GPS noise.
- Keep provider credentials and routing policy on the server.
- Bound CPU, network, and payload cost for long traces.
- Preserve an honest degraded mode when matching is unavailable.
- Keep approved toll prices and legal policy separate from route geometry.
- Support deterministic tests with reviewed synthetic traces.
- Avoid describing a probabilistic match as unquestionable ground truth.

## Decision

KiloDrive uses an OSRM-compatible road-network map-matching adapter for
financially or operationally sensitive route interpretation.

The adapter accepts a validated, ordered trace; reduces it to a configured
maximum number of representative points; sends invariant-culture
`longitude,latitude` coordinates to `/match`; requests the matched geometry;
and accepts the result only when the provider response is well formed and its
confidence meets the reviewed threshold.

The matched route is used as evidence for downstream logic, not as its price or
policy source:

- toll detection compares matched traversal with reviewed plaza locations and
  effective-dated country rate matrices;
- route-deviation logic combines road evidence with sample accuracy,
  consecutive observations, elapsed time, cooldown, and rider response;
- trip replay labels gaps and low-confidence portions instead of silently
  drawing an invented path; and
- reports distinguish measured, matched, and manually overridden values.

When matching fails or confidence is too low, the result is explicitly
unverified. KiloDrive may still display a route or use a coarse geometric check
for non-financial guidance, but it does not invent a toll traversal or silently
upgrade weak evidence into a charge.

The rollout is incremental. A decoded-polyline implementation remains a
guarded compatibility and degraded path for non-authoritative decisions while
spatial projections, provider capacity, and reference matrices are certified
country by country.

## Processing pipeline

```text
validated trace
    -> remove duplicates and impossible jumps
    -> bound/sample the trace without changing order
    -> OSRM /match with timeout and circuit telemetry
    -> require usable confidence and geometry
    -> spatial bounding-box prefilter
    -> precise plaza/corridor comparison
    -> traversal ordering and direction checks
    -> effective-dated country pricing or safety policy
    -> itemized, auditable result
```

Each stage has a separate duration and outcome in telemetry. Coordinates,
addresses, and full provider payloads are not metric labels or ordinary log
fields.

## Alternatives considered

### Fixed Haversine distance to decoded polyline points

This is simple and cheap, and remains useful as a first-pass filter. It cannot
reliably distinguish parallel roads and its result changes with polyline point
density. It is not accepted as sole evidence for a toll charge.

### Provider directions geometry without matching

A planned route is valuable for quotation but does not prove the vehicle
followed it. Using the original route for settlement would miss diversions,
exit/re-entry, and changed plans. Provider route geometry remains an input, not
completed-trip evidence.

### MySQL spatial functions only

`POINT SRID 4326`, spatial indexes, bounding boxes, and
`ST_Distance_Sphere` efficiently answer geometric proximity. They do not map a
noisy observation to a road identity by themselves. MySQL spatial queries are
used after or alongside matching, not as a replacement for it.

### H3 cells

H3 is useful for aggregation and coarse partitioning. A hexagonal cell does not
say which carriageway was travelled. It may become an additional prefilter,
but it is not map matching.

### A commercial map-matching provider for every trace

This may offer excellent road and traffic data, but creates recurring cost,
quota coupling, data-transfer/privacy questions, and provider lock-in. The
adapter boundary permits a reviewed alternative later without changing the
domain contract.

### No automated toll determination

Manual review avoids automated false charges but cannot support an immediate
calculator at useful scale. KiloDrive instead automates only when both route
evidence and approved pricing data are sufficient, and reports uncertainty
otherwise.

## Consequences

### Benefits

- Parallel-road and frontage-road ambiguity is materially reduced.
- Toll results can be itemized in actual traversal order.
- Route-deviation detection has better road context and fewer noisy alerts.
- OSRM data can be self-operated and updated on a controlled schedule.
- One adapter contract supports synthetic testing and future provider changes.
- An unavailable provider produces an honest state rather than a fabricated
  charge.

### Costs and risks

- OSRM needs current regional extracts, enough memory, disk, CPU, and monitored
  data-refresh procedures.
- Sparse, inaccurate, or out-of-order traces can still produce low-confidence
  or incorrect matches.
- OpenStreetMap road metadata can lag a physical road change.
- Long traces require sampling, which can remove a short exit/re-entry if done
  carelessly.
- A provider outage can temporarily reduce authoritative toll or safety
  decisions.
- Confidence thresholds require fixture evidence and may differ by geography;
  they must not be tuned to make tests green without investigating the data.

Mitigations include bounded payloads, direction/order checks, confidence
gating, versioned map data, reviewed country fixtures, itemized output, and a
manual audited override path that never edits the original evidence.

## Security, privacy, and compliance

- Route traces are location data and receive purpose-limited authorization,
  retention, access audit, and deletion/hold treatment.
- Public documentation, logs, and metrics do not contain customer traces or
  addresses.
- Provider calls use server-side configuration and strict egress policy; no
  private key is shipped to Flutter.
- A manual override records actor, reason, prior value, replacement value, and
  correlation evidence without rewriting the source trace.
- Toll pricing is drawn from approved, effective-dated country reference data.
  Geometry cannot create a price that the catalogue does not contain.

## Reliability and operations

Monitor provider reachability, request timeout rate, match confidence
distribution, bounded trace size, stage latency, fallback use, zero-toll rates
on certified fixtures, and route-deviation alert/false-positive rates. Keep map
data version and last successful refresh visible to operators.

During OSRM loss:

1. confirm the failure is provider-specific rather than a general API or DNS
   outage;
2. stop treating new low-confidence geometry as financial proof;
3. expose a controlled unavailable/unverified response where policy requires;
4. keep already committed trips and ledgers intact;
5. restore or fail over the routing service;
6. rerun certified route fixtures before re-enabling authoritative matching;
   and
7. reconcile calculations created during the degraded window.

See the [geospatial degradation runbook](../runbooks/geospatial-degradation.md)
for operator steps.

## Validation

- Exact road trace and noisy trace both map to the intended road.
- Parallel frontage-road trace does not trigger the motorway plaza.
- Multi-plaza route preserves traversal order and itemized total.
- Exit/re-entry, intermediate stop, diversion, return trip, and historical-rate
  fixtures calculate correctly.
- Low-confidence, no-match, timeout, malformed JSON, and provider-5xx results
  remain explicitly unverified.
- Longitude/latitude reversal, invalid bounds, duplicate points, excessive
  points, and impossible jumps are rejected or normalized deterministically.
- A route-deviation alert requires the configured sequence and can be allowed,
  escalated, rejoined, and deduplicated.
- Logs and traces contain operation, duration, sanitized result, and
  correlation ID—but no coordinate arrays or addresses.
- Controlled provider loss and recovery leaves no invented charges and passes
  certified fixtures before normal service resumes.

## Follow-up

- Keep the public [geospatial chapter](../architecture/geospatial.md) aligned
  with the actual rollout state.
- Version the map extract and reviewed toll reference set in release evidence.
- Add optional database spatial projections only through reviewed idempotent
  schema changes and fingerprint checks.
- Revisit H3 only for a measured aggregation or candidate-partitioning need,
  with a separate decision record.
