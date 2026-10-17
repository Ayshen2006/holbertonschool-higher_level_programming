#!/usr/bin/python3
"""Find elements that appear in only one of two sets."""


def only_diff_elements(set_1, set_2):
    """Return a set of elements unique to either input set."""
    return set_1 ^ set_2
