#!/usr/bin/python3
"""This module provides a function that prints text with indentation.

The text is printed with two new lines after each '.', '?' and ':'
character while removing leading spaces from each new printed line.
"""


def text_indentation(text):
    """Print a text with two new lines after '.', '?' and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""

    for char in text:
        line += char
        if char in ".?:":
            print(line.strip(), end="\n\n")
            line = ""

    if line:
        print(line.strip(), end="")
