# Schema Lifecycle

## Change process

1. Change EF relational metadata and the canonical MySQL schema together.
2. Update reviewed, rerunnable alignment SQL; do not generate EF migrations.
3. Compare canonical schema, approved update scripts, EF metadata, and normalized
   `information_schema` fingerprints.
4. Apply to disposable MySQL 8 clones from both empty and previous-release state.
5. Prove empty-bootstrap and upgrade parity.
6. Review destructive operations separately; an empty table is not evidence it
   can be dropped.
7. Snapshot production, apply the idempotent script, verify fingerprints, then
   deploy/enable the compatible binary.

## Startup behavior

The API validates the configured schema contract in production. A missing or
incompatible object fails readiness or startup according to the protected
configuration. Error output identifies metadata categories without exposing
connection strings.

## Country activation gate

Activation requires a provisioned shard record, reachable connection, expected
contract version/fingerprint, required seed/catalogue data, and approved country
policy. Drift forces the cell out of activation until reconciled.

## Rollback

Prefer forward-compatible additive changes and expand/contract releases.
Rollback means restoring the previous compatible binary and, only when reviewed,
restoring data from a protected snapshot. Never run an improvised reverse script
against financial or identity data.
