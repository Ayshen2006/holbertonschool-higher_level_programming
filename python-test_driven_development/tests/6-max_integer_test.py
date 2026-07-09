#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_list_of_one_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_max_at_the_beginning(self):
        """Test when the maximum is at the beginning."""
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_at_the_end(self):
        """Test when the maximum is at the end."""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_max_in_the_middle(self):
        """Test when the maximum is in the middle."""
        self.assertEqual(max_integer([1, 9, 3, 2]), 9)

    def test_one_negative_number(self):
        """Test a list containing one negative number."""
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def test_only_negative_numbers(self):
        """Test a list of only negative numbers."""
        self.assertEqual(max_integer([-8, -2, -5, -9]), -2)

    def test_duplicate_maximum(self):
        """Test duplicate maximum values."""
        self.assertEqual(max_integer([4, 7, 7, 2]), 7)

    def test_float_numbers(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.2, 5.6, 3.4]), 5.6)


if __name__ == "__main__":
    unittest.main()
