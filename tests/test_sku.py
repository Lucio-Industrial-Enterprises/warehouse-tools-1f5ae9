import unittest

from warehouse.sku import normalize_sku


class SkuTests(unittest.TestCase):
    def test_canonical_sku(self):
        for value, expected in (
            (" a-12 ", "A-12"),
            ("\tAb-12\n", "AB-12"),
            ("A-12", "A-12"),
        ):
            with self.subTest(value=value):
                self.assertEqual(normalize_sku(value), expected)

    def test_blank_sku(self):
        with self.assertRaises(ValueError):
            normalize_sku("  ")
