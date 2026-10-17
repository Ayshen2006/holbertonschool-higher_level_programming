#!/usr/bin/python3
"""Multiply all dictionary values by two."""


def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by two."""
    return {key: value * 2 for key, value in a_dictionary.items()}
