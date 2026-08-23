# Runbook: Backup and Recovery

## Backup scope

Backups cover the identity control database, every active country cell, protected
object metadata/content according to class, configuration, key metadata, and the
release/schema evidence needed to recreate a compatible application.

## Recovery sequence

1. Declare incident scope and stop writes where consistency requires it.
2. Select a tested recovery point and compatible application/schema version.
3. Restore control and affected cells into isolated infrastructure.
4. Validate integrity, foreign keys, schema fingerprints, ledger balance,
   outbox state, identity/cell memberships, and object references.
5. Reconcile events and provider outcomes after the recovery point.
6. Run safe fixture and authorization checks.
7. Cut over gradually, verify readiness, and retain the old environment until
   acceptance completes.

Cross-database restore timing matters: do not expose an identity/control state
that authorizes a missing or older country projection without reconciliation.
Exact RPO/RTO and backup locations are private.
