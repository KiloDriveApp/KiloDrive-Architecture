#!/usr/bin/env python3
"""Export an explicitly reviewed subset; verify it without private source in CI."""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import re
import subprocess
from public_api_semantics import field_meaning, purpose, words
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = ROOT / "docs" / "api"
SPEC = API / "openapi" / "kilodrive-public-v1.json"
METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}
ALLOWED_EXTENSIONS = {
    "x-allow-anonymous", "x-authorization-required", "x-authorization-roles",
    "x-mobile-version-policy", "x-idempotency-protected",
    "x-entity-revision-protected", "x-entity-revision-published",
    "x-if-match-condition", "x-recent-authentication-condition",
}
DROP_KEYS = {"description", "example", "examples", "default", "externalDocs", "callbacks", "links"}
TOPICS = {
    "discovery": "Public information and capability discovery",
    "identity": "Identity, account and installation lifecycle",
    "rides": "Rider requests, bidding and recurring rides",
    "drivers": "Driver onboarding, readiness and work",
    "trips": "Trip lifecycle, receipts and participant activity",
    "wallets": "Wallet, top-up, transfer and payout workflows",
    "memberships": "Membership and store entitlement workflows",
    "vehicles": "Account vehicles and maintenance",
    "deliveries": "Delivery requests and driver fulfillment",
    "rentals": "Rental bookings and organization workflows",
    "notifications": "Notification inbox, preferences and push binding",
    "support": "Support tickets and review appeals",
    "safety": "Safety, contacts, consent and supervision",
    "profiles": "Travel profiles and business accounts",
    "reports": "Personal and scheduled reports",
    "maps-and-tools": "Maps, fare tools and saved calculations",
    "uploads": "Private uploads and authorized retrieval",
    "communications": "Participant call workflows",
}


def encoded(value: object) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sanitized(value: object) -> object:
    if isinstance(value, dict):
        return {
            key: sanitized(item) for key, item in value.items()
            if key not in DROP_KEYS and (not key.startswith("x-") or key in ALLOWED_EXTENSIONS)
        }
    if isinstance(value, list):
        return [sanitized(item) for item in value]
    return copy.deepcopy(value)


def references(value: object) -> set[str]:
    result: set[str] = set()
    if isinstance(value, dict):
        if "$ref" in value:
            result.add(value["$ref"])
        for item in value.values():
            result.update(references(item))
    elif isinstance(value, list):
        for item in value:
            result.update(references(item))
    return result


def component_id(ref: str) -> tuple[str, str]:
    parts = ref.split("/")
    if len(parts) != 4 or parts[:2] != ["#", "components"]:
        raise ValueError(f"Only local component references are allowed: {ref}")
    return parts[2], parts[3].replace("~1", "/").replace("~0", "~")


def is_privileged(path: str, operation: dict) -> bool:
    return (
        not path.startswith("/api/v1/")
        or path.startswith(("/api/v1/admin", "/api/v1/workspaces", "/api/v1/realtime"))
        or "/webhook" in path
        or path.startswith(("/api/v1/payments/", "/api/v1/payouts/"))
        or path in {"/api/v1/auth/apple/notifications", "/api/v1/auth/workspaces",
                       "/api/v1/account/store-review-policy"}
        or path.startswith("/api/v1/store-billing/notifications/")
        or any(role in {"Admin", "Administrator", "SystemAdmin"}
               for role in operation.get("x-authorization-roles", []))
    )


