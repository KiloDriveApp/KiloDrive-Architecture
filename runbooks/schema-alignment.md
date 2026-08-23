# Runbook: Schema Alignment

## Trigger

Startup/readiness reports schema drift, a new relational model is approved, or a
country cell is being provisioned.

## Procedure

1. Freeze unrelated schema work and identify the exact release commit.
2. Compare canonical MySQL scripts, approved updates, EF relational metadata,
   and normalized control/cell `information_schema` output.
3. Classify every mismatch: missing object, type/nullability, index, foreign key,
   collation/encoding, seed, or unexpected extra object.
4. Generate/review one idempotent alignment script. Do not drop an object because
   it is empty.
5. Apply from empty and previous-release disposable MySQL 8 clones.
6. Prove equal normalized fingerprints and run canonical fixtures/tests.
7. Snapshot production.
8. Apply to control and each intended country cell from a controlled bastion.
9. Re-run counts, fingerprints, foreign-key checks, encoding checks, and API
   readiness.
10. Record sanitized evidence and close the change only after every cell agrees.

## Failure handling

Stop on the first SQL error. Do not edit schema metadata to conceal drift. Restore
from snapshot only when forward repair is riskier and the restore plan preserves
all post-snapshot transactions.
