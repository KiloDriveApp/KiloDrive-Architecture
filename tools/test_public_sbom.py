"""Public SBOM provenance, ownership and fork-identity checks."""

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from generate_public_sbom import merge_components, component_record, reviewed_text, parse_flutter


class PublicSbomTests(unittest.TestCase):
    def item(self, owner, version="1.0", origin="hosted"):
        return {"ecosystem": "pub", "name": "example", "version": version,
                "scope": "runtime", "owners": owner, "origin": origin, "declaration": "direct main"}

    def test_shared_package_retains_both_app_owners(self):
        rows = merge_components([self.item("consumer"), self.item("system-admin")])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["owners"], "consumer,system-admin")

    def test_different_app_versions_remain_separate(self):
        self.assertEqual(len(merge_components([self.item("consumer"), self.item("system-admin", "2.0")])), 2)

    def test_local_fork_is_not_misrepresented_as_upstream_pub_package(self):
        hosted = self.item("system-admin")
        local = self.item("consumer", origin="reviewed-source-fork")
        self.assertEqual(len(merge_components([hosted, local])), 2)
        self.assertTrue(component_record(hosted)["purl"].startswith("pkg:pub/"))
        self.assertTrue(component_record(local)["purl"].startswith("pkg:generic/kilodrive-vendored/"))

    def test_modified_dependency_metadata_cannot_claim_committed_provenance(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "pubspec.yaml").write_text("version: 2.0\n", encoding="utf-8")
            with patch("generate_public_sbom.subprocess.check_output", return_value=b"version: 1.0\n"):
                with self.assertRaisesRegex(ValueError, "differs from the source commit"):
                    reviewed_text(root, "pubspec.yaml")

    def test_line_endings_do_not_create_false_source_drift(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "pubspec.yaml").write_bytes(b"version: 1.0\r\n")
            with patch("generate_public_sbom.subprocess.check_output", return_value=b"version: 1.0\n"):
                self.assertEqual(reviewed_text(root, "pubspec.yaml"), "version: 1.0\n")

    def test_arbitrary_nonhosted_package_requires_publication_review(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            app = root / "src/client/system_admin"
            app.mkdir(parents=True)
            (app / "pubspec.yaml").write_text("version: 1.0.0+1\n", encoding="utf-8")
            (app / "pubspec.lock").write_text('packages:\n  private_plugin:\n    dependency: "direct main"\n    source: git\n    version: "1.0"\n', encoding="utf-8")
            with patch("generate_public_sbom.reviewed_text", side_effect=lambda base, name: (base / name).read_text()):
                with self.assertRaisesRegex(ValueError, "publication review"):
                    parse_flutter(root, "system_admin")


if __name__ == "__main__":
    unittest.main()
