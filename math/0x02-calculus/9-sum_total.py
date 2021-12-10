#!/usr/bin/env python3
"""	summation """


def summation_i_squared(n):
    """ summation exp """
    if type(n) is not int or n < 1:
        return None
    else:
        return int(n * (n + 1) * (2 * n + 1) / 6)