def export(source: dict, policy: dict) -> dict:
    paths: dict = {}
    for path, rule in policy["routes"].items():
        if rule["topic"] not in TOPICS:
            raise ValueError(f"Unknown topic for {path}")
        item = source.get("paths", {}).get(path)
        if not item:
            raise ValueError(f"Reviewed path missing from source: {path}")
        methods = rule["methods"]
        if not methods or len(set(methods)) != len(methods):
            raise ValueError(f"Invalid method allowlist: {path}")
        public_item = {key: sanitized(item[key]) for key in ("parameters",) if key in item}
        for method in methods:
            if method not in METHODS or method not in item:
                raise ValueError(f"Reviewed operation missing: {method} {path}")
            operation = item[method]
            if is_privileged(path, operation):
                raise ValueError(f"Privileged operation cannot be exported: {method} {path}")
            clean = sanitized(operation)
            clean["tags"] = [rule["topic"]]
            clean["security"] = [] if clean.get("x-allow-anonymous") else clean.get("security", source.get("security", []))
            public_item[method] = clean
        paths[path] = public_item

    components: dict = {}
    pending = references(paths)
    for item in paths.values():
        for method, operation in item.items():
            if method in METHODS:
                for requirement in operation.get("security", []):
                    pending.update(f"#/components/securitySchemes/{key}" for key in requirement)
    seen: set[str] = set()
    while pending:
        ref = min(pending)
        pending.remove(ref)
        if ref in seen:
            continue
        group, name = component_id(ref)
        if re.match(r"^(?:Admin|SystemAdmin)", name):
            raise ValueError(f"Administrative component referenced by reviewed subset: {name}")
        try:
            clean = sanitized(source["components"][group][name])
        except KeyError as error:
            raise ValueError(f"Missing component: {ref}") from error
        components.setdefault(group, {})[name] = clean
        seen.add(ref)
        pending.update(references(clean) - seen)
    for group in components:
        components[group] = dict(sorted(components[group].items()))
    # Response descriptions are mandatory in OpenAPI. Do not copy source prose.
    for item in paths.values():
        for method, operation in item.items():
            if method in METHODS:
                for status, response in operation.get("responses", {}).items():
                    if "$ref" not in response:
                        response["description"] = f"HTTP {status}; see the error and workflow guides."
    for response in components.get("responses", {}).values():
        response["description"] = "Referenced response contract."
    return {
        "openapi": source["openapi"],
        "info": {
            "title": "KiloDrive curated public API reference",
            "version": "v1",
            "description": "Reviewed anonymous and first-party contracts. Publication grants no account, device, role, country or partner access. Administrative and provider callbacks are excluded. Source examples, defaults and operational prose are omitted. Read docs/api/README.md before integration.",
        },
        "servers": [{"url": "https://api.example.invalid", "description": "Reserved example host; no live service."}],
        "tags": [{"name": topic, "description": title} for topic, title in TOPICS.items()
                 if any(rule["topic"] == topic for rule in policy["routes"].values())],
        "paths": paths,
        "components": components,
    }


def schema_names(value: object) -> list[str]:
    return sorted({component_id(ref)[1] for ref in references(value) if ref.startswith("#/components/schemas/")})


def cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def type_label(schema: dict) -> str:
    if "$ref" in schema:
        return component_id(schema["$ref"])[1]
    if schema.get("type") == "array":
        return type_label(schema.get("items", {})) + "[]"
    return schema.get("type", "schema") + (f" ({schema['format']})" if "format" in schema else "")


def model_link(name: str, parent: str = "../schemas/") -> str:
    return f"[{name}]({parent}{name[0].lower()}.md#{name.lower()})"


def constraints(schema: dict) -> str:
    values = []
    for name in ("minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum", "minLength", "maxLength", "minItems", "maxItems", "uniqueItems", "pattern", "readOnly", "writeOnly"):
        if name in schema:
            values.append(f"{name}: `{schema[name]}`")
    if "enum" in schema:
        values.append("Allowed wire values: " + ", ".join(f"`{value}`" for value in schema["enum"]))
    return "; ".join(values) or "No further constraint recorded"


