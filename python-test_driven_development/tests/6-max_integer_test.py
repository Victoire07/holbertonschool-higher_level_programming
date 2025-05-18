#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests unitaires pour la fonction max_integer"""

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_beginning(self):
        self.assertEqual(max_integer([5, 2, 3, 1]), 5)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, 9, 2, 3]), 9)

    def test_one_element(self):
        self.assertEqual(max_integer([8]), 8)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_all_negative(self):
        self.assertEqual(max_integer([-10, -20, -5, -30]), -5)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-1, 0, 7, -8]), 7)

    def test_all_equal(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_float_list(self):
        self.assertEqual(max_integer([1.5, 2.8, 3.9, 2.0]), 3.9)

    def test_string_input(self):
        self.assertEqual(max_integer("bonjour"), "u")

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])
