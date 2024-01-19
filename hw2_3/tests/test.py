from otus_course.hw2_3.src.Square import Square
from otus_course.hw2_3.src.Triangle import Triangle
from otus_course.hw2_3.src.Circle import Circle
from otus_course.hw2_3.src.Rectangle import Rectangle

def test_positive_rec():
    r = Rectangle(4, 8)
    assert r.get_area() == 32