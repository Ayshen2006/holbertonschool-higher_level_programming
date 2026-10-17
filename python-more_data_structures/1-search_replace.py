#!/usr/bin/python3
"""Replace occurrences of an element in a list."""


def search_replace(my_list, search, replace):
    """Return a new list with matching elements replaced."""
    return [replace if item == search else item for item in my_list]
