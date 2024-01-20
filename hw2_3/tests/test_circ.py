import pytest

from otus_course.hw2_3.src.Circle import Circle
from otus_course.hw2_3.src.Triangle import Triangle


@pytest.mark.parametrize(('r', 'area'),
                         [(5, 78.50), (3.5, 38.47)],
                         ids=['int_value', 'float_value'])
def test_positive_circ_area(r, area):
    s = Circle(r)
    assert round(s.get_area(), 2) == round(area, 2)


def test_negative_circ_area():
    with pytest.raises(ValueError):
        Circle(-5)


@pytest.mark.parametrize(('r', 'perim'),
                         [(5, 31.40), (5.5, 34.54)],
                         ids=['int_value', 'float_value'])
def test_positive_circ_perim(r, perim):
    r = Circle(r)
    assert round(r.get_perimeter(), 2) == round(perim, 2)


def test_negative_circ_perim():
    with pytest.raises(ValueError):
        Circle(-3)


@pytest.mark.parametrize(('figure1', 'figure2'),
                         [(Circle(5), Triangle(16, 20, 32))],
                         ids=['Круг + Треугольник'])
def test_area_summ(figure1, figure2):
    area_sum = figure1.get_area() + figure2.get_area()
    assert area_sum == figure1.add_area(figure2)
