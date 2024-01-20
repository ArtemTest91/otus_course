import pytest

from otus_course.hw2_3.src.Triangle import Triangle
from otus_course.hw2_3.src.Rectangle import Rectangle


@pytest.mark.parametrize(('side1', 'side2', 'side3', 'area'),
                         [(16, 20, 32, 130.90), (4.5, 6.5, 10.5, 8.45)],
                         ids=['int_value', 'float_value'])
def test_positive_tria_area(side1, side2, side3, area):
    s = Triangle(side1, side2, side3)
    assert round(s.get_area(), 2) == round(area, 2)


def test_negative_tria_area():
    with pytest.raises(ValueError):
        Triangle(-5, 9, 18)


@pytest.mark.parametrize(('side1', 'side2', 'side3', 'perim'),
                         [(16, 20, 32, 68), (4.5, 6.5, 10.5, 21.50)],
                         ids=['int_value', 'float_value'])
def test_positive_tria_perim(side1, side2, side3, perim):
    r = Triangle(side1, side2, side3)
    assert round(r.get_perimeter(), 2) == round(perim, 2)


def test_negative_tria_perim():
    with pytest.raises(ValueError):
        Triangle(-3, 7, 12)


@pytest.mark.parametrize(('figure1', 'figure2'),
                         [(Rectangle(5, 3), Triangle(16, 20, 32))],
                         ids=['Прямоугольник + Треугольник'])
def test_area_summ(figure1, figure2):
    area_sum = figure1.get_area() + figure2.get_area()
    assert area_sum == figure1.add_area(figure2)
