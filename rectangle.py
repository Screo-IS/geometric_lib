def area(a, b):
    """функция принимает на вход два числовых значения a и b, а потом
    при помощи формулы S = a * b находит и возвращает площадь прямоугольника"""
    if (a == '\n' or b == '\n'):
        return "length of side/sides not specified"
    if isinstance(a, bool) or isinstance(b, bool):
        return 'incorrect input, input cannot be a boolean value'
    if isinstance(a, str) or isinstance(b, str):
        return 'incorrect input, input cannot contain letters'
    if a <= 0 or b <= 0:
        return 'incorrect input, the input must contain numbers greater than 0'
    return a * b

def perimeter(a, b):
    """функция принимает на вход два числовых значения a и b, а потом
        при помощи формулы P = 2*a + 2*b находит и возвращает периметр прямоугольника"""
    if (a == '\n' or b == '\n'):
        return "length of side/sides not specified"
    if isinstance(a, bool) or isinstance(b, bool):
        return 'incorrect input, input cannot be a boolean value'
    if isinstance(a, str) or isinstance(b, str):
        return 'incorrect input, input cannot contain letters'
    if a <= 0 or b <= 0:
        return 'incorrect input, the input must contain numbers greater than 0'
    return 2*a + 2*b