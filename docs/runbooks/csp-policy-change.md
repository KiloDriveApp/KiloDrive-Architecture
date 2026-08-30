# Content Security Policy Change

- **Owner:** Web platform and application security
- **Status:** Maintained public-safe procedure
- **Last reviewed:** 2026-08-30
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Application security](../security/application-security.md) and [Portal and website](../architecture/portal-and-website.md)
- **Use when:** Portal or corporate-site resources need a reviewed CSP change

This runbook prevents a content fix from becoming a production security outage.
It deliberately omits environment names, approver identities, and privileged
commands; those belong in restricted operations material.

## Non-negotiable rules

- Do not paste an arbitrary raw policy into production.
- Do not add a wildcard source or `unsafe-inline` to make a console warning go
  away.
- Do not remove `frame-ancestors`, `object-src`, or `base-uri` protection without
  an approved security design.
- Do not activate a candidate without recent authentication, the required
  System Administrator capability, independent approval, and a passing probe.
- Keep the last known probe-passed version available for one-action rollback.

## Before changing policy

1. Capture the page, blocked resource, browser violation, correlation ID, current
   policy version, and user impact. Do not capture tokens or user content.
2. Confirm the resource is necessary, owned, pinned, privacy-reviewed, and
   compatible with the site's tracking declaration.
3. Prefer removing inline code, self-hosting a reviewed asset, or using a narrow
   nonce/hash before adding a new origin.
4. Check Portal and corporate-site behavior independently; their policies and
   resource needs are not interchangeable.

## Stage and validate

1. Add the source to the parsed directive model. The editor must reject unknown
   directives, malformed source expressions, unsafe schemes, policy duplicates,
   broad wildcards, and unreviewed inline execution.
2. Review the semantic diff: which directive changed, which pages gain access,
   which data may leave the origin, and which older protection remains.
3. Save a new immutable candidate version with a reason and sanitized evidence.
4. Apply it to the approved staging/canary boundary, never directly to all
   traffic.
5. Run a no-redirect synthetic probe and rendered browser checks for login,
   navigation, forms, errors, static assets, localization, and logout. Confirm
   all security headers survive both success and Problem Details responses.
6. Obtain the second approval required for production activation.

## Activate and observe

Activate the exact candidate that passed review; do not rebuild it by hand.
Observe CSP violations, browser errors, login/form failures, static-resource
health, latency, and error rate for the defined windows. A violation report is a
diagnostic signal, not permission to weaken the policy.

## Roll back

Rollback selects the previous activated, probe-passed version. Roll back when
critical pages or authentication fail, required assets remain blocked, an
unexpected origin receives access, header coverage regresses, or evidence cannot
identify the active version. Re-run the same probe after rollback and record the
result.

## Closure evidence

Retain the old/new version IDs, parsed diff, approvals, probe results, browser
matrix, observation window, rollback proof, sanitized correlation IDs, and the
reason the new source is required. Never retain session cookies, tokens, form
payloads, or customer identifiers in this evidence.

## Related reading

- [Application security](../security/application-security.md)
- [Portal and website release](portal-website-release.md)
- [System Administration](../architecture/system-administration.md)
