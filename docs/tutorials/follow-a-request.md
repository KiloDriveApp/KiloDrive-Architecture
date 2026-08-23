# Tutorial: Follow a Request from Tap to Durable State

This tutorial follows a fictional `Accept offer` action. The names are generic;
the important part is the sequence. Use the same method for trip cancellation,
wallet transfer, document review, or membership change.

## 1. The mobile app prepares a command

The button is only enabled when the screen has the data needed to describe the
action. Client validation improves usability, but it is not a security control.
A modified client can skip it.

For a retry-sensitive mutation, the app creates an idempotency key and keeps it
for that logical attempt. A second tap caused by an uncertain response reuses
the key; an intentionally different action receives a new key. Reusing one key
for unrelated payloads should produce a contract error, not silently replace
the first command.

The client also sends its authenticated session and current entity version when
the contract requires optimistic concurrency. It does not send secrets in the
URL.

## 2. Edge and middleware establish context

The edge terminates public TLS and applies broad abuse controls. The API still
authenticates and authorizes every request; a WAF is not an authorization
layer.

Middleware validates or creates a correlation ID early enough that it survives
both successful and error responses. Proxy-provided client IP headers are
trusted only when requests came through the configured trusted boundary.

The request then acquires:

- authenticated global user identity;
- authorized country/cell context;
- tenant context where the resource is tenant-scoped;
- active System Admin workspace where privileged cross-tenant access is
  explicitly supported; and
- rate-limit and idempotency context.

Ordering matters. If tenant resolution happens after a tenant-aware limiter,
the limiter cannot actually partition by tenant. If model validation performs
expensive lookup before authorization, anonymous callers can trigger work they
should never reach.

## 3. The handler revalidates current truth

The server does not trust the screen that originally displayed the offer. Time
has passed. Inside the protected operation it rechecks the states that matter:

- the request is still open;
- the bid is still actionable;
- the expected version matches;
- the driver is online and not already assigned;
- licence, vehicle, document, membership, duty, and trust requirements still
  pass; and
- the selected vehicle is still the compliant primary vehicle.

This is where a common marketplace race is settled. Two users may see an open
offer, but only one locked conditional transition can win.

## 4. One country-cell transaction commits the result

The handler uses a short transaction. It changes the authoritative rows,
increments persisted entity versions, snapshots mutable safety evidence, writes
timeline/audit intent where applicable, and inserts durable outbox messages.

The transaction does **not** call push, email, maps, or a webhook while holding
row locks. Slow provider calls inside a financial or assignment transaction
increase contention and create ambiguous commit behavior.

The outbox row is part of the same commit. This gives a useful guarantee:

> If the assignment exists, a durable record requesting its side effects also
> exists.

It does not guarantee that every side effect already happened.

## 5. The API returns the committed representation

The response includes the correlation ID and required security headers even if
the handler returns a domain error. Expected conflicts use a stable error code;
they do not expose exception text or SQL details.

If the client disconnects just after commit, the server must not use the HTTP
cancellation token to abandon durable post-commit work. The client may see an
unknown outcome. It reconciles by retrying with the same idempotency key or
fetching current state.

## 6. Workers deliver side effects

An isolated worker scope claims the outbox row. Depending on the event, it may:

- publish a versioned SignalR event;
- enqueue or deliver a push notification;
- publish to the dispatch bus;
- create sanitized audit evidence; or
- schedule another durable action.

Handlers are idempotent because worker retries are normal. A crash can occur
after an external provider accepted a request but before the local row was
marked complete. Provider idempotency or reconciliation must settle that
unknown result before another non-idempotent request is sent.

## 7. The other device merges and reconciles

Realtime delivery is the fast path. The receiving notifier merges the event
only when its persisted entity version is newer than the local version. It
keeps a fallback refresh path for reconnect, app resume, or suspected gaps.

The event should help the screen update; it should not contain more private
data than the recipient needs. The subsequent authorized query returns the full
representation.

## Where failures appear

| Observation | Likely boundary | First question |
| --- | --- | --- |
| Request never reaches API trace | device, DNS, edge, or TLS | Does the client have a correlation ID or only a local failure? |
| API returns conflict | domain/version/idempotency | Did current state legitimately change? |
| Database changed, peer screen stale | outbox, hub, backplane, subscription, or client merge | Is the durable event pending, failed, or completed? |
| Push arrives but screen is stale | realtime/client refresh | Did the app route the notification but fail to reconcile? |
| Client shows failure but state changed | post-commit exception or lost response | Was the command retried with the same idempotency key? |

## The lesson

A request is a chain of independently observable boundaries. Trace each
boundary in order. Jumping directly from “the button did nothing” to “the
database is broken” wastes time and can make recovery dangerous.

Next: [investigate a stale realtime screen](investigate-stale-realtime.md).