def fields_catalog(spec: dict, enum_labels: dict) -> dict[str, bytes]:
    groups: dict[str, list[tuple[str, dict]]] = {}
    for name, schema in sorted(spec["components"].get("schemas", {}).items()):
        groups.setdefault(name[0].lower(), []).append((name, schema))
    outputs = {}
    index = ["# Request and response field dictionary", "", "[API Guide](../README.md) · [Endpoint reference](../reference/README.md)", "", "Every referenced component schema is included below. Field names, types, required", "markers, nullability and constraints come from the curated contract. Explanations", "describe contract meaning without inventing unrecorded business rules. A field marked", "not required by the schema can still be required by workflow validation.", "", "Numeric enum labels are checked against the reviewed source declarations. These", "labels explain values; they do not grant a role, provider or lifecycle permission.", "Unknown future values must remain neutral and disable unsafe actions.", "", "| Initial | Models |", "| --- | ---: |"]
    for letter, models in groups.items():
        index.append(f"| [{letter.upper()}]({letter}.md) | {len(models)} |")
        lines = [f"# Field dictionary: {letter.upper()}", "", "[Dictionary index](README.md) · [API Guide](../README.md)", "", "Requiredness and nullability below are schema metadata, not a replacement for", "workflow validation. Monetary amounts use integer minor units; timestamp fields", "use strict UTC parsing. Private tokens, passwords, document references and", "personal fields must remain outside public logs and examples.", ""]
        for name, schema in models:
            lines.extend([f"## {name}", "", f"**Wire type:** `{type_label(schema)}`. {constraints(schema)}.", ""])
            if "enum" in schema:
                values = enum_labels.get(name, {})
                lines.extend(["| Wire value | Source label | Meaning |", "| --- | --- | --- |"])
                for value in schema["enum"]:
                    label = values.get(str(value))
                    explanation = f"{field_meaning(label, {'type': 'string'})}" if label else "Source label unavailable in this snapshot; use the wire value without inventing a status mapping."
                    if label:
                        explanation = words(label).capitalize() + " state/choice in this specific enum."
                    lines.append(f"| `{value}` | {label or 'Not recorded'} | {cell(explanation)} |")
                lines.append("")
            properties = schema.get("properties", {})
            if properties:
                required = set(schema.get("required", []))
                lines.extend(["| Field | Type | Required by schema | Nullability | Meaning | Additional constraints |", "| --- | --- | --- | --- | --- | --- |"])
                for field, definition in properties.items():
                    label = type_label(definition)
                    field_type = model_link(component_id(definition["$ref"])[1], "") if "$ref" in definition else f"`{cell(label)}`"
                    if definition.get("type") == "array" and "$ref" in definition.get("items", {}):
                        field_type = model_link(component_id(definition["items"]["$ref"])[1], "") + "[]"
                    null = "Explicitly allowed" if definition.get("nullable") else "Not declared nullable"
                    lines.append(f"| `{field}` | {field_type} | {'Yes' if field in required else 'No'} | {null} | {cell(field_meaning(field, definition, name))} | {cell(constraints(definition))} |")
                lines.append("")
            for kind in ("allOf", "oneOf", "anyOf"):
                if kind in schema:
                    lines.extend([f"**Composition ({kind}):** " + ", ".join(model_link(model, "") for model in schema_names(schema[kind])) + ".", ""])
            if "additionalProperties" in schema:
                extra = schema["additionalProperties"]
                if isinstance(extra, bool):
                    lines.extend([f"**Additional object properties:** {'allowed' if extra else 'not allowed by the schema'}.", ""])
                else:
                    lines.extend([f"**Additional property value type:** `{type_label(extra)}`.", ""])
            if not properties and "enum" not in schema:
                lines.extend(["This is a scalar/composed model. Follow the recorded type and referenced definitions;", "the schema does not declare a separate property table.", ""])
        outputs[f"schemas/{letter}.md"] = ("\n".join(lines).rstrip() + "\n").encode("utf-8")
    index.extend(["", "Use [wire conventions](../wire-conventions.md) for cross-cutting interpretation and", "[contract limitations](../coverage-and-limitations.md) for metadata gaps.", ""])
    outputs["schemas/README.md"] = "\n".join(index).encode("utf-8")
    return outputs


