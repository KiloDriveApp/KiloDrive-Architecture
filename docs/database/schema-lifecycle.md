# Schema Lifecycle

## The goal is parity, not a successful script

A database release is complete when all of these describe the same contract:

- the canonical empty-bootstrap MySQL schema;
- every approved idempotent alignment/update script;
- the API binary's EF relational metadata;
- the normalized metadata in every provisioned control/country database; and
- the recorded schema version and fingerprint.

If one differs, KiloDrive treats it as drift. A script returning exit code zero
only proves that MySQL accepted the statements it saw.

## Why KiloDrive does not deploy EF migrations

EF Core is valuable for mapping, query translation, and describing the expected
relational model. KiloDrive does not use generated migration classes or
`database update` as the production deployment mechanism.

The reasons are practical:

- operators need readable, reviewable MySQL 8 scripts;
- all country cells must be aligned deterministically;
- seed/reference changes and conditional repair need database-native control;
- production scripts must be safely rerunnable after an interrupted rollout;
- clone testing needs the same artifact production will receive; and
- destructive changes need explicit review rather than an ORM-generated guess.

The discipline is stricter: engineers must update model and SQL together.

## Contract contents

The verifier builds a normalized manifest from required EF relational objects:

```text
T|table
C|table|column|normalized_type|nullable
I|table|index|unique|ordered_columns
F|table|constraint|principal|delete_action|columns|principal_columns
```

It sorts the lines ordinally and hashes them with SHA-256. The actual manifest is
read from MySQL `information_schema`. The verifier checks both object parity and
the `KiloDriveSchemaMetadata` row for the expected scope, version, and
fingerprint.

Primary-key shape is represented through model/table design; required secondary
indexes and foreign keys are explicitly compared. Objects outside the compiled
required model do not automatically make the contract valid or invalid, which
is why retirement still needs a separate zero-reference process.

### Why a version string is insufficient

Consider two cells both labelled `vN`:

- Cell A has `AmountMinor bigint NOT NULL`.
- Cell B has `AmountMinor int NULL`.

The version is the same; behavior is not. Fingerprinting normalized types and
nullability exposes the mismatch.

### Configuration is also checked

The protected configured fingerprint must equal the model fingerprint compiled
into the API. This catches a common deployment mistake: a new binary paired with
old app settings, or new app settings paired with an old binary.

Changing the configured hash to whatever production reports is not alignment.
It is bypassing the contract.

## Change classes

| Change | Example | Preferred rollout |
| --- | --- | --- |
| Additive | Nullable column, new table, compatible index | Schema first, then compatible code |
| Backfill | Populate a new normalized column | Bounded batches with progress and resume marker |
| Constraint tightening | Nullable to required, broader to narrower type | Observe/backfill/validate, then enforce |
| Rename | Column or table rename | Expand with new object, dual-read/write if needed, backfill, contract cutover, retire later |
| Destructive | Drop legacy table/column | Zero-reference proof, backup, separate approval, delayed retirement |
| Reference data | New country bank, toll period, vehicle model | Version/effective date and idempotent natural-key upsert |
| Spatial projection | SRID point/index projection | Additive guarded rollout, backfill, compare, enable, fingerprint |

## The standard development workflow

### 1. State the ownership and compatibility impact

Before editing SQL, write down:

- control or country cell;
- tenant scope;
- new/changed reads and writes;
- whether old and new binaries can run against the intermediate schema;
- backfill volume and lock risk; and
- rollback or forward-fix strategy.

This catches cross-cell mistakes earlier than code review.

### 2. Update EF metadata and canonical SQL together

The canonical script must create the final object correctly from an empty MySQL
8 database. The alignment script must bring a previous supported release to the
same result and be safe to rerun.

Do not add an EF migration class “temporarily.” Temporary deployment paths have
a habit of becoming production dependencies.

### 3. Make the SQL genuinely idempotent

`CREATE TABLE IF NOT EXISTS` is not enough. If the table exists with the wrong
column type, the statement succeeds and fixes nothing.

KiloDrive alignment helpers inspect `information_schema` and ensure columns,
indexes, and constraints. A mature script also distinguishes:

- absent object: add it;
- exact object: no-op;
- safely convertible drift: repair under reviewed rules;
- dangerous conflict or data loss: stop with an actionable error.

