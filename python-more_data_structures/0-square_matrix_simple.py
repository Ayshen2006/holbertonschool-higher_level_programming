#!/usr/bin/python3
"""Compute the square of each integer in a matrix."""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with each integer squared."""
    return [[num ** 2 for num in row] for row in matrix]
