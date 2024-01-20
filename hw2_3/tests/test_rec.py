import pytest

from otus_course.hw2_3.src.Rectangle import Rectangle
from otus_course.hw2_3.src.Circle import Circle


@pytest.mark.parametrize(('side1', 'side2', 'area'),
                         [(4, 8, 32), (5.5, 3.5, 19.25)],
                         ids=['int_value', 'float_value'])
def test_positive_rec_area(side1, side2, area):
    r = Rectangle(side1, side2)
    assert r.get_area() == area


def test_negative_rec_area():
    with pytest.raises(ValueError):
        Rectangle(-3, 5)


@pytest.mark.parametrize(('side1', 'side2', 'perim'),
                         [(4, 8, 24), (5.5, 3.5, 18)],
                         ids=['int_value', 'float_value'])
def test_positive_rec_perim(side1, side2, perim):
    r = Rectangle(side1, side2)
    assert r.get_perimeter() == perim


def test_negative_rec_perim():
    with pytest.raises(ValueError):
        Rectangle(-3, -5)


@pytest.mark.parametrize(('figure1', 'figure2'),
                         [(Rectangle(5, 3), Circle(10))],
                         ids=['Прямоугольник + Круг'])
def test_area_summ(figure1, figure2):
    area_sum = figure1.get_area() + figure2.get_area()
    assert area_sum == figure1.add_area(figure2)
