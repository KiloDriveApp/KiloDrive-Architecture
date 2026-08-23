# Runbook: Realtime and SignalR

## Symptoms

Delayed bids/offers, missing chat, stale ride removal, reconnect loops, viewer
count lag, cross-node inconsistency, or Valkey pub/sub permission errors.

## Procedure

1. Confirm the domain mutation and durable lifecycle/outbox event committed.
2. Compare entity versions on server and clients.
3. Validate hub authentication, trip/role scope, participant authorization, and
   token expiry without logging the token/query string.
4. Check Valkey reachability, channel ACL, backplane errors, API-node count, and
   connection saturation.
5. Verify the client reconnect and bounded polling recovery path.
6. Test two clients through create/change/withdraw/replace/accept/chat/cancel with
   disconnect, retry, background, and node-switch races.

Do not repair realtime by bypassing domain authorization or treating viewer-feed
polling as explicit per-ride visibility.
