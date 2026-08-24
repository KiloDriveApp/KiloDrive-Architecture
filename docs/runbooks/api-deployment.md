# API deployment runbook

- **Owner:** API platform and release engineering
- **Status:** Operational release procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [API architecture](../architecture/api.md), [hosting](../architecture/hosting.md), and [observability](../architecture/observability.md)
- **Verification policy:** [Testing and verification](../quality/testing-and-verification.md)

## Purpose and scope

Use this runbook to promote one reviewed KiloDrive API package into an
environment that serves real traffic. It covers the application binary,
configuration references, schema compatibility, background workers, health
checks, traffic restoration, and rollback.

It does **not** authorize an operator to edit customer data, rotate a signing
key, weaken a security control, or improvise database DDL. Those are separate,
reviewed changes. If the release needs a schema change, use the
[schema alignment runbook](schema-alignment.md) before switching traffic.

The guiding idea is simple: a deployment is not “copy some files and see if the
site starts.” It is a controlled replacement of one known release with another,
with enough evidence to return to the previous release safely.

The required unit, property, real-MySQL, authorization, contract, concurrency,
failure-injection, and compatibility evidence is defined in
[Testing and verification](../quality/testing-and-verification.md). A broad
controller smoke test does not replace those boundary-specific gates.

## Roles and decision rights

| Role | Responsibility |
| --- | --- |
| Release lead | Owns the change window, checklist, go/no-go decision, and final record |
| Application operator | Stages the immutable package, switches traffic, and observes process health |
| Database operator | Confirms schema compatibility and performs separately reviewed alignment |
| Security reviewer | Reviews configuration, key references, permissions, headers, and secret handling |
| Service owner | Confirms business smoke tests and accepts residual risk |
| Incident commander | Takes control if the change causes material customer or financial impact |

One person may fill more than one role in a small team, but the release and the
evidence should still name the roles. A material production change should have a
second pair of eyes.

## Preconditions

Do not begin until all of the following are true:

- the release commit is reviewed, immutable, and identifiable by commit hash;
- release-mode build, tests, security gates, and OpenAPI contract checks pass;
- the package was produced by the approved build workflow, not an operator's
  ad-hoc development folder;
- package hash, SBOM, dependency notices, and build log are retained;
- the target schema version and normalized control/cell fingerprints are known;
- clone testing proved the new binary against an aligned MySQL 8 schema;
- protected configuration was validated against the code's option validators;
- a previous known-good package and its configuration contract remain available;
- liveness, readiness, outbox lag, reconciliation, provider state, and current
  customer symptoms have been recorded; and
- an authorized rollback decision-maker is available for the whole window.

Schedule the release when its risk warrants a controlled window. “Small code
change” is not a reason to skip the gate: a one-line route, option-name, or
outbox-message change can prevent startup or strand work.

## Safety and stop conditions

Stop the deployment and keep or return traffic to the previous release when:

- the source commit and package hash cannot be proven;
- schema fingerprints differ from the reviewed expectation;
- a required secret, signing key, protected file, or workload permission is
  missing;
- the release would require changing a security setting merely to make startup
  pass;
- reconciliation has an unexplained critical exception;
- outbox backlog is increasing and the responsible handler is unknown;
- the prior release or rollback path is unavailable;
- clone/smoke results cannot be reproduced; or
- any operator is uncertain which directory, site, node, database, or country
  cell a command would affect.

Never copy a local `appsettings.json`, private key, connection string, fixture
credential, upload directory, or log directory into the release package. Never
make the new package writable so that it can “fix itself.”

## Build and package procedure

1. Start from a clean checkout of the reviewed commit.
2. Restore with the pinned .NET SDK and locked/reviewed package graph.
3. Build and test in release mode. Treat warnings promoted by the repository as
   failures; do not suppress a new analyzer or security failure in the release.
4. Generate the reviewed OpenAPI artifact and verify its SHA-256 sidecar.
5. Publish into a new, isolated staging directory. Never publish over a running
   application's directory.
