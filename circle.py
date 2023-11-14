import math
import unittest

def area(r):
    """принимает число r (радиус), возвращает площадь круга через формулу
    S = π * r * r"""
    if (r == '\n'):
        return "length of side/sides not specified"
    if isinstance(r, bool):
        return 'incorrect input, input cannot be a boolean value'
    if isinstance(r, str):
        return 'incorrect input, input cannot contain letters'
    if r <= 0:
        return 'incorrect input, the input must contain numbers greater than 0'
    return math.pi * r * r


def perimeter(r):
    """"принимает число r (радиус), возвращает периметр круга через формулу
    P = 2 * π * r"""
    if (r == '\n'):
        return "length of side/sides not specified"
    if isinstance(r, bool):
        return 'incorrect input, input cannot be a boolean value'
    if isinstance(r, str):
        return 'incorrect input, input cannot contain letters'
    if r <= 0:
        return 'incorrect input, the input must contain numbers greater than 0'
    return 2 * math.pi * r
