# Hosting and Deployment Topology

## Current deployment style

The API, portal, and website are independently publishable ASP.NET Core
applications. The production Windows hosting pattern uses IIS as the process and
reverse-proxy host. Cloudflare or another approved TLS edge can sit in front of
public sites. MySQL, Valkey, object storage, dispatch infrastructure, voice, and
telemetry are separate dependencies.

This repository omits hostnames, IP addresses, instance sizes, account IDs,
security groups, and filesystem paths.

## Scale-out

- API nodes are stateless except for explicitly distributed state.
- SignalR uses a Valkey backplane before multiple API nodes are enabled.
- Passkey ceremonies and other cross-node single-use state use a distributed
  store.
- Country routing selects the owning MySQL cell for each request/worker scope.
- EventBridge/SQS can absorb high-throughput dispatch bursts while the SQL
  outbox provides recovery authority.
- Static/media objects are served through authorized object storage paths rather
  than local web roots.

## Release sequence

1. Produce immutable binaries and hashes from a reviewed commit.
2. Back up/snapshot affected data infrastructure.
3. Apply reviewed, idempotent MySQL alignment to controlled clones.
4. Verify empty-bootstrap and metadata fingerprint parity.
5. Align production cells and control plane.
6. Deploy binaries while preserving protected configuration and key material.
7. Verify process health, readiness, schema contract, JWKS, critical contracts,
   outbox, cache, and telemetry.
8. Retain rollback artifacts and sanitized evidence.

## Environment configuration

KiloDrive uses one application settings file per ASP.NET Core application in its
current hosting model, with secrets kept out of public repositories. Production
credentials should preferentially use workload identity, protected machine
files, or a secret manager. Environment-specific JSON copies are not part of the
current API configuration contract.
