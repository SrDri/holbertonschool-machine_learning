#!/usr/bin/env python3
""" calculates the derivative """


def poly_derivative(poly):
    """ function calculate the derivative """

    if type(poly) != list or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    if poly is None:
        return None
    new = list(range(len(poly)-1))
    for i in range(len(new)):
        if type(i) != int:
            return None
        new[i] = poly[i + 1] * (i + 1)
    return new
