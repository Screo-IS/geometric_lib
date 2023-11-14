
def area(a):
    """функция принимает на вход число a, а потом при помощи формулы
    S = a * a находит и возвращает площадь квадрата"""
    if (a == '\n'):
        return "length of side/sides not specified"
    if isinstance(a, bool):
        return 'incorrect input, input cannot be a boolean value'
    if isinstance(a, str):
        return 'incorrect input, input cannot contain letters'
    if a <= 0:
        return 'incorrect input, the input must contain numbers greater than 0'
    return a * a


def perimeter(a):
    """функция принимает на вход число a, а потом при помощи формулы
        P = 4*a находит и возвращает площадь квадрата"""
    if (a == '\n'):
        return "length of side/sides not specified"
    if isinstance(a, bool):
        return 'incorrect input, input cannot be a boolean value'
    if isinstance(a, str):
        return 'incorrect input, input cannot contain letters'
    if a <= 0:
        return 'incorrect input, the input must contain numbers greater than 0'
    return 4 * a
