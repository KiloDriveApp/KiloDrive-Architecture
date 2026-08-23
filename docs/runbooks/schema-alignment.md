# MySQL schema alignment runbook

- **Owner:** Database engineering with API and release owners
- **Status:** Operational schema-change procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Tenancy and country cells](../architecture/tenancy-and-country-cells.md) and [schema lifecycle](../database/schema-lifecycle.md)

## Purpose and scope

Use this runbook to reconcile KiloDrive's canonical MySQL 8 schema, approved
update scripts, EF Core model expectations, configured schema contract, and live
control/country metadata. It applies to `kilodrive_control` and every configured
country cell—not only the current worker cell.

KiloDrive deploys schema changes with reviewed idempotent MySQL scripts. EF model
metadata is an input to comparison, not a deployment mechanism. Do not generate
or apply EF migrations.

## Authorities and precedence

Alignment compares five sources:

1. canonical empty-bootstrap schema;
2. every approved update/alignment script in deployment order;
3. EF model metadata used by the target API binary;
4. configured schema version and expected control/cell fingerprints; and
5. normalized `information_schema` metadata from control and all country cells.

No single source is automatically right when they disagree. The team reviews the
intended contract, corrects source and scripts, proves it on clones, and only then
changes production.

## Owners and roles

| Role | Responsibility |
| --- | --- |
| Schema change owner | Describes intended contract and data/backward-compatibility effect |
| Database operator | Captures metadata/backups and applies the exact reviewed script |
| API owner | Identifies binary/model expectations and validates startup/contracts |
| Reviewer | Reviews DDL, data preconditions, idempotency, lock/runtime risk, and rollback |
| Financial/privacy owner | Approves changes affecting ledgers, holds, evidence, retention, or deletion |
| Release lead | Sequences schema and binary, controls stop/go, retains evidence |

## Preconditions

- The target API commit/package is identified independently of database version.
- The database topology and complete configured cell list are known.
- A least-privilege read-only metadata path exists for discovery.
- Disposable MySQL 8 clones can represent empty bootstrap and upgraded production
  shapes without exposing real customer data.
- Backup and restore procedures are current and tested for material DDL.
- No unrelated schema, fixture reset, or deployment process is active.
- The change has explicit expand/contract sequencing and previous-binary
  compatibility where rolling deployment is used.

## Safety and stop conditions

Stop immediately when:

- a command target, database name, server, or script hash is ambiguous;
- backups or restore instructions are missing for a material change;
- actual metadata differs from the clone/input used for review;
- destructive DDL lacks zero-reference, data, retention, and rollback proof;
- a second schema/deploy/fixture job is active;
- the script depends on manual editing, current default database, unresolved
  variables, or implicit object order;
- a cell reports an error or a post-step fingerprint differs; or
- the proposed “fix” is to change configured expected hashes to unexpected live
  values.

Never drop a table because it is empty. Never run an unreviewed “full alignment”
script first on production. Never print connection strings or customer data in
evidence. Never assume DDL rollback is transactional.

## Phase 1: identify the target contract

1. Record target API commit/package hash and schema-contract version.
2. Generate or inspect EF relational metadata from that exact binary/source.
3. Apply canonical bootstrap plus every approved update to a fresh empty MySQL 8
   environment.
4. Normalize its tables, columns, types, nullability, defaults, collations,
   generated expressions, indexes/order, unique constraints, foreign keys/actions,
   spatial SRIDs, views, triggers, routines, and events.
5. Compute expected control and cell fingerprints using the same reviewed
   algorithm as startup validation.
6. Compare the result with the configured version/fingerprints. Correct source
   artifacts before touching live databases.

The expected fingerprint is a checksum of a reviewed structure, not a number to
copy from whichever database happens to run.

## Phase 2: capture live metadata read-only

From a controlled bastion or approved operator host, collect for control and every
configured cell:

- MySQL version, SQL mode, timezone, character sets, and collations;
- schema version/fingerprint records;
- table, column, index, unique, FK, view, trigger, routine, event, and spatial
  counts;
- the exact normalized definitions used by the fingerprint;
- table sizes and bounded row counts needed for DDL risk;
- FK/index coverage and normalized duplicate-table candidates; and
- active sessions/long transactions relevant to the maintenance window.

Use read-only credentials and retain hashes/metadata, not row contents. Compare
names case-exactly because filesystem and lower-case-table settings can differ
between development and production.

## Phase 3: classify every difference

Do not jump from “17 mismatches” to a generic script. Classify each difference:

| Class | Example | Treatment |
| --- | --- | --- |
| Missing required object | new column/index/FK | reviewed expand DDL plus data/default plan |
| Incompatible definition | nullability, precision, collation, FK action | assess data and binary compatibility before alter |
| Unexpected extra object | old column/table/index | keep unless explicit contract/zero-reference retirement is approved |
| Data precondition | nulls before `NOT NULL`, duplicates before unique | bounded validation and reviewed data repair |
| Seed/reference drift | missing country rules or wrong encoding | separate idempotent reviewed seed repair |
| Fingerprint bug | normalizer differs by server representation | fix/test algorithm; do not mutate schema to suit a bug |
| Configuration mismatch | expected version/hash is stale after approved contract | update reviewed config artifact only after proving canonical result |

Decimal precision, `longtext` nullability, default expressions, index column
order, collation, and FK delete behavior are meaningful. A superficially similar
table can still violate the model.

## Phase 4: produce one reviewed idempotent script

The alignment script should:

- identify its contract version and hash;
- set connection character encoding explicitly where text seeds are included;
- use explicit schema/object names;
- test whether each change is needed;
- validate data preconditions before narrowing/unique/FK changes;
- fail on unexpected shape rather than guessing;
- avoid table drops/renames in the expand phase;
- record a schema version only after all required checks succeed; and
- finish by emitting safe verification metadata.

Review expected lock duration, online/in-place algorithm support, temporary disk,
replication impact, and application compatibility. Split large backfills from DDL
when needed, with a restartable cursor and bounded batches.

## Phase 5: prove empty and upgraded parity

Use two disposable paths:

### Empty path

Create empty control/cell databases, apply canonical bootstrap and all approved
updates exactly as a new environment would.

### Upgrade path

Restore sanitized structural clones representative of the live versions, then
apply the proposed alignment.

For each path:

1. run alignment once;
2. recompute normalized metadata and fingerprints;
3. run alignment a second time and prove no further change;
4. compare empty and upgraded fingerprints/definitions;
5. start the target API and require valid readiness;
6. run canonical fixture, financial, ride/bid, rental, support/privacy, and
   authorization tests; and
7. retain failures and exact script hash.

If empty bootstrap and upgraded clone differ, the canonical schema/history is
still broken even if one production cell starts.

## Phase 6: production execution

1. Open the approved change and record before-state package/schema/fingerprints.
2. Confirm tested backups and restore instructions.
3. Freeze unrelated deploy/schema/fixture work.
4. Assess active traffic/transactions and enter the approved maintenance or
   expand-first mode.
5. Verify the exact script hash matches the reviewed clone-tested script.
6. Apply to `kilodrive_control` when the contract requires it. Stop on any error.
7. Recompute and record control metadata/fingerprint before moving on.
8. Apply to country cells one at a time in the documented order. After each,
   recompute fingerprint and stop on the first mismatch.
9. Run the script a second time only after first-run success, proving idempotency.
10. Start one target API canary and validate schema startup/readiness.
11. Run bounded representative smoke tests and observe database waits, errors,
    workers, outbox, and reconciliation.
12. Restore traffic gradually through the
    [API deployment runbook](api-deployment.md).

Do not continue to later cells because “they probably have the same issue.” One
cell error is a stop condition.

## Diagnosing common fingerprint output

### Repeated `configuration:1 mismatch`

Compare the configured version/hash location and precedence. The table schema may
be right while each environment reads a stale setting. Prove configuration
sources without printing sensitive values.

### Same mismatch count across several cells

This often points to a missing shared historical update. Compare the first few
normalized differences, not only hashes. Do not assume copying one cell's DDL is
safe until all data preconditions match.

### One active cell passes, inactive cells fail

Inactive/provisioned cells still need alignment or must remain explicitly
inactive with activation blocked. Leaving drift for “later” causes the next
country launch to fail under pressure.

### Expected and actual definitions look similar

Inspect full precision/scale, nullability, default expression, collation,
generated column, spatial SRID, index order/prefix, and FK action. MySQL metadata
normalization must be deterministic across supported server versions.

## Failure recovery

On any error:

1. stop; record UTC time, database, statement/step ID, MySQL error, and sanitized
   metadata;
2. determine whether the DDL completed, partially completed, or was atomic;
3. keep the application/affected country out of unsafe traffic;
4. do not blindly rerun a partially destructive operation;
5. reproduce the exact state on a clone;
6. correct the canonical source/script, repeat both parity paths, and obtain
   review; then
7. resume only from a proven idempotent state, or restore if integrity cannot be
   demonstrated.

## Rollback strategy

Prefer expand-first schema so the previous application remains compatible. If
the binary fails after a successful compatible expansion, roll back the binary,
not the schema.

Destructive contract cleanup happens in a later release after zero-reference and
data-retention proof. If a destructive operation fails and integrity is uncertain,
restore through the [backup and recovery runbook](backup-and-recovery.md); do not
improvise reverse DDL.

## Verification criteria

Alignment is complete only when:

- control and every configured/provisioned cell report the intended version and
  fingerprint;
- expected canonical, empty bootstrap, upgraded clone, and production normalized
  definitions agree;
- the script's second run produces no change;
- target API startup/readiness passes without bypass;
- previous binary compatibility is proven where required by rollout;
- critical fixture, accounting, ride/bid, rental, privacy, and auth tests pass;
- database waits/locks and application errors return to baseline; and
- country activation remains blocked on any future drift.

## Evidence to retain

Retain change ID, roles/review, target commit/package, MySQL/config versions,
before/after table/index/FK counts, normalized difference summary, expected/actual
fingerprints, exact script hash/output, backup/restore proof, empty/upgraded clone
results, idempotency result, API readiness/smoke correlation IDs, timing/lock
metrics, rollback decision, and follow-up owner.

Never retain connection strings, passwords, customer rows, private hostnames, or
full sensitive configuration.

## Escalation

Escalate data loss, financial-table drift, broken FK/journal integrity,
cross-country misrouting, unexpected destructive DDL, inability to restore, or a
schema normalizer defect affecting startup to incident command and the relevant
financial/privacy/security owner.

## Common pitfalls

- Treating EF migrations as the deployment path in a script-managed system.
- Updating only the worker cell and ignoring other provisioned cells.
- Fixing configuration hashes before proving canonical metadata.
- Dropping empty legacy tables without code/FK/view/routine/report references.
- Assuming MySQL DDL rollback behaves like an application transaction.
- Testing only an upgraded database and never a fresh bootstrap.
- Running two alignment processes concurrently.
- Omitting `SET NAMES utf8mb4` from standalone text/reference scripts.
- Recording “schema matched” without retaining normalized counts and hashes.