6. Verify the package excludes source, tests, development settings, `bin`/`obj`
   history, logs, dumps, uploads, fixtures, keys, and credentials.
7. Generate a manifest of files and cryptographic hashes. Store it with the
   release evidence.
8. Run the packaged binary against disposable, aligned databases with outbound
   providers disabled or replaced by approved fakes.
9. Exercise startup, liveness, readiness, JWKS, security headers, correlation
   IDs, OpenAPI, authentication, one idempotent mutation, outbox dispatch, and a
   representative country-scoped read.

The package that passes these checks is the package that is promoted. Rebuilding
after approval creates a different artifact and restarts the evidence chain.

## Configuration gate

Compare the production configuration **shape** with the options bound by the
release. Check required fields, optional features, provider selection, timeouts,
limits, paths, and case-sensitive names. This is a schema comparison, not an
excuse to expose values.

Verify in particular:

- JWT signing references identify the intended protected key and algorithm;
- previous public keys required for token rollover are present;
- data-protection keys persist outside the application directory and are
  encrypted at rest;
- database, cache, queue, object-storage, messaging, and telemetry credentials
  use protected files, workload identity, or an approved secret manager;
- selected providers have the least privileges and required region/configuration;
- unconfigured optional canaries are disabled rather than logging warnings every
  minute;
- security policy strings remain literal and were not rewritten by a generic
  serializer; and
- logging cannot include authorization headers, query tokens, message bodies,
  phone numbers, email addresses, document paths, or connection strings.

Validate the actual configuration as the application-pool identity. A file that
an administrator can read may still be inaccessible to the service process.

## Pre-deployment baseline

Immediately before the change, record:

- UTC time and approved change reference;
- current commit/package hash and API-reported build identifier;
- schema version and control/country fingerprints;
- node count and traffic state;
- request rate, error rate, and p50/p95/p99 latency;
- database connections, waits, and pool saturation;
- Valkey reachability and latency;
- queue depth, outbox pending/failed count, oldest lag, and worker heartbeat;
- accounting reconciliation timestamp and exception count; and
- required-provider and canary status.

Use dashboards and bounded metadata queries. Do not paste raw payloads into the
change record.

## Deployment procedure

1. Announce the start of the change window and freeze unrelated deployments.
2. If schema alignment is required, complete the reviewed expand-first change and
   its verification. Do not switch the binary while DDL is still running.
3. Remove one node from traffic or drain the single node. Allow in-flight requests
   a bounded period to complete.
4. Stop the application cleanly. Confirm the worker heartbeat stopped for the
   intended node and that no fixture, repair, or schema process remains active.
5. Place the immutable package in a new versioned directory.
6. Attach only approved configuration and protected-key references. Preserve
   ACLs; do not inherit broad write permission from a staging folder.
7. Point the site/service to the new directory and start **one** node.
8. Confirm the process identity, reported version, content root, and environment.
9. Check liveness. If it fails, capture sanitized startup evidence and roll back.
10. Check readiness. Diagnose any degraded item with the
    [readiness triage runbook](readiness-triage.md); do not disable the check.
11. Run the smoke matrix below against the canary node.
12. Observe at least two normal monitoring windows. Confirm worker lag is stable
    or falling before restoring traffic.
13. Return a small share of traffic, observe, then restore normal traffic in
    stages. Add remaining nodes one at a time and prove their reported package
    hash.

## Production-safe smoke matrix

Use dedicated non-user fixtures and idempotency keys. Cleanup must run in a
`finally` path and leave only sanitized correlation evidence.

