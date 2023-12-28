import pytest
from shapes import Rectangle


@pytest.fixture
def rectangle_instance():
    return Rectangle(4, 5)


def test_get_area(rectangle_instance):
    assert rectangle_instance.get_area() == 20


def test_get_perimeter(rectangle_instance):
    assert rectangle_instance.get_perimeter() == 18


def test_non_numeric_input():
    with pytest.raises(TypeError):
        Rectangle("a", 5)

    with pytest.raises(TypeError):
        Rectangle(4, "b")

    with pytest.raises(TypeError):
        Rectangle("x", "y")


def test_negative_width():
    with pytest.raises(ValueError):
        Rectangle(-2, 5)


def test_negative_height():
    with pytest.raises(ValueError):
        Rectangle(4, -5)