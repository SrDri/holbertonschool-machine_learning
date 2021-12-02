#!/usr/bin/env python3
"""Add matrix"""


def add_arrays(arr1, arr2):
    """Add arrays"""
    if len(arr1) != len(arr2):
        return None
    else:
        result = []
        for i in range(len(arr1)):
            result.append(arr1[i] + arr2[i])
        return result
