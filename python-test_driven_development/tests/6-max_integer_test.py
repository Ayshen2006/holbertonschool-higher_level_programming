#!/usr/bin/python3
"""Unit tests for max_integer."""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_item(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_ordered_list(self):
        """Test an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list."""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test a list of negative integers."""
        self.assertEqual(max_integer([-8, -3, -15, -1]), -1)

    def test_mixed_numbers(self):
        """Test a list of positive and negative integers."""
        self.assertEqual(max_integer([-5, 0, 10, -2]), 10)

    def test_duplicate_maximum(self):
        """Test duplicate maximum values."""
        self.assertEqual(max_integer([4, 2, 4, 1]), 4)

    def test_max_at_beginning(self):
        """Test when the maximum is the first element."""
        self.assertEqual(max_integer([9, 3, 2, 1]), 9)

    def test_float_numbers(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.1, 5.5, 2.2]), 5.5)

    def test_string(self):
        """Test a string."""
        self.assertEqual(max_integer("Holberton"), "t")


if __name__ == "__main__":
    unittest.main()


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
