#!/usr/bin/python3
"""
This module contains functions that do simple math operations.
"""



def add_integer(a, b=100):
    """Adds two integers and returns the result."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
