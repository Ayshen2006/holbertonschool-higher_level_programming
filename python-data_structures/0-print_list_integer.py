#!/usr/bin/python3
"""Print integers from a list."""


def print_list_integer(my_list=[]):
    """Print each integer in the list on a separate line."""
    for num in my_list:
        print("{:d}".format(num))
