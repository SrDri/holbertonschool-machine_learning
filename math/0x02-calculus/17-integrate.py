#!/usr/bin/env python3
""" integrate func"""


def poly_integral(poly, C=0):
    """ all integrate """
    if type(poly) is not list:
        return None
    elif not poly:
        return None
    elif len(poly) == 0:
        return None
    elif type(C) is not int:
        return None
    elif poly == [0]:
        return [C]
    else:
        new_integral = []
        new_integral.append(C)
        for i in range(len(poly)):
            if poly[i] % (i + 1) == 0:
                new_integral.append(int(poly[i]/(i + 1)))
            else:
                new_integral.append(poly[i]/(i + 1))

        return new_integral
