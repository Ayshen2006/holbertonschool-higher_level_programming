#!/usr/bin/python3
"""Module containing matrix_divided function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Returns a new matrix with all values rounded to 2 decimals.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix "
            "(list of lists) of integers/floats"
        )

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix "
                "(list of lists) of integers/floats"
            )

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats"
                )

    row_size = len(matrix[0])

    for row in matrix:
        if len(row) != row_size:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
