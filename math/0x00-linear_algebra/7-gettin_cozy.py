#!/usr/bin/env python3
"""Cat 2D matrix"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenate 2 matrix"""
    if (len(mat1[0]) == len(mat2[0])) and axis == 0:
        aux_mat1 = [x[:] for x in mat1]
        aux_mat2 = [x[:] for x in mat2]
        aux_mat = aux_mat1 + aux_mat2
        return aux_mat
    elif (len(mat1) == len(mat2)) and axis == 1:
        aux_mat = [mat1[x] + mat2[x] for x in range(len(mat1))]
        return aux_mat
    else:
        return None