Reference seeds use stable natural keys and explicit update behavior. Never use
random IDs as the only match criterion for rerunnable catalogue seeds.

### 4. Test an empty bootstrap

Create disposable control and cell databases, run the canonical schema, and
verify the compiled fingerprint. This proves a new environment does not depend
on years of incremental history.

Run the bootstrap twice. The second execution should make no destructive change
and should preserve fingerprints and seed identity.

### 5. Test upgrades from supported prior states

Restore sanitized/disposable snapshots or construct controlled prior-release
schemas. Apply the exact alignment artifact. Compare normalized table, column,
index, foreign-key counts and fingerprints with the empty bootstrap.

One clone per materially different state matters. A schema that has been
manually repaired in the past may fail differently from a clean previous
release.

### 6. Run behavior and crash-point tests

Metadata parity cannot prove accounting or state-transition behavior. Run the
relevant API/integration suite, including:

- concurrent mutation;
- idempotent replay;
- process crash before/after critical writes;
- outbox recovery;
- ledger balance and held-funds reconciliation;
- tenancy and IDOR checks; and
- old/new data compatibility during expand/contract.

### 7. Review generated evidence

The release evidence should record artifact hash, schema version/fingerprints,
clone results, row/backfill counts, test results, backup checkpoint, binary
version, and reviewer approval. Evidence must not contain connection strings or
customer rows.

## Production rollout order

An additive/compatible release generally follows this sequence:

1. Confirm the exact production binary currently deployed. Do not infer it from
   database metadata.
2. Verify backups and restore readiness, not merely that a backup job ran.
3. Put the reviewed SQL artifact and hash in the deployment channel.
4. Apply to a fresh production-like clone and compare the expected fingerprint.
5. Drain or pause only the workers affected by the schema change.
6. Apply the idempotent alignment to control and each intended cell in a defined
   order.
7. Verify actual metadata and `KiloDriveSchemaMetadata` after every database.
8. Deploy the compatible API binary and protected configuration together.
9. Require healthy startup/readiness before resuming workers or country
   activation.
10. Run targeted smoke tests, reconciliation, outbox, and error-rate checks.
11. Observe before performing any later contract/destructive phase.

For a change where new code cannot run on the old schema, redesign toward
expand/contract. Coordinating a simultaneous cutover across many cells is
fragile.

## Startup and readiness behavior

In production, schema validation is enabled and a mismatch prevents startup.
The startup exception includes bounded schema/category details and expected vs.
actual fingerprints, but not credentials.

Readiness verifies control and the selected country contract alongside
operational health such as outbox and wallet reconciliation. Verification
results are cached briefly to avoid querying `information_schema` on every
health probe. The cache key includes server endpoint, port, schema name, version,
and expected fingerprint so one server's result cannot validate another server
that happens to use the same database name.

Outside production, an unreachable database may produce a warning to keep local
work possible. That development convenience must not weaken production.

## Country activation is a schema gate

`CountryShards.IsProvisioned` means the routing directory knows a protected
connection for the cell. It does not by itself mean signup should be active.

Activation requires:

- supported-country rules and a provisioned shard;
- reachable connection and expected fingerprint;
- canonical seeds/reference data;
- tenant and provider configuration;
- backup/restore, monitoring, and operational runbooks;
- legal/financial/privacy approval; and
- smoke and country-switch tests.

If a fresh verification detects drift, keep the country inactive until the
reviewed alignment succeeds. Never disable schema validation to make an
activation deadline.

## Expand/contract example

Suppose a booking currently stores `FuelPercent` and needs separate start/end
values.

1. **Expand:** Add nullable `StartFuelPercent` and `EndFuelPercent`.
2. **Expand:** Deploy code that reads new values when present and falls back to the old
   value; write both during transition.
3. **Expand:** Backfill in bounded batches with a resume marker.
4. **Expand:** Compare old/new values and monitor mismatch.
5. **Contract:** Make required fields non-null only after data-quality proof.
6. **Contract:** Stop reading/writing the old column.
7. **Contract:** Prove no source, compiled binary, report, job, or rollback path
   references it.
8. **Contract:** Drop it in a separately reviewed later release.

This seems slower than renaming in place. It is much faster than recovering from
a half-deployed fleet of API nodes and cells.

## Backfills without outages

