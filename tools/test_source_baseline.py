"""Version extraction and generated-document drift protection."""

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from native_handbook import source_schema_version, source_version
from source_baseline import current_row_matches, render


class SourceBaselineTests(unittest.TestCase):
    def test_current_row_cannot_pass_using_a_historical_mention(self):
        content = "| Consumer source | `1.0.0+168` | old |\nHistorical 1.0.0+198\n"
        self.assertFalse(current_row_matches(content, "Consumer source", "1.0.0+198"))
        self.assertTrue(current_row_matches(content, "Consumer source", "1.0.0+168"))

    def test_reads_authoritative_flutter_build(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "pubspec.yaml"
            path.write_text("name: app\nversion: 1.0.0+198\n", encoding="utf-8")
            self.assertEqual("1.0.0+198", source_version(path))

    def test_missing_version_is_rejected_not_defaulted(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "pubspec.yaml"
            path.write_text("name: app\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                source_version(path)

    def test_schema_comes_from_constant_not_old_document(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "SchemaContract.cs"
            path.write_text('public const string CurrentVersion = "2026.10.08.2";', encoding="utf-8")
            self.assertEqual("2026.10.08.2", source_schema_version(path))

    def test_all_facts_render_and_change_when_source_changes(self):
        snapshot = dict(reviewedDate="2026-10-08", productSourceRevision="a" * 40,
                        consumerVersion="1.0.0+198", systemAdminVersion="0.1.0+33",
                        schemaContract="2026.10.08.2", privateOpenApiSha256="b" * 64)
        original = render(snapshot)
        for value in snapshot.values():
            self.assertIn(value, original)
        snapshot["consumerVersion"] = "1.0.0+199"
        self.assertNotEqual(original, render(snapshot))


if __name__ == "__main__":
    unittest.main()
