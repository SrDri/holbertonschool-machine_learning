#!/usr/bin/env python3
""" Size matrix """


def matrix_shape(matrix):
    result = []
    try:
        result.append(len(matrix))
        while type(matrix[0]) != int:
            result.append(len(matrix[0]))
            matrix = matrix[0]
    except TypeError:
        pass
    return result
