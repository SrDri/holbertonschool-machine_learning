#!/usr/bin/env python3
"""multiplication Matrix"""


def mat_mul(mat1, mat2):
    """Multiplication mat1 * mat2"""
    if len(mat1[0]) != len(mat2):
        return None
    else:
        result = []
        for i in range(len(mat1)):
            aux = []
            for j in range(len(mat2[0])):
                counter = 0
                for k in range(len(mat2)):
                    counter += mat1[i][k] * mat2[k][j]
                aux.append(counter)
            result.append(aux)
        return result
