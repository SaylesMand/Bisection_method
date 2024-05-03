from math import *

import sympy
from sympy.abc import x
from sympy import sympify
from sympy.utilities.lambdify import lambdastr


def parse_math(expr):
    if expr != '':
        # вот здесь самая главная часть программы
        res = lambdastr(x, expr)
        res = eval(res)
        # ----------
        return res
    else:
        return False


def bisection_method(f, error, a, b, max_iter=100):
    f = parse_math(f)

    if f(a) * f(b) > 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала")

    n = 0
    while (b - a) / 2 > error and n < max_iter:
        x = (a + b) / 2

        if f(x) == 0:
            return x

        elif f(x) * f(a) < 0:
            b = x

        else:
            a = x

        n += 1

    return (a + b) / 2


if __name__ == '__main__':
    bisection_method()
