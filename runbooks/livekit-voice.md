# Runbook: LiveKit Voice and Recording

## Call failure

1. Determine whether token issuance, signalling, TURN/media, push ring, mobile
   background state, or room authorization failed.
2. Validate a non-user token/room canary and TURN reachability from representative
   networks.
3. Check LiveKit resource saturation, packet loss, jitter, bandwidth, and TLS.
4. Preserve GSM fallback where the plan and trip policy permit it.
5. Verify foreground, background, killed launch, network handoff, decline,
   timeout, reconnect, and orphan cleanup after recovery.

## Recording failure

1. Confirm recording was authorized and consented.
2. Inspect the durable recording outbox and current egress state.
3. Reconcile existing egress before starting another job.
4. Verify private encrypted S3 output and safe audit metadata.
5. If output is partial/unknown, mark it for review; never represent it as a
   complete recording.

Do not log tokens, room secrets, audio paths, participant contact data, or media
payloads.
