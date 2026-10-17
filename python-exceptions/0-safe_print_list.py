#!/usr/bin/python3
"""Print list elements safely."""


def safe_print_list(my_list=[], x=0):
    """Print x elements and return the number actually printed."""
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
