from otus_course.hw2.src.Figure import Figure



class Circle(Figure):

    def __init__(self, r: int):
        super().__init__(name='circ')
        if r <= 0:
            raise ValueError("Радиус круга должен быть больше 0")
        self.PI = 3.14
        self.r = r
        self.d = r * 2

    def get_area(self):
        return self.PI * (self.r ** 2)

    def get_perimeter(self):
        return self.PI * self.d

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()
