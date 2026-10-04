"""Navigation and public-content regression tests."""

import unittest
from unittest.mock import patch
from pathlib import Path
from tempfile import TemporaryDirectory

import audit_docs
from doc_links import anchors, heading_id


class DocumentationTests(unittest.TestCase):
    def test_api_heading_preserves_the_actual_github_anchor(self):
        self.assertEqual(heading_id("GET `/api/v1/trips/{tripId}`"), "get-apiv1tripstripid")

    def test_duplicate_headings_code_fences_and_explicit_anchors(self):
        text = '# Title\n## Same\n## Same\n```md\n## Not a heading\n```\n<a id="custom"></a>'
        self.assertEqual(anchors(text), {"title", "same", "same-1", "custom"})

    def test_missing_fragment_and_case_are_caught(self):
        with TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            page = root / "README.md"
            page.write_text('# Title\n## Existing\n', encoding='utf-8')
            with patch.object(audit_docs, "ROOT", root):
                self.assertEqual(audit_docs.relative_link_errors(page, '[jump](#existing)'), [])
                self.assertIn("missing heading anchor", audit_docs.relative_link_errors(page, '[jump](#missing)')[0])
                self.assertTrue(audit_docs.relative_link_errors(page, '[page](readme.md)'))
                self.assertEqual(audit_docs.relative_link_errors(page, '```md\n[x](missing.md)\n```'), [])
            audit_docs.file_anchors.cache_clear()

    def test_digest_is_not_an_account_id_but_standalone_digits_are(self):
        account = "123456" * 2
        digest = "a" * 26 + account + "f" * 26
        pattern = audit_docs.SECRET_PATTERNS["AWS account ID"]
        self.assertIsNone(pattern.search('"' + digest + '"'))
        self.assertIsNotNone(pattern.search('"account": "' + account + '"'))


if __name__ == "__main__":
    unittest.main()
