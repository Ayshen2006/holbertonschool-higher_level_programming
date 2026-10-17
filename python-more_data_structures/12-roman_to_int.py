#!/usr/bin/python3
"""Convert a Roman numeral to an integer."""


def roman_to_int(roman_string):
    """Return the integer value of a Roman numeral."""
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    total = 0
    previous = 0

    for char in reversed(roman_string):
        value = values.get(char, 0)
        if value < previous:
            total -= value
        else:
            total += value
        previous = value

    return total