def catalog(spec: dict, policy: dict) -> dict[str, bytes]:
    outputs: dict[str, bytes] = {}
    index = ["# Endpoint reference", "", "Generated from the reviewed publication policy and curated OpenAPI. These are", "documentation groups, not permission grants or separate services. Read the", "[access guide](../access-and-authentication.md) and [recovery guide](../errors-and-recovery.md)", "before implementing a protected operation. Defaults and source examples are intentionally omitted.", "", "| Group | Paths | Operations |", "| --- | ---: | ---: |"]
    for topic, title in TOPICS.items():
        selected = [(path, item) for path, item in spec["paths"].items() if policy["routes"][path]["topic"] == topic]
        if not selected:
            continue
        op_count = sum(sum(method in METHODS for method in item) for _, item in selected)
        index.append(f"| [{title}]({topic}.md) | {len(selected)} | {op_count} |")
        lines = [f"# {title}", "", "[Reference index](README.md) · [API guide](../README.md)", "", "Access shown here describes bearer metadata only. Anonymous operations can still", "require installation admission, application attestation, contact proof or country", "context. A bearer token does not replace ownership, feature gates or role checks.", "", "Each entry lists recorded schemas, parameters, status codes and mutation guards.", "Response metadata is not a complete list of runtime business outcomes; read the", "[contract limitations](../coverage-and-limitations.md).", ""]
        for path, item in selected:
            for method in sorted(METHODS.intersection(item)):
                operation = item[method]
                roles = operation.get("x-authorization-roles", [])
                access = "Anonymous bearer metadata" if operation.get("x-allow-anonymous") else "Bearer required" if operation.get("security") else "No bearer requirement recorded; confirm runtime policy"
                if roles:
                    access += "; declared roles: " + ", ".join(roles)
                lines.extend([f"## {method.upper()} `{path}`", "", f"**What it does:** {purpose(method, path)}", "", f"**Access:** {access}.", ""])
                body = operation.get("requestBody")
                if body:
                    schemas = schema_names(body)
                    inline = ", ".join(f"`{kind}`" for kind in body.get("content", {}))
                    names = ", ".join(model_link(name) for name in schemas) or "inline schema in OpenAPI"
                    lines.extend([f"**Body:** {names}; {'required' if body.get('required') else 'requiredness not asserted in metadata'}; media types: {inline}.", ""])
                    for media in body.get("content", {}).values():
                        inline_properties = media.get("schema", {}).get("properties", {})
                        if inline_properties:
                            lines.extend(["| Inline body field | Type | Meaning |", "| --- | --- | --- |"])
                            for field, definition in inline_properties.items():
                                lines.append(f"| `{field}` | `{cell(type_label(definition))}` | {cell(field_meaning(field, definition))} |")
                            lines.append("")
                            break
                parameters = item.get("parameters", []) + operation.get("parameters", [])
                if parameters:
                    lines.extend(["| Parameter | Location | Required | Type | Meaning |", "| --- | --- | --- | --- | --- |"])
                    for parameter in parameters:
                        if "$ref" in parameter:
                            lines.append(f"| `{cell(parameter['$ref'])}` | Referenced | See schema | See schema | Referenced parameter contract |")
                        else:
                            lines.append(f"| `{cell(parameter['name'])}` | {parameter['in']} | {'Yes' if parameter.get('required') else 'Conditional or optional'} | `{cell(type_label(parameter.get('schema', {})))}` | {cell(field_meaning(parameter['name'], parameter.get('schema', {})))} |")
                    lines.append("")
                lines.extend(["| Recorded status | Response schema | Media types | Response headers |", "| --- | --- | --- | --- |"])
                for status, response in operation.get("responses", {}).items():
                    names = ", ".join(model_link(name) for name in schema_names(response))
                    media = response.get("content", {})
                    if not names:
                        inline = sorted({type_label(value["schema"]) for value in media.values() if "schema" in value})
                        names = ", ".join(f"`{cell(value)}`" for value in inline) or "No typed schema recorded"
                    media_types = ", ".join(f"`{kind}`" for kind in media) or "None recorded"
                    headers = ", ".join(f"`{name}`" for name in response.get("headers", {})) or "None recorded"
                    lines.append(f"| {status} | {names} | {media_types} | {headers} |")
                guards = []
                if any(p.get("name", "").lower() == "idempotency-key" for p in parameters) or operation.get("x-idempotency-protected"):
                    guards.append("Preserve the original idempotency key and payload through unknown outcomes.")
                if any(p.get("name", "").lower() == "if-match" for p in parameters):
                    guards.append("Preserve the original revision during outcome recovery; refresh before a new logical edit.")
                if operation.get("x-recent-authentication-condition"):
                    guards.append("The server can require recent authentication; local app unlock is not proof.")
                if guards:
                    lines.extend(["", "**Mutation handling:** " + " ".join(guards)])
                lines.append("")
        outputs[f"reference/{topic}.md"] = ("\n".join(lines).rstrip() + "\n").encode("utf-8")
    index.extend(["", "The [field dictionary](../schemas/README.md) explains every referenced model and", "the [curated OpenAPI](../openapi/kilodrive-public-v1.json) retains the wire definitions.", "The [snapshot manifest](../openapi/manifest.json) records provenance, scope and checksums.", ""])
    outputs["reference/README.md"] = "\n".join(index).encode("utf-8")
    return outputs


def counts(spec: dict) -> dict:
    operations = [op for item in spec["paths"].values() for method, op in item.items() if method in METHODS]
    return {
        "paths": len(spec["paths"]), "operations": len(operations),
        "schemas": len(spec.get("components", {}).get("schemas", {})),
        "modelProperties": sum(len(schema.get("properties", {})) for schema in spec.get("components", {}).get("schemas", {}).values()),
        "numericEnums": sum("enum" in schema for schema in spec.get("components", {}).get("schemas", {}).values()),
        "anonymousOperations": sum(bool(op.get("x-allow-anonymous")) for op in operations),
        "bearerOperations": sum(bool(op.get("security")) for op in operations),
    }


