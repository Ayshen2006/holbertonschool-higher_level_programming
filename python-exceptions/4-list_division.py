#!/usr/bin/python3
"""Divide elements of two lists safely."""


def list_division(my_list_1, my_list_2, list_length):
    """Return a list of element-by-element divisions."""
    result = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if not isinstance(a, (int, float)) or not isinstance(
                    b, (int, float)):
                print("wrong type")
                result.append(0)
            else:
                result.append(a / b)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result
