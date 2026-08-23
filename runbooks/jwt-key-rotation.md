# Runbook: JWT Signing-Key Rotation

## Planned rotation

1. Generate a new RSA or EC private key in a protected environment.
2. Assign a unique `kid`; protect the private key with machine ACL/workload
   secret access.
3. Publish the new public key in JWKS while retaining the previous public key for
   the bounded access-token overlap.
4. Deploy signing configuration and verify newly issued tokens use the new
   algorithm/key ID.
5. Verify current and previous tokens according to the rotation window.
6. After all previous tokens expire, remove the old public key and destroy/archive
   old private material according to policy.

## Emergency rotation

Treat suspected private-key exposure as a security incident. Replace the key,
increment token versions or revoke sessions as required, shorten overlap, notify
stakeholders, and preserve evidence. Never fall back to a shared symmetric secret
for production convenience.
