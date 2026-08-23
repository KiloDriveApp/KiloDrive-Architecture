# Runbook: Portal and Website Release

## Procedure

1. Build/test from the reviewed commit and verify API contract compatibility.
2. Run authenticated role/route/modal/validation browser tests and public website
   link/content/calculator tests.
3. Assert correlation IDs, anti-forgery, redirects, security headers, strict CSP,
   console cleanliness, localization parity, and no inline-policy regression.
4. Publish immutable artifacts; preserve the single protected settings file and
   data-protection key ring.
5. Drain the IIS application, replace files atomically, start, and test health,
   login, System Admin routes, public pages, calculators, and API correlation.
6. Monitor errors, CSP reports, latency, and API/provider failures.

Rollback restores the previous compatible artifact; it never overwrites current
protected secrets with repository examples.
