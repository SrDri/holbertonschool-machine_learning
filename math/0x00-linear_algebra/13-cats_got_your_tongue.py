#!/usr/bin/env python3
"""concatenate matrix"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """concatenate func"""
    mat_1 = np.array(mat1)
    mat_2 = np.array(mat2)
    result = np.concatenate((mat_1, mat_2), axis)
    return result
