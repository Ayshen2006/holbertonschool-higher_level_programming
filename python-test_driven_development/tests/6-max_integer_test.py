#!/usr/bin/python3
"""Unit tests for max_integer."""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 3, 2, 1]), 9)

    def max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 9, 3, 2]), 9)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4)

    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-9, -2, -7, -5]), -2)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([3, 5, 5, 2]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.2, 5.6, 3.4]), 5.6)

    def test_string(self):
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
