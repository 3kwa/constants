import unittest
import os

import constants


class TestConstants(unittest.TestCase):
    def test_integer_cast(self):
        result = constants.Constants.cast("1")
        self.assertEqual(1, result)

    def test_float_cast(self):
        result = constants.Constants.cast("3.14")
        self.assertEqual(3.14, result)

    def test_float_cast_starting_with_0(self):
        result = constants.Constants.cast("0.02")
        self.assertEqual(0.02, result)

    def test_string_cast(self):
        result = constants.Constants.cast("a_string")
        self.assertEqual("a_string", result)

    def test_integer_with_leading_zero_not_cast(self):
        result = constants.Constants.cast("0350")
        self.assertEqual("0350", result)

    def test_boolean(self):
        result = constants.Constants.cast("True")
        self.assertEqual(True, result)

    def test_expression(self):
        result = constants.Constants.cast("365 * 24 * 60")
        self.assertEqual(525600, result)

    def test_invalid_expression(self):
        result = constants.Constants.cast("3 * 5 / 100 %")
        self.assertEqual("3 * 5 / 100 %", result)
