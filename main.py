from sympy import *

from bisection import bisection_method
from plotting import plotting

from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

func = ""


class Interface(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # данные для графика
        labelEntry = Label(text="Введите функцию")
        labelEntry.pack(anchor="n", padx=6, pady=6)

        self.entry = Entry()
        self.entry.pack(anchor="n", padx=6, pady=6)

        labelArea = Label(text="Введите границы функции")
        labelArea.pack(anchor="n", padx=6, pady=6)

        self.area = Entry()
        self.area.pack(anchor="n", padx=6, pady=6)

        # вывод графика
        self.btn = Button(text="Построить график", command=self.get_entry)
        self.btn.pack(anchor="n", padx=6, pady=6)

        # данные для нахождения корня уравнения
        labelBoundary = Label(text="Введите диапазон корня")
        labelBoundary.pack(anchor="n", padx=6, pady=6)

        self.boundary = Entry()
        self.boundary.pack(anchor="n", padx=6, pady=6)

        # точность
        labelaccuracy = Label(text="Введите точность")
        labelaccuracy.pack(anchor="n", padx=6, pady=6)

        self.accuracy = Entry()
        self.accuracy.pack(anchor="n", padx=6, pady=6)

        # получение корня
        self.btnRoot = Button(text="Найти корень", command=self.get_root)
        self.btnRoot.pack(anchor="n", padx=6, pady=6)

        self.labelRoot = Label(text="Корень уравнения: ", font=("Arial", 14), anchor="ne", padx=6, pady=6)
        self.labelRoot.pack(anchor="n", padx=6, pady=6)

        # график
        self.graph = FigureCanvasTkAgg(None, self.master)
        self.graph.get_tk_widget().pack(anchor='s', expand=True, pady=10)

    def get_area(self):
        area = self.area.get()
        self.x1, self.x2 = map(float, area.split())

    def get_boundary(self):
        boundary = self.boundary.get()
        self.a, self.b = map(float, boundary.split())

    # Нахождение корня уравнения
    def get_root(self):
        self.get_boundary()
        self.accur = float(self.accuracy.get())

        root = bisection_method(self.expr, self.accur, self.a, self.b)  # получение корня
        self.labelRoot["text"] = f"Корень уравнения: {round(root, 3)}"

    def get_entry(self):
        self.expr = self.entry.get()

        self.get_area()  # получаем веденные границы

        # Построение графика
        self.graph.figure = plotting(self.expr, self.x1, self.x2)
        self.graph.draw()


def main():
    win = Tk()
    win.geometry("1280x720")
    win.title("Bisection method")
    app = Interface()

    win.mainloop()


if __name__ == '__main__':
    main()
