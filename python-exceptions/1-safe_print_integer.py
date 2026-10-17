#!/usr/bin/python3
"""Print an integer safely."""


def safe_print_integer(value):
    """Print value as an integer and return True if successful."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
