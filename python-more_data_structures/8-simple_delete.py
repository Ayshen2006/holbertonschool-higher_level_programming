#!/usr/bin/python3
"""Delete a key from a dictionary."""


def simple_delete(a_dictionary, key=""):
    """Delete the specified key if it exists and return the dictionary."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