- Process deterministic primary-key ranges or time windows.
- Bound each transaction and release locks frequently.
- Persist progress outside process memory.
- Make each batch idempotent.
- Measure rows, duration, lock waits, replication lag, and errors.
- Throttle under real load and support a clean pause.
- Validate counts and semantic invariants, not just non-null values.
- Do not send provider notifications from a historical backfill unless that is
  an explicit, idempotent requirement.

## Destructive change policy

Before dropping an obsolete table or column, prove:

1. no current source reference;
2. no compiled/deployed binary reference;
3. no SQL, report, export, worker, fixture, or runbook reference;
4. no supported rollback binary dependency;
5. no foreign key, view, trigger, event, or scheduled procedure reference;
6. no required data retention or legal hold;
7. backup and tested restore availability; and
8. an observation period at zero reads/writes.

“The table is empty” satisfies none of those by itself.

## Rollback and recovery

Database rollback is usually a compatibility problem, not a reverse-script
problem.

- Additive schema can generally remain while the prior compatible binary is
  restored.
- A failed backfill should pause and resume or be forward-fixed.
- A destructive or data-converting step may require snapshot restore and an
  incident decision; do not improvise against identity or financial data.
- If only one cell fails alignment, keep it out of service while healthy cells
  remain available. Do not stamp the expected fingerprint onto the failed cell.

After recovery, verify actual fingerprint, application readiness, wallet
reconciliation, outbox lag, and affected feature behavior.

## Troubleshooting the familiar startup error

When the API says the schema contract failed:

1. Do not disable `ValidateOnStartup`.
2. Capture the deployed binary version/commit.
3. Capture the protected configured schema version and fingerprints without
   printing other app settings.
4. Run the read-only verifier against control and every provisioned cell.
5. Classify each mismatch: configuration, missing table, column type/nullability,
   index, foreign key, or metadata row.
6. Compare with the reviewed model manifest and alignment script.
7. Reproduce the repair on a disposable clone.
8. Apply the reviewed idempotent alignment.
9. verify again with a fresh (non-cached) check, then start the API.

Repeated `configuration:1 mismatch` messages often mean binary/config hashes do
not agree, not that running the SQL six more times will help. Repeated cell
column mismatches mean the alignment artifact did not create the shape the EF
model expects.

## Frequent mistakes

### Updating only the canonical bootstrap

New environments work, existing cells do not. Every deployed change needs a
reviewed upgrade/alignment path.

### Updating only `full-schema-alignment.sql`

Production upgrades work, a disaster-recovery bootstrap produces an older
schema. Empty and upgraded paths must converge.

### Editing production manually, then documenting it later

The next cell or restore misses the fix, and nobody can prove what happened.
Emergency SQL still needs capture, review, canonical integration, and parity
verification.

### Writing a non-rerunnable procedure

An SSM/network timeout leaves the operator unsure whether it committed. Use
natural-key checks, transactions, resumable phases, and postconditions.

### Copying app settings through a JSON serializer

Some serializers escape policy text or reorder/alter settings. Read and patch
only the intended values through a reviewed method; keep secrets outside source.

### Verifying only the default country

The API verifies all provisioned/built-in cells because a missed country becomes
the next deployment outage. Release evidence should list each checked scope.

## Pull-request checklist

- [ ] Ownership (control or cell) is explicit.
- [ ] Canonical schema creates the final state from empty.
- [ ] Alignment SQL safely reaches the same state from supported prior states.
- [ ] Script is rerunnable and stops on unsafe conflict.
- [ ] EF relational metadata matches SQL types, nullability, indexes, and FKs.
- [ ] Schema version/fingerprints are updated through the reviewed process.
- [ ] Empty bootstrap and upgrade clone fingerprints match.
- [ ] Backfill is bounded, resumable, observable, and reversible/forward-fixable.
- [ ] Tenant, IDOR, idempotency, concurrency, and crash-point tests pass.
- [ ] No table is dropped solely because it is empty.
- [ ] Deployment order, rollback, alerts, and runbook changes are documented.

## Related reading

- [Database architecture](README.md)
- [Data ownership](data-ownership.md)
- [Tenancy and country cells](../architecture/tenancy-and-country-cells.md)
- [Country-cell sharding ADR](../adr/001-country-cell-sharding.md)
- [Schema alignment runbook](../runbooks/schema-alignment.md)
- [Country activation runbook](../runbooks/country-activation.md)
