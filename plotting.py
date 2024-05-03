from sympy import *
from sympy.plotting import plot

import matplotlib


# получение backend графика
def plotting(func, x1, x2):
    x = Symbol('x')
    plt = plot(func, (x, x1, x2), line_color='red', xlabel='x', ylabel='y', show=False)

    backend = plt.backend(plt)
    backend.process_series()  # Обработать данные графика

    fig = backend.fig  # Получили Figure
    return fig


if __name__ == '__main__':
    plotting()
