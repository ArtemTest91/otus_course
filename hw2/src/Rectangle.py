from otus_course.hw2.src.Figure import Figure
from otus_course.hw2.src.Square import Square
from otus_course.hw2.src.Triangle import Triangle
from otus_course.hw2.src.Circle import Circle


class Rectangle(Figure):
    def __init__(self, side1: int, side2: int):
        super().__init__(name='rect')
        if side1 <= 0 or side2 <= 0:
            raise ValueError("Стороны прямоугольника должны быть больше 0")
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        return self.side1 * self.side2

    def get_perimeter(self):
        return (self.side1 + self.side2) * 2

    def add_area(self, other_figure):
        return self.get_area() + other_figure.get_area()


rect = Rectangle(5, 3)
print(rect.add_area + squa.get_area(10))