| Area | Minimum proof |
| --- | --- |
| Process | liveness and readiness respond with the deployed version |
| HTTP hardening | correlation and required security headers survive 2xx, 4xx, and sanitized 5xx paths |
| Identity | JWKS is valid; login, refresh rotation, and logout revocation behave as designed |
| Tenancy | one authorized country request succeeds; a cross-country attempt is denied coarsely |
| Contract | OpenAPI v1 hash matches the reviewed artifact; no accidental doubled-version route |
| Rate limiting | a dedicated safe endpoint returns the documented `Retry-After` behavior |
| Idempotency | replaying the same safe fixture mutation returns the canonical result without duplication |
| Realtime | SignalR connects through the backplane and reconnects without leaking a query token |
| Durable work | a known outbox event reaches its handler; heartbeat and lag recover |
| Money | read-only balance/reconciliation checks remain clean; no real transfer is improvised |
| Providers | only dedicated canary destinations are used, with sanitized results |

## Failure diagnosis

Separate failures by phase:

- **No process:** package/runtime/ACL/configuration problem.
- **Live but not ready:** schema, database, Valkey, worker, reconciliation, queue,
  or required-provider contract problem.
- **Ready but requests fail:** route, authentication, tenant resolution, proxy,
  CSP/header, dependency, or data-contract problem.
- **Requests succeed but work stalls:** outbox, queue permissions, handler
  registration, worker scope, or provider outcome problem.
- **Only one node fails:** package drift, machine ACL, local certificate/key,
  environment variable, network path, or clock skew.

Do not call a database version “the deployed API version.” Prove binary currency
from the package/commit identity reported by the process.

## Rollback procedure

Rollback is the default when the canary cannot become healthy within the agreed
window or customer/financial safety is uncertain.

1. Remove the new node from traffic and stop it.
2. Capture its package hash, sanitized startup/readiness failure, and change time.
3. Point the service to the previous immutable directory without modifying that
   directory.
4. Restore only the previous configuration contract if the release introduced a
   separately versioned compatible configuration change.
5. Start one prior-version node and prove its version, liveness, readiness, worker
   health, and representative smoke paths.
6. Restore traffic gradually and monitor the same baseline signals.
7. Keep the failed package and evidence quarantined for investigation.

Do not attempt a destructive schema downgrade during an application rollback.
Expand-first changes should remain compatible. If the release performed an
irreversible data change, follow its separately approved recovery plan and hand
control to the incident commander.

## Recovery and verification

The deployment is complete only when:

- every serving node reports the intended commit/package hash;
- readiness is healthy or an explicitly approved optional degradation is visible;
- schema version and fingerprints match the reviewed contract;
- request errors and latency remain within the baseline envelope;
- worker heartbeat is fresh and queue/outbox lag is stable or decreasing;
- reconciliation has no new unexplained exception;
- security headers, JWKS, tenant boundaries, and rate limits pass;
- provider canaries use only dedicated destinations and return sanitized results;
  and
- fixture cleanup is proven.

A green liveness endpoint alone is not completion.

## Evidence to retain

Retain the change reference, operator/reviewer, start/end times, commit, package
manifest and hash, SBOM, tests, OpenAPI hash, before/after schema fingerprints,
configuration-validation result, baseline and recovery metrics, smoke correlation
IDs, node rollout order, alarms, rollback decision, and cleanup result.

Evidence must not contain credentials, private keys, access tokens, connection
strings, fixture passwords, document URLs, customer identifiers, or provider
message bodies.

## Escalation

Escalate immediately to the incident commander and relevant security/financial
owner when there is cross-tenant exposure, signing-key uncertainty, lost audit
durability, an unexplained money mismatch, repeated provider charge, data loss,
or inability to prove which binary served traffic. Keep the affected capability
contained until the owner explicitly accepts recovery evidence.

## Common pitfalls

- Publishing into the live directory leaves a half-old, half-new application.
- Updating the expected schema hash to match an unexpected database hides drift;
  it does not align the schema.
- A service starts under an administrator but fails under the application-pool
  identity because protected-file ACLs differ.
- Restarting workers without checking handler registration repeats poison work.
- A post-commit provider/audit failure may return an HTTP error even though the
  business mutation succeeded; reconcile by idempotency key before retrying.
- Deploying all nodes together destroys the canary and makes rollback ambiguous.
- Treating “the homepage loaded” as a smoke test misses auth, tenancy, worker,
  accounting, and failure-path regressions.
