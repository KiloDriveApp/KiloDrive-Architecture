# Field dictionary: V

[Dictionary index](README.md) · [API Guide](../README.md)

Requiredness and nullability below are schema metadata, not a replacement for
workflow validation. Monetary amounts use integer minor units; timestamp fields
use strict UTC parsing. Private tokens, passwords, document references and
personal fields must remain outside public logs and examples.

## Vehicle

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |
| `ownerUserId` | `string (uuid)` | No | Not declared nullable | Identifier of the related owner user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `ownerUser` | [User](u.md#user) | No | Not declared nullable | Owner user represented by the `User` model or enum; use that definition's fields/values. | No further constraint recorded |
| `driverProfileId` | `string (uuid)` | No | Explicitly allowed | Driver-profile record associated with this operation or result. | No further constraint recorded |
| `driverProfile` | [DriverProfile](d.md#driverprofile) | No | Not declared nullable | Driver profile represented by the `DriverProfile` model or enum; use that definition's fields/values. | No further constraint recorded |
| `vehicleCategoryId` | `string (uuid)` | No | Not declared nullable | Identifier of the related vehicle category record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `vehicleCategory` | [VehicleCategory](v.md#vehiclecategory) | No | Not declared nullable | Vehicle category represented by the `VehicleCategory` model or enum; use that definition's fields/values. | No further constraint recorded |
| `make` | `string` | No | Explicitly allowed | Vehicle manufacturer name/catalog selection. | No further constraint recorded |
| `model` | `string` | No | Explicitly allowed | Model in the owning domain; for vehicle contracts, the vehicle model associated with the manufacturer. | No further constraint recorded |
| `year` | `integer (int32)` | No | Not declared nullable | Numeric year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `color` | `string` | No | Explicitly allowed | Color text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `plateNumber` | `string` | No | Explicitly allowed | Country-specific vehicle registration plate; validate through the applicable country workflow. | No further constraint recorded |
| `conditionCode` | `string` | No | Explicitly allowed | Condition code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `vinChassis` | `string` | No | Explicitly allowed | Vehicle VIN/chassis identification data; keep the actual value private and within authorized views. | No further constraint recorded |
| `registrationExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for registration expires at; parse strictly and localize only for display. | No further constraint recorded |
| `fitnessExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for fitness expires at; parse strictly and localize only for display. | No further constraint recorded |
| `interiorImageFileRef` | `string` | No | Explicitly allowed | Interior image file ref text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `frontExteriorImageFileRef` | `string` | No | Explicitly allowed | Front exterior image file ref text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `isActive` | `boolean` | No | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | No further constraint recorded |
| `allowsPets` | `boolean` | No | Not declared nullable | Whether allows pets applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `childSeatCapacity` | `integer (int32)` | No | Not declared nullable | Numeric child seat capacity for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `isWheelchairAccessible` | `boolean` | No | Not declared nullable | Whether is wheelchair accessible applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `isAirportPickupEligible` | `boolean` | No | Not declared nullable | Whether is airport pickup eligible applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `verificationStatus` | [VehicleVerificationStatus](v.md#vehicleverificationstatus) | No | Not declared nullable | Current vehicle verification enum; a saved vehicle is not automatically approved for work. | No further constraint recorded |
| `verificationNote` | `string` | No | Explicitly allowed | Human-readable verification decision/reason for the vehicle. | No further constraint recorded |
| `verifiedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for verified at; parse strictly and localize only for display. | No further constraint recorded |
| `insuranceStatus` | [InsuranceStatus](i.md#insurancestatus) | No | Not declared nullable | Insurance review/status enum; an uploaded policy is not automatically current confirmed coverage. | No further constraint recorded |
| `insuranceProviderId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related insurance provider record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `insuranceProvider` | `string` | No | Explicitly allowed | Insurance provider text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `insurancePolicyNumberLast4` | `string` | No | Explicitly allowed | Masked last-four insurance policy identifier; not the full policy number. | No further constraint recorded |
| `insuranceEffectiveAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for insurance effective at; parse strictly and localize only for display. | No further constraint recorded |
| `insuranceExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for insurance expires at; parse strictly and localize only for display. | No further constraint recorded |
| `isArchived` | `boolean` | No | Not declared nullable | Whether is archived applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `archivedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for archived at; parse strictly and localize only for display. | No further constraint recorded |
| `documents` | [DriverDocument](d.md#driverdocument)[] | No | Explicitly allowed | Collection of documents for this model; interpret each item through the declared item type. | No further constraint recorded |
| `driverAssignments` | [VehicleDriverAssignment](v.md#vehicledriverassignment)[] | No | Explicitly allowed | Collection of driver assignments for this model; interpret each item through the declared item type. | No further constraint recorded |
| `odometerReadings` | [VehicleOdometerReading](v.md#vehicleodometerreading)[] | No | Explicitly allowed | Collection of odometer readings for this model; interpret each item through the declared item type. | No further constraint recorded |
| `maintenanceSchedules` | [VehicleMaintenanceSchedule](v.md#vehiclemaintenanceschedule)[] | No | Explicitly allowed | Collection of maintenance schedules for this model; interpret each item through the declared item type. | No further constraint recorded |
| `serviceRecords` | [VehicleServiceRecord](v.md#vehicleservicerecord)[] | No | Explicitly allowed | Collection of service records for this model; interpret each item through the declared item type. | No further constraint recorded |
| `defects` | [VehicleDefect](v.md#vehicledefect)[] | No | Explicitly allowed | Collection of defects for this model; interpret each item through the declared item type. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleBiddingEligibilityResult

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `vehicleId` | `string (uuid)` | Yes | Not declared nullable | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `isEligible` | `boolean` | Yes | Not declared nullable | Whether is eligible applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `membershipStatus` | `string` | Yes | Not declared nullable | Membership status text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `vehicleReadiness` | `string` | Yes | Not declared nullable | Vehicle readiness text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `reasons` | [VehicleEligibilityReason](v.md#vehicleeligibilityreason)[] | Yes | Not declared nullable | Collection of reasons for this model; interpret each item through the declared item type. | No further constraint recorded |
| `currentLimit` | `integer (int32)` | No | Explicitly allowed | Numeric current limit for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `currentUsage` | `integer (int32)` | No | Explicitly allowed | Numeric current usage for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `remainingAllowance` | `integer (int32)` | No | Explicitly allowed | Numeric remaining allowance for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `evaluatedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for evaluated at; parse strictly and localize only for display. | No further constraint recorded |
| `stateRevision` | `integer (int64)` | No | Not declared nullable | Revision of the returned state snapshot, distinct from a display timestamp. | No further constraint recorded |
| `policyVersion` | `string` | No | Explicitly allowed | Policy revision used for this assessment; not the mobile app build number. | No further constraint recorded |
| `primaryReasonCode` | `string` | No | Explicitly allowed | Primary reason code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `nextAction` | `string` | No | Explicitly allowed | Suggested next workflow step returned by the server; it does not override authorization. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleBrakeRecord

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `vehicleId` | `string (uuid)` | No | Not declared nullable | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `vehicle` | [Vehicle](v.md#vehicle) | No | Not declared nullable | Vehicle represented by the `Vehicle` model or enum; use that definition's fields/values. | No further constraint recorded |
| `recordedByUserId` | `string (uuid)` | No | Not declared nullable | Identifier of the related recorded by user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `inspectedAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for inspected at; parse strictly and localize only for display. | No further constraint recorded |
| `odometer` | `number (double)` | No | Explicitly allowed | Numeric odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `componentCode` | `string` | No | Explicitly allowed | Component code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `conditionCode` | `string` | No | Explicitly allowed | Condition code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `measurementMillimeters` | `number (double)` | No | Explicitly allowed | Numeric measurement millimeters for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `recommendedAction` | `string` | No | Explicitly allowed | Recommended action text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `costMinor` | `integer (int64)` | No | Not declared nullable | Cost in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | No | Explicitly allowed | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `attachmentFileRef` | `string` | No | Explicitly allowed | Attachment file ref text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `notes` | `string` | No | Explicitly allowed | Human notes for this record; keep them within the authorized data scope. | No further constraint recorded |
| `clientOperationId` | `string` | No | Explicitly allowed | Client's stable identity for this logical operation; preserve it through interrupted responses. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleCategory

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `name` | `string` | No | Explicitly allowed | Name of the record described by this model; distinct from its opaque ID. | No further constraint recorded |
| `iconUrl` | `string` | No | Explicitly allowed | URL for icon; validate the intended origin/access and never assume private links are public. | No further constraint recorded |
| `maxPassengers` | `integer (int32)` | No | Not declared nullable | Numeric max passengers for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `fareMultiplier` | `number (double)` | No | Not declared nullable | Numeric fare multiplier for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `sortOrder` | `integer (int32)` | No | Not declared nullable | Numeric sort order for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `isActive` | `boolean` | No | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleDefect

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `vehicleId` | `string (uuid)` | No | Not declared nullable | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `vehicle` | [Vehicle](v.md#vehicle) | No | Not declared nullable | Vehicle represented by the `Vehicle` model or enum; use that definition's fields/values. | No further constraint recorded |
| `reportedByUserId` | `string (uuid)` | No | Not declared nullable | Identifier of the related reported by user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `componentCode` | `string` | No | Explicitly allowed | Component code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `severity` | [VehicleMaintenanceSeverity](v.md#vehiclemaintenanceseverity) | No | Not declared nullable | Severity represented by the `VehicleMaintenanceSeverity` model or enum; use that definition's fields/values. | No further constraint recorded |
| `status` | [VehicleDefectStatus](v.md#vehicledefectstatus) | No | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `observedAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for observed at; parse strictly and localize only for display. | No further constraint recorded |
| `odometer` | `number (double)` | No | Explicitly allowed | Numeric odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `reporterBelievesSafeToDrive` | `boolean` | No | Not declared nullable | Whether reporter believes safe to drive applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `evidenceFileRefsJson` | `string` | No | Explicitly allowed | Evidence file refs json text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `assignedToUserId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related assigned to user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `resolutionServiceRecordId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related resolution service record record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `resolutionNotes` | `string` | No | Explicitly allowed | Resolution notes text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `resolvedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for resolved at; parse strictly and localize only for display. | No further constraint recorded |
| `clientOperationId` | `string` | No | Explicitly allowed | Client's stable identity for this logical operation; preserve it through interrupted responses. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleDefectStatus

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Open | Open state/choice in this specific enum. |
| `1` | InProgress | In progress state/choice in this specific enum. |
| `2` | Resolved | Resolved state/choice in this specific enum. |
| `3` | Voided | Voided state/choice in this specific enum. |

## VehicleDriverAssignment

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `vehicleId` | `string (uuid)` | No | Not declared nullable | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `vehicle` | [Vehicle](v.md#vehicle) | No | Not declared nullable | Vehicle represented by the `Vehicle` model or enum; use that definition's fields/values. | No further constraint recorded |
| `driverProfileId` | `string (uuid)` | No | Not declared nullable | Driver-profile record associated with this operation or result. | No further constraint recorded |
| `driverProfile` | [DriverProfile](d.md#driverprofile) | No | Not declared nullable | Driver profile represented by the `DriverProfile` model or enum; use that definition's fields/values. | No further constraint recorded |
| `startedAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for started at; parse strictly and localize only for display. | No further constraint recorded |
| `endedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for ended at; parse strictly and localize only for display. | No further constraint recorded |
| `assignedByUserId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related assigned by user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `endReason` | `string` | No | Explicitly allowed | End reason text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `make` | `string` | Yes | Not declared nullable | Vehicle manufacturer name/catalog selection. | No further constraint recorded |
| `model` | `string` | Yes | Not declared nullable | Model in the owning domain; for vehicle contracts, the vehicle model associated with the manufacturer. | No further constraint recorded |
| `year` | `integer (int32)` | Yes | Not declared nullable | Numeric year for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `color` | `string` | Yes | Not declared nullable | Color text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `plateNumber` | `string` | Yes | Not declared nullable | Country-specific vehicle registration plate; validate through the applicable country workflow. | No further constraint recorded |
| `vehicleCategoryId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related vehicle category record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `categoryName` | `string` | No | Explicitly allowed | Category name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | No further constraint recorded |
| `verificationStatus` | [VehicleVerificationStatus](v.md#vehicleverificationstatus) | Yes | Not declared nullable | Current vehicle verification enum; a saved vehicle is not automatically approved for work. | No further constraint recorded |
| `verificationNote` | `string` | No | Explicitly allowed | Human-readable verification decision/reason for the vehicle. | No further constraint recorded |
| `verifiedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for verified at; parse strictly and localize only for display. | No further constraint recorded |
| `insuranceStatus` | [InsuranceStatus](i.md#insurancestatus) | Yes | Not declared nullable | Insurance review/status enum; an uploaded policy is not automatically current confirmed coverage. | No further constraint recorded |
| `insuranceProvider` | `string` | No | Explicitly allowed | Insurance provider text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `insurancePolicyNumberLast4` | `string` | No | Explicitly allowed | Masked last-four insurance policy identifier; not the full policy number. | No further constraint recorded |
| `insuranceEffectiveAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for insurance effective at; parse strictly and localize only for display. | No further constraint recorded |
| `insuranceExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for insurance expires at; parse strictly and localize only for display. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `allowsPets` | `boolean` | No | Not declared nullable | Whether allows pets applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `childSeatCapacity` | `integer (int32)` | No | Not declared nullable | Numeric child seat capacity for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `isWheelchairAccessible` | `boolean` | No | Not declared nullable | Whether is wheelchair accessible applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `isAirportPickupEligible` | `boolean` | No | Not declared nullable | Whether is airport pickup eligible applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `conditionCode` | `string` | No | Explicitly allowed | Condition code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `vinChassis` | `string` | No | Explicitly allowed | Vehicle VIN/chassis identification data; keep the actual value private and within authorized views. | No further constraint recorded |
| `registrationExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for registration expires at; parse strictly and localize only for display. | No further constraint recorded |
| `fitnessExpiresAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for fitness expires at; parse strictly and localize only for display. | No further constraint recorded |
| `interiorImageFileRef` | `string` | No | Explicitly allowed | Interior image file ref text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `frontExteriorImageFileRef` | `string` | No | Explicitly allowed | Front exterior image file ref text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `insuranceProviderId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related insurance provider record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `isPrimary` | `boolean` | No | Not declared nullable | Whether the vehicle is designated primary in this account context; work eligibility is assessed separately. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleEligibilityReason

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |
| `messageKey` | `string` | Yes | Not declared nullable | Message key text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `isBlocking` | `boolean` | Yes | Not declared nullable | Whether is blocking applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `correctiveAction` | `string` | No | Explicitly allowed | Corrective action text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `route` | `string` | No | Explicitly allowed | Route text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleExpense

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `vehicleId` | `string (uuid)` | No | Not declared nullable | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `vehicle` | [Vehicle](v.md#vehicle) | No | Not declared nullable | Vehicle represented by the `Vehicle` model or enum; use that definition's fields/values. | No further constraint recorded |
| `recordedByUserId` | `string (uuid)` | No | Not declared nullable | Identifier of the related recorded by user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `categoryCode` | `string` | No | Explicitly allowed | Category code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `incurredAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for incurred at; parse strictly and localize only for display. | No further constraint recorded |
| `amountMinor` | `integer (int64)` | No | Not declared nullable | Monetary amount in the accompanying currency's integer minor units. | No further constraint recorded |
| `currency` | `string` | No | Explicitly allowed | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `vendor` | `string` | No | Explicitly allowed | Vendor text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `notes` | `string` | No | Explicitly allowed | Human notes for this record; keep them within the authorized data scope. | No further constraint recorded |
| `receiptFileRef` | `string` | No | Explicitly allowed | Receipt file ref text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `clientOperationId` | `string` | No | Explicitly allowed | Client's stable identity for this logical operation; preserve it through interrupted responses. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleInsurerReferenceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | Yes | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `countryCode` | `string` | Yes | Not declared nullable | Country ISO code for this model/context; it cannot override authenticated country authority. | No further constraint recorded |
| `name` | `string` | Yes | Not declared nullable | Name of the record described by this model; distinct from its opaque ID. | No further constraint recorded |
| `websiteUrl` | `string` | No | Explicitly allowed | URL for website; validate the intended origin/access and never assume private links are public. | No further constraint recorded |
| `isActive` | `boolean` | Yes | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | No further constraint recorded |
| `sortOrder` | `integer (int32)` | Yes | Not declared nullable | Numeric sort order for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleMaintenanceSchedule

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `vehicleId` | `string (uuid)` | No | Not declared nullable | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `vehicle` | [Vehicle](v.md#vehicle) | No | Not declared nullable | Vehicle represented by the `Vehicle` model or enum; use that definition's fields/values. | No further constraint recorded |
| `createdByUserId` | `string (uuid)` | No | Not declared nullable | Identifier of the related created by user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `categoryCode` | `string` | No | Explicitly allowed | Category code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `name` | `string` | No | Explicitly allowed | Name of the record described by this model; distinct from its opaque ID. | No further constraint recorded |
| `trigger` | [VehicleMaintenanceTrigger](v.md#vehiclemaintenancetrigger) | No | Not declared nullable | Trigger represented by the `VehicleMaintenanceTrigger` model or enum; use that definition's fields/values. | No further constraint recorded |
| `severity` | [VehicleMaintenanceSeverity](v.md#vehiclemaintenanceseverity) | No | Not declared nullable | Severity represented by the `VehicleMaintenanceSeverity` model or enum; use that definition's fields/values. | No further constraint recorded |
| `lastCompletedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last completed at; parse strictly and localize only for display. | No further constraint recorded |
| `lastCompletedOdometer` | `number (double)` | No | Explicitly allowed | Numeric last completed odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `nextDueAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for next due at; parse strictly and localize only for display. | No further constraint recorded |
| `nextDueOdometer` | `number (double)` | No | Explicitly allowed | Numeric next due odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `recurrenceDays` | `integer (int32)` | No | Explicitly allowed | Recurrence, measured in days under this workflow's calendar rules. | No further constraint recorded |
| `recurrenceDistance` | `number (double)` | No | Explicitly allowed | Numeric recurrence distance for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `dueSoonDays` | `integer (int32)` | No | Not declared nullable | Due soon, measured in days under this workflow's calendar rules. | No further constraint recorded |
| `dueSoonDistance` | `number (double)` | No | Not declared nullable | Numeric due soon distance for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `remindersEnabled` | `boolean` | No | Not declared nullable | Whether reminders enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `lastReminderStatus` | [VehicleMaintenanceStatus](v.md#vehiclemaintenancestatus) | No | Not declared nullable | Last reminder status represented by the `VehicleMaintenanceStatus` model or enum; use that definition's fields/values. | No further constraint recorded |
| `lastReminderAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for last reminder at; parse strictly and localize only for display. | No further constraint recorded |
| `snoozedUntilUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for snoozed until; parse strictly and localize only for display. | No further constraint recorded |
| `isActive` | `boolean` | No | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | No further constraint recorded |
| `clientOperationId` | `string` | No | Explicitly allowed | Client's stable identity for this logical operation; preserve it through interrupted responses. | No further constraint recorded |
| `revision` | `integer (int64)` | No | Not declared nullable | Authoritative record revision used for applicable concurrency checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleMaintenanceSeverity

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Advisory | Advisory state/choice in this specific enum. |
| `1` | Important | Important state/choice in this specific enum. |
| `2` | SafetyCritical | Safety critical state/choice in this specific enum. |

## VehicleMaintenanceStatus

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | Good | Good state/choice in this specific enum. |
| `1` | DueSoon | Due soon state/choice in this specific enum. |
| `2` | DueNow | Due now state/choice in this specific enum. |
| `3` | Overdue | Overdue state/choice in this specific enum. |
| `4` | CriticallyOverdue | Critically overdue state/choice in this specific enum. |
| `5` | Completed | Completed state/choice in this specific enum. |
| `6` | Snoozed | Snoozed state/choice in this specific enum. |
| `7` | Inactive | Inactive state/choice in this specific enum. |

## VehicleMaintenanceSummaryDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `vehicleId` | `string (uuid)` | Yes | Not declared nullable | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `currentOdometer` | `number (double)` | No | Explicitly allowed | Numeric current odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `odometerUnit` | `string` | No | Explicitly allowed | Odometer unit text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `latestOdometerAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for latest odometer at; parse strictly and localize only for display. | No further constraint recorded |
| `overallStatus` | [VehicleMaintenanceStatus](v.md#vehiclemaintenancestatus) | Yes | Not declared nullable | Overall status represented by the `VehicleMaintenanceStatus` model or enum; use that definition's fields/values. | No further constraint recorded |
| `dueSoonCount` | `integer (int32)` | Yes | Not declared nullable | Number of due soon in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `overdueCount` | `integer (int32)` | Yes | Not declared nullable | Number of overdue in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `openDefectCount` | `integer (int32)` | Yes | Not declared nullable | Number of open defect in this model's stated scope; not automatically a global/live total. | No further constraint recorded |
| `hasSafetyCriticalDefect` | `boolean` | Yes | Not declared nullable | Whether has safety critical defect applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `schedules` | [MaintenanceStatusResult](m.md#maintenancestatusresult)[] | Yes | Not declared nullable | Collection of schedules for this model; interpret each item through the declared item type. | No further constraint recorded |
| `monthToDateByCurrency` | `object` | Yes | Not declared nullable | Structured month to date by currency data; follow the referenced/inline properties and additional-property rules. | No further constraint recorded |
| `yearToDateByCurrency` | `object` | Yes | Not declared nullable | Structured year to date by currency data; follow the referenced/inline properties and additional-property rules. | No further constraint recorded |
| `lifetimeByCurrency` | `object` | Yes | Not declared nullable | Structured lifetime by currency data; follow the referenced/inline properties and additional-property rules. | No further constraint recorded |
| `evaluatedAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for evaluated at; parse strictly and localize only for display. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleMaintenanceTrigger

**Wire type:** `integer (int32)`. Allowed wire values: `0`, `1`, `2`, `3`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `0` | None | None state/choice in this specific enum. |
| `1` | Date | Date state/choice in this specific enum. |
| `2` | Odometer | Odometer state/choice in this specific enum. |
| `3` | WhicheverComesFirst | Whichever comes first state/choice in this specific enum. |

## VehicleOdometerReading

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `vehicleId` | `string (uuid)` | No | Not declared nullable | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `vehicle` | [Vehicle](v.md#vehicle) | No | Not declared nullable | Vehicle represented by the `Vehicle` model or enum; use that definition's fields/values. | No further constraint recorded |
| `recordedByUserId` | `string (uuid)` | No | Not declared nullable | Identifier of the related recorded by user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `reading` | `number (double)` | No | Not declared nullable | Numeric reading for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `unitCode` | `string` | No | Explicitly allowed | Unit code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `observedAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for observed at; parse strictly and localize only for display. | No further constraint recorded |
| `sourceCode` | `string` | No | Explicitly allowed | Source code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `notes` | `string` | No | Explicitly allowed | Human notes for this record; keep them within the authorized data scope. | No further constraint recorded |
| `dashboardImageFileRef` | `string` | No | Explicitly allowed | Dashboard image file ref text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `correctsReadingId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related corrects reading record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `correctionReason` | `string` | No | Explicitly allowed | Correction reason text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `clientOperationId` | `string` | No | Explicitly allowed | Client's stable identity for this logical operation; preserve it through interrupted responses. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleServiceRecord

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `vehicleId` | `string (uuid)` | No | Not declared nullable | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `vehicle` | [Vehicle](v.md#vehicle) | No | Not declared nullable | Vehicle represented by the `Vehicle` model or enum; use that definition's fields/values. | No further constraint recorded |
| `scheduleId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related schedule record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `schedule` | [VehicleMaintenanceSchedule](v.md#vehiclemaintenanceschedule) | No | Not declared nullable | Schedule represented by the `VehicleMaintenanceSchedule` model or enum; use that definition's fields/values. | No further constraint recorded |
| `recordedByUserId` | `string (uuid)` | No | Not declared nullable | Identifier of the related recorded by user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `categoryCode` | `string` | No | Explicitly allowed | Category code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `completedAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for completed at; parse strictly and localize only for display. | No further constraint recorded |
| `completedOdometer` | `number (double)` | No | Explicitly allowed | Numeric completed odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `workshop` | `string` | No | Explicitly allowed | Workshop text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `workPerformed` | `string` | No | Explicitly allowed | Work performed text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `partsJson` | `string` | No | Explicitly allowed | Parts json text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `labourCostMinor` | `integer (int64)` | No | Not declared nullable | Labour cost in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `partsCostMinor` | `integer (int64)` | No | Not declared nullable | Parts cost in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `taxMinor` | `integer (int64)` | No | Not declared nullable | Tax in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `discountMinor` | `integer (int64)` | No | Not declared nullable | Discount in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `totalMinor` | `integer (int64)` | No | Not declared nullable | Total in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | No | Explicitly allowed | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `warrantyNotes` | `string` | No | Explicitly allowed | Warranty notes text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `notes` | `string` | No | Explicitly allowed | Human notes for this record; keep them within the authorized data scope. | No further constraint recorded |
| `receiptFileRef` | `string` | No | Explicitly allowed | Receipt file ref text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `evidenceFileRefsJson` | `string` | No | Explicitly allowed | Evidence file refs json text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `nextRecommendedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for next recommended at; parse strictly and localize only for display. | No further constraint recorded |
| `nextRecommendedOdometer` | `number (double)` | No | Explicitly allowed | Numeric next recommended odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `isVoided` | `boolean` | No | Not declared nullable | Whether is voided applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `voidReason` | `string` | No | Explicitly allowed | Void reason text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `clientOperationId` | `string` | No | Explicitly allowed | Client's stable identity for this logical operation; preserve it through interrupted responses. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleTyreRecord

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | `string (uuid)` | No | Not declared nullable | Opaque identifier of this model's record; knowing it does not grant access. | No further constraint recorded |
| `createdAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for created at; parse strictly and localize only for display. | No further constraint recorded |
| `updatedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for updated at; parse strictly and localize only for display. | No further constraint recorded |
| `tenantId` | `string (uuid)` | No | Not declared nullable | Tenant associated with this record; it is not caller authority to switch tenants. | No further constraint recorded |
| `vehicleId` | `string (uuid)` | No | Not declared nullable | Account vehicle record associated with this operation or result. | No further constraint recorded |
| `vehicle` | [Vehicle](v.md#vehicle) | No | Not declared nullable | Vehicle represented by the `Vehicle` model or enum; use that definition's fields/values. | No further constraint recorded |
| `recordedByUserId` | `string (uuid)` | No | Not declared nullable | Identifier of the related recorded by user record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `positionCode` | `string` | No | Explicitly allowed | Position code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `brand` | `string` | No | Explicitly allowed | Brand text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `model` | `string` | No | Explicitly allowed | Model in the owning domain; for vehicle contracts, the vehicle model associated with the manufacturer. | No further constraint recorded |
| `size` | `string` | No | Explicitly allowed | Size text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `observedAtUtc` | `string (date-time)` | No | Not declared nullable | UTC instant for observed at; parse strictly and localize only for display. | No further constraint recorded |
| `odometer` | `number (double)` | No | Explicitly allowed | Numeric odometer for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `treadDepthMillimeters` | `number (double)` | No | Explicitly allowed | Numeric tread depth millimeters for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `pressurePsi` | `number (double)` | No | Explicitly allowed | Numeric pressure psi for this model. No additional unit or business rule is asserted by the source schema; follow the owning workflow. | No further constraint recorded |
| `conditionCode` | `string` | No | Explicitly allowed | Condition code text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `isActive` | `boolean` | No | Not declared nullable | Whether this record is marked active; other permission/provider/readiness checks still apply. | No further constraint recorded |
| `costMinor` | `integer (int64)` | No | Not declared nullable | Cost in the accompanying currency's integer minor units; do not send a formatted money string. | No further constraint recorded |
| `currency` | `string` | No | Explicitly allowed | ISO currency code for the accompanying monetary amounts. | No further constraint recorded |
| `notes` | `string` | No | Explicitly allowed | Human notes for this record; keep them within the authorized data scope. | No further constraint recorded |
| `clientOperationId` | `string` | No | Explicitly allowed | Client's stable identity for this logical operation; preserve it through interrupted responses. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VehicleVerificationStatus

**Wire type:** `integer (int32)`. Allowed wire values: `1`, `2`, `3`.

| Wire value | Source label | Meaning |
| --- | --- | --- |
| `1` | Pending | Pending state/choice in this specific enum. |
| `2` | Verified | Verified state/choice in this specific enum. |
| `3` | Rejected | Rejected state/choice in this specific enum. |

## VerifyStorePurchaseDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `platform` | `string` | Yes | Not declared nullable | Platform selector in this contract; numeric enums and string selectors are not interchangeable. | Allowed wire values: `apple`, `google` |
| `productId` | `string` | Yes | Not declared nullable | Identifier of the related product record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `verificationData` | `string` | Yes | Not declared nullable | Verification data text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `transactionId` | `string` | No | Explicitly allowed | Identifier of the related transaction record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `rentalOrganizationId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related rental organization record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `restore` | `boolean` | No | Not declared nullable | Whether restore applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `purchaseQuoteToken` | `string` | No | Explicitly allowed | Private purchase quote token used by this specific ceremony; never log, publish or substitute it for another proof. | No further constraint recorded |
| `operationId` | `string (uuid)` | No | Explicitly allowed | Durable operation reference used for applicable outcome discovery. | No further constraint recorded |
| `recovery` | `boolean` | No | Not declared nullable | Whether recovery applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VerifyTwoFactorLoginRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `ticket` | `string` | Yes | Not declared nullable | Ticket text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `code` | `string` | Yes | Not declared nullable | Code in this model's vocabulary; distinguish business/error/catalog codes from confidential verification codes. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VoiceCallLifecycleDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `callId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related call record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `status` | `string` | Yes | Not declared nullable | Current domain status; use this model's enum or documented string vocabulary. | No further constraint recorded |
| `recordingStatus` | `string` | Yes | Not declared nullable | Recording status text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `connectedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for connected at; parse strictly and localize only for display. | No further constraint recorded |
| `endedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for ended at; parse strictly and localize only for display. | No further constraint recorded |
| `recordingStartedAtUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for recording started at; parse strictly and localize only for display. | No further constraint recorded |
| `recordingDeleteAfterUtc` | `string (date-time)` | No | Explicitly allowed | UTC instant for recording delete after; parse strictly and localize only for display. | No further constraint recorded |
| `recordingJurisdiction` | `string` | No | Explicitly allowed | Recording jurisdiction text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `recordingPolicyVersion` | `string` | No | Explicitly allowed | Recording policy version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `recordingDisclosureVersion` | `string` | No | Explicitly allowed | Recording disclosure version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `durationSeconds` | `integer (int64)` | No | Explicitly allowed | Duration, measured in seconds. | No further constraint recorded |
| `providerSessionId` | `string` | No | Explicitly allowed | Identifier of the related provider session record in this model; ownership and scope are checked separately. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VoiceCallLifecycleRequest

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `callId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related call record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `disclosureVersion` | `string` | No | Explicitly allowed | Disclosure version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `providerEventId` | `string` | No | Explicitly allowed | Identifier of the related provider event record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `realtimeEventId` | `string` | No | Explicitly allowed | Identifier of the related realtime event record in this model; ownership and scope are checked separately. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VoiceCallOptionsDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `canUseInAppCalling` | `boolean` | Yes | Not declared nullable | Whether can use in app calling applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `peerPhoneNumber` | `string` | No | Explicitly allowed | Peer phone number text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `peerName` | `string` | Yes | Not declared nullable | Peer name text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `unavailableReason` | `string` | No | Explicitly allowed | Unavailable reason text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VoiceCallStartDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `callId` | `string (uuid)` | Yes | Not declared nullable | Identifier of the related call record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `tripId` | `string (uuid)` | Yes | Not declared nullable | Accepted trip record, distinct from the originating ride request. | No further constraint recorded |
| `recordingEnabled` | `boolean` | Yes | Not declared nullable | Whether recording enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `recordingRequired` | `boolean` | Yes | Not declared nullable | Whether recording required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `ringExpiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for ring expires at; parse strictly and localize only for display. | No further constraint recorded |
| `recordingDisclosureVersion` | `string` | No | Explicitly allowed | Recording disclosure version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |
| `realtimeEventId` | `string` | No | Explicitly allowed | Identifier of the related realtime event record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `providerSessionId` | `string` | No | Explicitly allowed | Identifier of the related provider session record in this model; ownership and scope are checked separately. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VoiceSessionDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `provider` | `string` | Yes | Not declared nullable | Configured provider selector for this operation; a named provider is not proof of readiness. | No further constraint recorded |
| `channel` | `string` | Yes | Not declared nullable | Channel text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `token` | `string` | Yes | Not declared nullable | Token for this specific contract, such as push registration; sensitive values must not be logged or reused in another ceremony. | No further constraint recorded |
| `expiresAtUtc` | `string (date-time)` | Yes | Not declared nullable | UTC instant for expires at; parse strictly and localize only for display. | No further constraint recorded |
| `url` | `string` | No | Explicitly allowed | Url text/value for this model. The source schema does not specify a further vocabulary; server validation and the owning workflow define permitted use. | No further constraint recorded |
| `callId` | `string (uuid)` | No | Explicitly allowed | Identifier of the related call record in this model; ownership and scope are checked separately. | No further constraint recorded |
| `recordingEnabled` | `boolean` | Yes | Not declared nullable | Whether recording enabled applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `recordingRequired` | `boolean` | Yes | Not declared nullable | Whether recording required applies in this model's context. This flag does not replace server permission or lifecycle checks. | No further constraint recorded |
| `recordingDisclosureVersion` | `string` | No | Explicitly allowed | Recording disclosure version for this model's state or policy; do not substitute a timestamp or mobile build. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.

## VoidVehicleServiceDto

**Wire type:** `object`. No further constraint recorded.

| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |
| --- | --- | --- | --- | --- | --- |
| `reason` | `string` | Yes | Not declared nullable | Reason supplied or returned for this workflow; follow any catalog/required validation rules. | No further constraint recorded |

**Additional object properties:** not allowed by the schema.
