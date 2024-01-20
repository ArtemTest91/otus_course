from otus_course.hw2_3.src.Figure import Figure


class Triangle(Figure):

    def __init__(self, side1: int, side2: int, side3: int):
        super().__init__(name='tria')
        if ((side1 <= 0 or side2 <= 0 or side3 <= 0) or
                (side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1)):
            raise ValueError("Некорректные значения сторон треугольника")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.p = 0.5 * (side1 + side2 + side3)

    def get_area(self):
        return round((self.p * (self.p - self.side1) * (self.p - self.side2) * (self.p - self.side3)) ** 0.5, 2)

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()
