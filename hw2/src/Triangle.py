from otus_course.hw2.src.Figure import Figure
from otus_course.hw2.src.Square import Square
from otus_course.hw2.src.Circle import Circle
from otus_course.hw2.src.Rectangle import Rectangle


class Triangle(Figure):

    def __init__(self, side1: int, side2: int, side3: int):
        super().__init__(name='tria')
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Стороны треугольника должны быть больше 0")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.p = 0.5 * (side1 + side2 + side3)

    def get_area(self):
        return (self.p * (self.p - self.side1) * (self.p - self.side2) * (self.p - self.side3)) ** 0.5

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def add_area(self, other_figure):
        return self.get_area() + other_figure.get_area()
