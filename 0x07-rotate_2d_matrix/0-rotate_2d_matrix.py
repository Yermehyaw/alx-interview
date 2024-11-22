#!/usr/bin/python3
"""
Rotate a 2d matrix in-place

Modules imported: None

"""


def rotate_2d_matrix(matrix):
    """Rotates a 2d matrix without returning a new copy of the matrix
    """
    # reverse each row in the matrix
    for row in matrix:
        i = 0
        j = len(row) - 1
        while j != i:
            temp = row[j]
            row[j] = row[i]
            row[i] = temp
            j -= 1
            i += 1

    # transpose the matrix
