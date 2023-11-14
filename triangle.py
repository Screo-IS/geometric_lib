def area(a, h):
    """функция принимает на вход числа:
    а - основание треугольника
    h - высота треугольника
    Потом при помощи формулы S = a * h / 2 находит и возвращает площадь треугольника"""
    if (a == '\n') or (h == '\n'):
        return "length of side/sides not specified"
    if isinstance(a, bool) or isinstance(h, bool):
        return 'incorrect input, input cannot be a boolean value'
    if isinstance(a, str) or isinstance(h, str):
        return 'incorrect input, input cannot contain letters'
    if a <= 0 or h <= 0:
        return 'incorrect input, the input must contain numbers greater than 0'
    return a * h / 2

def perimeter(a, b, c):
    """функция принимает на вход три числа:
      a,b,c - стороны треугольника
      Потом при помощи формулы P = a + b + c находит и возвращает периметр треугольника"""
    if (a == '\n' or b == '\n' or c == '\n'):
        return "length of side/sides not specified"
    if isinstance(a, bool) or isinstance(b, bool) or isinstance(c, bool):
        return 'incorrect input, input cannot be a boolean value'
    if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
        return 'incorrect input, input cannot contain letters'
    if a <= 0 or b <= 0 or c <= 0:
        return 'incorrect input, the input must contain numbers greater than 0'
    if max(a, b, c) - ((a + b + c) - max(a, b, c)) >= 0:
        return 'incorrect input, the basic property of a triangle must be satisfied'
    return a + b + c