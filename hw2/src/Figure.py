from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(Figure, other_figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()
