# Consumer 1.0.0+260 — active navigation and pickup recovery

Reviewed 3 November 2026. The committed source revision and independent client
versions are recorded in the [current baseline](../current-baseline.md).
Store approval, deployed server state and physical-device certification remain
separate evidence. Earlier releases retain their dated records.

## What changed

Drivers can keep navigation inside KiloDrive. The active navigation view uses
the native navigation SDK for route guidance, a tilted heading-up follow
camera, route overview, manual map exploration and recentering. Full-screen
navigation retains speed and ETA; returning to trip details keeps lifecycle
actions separate from map guidance. Before boarding, the navigation destination
is the booked pickup. After the driver starts the trip, it is the drop-off.

Audio preference follows the authenticated trip between embedded and
full-screen views. It is applied before route guidance starts. Rerouting and
navigation errors clear obsolete estimates instead of leaving the old route's
ETA or arrival indication on screen. A genuine fresh stationary observation
can show zero speed; missing or stale location does not become a fabricated
zero or a precise ETA.

The arrival radius is an administrator-managed setting evaluated against the
effective membership for that trip's provider context. The server remains the
authority for arrival eligibility. Membership does not approve documents,
change account access, or automatically begin or complete a journey.

Pickup recovery explains that a booked pickup is a fixed meeting point. An
assigned driver can use the permitted cancellation flow when the trip cannot
proceed. Active-job cards open their trip and expose a short support reference;
that reference is an identifier, never authorization to retrieve private data.

Community road advisories are filtered for the current route, freshness and
direction. Icons and optional spoken advisories supplement navigation. They
are not a complete hazard database or a guarantee that a road is clear.

## Operational ownership

The client owns camera state, audio presentation and SDK recovery. The API
owns participant access, trip lifecycle, effective membership policy and
payment outcomes. Native navigation failure must leave the trip recoverable;
it cannot manufacture arrival, payment, collection or completion evidence.

Use the [active-navigation runbook](../runbooks/active-navigation.md) for SDK
configuration checks, diagnosis, containment, rollback and verification.
The [geospatial chapter](geospatial.md) describes the wider location boundary.

## Published guidance and verification limits

The End User and Transportation Provider manuals explain fixed pickups,
navigation controls and recovery, with actual Android screenshots in phone
frames. Their illustration ledger preserves each capture's original build;
an earlier screenshot is not relabelled as a newer device test.

Automated navigation tests cover audio handoff, account isolation, rerouting
and interrupted-operation recovery. Stationary Android UI checks can verify
layout and controls. They do not certify real-road routing, audible guidance
while driving, weak-connectivity travel, or native iPhone behavior. These need
their own device and journey evidence before broader claims are made.

The [public build-260 notes](https://kilodrive.com/changelog/1.0.0/build/260)
describe the customer-facing changes. Publication of those notes or manuals
does not mean Apple or Google has approved a corresponding binary.

[Current baseline](../current-baseline.md) ·
[Mobile release runbook](../runbooks/mobile-release.md) ·
[Build-250 history](release-1.0.0-250.md)
