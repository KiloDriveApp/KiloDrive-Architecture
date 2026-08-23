# Runbook: Geospatial Provider Degradation

## Symptoms

Slow current-location resolution, autocomplete/route timeout, missing toll plaza,
incorrect route total, stale driver telemetry, or map tiles unavailable.

## Procedure

1. Separate KiloDrive stage time from provider route/geocode time using sanitized
   spans and a controlled fixture.
2. Check provider health/quota, cache hit rate, OSRM/routing fallback, and country
   reference-data version.
3. For location, use an age/accuracy-qualified last-known fix, request fresh GPS
   in parallel, and reverse-geocode asynchronously.
4. For fare/ride creation, keep quote and creation inputs identical; never invent
   provider distance.
5. For tolls, verify route geometry, map matching, plaza/journey matrix, vehicle
   class, effective period, stops/diversions/return, and itemized total.
6. If accuracy cannot be assured, present a clear unavailable/estimate state and
   allow only the documented user proposal path.

Do not increase timeouts or disable rate limits before reproducing the stage that
is slow.