def validate_bundle(spec: dict, policy: dict) -> None:
    if spec.get("servers") != [{"url": "https://api.example.invalid", "description": "Reserved example host; no live service."}]:
        raise ValueError("Example server must remain a reserved, non-live host")
    if set(spec["paths"]) != set(policy["routes"]):
        raise ValueError("Export paths do not match reviewed policy")
    operation_ids: set[str] = set()
    for path, item in spec["paths"].items():
        if METHODS.intersection(item) != set(policy["routes"][path]["methods"]):
            raise ValueError(f"Methods disagree with policy: {path}")
        for method in METHODS.intersection(item):
            op = item[method]
            if is_privileged(path, op):
                raise ValueError(f"Privileged operation in public artifact: {path}")
            if op.get("x-allow-anonymous") and op.get("security"):
                raise ValueError(f"Anonymous operation inherits bearer requirement: {path}")
            if op.get("x-authorization-required") and not op.get("security"):
                raise ValueError(f"Protected operation lacks bearer requirement: {path}")
            if not op.get("responses"):
                raise ValueError(f"Missing responses: {path}")
            names = {p.get("name") for p in item.get("parameters", []) + op.get("parameters", []) if p.get("in") == "path" and p.get("required")}
            if set(re.findall(r"\{([^}]+)\}", path)) - names:
                raise ValueError(f"Required path parameters missing: {path}")
            identity = op.get("operationId")
            if identity:
                if identity in operation_ids:
                    raise ValueError(f"Duplicate operationId: {identity}")
                operation_ids.add(identity)
    for ref in references(spec):
        group, name = component_id(ref)
        if name not in spec.get("components", {}).get(group, {}):
            raise ValueError(f"Unresolved reference: {ref}")
    reachable = references(spec["paths"])
    for item in spec["paths"].values():
        for method in METHODS.intersection(item):
            for requirement in item[method].get("security", []):
                reachable.update(f"#/components/securitySchemes/{name}" for name in requirement)
    seen: set[str] = set()
    while reachable - seen:
        ref = min(reachable - seen)
        group, name = component_id(ref)
        seen.add(ref)
        reachable.update(references(spec["components"][group][name]))
    for group, entries in spec.get("components", {}).items():
        for name in entries:
            if f"#/components/{group}/{name}" not in seen:
                raise ValueError(f"Unreferenced component leaked into public export: {name}")
    for group, entries in spec.get("components", {}).items():
        if any(re.match(r"^(?:Admin|SystemAdmin)", name) for name in entries):
            raise ValueError(f"Administrative component in {group}")
    # Descriptions generated locally are allowed; copied examples and defaults are not.
    def visit(value: object) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key in {"example", "examples", "default", "callbacks", "links", "externalDocs"}:
                    raise ValueError(f"Unreviewed source content retained: {key}")
                if key.startswith("x-") and key not in ALLOWED_EXTENSIONS:
                    raise ValueError(f"Unreviewed operational extension: {key}")
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)
    visit(spec)


