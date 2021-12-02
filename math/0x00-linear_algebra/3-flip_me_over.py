#!/usr/bin/env python3
"""Transpose a matrix"""


def matrix_transpose(matrix):
    """Matrix transpose"""
    result = []
    for i in range(len(matrix[0])):
        aux = []
        for j in matrix:
            aux += [j[i]]
        result += [aux]
    return result
