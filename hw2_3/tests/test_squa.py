import pytest

from otus_course.hw2_3.src.Square import Square
from otus_course.hw2_3.src.Triangle import Triangle


@pytest.mark.parametrize(('side1', 'area'),
                         [(4, 16), (4.5, 20.25)],
                         ids=['int_value', 'float_value'])
def test_positive_squa_area(side1, area):
    s = Square(side1)
    assert round(s.get_area() == area)


def test_negative_squa_area():
    with pytest.raises(ValueError):
        Square(-5)


@pytest.mark.parametrize(('side1', 'perim'),
                         [(5, 20), (5.5, 22)],
                         ids=['int_value', 'float_value'])
def test_positive_squa_perim(side1, perim):
    r = Square(side1)
    assert round(r.get_perimeter() == perim)


def test_negative_squa_perim():
    with pytest.raises(ValueError):
        Square(-3)


@pytest.mark.parametrize(('figure1', 'figure2'),
                         [(Square(5), Triangle(16, 20, 32))],
                         ids=['Квадрат + Треугольник'])
def test_area_summ(figure1, figure2):
    area_sum = figure1.get_area() + figure2.get_area()
    assert area_sum == figure1.add_area(figure2)
