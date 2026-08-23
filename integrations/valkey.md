# Valkey Architecture

## Uses

Valkey implements the Redis protocol and serves several separated logical
purposes:

- distributed application and tenant/template cache;
- SignalR scale-out backplane;
- high-frequency driver location telemetry and dirty-set batching;
- single-use cross-node passkey ceremonies;
- matching deduplication and short-lived dispatch state; and
- other bounded ephemeral coordination.

Key namespaces and exact TTLs are private implementation details. They include
tenant/account/entity scope and never use contact details or access tokens as
human-readable keys.

## Durability expectations

Valkey is not the financial or trip system of record. Durable state is persisted
to MySQL. Some operations can fall back safely or reconstruct cache; security
ceremonies that require atomic cross-node consumption fail closed when the
distributed store is unavailable.

## Access control

Runtime identities receive only required command and channel permissions.
SignalR requires publish/subscribe access to its dedicated namespace. General
cache, location, and administration privileges should not be granted to the hub
backplane account.

## Operations

Monitor latency, connection failures, memory pressure, eviction, replication,
persistence health where enabled, command denials, and SignalR pub/sub errors.
Scale-out is enabled only after the backplane and distributed security-state
tests pass.
