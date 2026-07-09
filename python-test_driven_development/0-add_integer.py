#!/usr/bin/python3
"""
Module containing the add_integer function.
The function accepts integers or floats, converts floats to integers,
and returns the sum.
"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
