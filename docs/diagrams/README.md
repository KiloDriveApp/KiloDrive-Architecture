# Learning Diagrams

These diagrams provide compact views of flows that span several chapters. They
are intended as conversation starters during onboarding, design review, and
incident response—not as substitutes for the state machine, schema, or runbook.

- [Request and side-effect lifecycle](request-lifecycle.md)
- [Ride bidding lifecycle](ride-bidding-lifecycle.md)
- [Country-cell ownership](country-cell-ownership.md)
- [Wallet and accounting flow](wallet-accounting-flow.md)

## How to use them

For a design review, trace one real command across a diagram and ask at each
arrow:

1. What proves the caller may do this?
2. Which component owns the authoritative state?
3. Can this arrow happen twice?
4. What if the caller disappears immediately after it succeeds?
5. How does an operator prove the final result without reading a sensitive
   payload?

For an incident, mark the last durable fact you can prove. Everything after
that point is a hypothesis until supported by an outbox row, provider ID,
entity version, journal, or sanitized trace.

A diagram is a map, not the territory. The linked chapter explains
authorization, durability, idempotency, privacy, and failure behavior in full.
