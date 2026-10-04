"""Publication boundary tests; these do not claim application certification."""

import copy
import unittest

from public_api import catalog, export, fields_catalog, validate_bundle


class PublicApiTests(unittest.TestCase):
    def setUp(self):
        self.path = "/api/v1/account/contact-details"
        self.policy = {"routes": {self.path: {"topic": "identity", "methods": ["get"]}}}
        self.source = {
            "openapi": "3.0.1",
            "paths": {
                self.path: {"get": {
                    "x-authorization-required": True,
                    "security": [{"Bearer": []}],
                    "responses": {"200": {"description": "Private source prose", "content": {
                        "application/json": {"schema": {"$ref": "#/components/schemas/Contact"}}
                    }}},
                }},
                "/api/v1/admin/people": {"get": {"responses": {"200": {"description": "Excluded"}}}},
            },
            "components": {
                "schemas": {
                    "Contact": {"type": "object", "required": ["name"], "properties": {
                        "name": {"type": "string", "example": "<unreviewed-source-value>"},
                        "address": {"$ref": "#/components/schemas/Address"},
                    }},
                    "Address": {"type": "object", "properties": {"city": {"type": "string"}}},
                    "AdminOnly": {"type": "object"},
                },
                "securitySchemes": {"Bearer": {"type": "http", "scheme": "bearer"}},
            },
        }

    def test_transitive_components_retained_admin_orphans_removed(self):
        result = export(self.source, self.policy)
        self.assertEqual(set(result["components"]["schemas"]), {"Contact", "Address"})
        self.assertEqual(set(result["paths"]), {self.path})
        validate_bundle(result, self.policy)

    def test_examples_defaults_and_operational_extensions_removed(self):
        operation = self.source["paths"][self.path]["get"]
        operation["x-private-retry-policy"] = "<not-for-publication>"
        operation["x-idempotency-retention-days"] = 99
        self.source["components"]["schemas"]["Contact"]["properties"]["name"]["default"] = "<private-default>"
        result = export(self.source, self.policy)
        self.assertNotIn("x-private-retry-policy", result["paths"][self.path]["get"])
        self.assertNotIn("x-idempotency-retention-days", result["paths"][self.path]["get"])
        field = result["components"]["schemas"]["Contact"]["properties"]["name"]
        self.assertNotIn("example", field)
        self.assertNotIn("default", field)

    def test_anonymous_does_not_inherit_global_bearer(self):
        self.source["security"] = [{"Bearer": []}]
        op = self.source["paths"][self.path]["get"]
        op.pop("x-authorization-required")
        op["x-allow-anonymous"] = True
        op.pop("security")
        result = export(self.source, self.policy)
        self.assertEqual(result["paths"][self.path]["get"]["security"], [])
        self.assertNotIn("securitySchemes", result["components"])

    def test_administrative_route_rejected_even_if_allowlisted(self):
        policy = {"routes": {"/api/v1/admin/people": {"topic": "identity", "methods": ["get"]}}}
        with self.assertRaisesRegex(ValueError, "Privileged"):
            export(self.source, policy)

    def test_privileged_role_outside_admin_prefix_rejected(self):
        self.source["paths"][self.path]["get"]["x-authorization-roles"] = ["SystemAdmin"]
        with self.assertRaisesRegex(ValueError, "Privileged"):
            export(self.source, self.policy)

    def test_provider_callback_rejected(self):
        path = "/api/v1/payments/paypal/webhook"
        self.source["paths"][path] = copy.deepcopy(self.source["paths"][self.path])
        policy = {"routes": {path: {"topic": "wallets", "methods": ["get"]}}}
        with self.assertRaisesRegex(ValueError, "Privileged"):
            export(self.source, policy)

    def test_referenced_admin_model_rejected(self):
        self.source["components"]["schemas"]["Contact"]["properties"]["operator"] = {"$ref": "#/components/schemas/AdminOnly"}
        with self.assertRaisesRegex(ValueError, "Administrative component"):
            export(self.source, self.policy)

    def test_unresolved_and_remote_refs_rejected(self):
        for ref in ("#/components/schemas/Missing", "https://example.invalid/private.json"):
            with self.subTest(ref=ref):
                source = copy.deepcopy(self.source)
                source["components"]["schemas"]["Contact"]["properties"]["address"]["$ref"] = ref
                with self.assertRaises(ValueError):
                    export(source, self.policy)

    def test_new_source_operation_not_published_without_review(self):
        self.source["paths"][self.path]["post"] = {"responses": {"200": {"description": "New"}}}
        result = export(self.source, self.policy)
        self.assertEqual(set(result["paths"][self.path]), {"get"})

    def test_removed_reviewed_operation_fails(self):
        self.policy["routes"][self.path]["methods"] = ["post"]
        with self.assertRaisesRegex(ValueError, "missing"):
            export(self.source, self.policy)

    def test_validator_rejects_security_drift_and_orphan_schema(self):
        result = export(self.source, self.policy)
        result["paths"][self.path]["get"]["security"] = []
        with self.assertRaisesRegex(ValueError, "lacks bearer"):
            validate_bundle(result, self.policy)
        result = export(self.source, self.policy)
        result["components"]["schemas"]["Orphan"] = {"type": "string"}
        with self.assertRaisesRegex(ValueError, "Unreferenced"):
            validate_bundle(result, self.policy)

    def test_every_operation_has_purpose_and_linked_models(self):
        outputs = catalog(export(self.source, self.policy), self.policy)
        text = outputs["reference/identity.md"].decode()
        self.assertIn("**What it does:**", text)
        self.assertIn("[Contact](../schemas/c.md#contact)", text)

    def test_dictionary_covers_fields_requiredness_and_nullability(self):
        self.source["components"]["schemas"]["Contact"]["properties"]["phoneNumber"] = {"type": "string", "nullable": True}
        outputs = fields_catalog(export(self.source, self.policy), {})
        text = outputs["schemas/c.md"].decode()
        self.assertIn("`phoneNumber`", text)
        self.assertIn("Explicitly allowed", text)
        self.assertIn("| `name` | `string` | Yes |", text)

    def test_scalar_and_binary_responses_are_described_without_invented_models(self):
        self.source["paths"][self.path]["get"]["responses"]["200"] = {
            "description": "Download", "content": {"application/pdf": {
                "schema": {"type": "string", "format": "binary"}
            }}
        }
        text = catalog(export(self.source, self.policy), self.policy)["reference/identity.md"].decode()
        self.assertIn("`string (binary)`", text)
        self.assertIn("`application/pdf`", text)


if __name__ == "__main__":
    unittest.main()
