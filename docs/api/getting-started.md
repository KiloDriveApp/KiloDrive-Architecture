# Getting started with the API

[API Guide](README.md)

## Choose the correct surface

KiloDrive has one authoritative API with several client audiences. The
corporate website reads published country content. Consumer applications
perform authenticated rider, driver and rental workflows. The separate System
Admin app performs restricted operations. Provider integrations send signed
events to dedicated callbacks. Sharing a server does not make these audiences
interchangeable.

| Surface | Typical use | What publication means |
| --- | --- | --- |
| Anonymous information | Country directory, published pages, release information, public membership prices | The operation does not declare bearer security; routing and applicable admission policies still apply |
| First-party consumer | Accounts, trips, wallet, documents, memberships, notifications | A reviewed app session and appropriate user authority are required |
| Organization member | Rental or business account management | Organization membership and role checks apply in addition to authentication |
| Restricted System Admin | People, readiness review, plan management, investigations and operations | Architectural behavior is described publicly; executable administrative contracts stay private |
| Provider callback | Payment and store events | Provider authenticity and durable record reconciliation are required; callback routes are excluded here |
| Future approved partner | A separately agreed integration | No generally available partner access or client-credentials flow is established by this guide |

For a new integration, first agree the purpose, environment, minimum scopes,
country coverage, data handling, rate expectations, support contact and recovery
responsibility with KiloDrive. Use an approved test environment and synthetic
records. Do not turn a documented first-party login into an unattended partner
credential or attempt to emulate native attestation.

## Canonical paths

New clients use `/api/v1/...`. The temporary `/api/...` compatibility aliases
are deprecated and scheduled to sunset on **2027-02-10**. They are not a second
API version. Do not concatenate a base path ending in `/api/v1` with another
`/v1`, and do not depend on redirects to correct an invalid route.

The examples and curated OpenAPI use `https://api.example.invalid`, a reserved
example host with no live service. Obtain the approved environment base URL
through the integration agreement. This prevents an example from becoming an
accidental production request.

## Before a protected request

1. Resolve the approved host and supported country context.
2. Complete the client audience's installation/admission process where required.
3. Complete registration or login, including contact proof or second factor
   when requested by the server.
4. Persist credentials in the platform secure store and restore the session
   before starting protected background work.
5. Read the applicable feature/capability and resource state.
6. For a mutation, persist one logical operation, its original payload and any
   original revision before sending it.
7. Handle the result, or reconcile the same operation if the response is lost.

The generated [reference](reference/README.md) identifies declared headers and
request models. It does not include every middleware admission requirement;
read [access and authentication](access-and-authentication.md).

## Establish a useful first read

Begin with read-only discovery in the approved environment: supported countries,
published capabilities, applicable feature flags and the current app-version
policy. A configured country is not automatically eligible for every feature.
A feature being enabled does not prove provider credentials, legal review,
payment products or native-store availability.

For a user session, verify the session and read an owner-scoped resource such
as the wallet or onboarding state. Show loading, empty and error states
explicitly. A 200 response containing a pending verification or blocked
readiness state is still a pending or blocked business outcome.

## Client implementation expectations

Keep a typed repository between HTTP and UI code. Parse numeric enums through
exhaustive domain-specific registries. Use centralized UTC parsing, locale-aware
display and integer minor-unit money. Scope caches, pending operations and
private media by account, country, session and installation as appropriate.

Only one refresh operation should run for a session at a time. Cancel stale
requests when the user signs out or changes accounts. A late response from an
old session must not overwrite the new session or rebind its push token.

Before release, test permission denials, cold launch, logout during refresh,
lost mutation responses, provider pending states, device changes and accessibility
layouts. Unit tests cannot certify signed native-store purchases, attestation or
provider delivery. See [testing and verification](../quality/testing-and-verification.md).
