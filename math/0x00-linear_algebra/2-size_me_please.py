#!/usr/bin/env python3


def matrix_shape(matrix):
    result = []
    try:
        while len(matrix) > 0:
            result.append(len(matrix))
            matrix = matrix[0]
    except TypeError:
        pass
    return result
