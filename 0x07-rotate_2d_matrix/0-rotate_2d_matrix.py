#!/usr/bin/python3
"""
Rotate a 2d matrix in-place

Modules imported: None

"""


def rotate_2d_matrix(matrix):
    """Rotates a n * n  matrix without returning a new copy of the matrix
    """
    # transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # reverse each row in the matrix
    for row in matrix:
        row.reverse()
