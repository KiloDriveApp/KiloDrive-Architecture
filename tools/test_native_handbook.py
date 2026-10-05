"""Focused invariants for the source-reviewed native-adapter register."""

import csv
import io
import json
import unittest

from native_handbook import INVENTORY_PATH, LIFECYCLES, matrix_text


class NativeHandbookTests(unittest.TestCase):
    def test_every_applicable_platform_has_each_lifecycle(self):
        inventory = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
        rows = list(csv.DictReader(io.StringIO(matrix_text(inventory))))
        for capability in inventory["capabilities"]:
            for platform in ("ios", "android"):
                selected = [
                    row for row in rows
                    if row["capability"] == capability["id"] and row["platform"] == platform
                ]
                if capability[platform].lower().startswith("not applicable"):
                    self.assertEqual([], selected)
                else:
                    self.assertEqual(set(LIFECYCLES), {row["lifecycle"] for row in selected})
                    self.assertTrue(all(row["status"] == "untested" for row in selected))

    def test_matrix_has_no_duplicate_scenario(self):
        inventory = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
        rows = list(csv.DictReader(io.StringIO(matrix_text(inventory))))
        keys = [
            (row["capability"], row["platform"], row["lifecycle"], row["provider_environment"])
            for row in rows
        ]
        self.assertEqual(len(keys), len(set(keys)))


if __name__ == "__main__":
    unittest.main()
