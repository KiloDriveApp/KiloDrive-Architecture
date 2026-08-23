# Geospatial, Routing, and Toll Handling

## Provider boundary

Mobile clients call KiloDrive map proxy endpoints. Provider credentials are kept
server-side. Implemented map operations include autocomplete, place details,
geocoding, reverse geocoding, routes, alternatives, distance/duration, and route
matrices.

Short bounded caches reduce repeated autocomplete, place-detail, route, and
geocode calls. Provider time is measured separately from KiloDrive processing so
capacity decisions do not confuse external latency with application latency.

## Location telemetry

High-frequency driver location is written to Valkey with a short TTL and batched
to MySQL for durable trip/safety evidence. Eligibility checks require freshness;
an online flag without current permitted telemetry is not enough for proximity
matching. Public documents deliberately omit key layouts and exact thresholds.

## Matching

Driver matching considers country/tenant, online and assignment state,
telemetry freshness, vehicle capability and compliance, membership/usage limits,
blocks, trust requirements, and requested hall. Driver eligibility is
revalidated inside acceptance, then the selected vehicle and compliance version
are snapshotted onto the trip.

## Toll detection

The toll calculator combines a provider route with country reference data for
roads, plazas, entry/exit relationships, vehicle classes, validity periods, and
approved prices. Route corridors and map matching identify credible traversals;
database spatial queries or H3 indexing can reduce application CPU and improve
precision where a country dataset supports them.

Controls include:

- no charge without a reviewed toll rule or journey/plaza mapping;
- Unicode-safe, versioned reference seeds;
- explicit pricing validity periods;
- stop, diversion, return-trip, and route alternative handling;
- itemized tolls and mathematically reconciled totals; and
- fixtures covering parallel roads and re-entry/exit cases.

Provider geometry alone is not authoritative for legal toll pricing. Reviewed
country data and effective dates remain required.
