#!/usr/bin/python3
"""Divide integers safely and print the result."""


def safe_print_division(a, b):
    """Return the division result, or None if division fails."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
