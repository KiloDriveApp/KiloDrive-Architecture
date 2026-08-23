# Runbook: Valkey Degradation

## Symptoms

Elevated cache latency, connection errors, command/ACL denials, stale driver
location, SignalR backplane warnings, failed passkey ceremonies, or matching
deduplication degradation.

## Response

1. Classify the affected namespace/capability and confirm MySQL health.
2. For SignalR, keep durable state available and increase bounded client refresh;
   do not claim realtime delivery is healthy.
3. For cache, allow safe cache misses and prevent a database stampede with
   bounded concurrency.
4. For location, expire stale online eligibility rather than matching from an
   old sample.
5. For passkey/single-use security state, fail closed and offer another approved
   authentication method.
6. Inspect server health, memory/eviction, network, TLS, credential expiry, and
   ACL/channel permissions.
7. Restore service, then verify cache operations, pub/sub, distributed consume,
   location freshness, and reconnect across two API nodes.

## Prohibited shortcuts

Do not grant broad administrative commands to an application account, disable
authorization, treat a process-local cache as a safe multi-node ceremony store,
or keep drivers online with expired telemetry.
