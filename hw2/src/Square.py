from otus_course.hw2.src.Figure import Figure
from otus_course.hw2.src.Rectangle import Rectangle
from otus_course.hw2.src.Triangle import Triangle
from otus_course.hw2.src.Circle import Circle


class Square(Figure):

    def __init__(self, side1: int):
        super().__init__(name='squa')
        if side1 <= 0:
            raise ValueError("Сторона квадрата должна быть больше 0")
        super().__init__(side1)
        self.side1 = side1

    def get_area(self):
        return self.side1 ** 2

    def get_perimeter(self):
        return self.side1 * 4

    def add_area(self, other_figure):
        return self.get_area() + other_figure.get_area()


squa = Square(10)