def generate(source_root: Path, commit: str, reviewed_date: str) -> None:
    source_path = source_root / "docs/contracts/openapi/kilodrive-v1.json"
    source_bytes = source_path.read_bytes()
    sidecar = source_path.with_suffix(".json.sha256").read_text().split()[0]
    if digest(source_bytes) != sidecar:
        raise ValueError("Private source contract SHA-256 sidecar mismatch")
    if not re.fullmatch(r"[a-f0-9]{40}", commit):
        raise ValueError("Source commit must be a full Git SHA")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", reviewed_date):
        raise ValueError("Review date must be explicit ISO date")
    source = json.loads(source_bytes)
    actual_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source_root, text=True).strip()
    if actual_commit != commit:
        raise ValueError("Provided source commit does not match the reviewed checkout")
    committed_contract = subprocess.check_output(["git", "show", f"{commit}:docs/contracts/openapi/kilodrive-v1.json"], cwd=source_root)
    if json.loads(committed_contract) != source:
        raise ValueError("Working contract differs from the claimed source commit")
    policy_bytes = (API / "publication-policy.json").read_bytes()
    policy = json.loads(policy_bytes)
    spec = export(source, policy)
    validate_bundle(spec, policy)
    versions = {}
    for name, folder in (("consumer", "mobile"), ("systemAdmin", "system_admin")):
        text = (source_root / "src/client" / folder / "pubspec.yaml").read_text(encoding="utf-8-sig")
        versions[name] = re.search(r"(?m)^version:\s*(\S+)", text).group(1)
    schema_text = (source_root / "src/server/KiloDrive.Api/Data/SchemaContract.cs").read_text(encoding="utf-8-sig")
    versions["schemaContract"] = re.search(r'CurrentVersion\s*=\s*"([^"]+)"', schema_text).group(1)
    committed_schema = subprocess.check_output(["git", "show", f"{commit}:src/server/KiloDrive.Api/Data/SchemaContract.cs"], cwd=source_root, text=True)
    if re.search(r'CurrentVersion\s*=\s*"([^"]+)"', committed_schema).group(1) != versions["schemaContract"]:
        raise ValueError("Working schema version differs from claimed source commit")
    for name, relative in (("consumer", "src/client/mobile/pubspec.yaml"), ("systemAdmin", "src/client/system_admin/pubspec.yaml")):
        committed = subprocess.check_output(["git", "show", f"{commit}:{relative}"], cwd=source_root, text=True)
        if re.search(r"(?m)^version:\s*(\S+)", committed).group(1) != versions[name]:
            raise ValueError(f"Working {name} version differs from claimed source commit")
    outputs = catalog(spec, policy)
    enum_path = API / "enum-labels.json"
    enum_labels = extract_enum_labels(source_root, spec)
    enum_path.write_bytes(encoded(enum_labels))
    outputs.update(fields_catalog(spec, enum_labels))
    outputs["openapi/kilodrive-public-v1.json"] = encoded(spec)
    spec_hash = digest(outputs["openapi/kilodrive-public-v1.json"])
    outputs["openapi/kilodrive-public-v1.json.sha256"] = f"{spec_hash}  kilodrive-public-v1.json\n".encode()
    manifest = {
        "exportVersion": 1, "reviewedDate": reviewed_date,
        "source": {"commit": commit, "contractSha256": digest(source_bytes), **versions,
                   "paths": len(source["paths"]), "operations": counts(source)["operations"]},
        "public": counts(spec), "publicationPolicySha256": digest(policy_bytes),
        "enumLabelsSha256": digest(enum_path.read_bytes()),
        "omissions": ["administrative and cross-workspace contracts", "provider webhooks and callback contracts", "operational diagnostics and infrastructure contracts", "source descriptions, examples, defaults and defensive thresholds", "unreferenced components"],
        "artifacts": {name: digest(data) for name, data in sorted(outputs.items())},
    }
    outputs["openapi/manifest.json"] = encoded(manifest)
    for name, data in outputs.items():
        target = API / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    print(f"Generated curated contract: {counts(spec)}")


