# Database Architecture

## MySQL as system of record

KiloDrive uses MySQL 8. The canonical database definition is maintained as
idempotent MySQL scripts; EF Core supplies relational mapping and metadata but is
not used to deploy migrations.

The topology consists of:

- one global control database for identity, country routing, global support,
  privacy coordination, global verification metadata, and security audit; and
- one complete operational database per provisioned country cell.

## Country-cell ownership

Each cell owns tenants, credential-free user projections, drivers, vehicles,
rides, bids, trips, deliveries, rentals, wallets, payments, accounting journals,
notifications, local audit, safety evidence, and its outbox. Settlement never
spans databases.

## Model safeguards

- tenant-owned entities have a tenant identifier and query filter;
- transactional/external identifiers use UUIDv7;
- money uses `bigint` minor units and explicit currency;
- timestamps are UTC;
- unique references enforce idempotency;
- foreign keys and indexes are part of the schema contract; and
- soft deletion is used where history, audit, or financial linkage must remain.

## Schema contract

At startup/readiness, normalized table, column, index, and foreign-key metadata is
fingerprinted and compared with the compiled expectation. A country cannot be
activated when its fingerprint drifts. Version strings alone are insufficient.

See [schema-lifecycle.md](schema-lifecycle.md) and
[data-ownership.md](data-ownership.md).
