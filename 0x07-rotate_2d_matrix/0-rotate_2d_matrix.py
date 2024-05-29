#!/usr/bin/env python
""" rotating a 2d matrix """


def rotate_2d_matrix(matrix):
    """the main func"""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
