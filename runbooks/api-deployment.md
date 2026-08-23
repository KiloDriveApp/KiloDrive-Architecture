# Runbook: API Deployment and Rollback

## Preconditions

- reviewed commit and release evidence;
- successful build, unit/integration/contract/security tests;
- reviewed OpenAPI artifact for contract changes;
- production configuration validated without exposing values;
- database snapshot and compatible schema alignment plan;
- previous binary/configuration backup; and
- incident owner and rollback authority identified.

## Deployment

1. Publish an immutable API artifact and compute its SHA-256 hash.
2. Transfer through an authenticated, encrypted deployment channel.
3. Drain the application pool/node from new traffic.
4. Stop/drain worker processes so native and managed files are not locked.
5. Preserve protected `appsettings.json`, signing material, data-protection keys,
   and filesystem ACLs.
6. Replace the application files atomically from a staging directory.
7. Start the node and verify liveness, readiness, schema contract, JWKS, security
   headers, correlation IDs, OpenAPI policy, Valkey, outbox, and worker heartbeat.
8. Compare the deployed assembly hash with the release artifact.
9. Return traffic gradually and watch latency, errors, saturation, queue lag,
   database waits, and provider outcomes.

## Rollback

Drain the node, restore the previous immutable binary and compatible protected
configuration, and re-run verification. Do not roll back across an incompatible
destructive schema change. Use forward correction or a reviewed snapshot restore
when data compatibility is uncertain.

## Evidence

Retain commit, artifact hash, schema fingerprint, timestamps, health results,
operator identity, test summary, and rollback decision—never secret values.