def extract_enum_labels(source_root: Path, spec: dict) -> dict:
    wanted = {name: schema["enum"] for name, schema in spec["components"]["schemas"].items() if "enum" in schema}
    source_files = list((source_root / "src/server/KiloDrive.Api").rglob("*.cs"))
    source_files.extend((source_root / "src/shared/KiloDrive.Contracts").rglob("*.cs"))
    texts = [(path, re.sub(r"/\*.*?\*/|//[^\n]*", "", path.read_text(encoding="utf-8-sig"), flags=re.S))
             for path in source_files]
    constants: dict[str, int] = {}
    for _, text in texts:
        for block in re.finditer(r"\bclass\s+(\w+)\s*\{([^}]+)\}", text, re.S):
            for value in re.finditer(r"\bconst\s+int\s+(\w+)\s*=\s*(-?\d+)\s*;", block[2]):
                constants[f"{block[1]}.{value[1]}"] = int(value[2])

    def expression_value(expression: str, known: dict) -> int:
        expression = re.sub(r"(?<=\d)[lL]\b", "", expression)
        node = ast.parse(" ".join(expression.split()), mode="eval").body

        def interpret(value: ast.AST) -> int:
            if isinstance(value, ast.Constant) and type(value.value) is int:
                return value.value
            if isinstance(value, ast.Name):
                return known[value.id]
            if isinstance(value, ast.Attribute) and isinstance(value.value, ast.Name):
                return constants[f"{value.value.id}.{value.attr}"]
            if isinstance(value, ast.UnaryOp) and isinstance(value.op, ast.USub):
                return -interpret(value.operand)
            if isinstance(value, ast.BinOp):
                left, right = interpret(value.left), interpret(value.right)
                if isinstance(value.op, ast.LShift):
                    return left << right
                if isinstance(value.op, ast.BitOr):
                    return left | right
                if isinstance(value.op, ast.Add):
                    return left + right
            raise ValueError("Unsupported source enum expression")
        return interpret(node)

    found: dict = {}
    for path, text in texts:
        for declaration in re.finditer(r"\benum\s+(\w+)(?:\s*:\s*\w+)?\s*\{([^}]+)\}", text, re.S):
            name, body = declaration.groups()
            if name not in wanted:
                continue
            known: dict = {}
            previous = -1
            for part in body.split(","):
                if not part.strip():
                    continue
                member = re.fullmatch(r"\s*(\w+)(?:\s*=\s*(.+))?\s*", part, re.S)
                if not member:
                    raise ValueError(f"Unparsed enum member in {name}")
                label, expression = member.groups()
                number = expression_value(expression, known) if expression else previous + 1
                known[label] = number
                previous = number
            labels = {str(number): label for label, number in known.items() if number in wanted[name]}
            if name in found and found[name] != labels:
                raise ValueError(f"Conflicting source declarations for {name}")
            found[name] = labels
            # Do not attach enum labels from uncommitted source changes.
            relative = path.relative_to(source_root).as_posix()
            committed = subprocess.check_output(["git", "show", f"HEAD:{relative}"], cwd=source_root).decode("utf-8-sig")
            if committed.replace("\r\n", "\n") != path.read_text(encoding="utf-8-sig").replace("\r\n", "\n"):
                raise ValueError(f"Working enum declaration differs from committed source: {name}")
    for name, values in wanted.items():
        if set(found.get(name, {})) != {str(value) for value in values}:
            raise ValueError(f"Source enum labels do not exactly cover the public wire values: {name}")
    return dict(sorted(found.items()))


def check() -> None:
    spec = json.loads(SPEC.read_bytes())
    policy_bytes = (API / "publication-policy.json").read_bytes()
    policy = json.loads(policy_bytes)
    manifest = json.loads((API / "openapi/manifest.json").read_bytes())
    validate_bundle(spec, policy)
    if counts(spec) != manifest["public"]:
        raise ValueError("Public counts differ from manifest")
    if digest(policy_bytes) != manifest["publicationPolicySha256"]:
        raise ValueError("Publication policy changed without regeneration")
    enum_bytes = (API / "enum-labels.json").read_bytes()
    if digest(enum_bytes) != manifest["enumLabelsSha256"]:
        raise ValueError("Enum labels changed without regeneration")
    labels = json.loads(enum_bytes)
    for name, schema in spec["components"].get("schemas", {}).items():
        if "enum" in schema and set(labels.get(name, {})) != {str(value) for value in schema["enum"]}:
            raise ValueError(f"Enum labels are incomplete or disagree with wire values: {name}")
    if SPEC.with_suffix(".json.sha256").read_text().split()[0] != digest(SPEC.read_bytes()):
        raise ValueError("Public contract SHA-256 mismatch")
    for name, expected in manifest["artifacts"].items():
        target = (API / name).resolve()
        if not target.is_relative_to(API.resolve()):
            raise ValueError("Manifest path escapes API directory")
        if digest(target.read_bytes()) != expected:
            raise ValueError(f"Generated artifact differs from manifest: {name}")
    regenerated = catalog(spec, policy)
    regenerated.update(fields_catalog(spec, json.loads(enum_bytes)))
    for name, expected in regenerated.items():
        if (API / name).read_bytes() != expected:
            raise ValueError(f"Generated endpoint catalog is stale: {name}")
    print(f"Public API verification passed: {manifest['public']}; source {manifest['source']['commit']}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--source-commit")
    parser.add_argument("--reviewed-date")
    args = parser.parse_args()
    if args.check:
        check()
    elif args.source_root and args.source_commit and args.reviewed_date:
        generate(args.source_root, args.source_commit, args.reviewed_date)
        check()
    else:
        parser.error("Use --check, or supply --source-root, --source-commit and --reviewed-date")


if __name__ == "__main__":
    main()
