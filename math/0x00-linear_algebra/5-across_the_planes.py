#!/usr/bin/env python3
"""Add 2D matrix"""


def add_matrices2D(mat1, mat2):
    """2D add matrix"""
    if len(mat1) == len(mat2):
        result = []
        for i in range(len(mat1)):
            aux = []
            if len(mat1[i]) == len(mat2[i]):
                for j in range(len(mat1[i])):
                    aux.append(mat1[i][j] + mat2[i][j])
                result.append(aux)
            else:
                return None
        return result
        