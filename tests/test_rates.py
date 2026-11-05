import unittest

from warehouse.rates import shipping_quote


class StandardRateTests(unittest.TestCase):
    def test_standard_local(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)

    def test_standard_regional(self):
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_service(self):
        self.assertEqual(shipping_quote(2, "local", service="standard"), 8.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "international")

    def test_invalid_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")


class ExpressRateTests(unittest.TestCase):
    def test_express_local(self):
        # base 10.0 + 3.0 * 2 = 16.0
        self.assertEqual(shipping_quote(2, "local", service="express"), 16.0)

    def test_express_regional(self):
        # base 15.0 + 3.0 * 2 = 21.0
        self.assertEqual(shipping_quote(2, "regional", service="express"), 21.0)

    def test_express_fractional_weight(self):
        # base 10.0 + 3.0 * 1.5 = 14.5
        self.assertEqual(shipping_quote(1.5, "local", service="express"), 14.5)

    def test_express_more_than_standard(self):
        standard = shipping_quote(5, "regional", service="standard")
        express = shipping_quote(5, "regional", service="express")
        self.assertGreater(express, standard)
