#!/usr/bin/python3
"""
This module contains functions that do simple math operations.
It is used to demonstrate test-driven development in Python.
All functions handle integers and floats with proper type checking.
"""
def add_integer(a, b=98):
    """Add two integers.

    Returns the addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
