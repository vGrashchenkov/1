import random
import pytest
from math import pi, sqrt
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture(params=["Circle", "Square", "Rectangle", "Triangle"])
def figure(request):
    if request.param == "Circle":
        diameter = random.uniform(0, 10)
        figure = Circle(diameter)
        area = pi * diameter ** 2 / 4
        perimeter = pi * diameter

        return dict(
            figure=figure,
            name="Circle",
            area=area,
            perimeter=perimeter
        )

    elif request.param == "Square":
        height = random.uniform(0, 10)
        figure = Square(height)
        area = height ** 2
        perimeter = height * 4

        return dict(
            figure=figure,
            name="Square",
            area=area,
            perimeter=perimeter
        )

    elif request.param == "Rectangle":
        height = random.uniform(0, 10)
        length = random.uniform(0, 10)
        figure = Rectangle(height, length)
        area = height * length
        perimeter = height * 2 + length * 2

        return dict(
            figure=figure,
            name="Rectangle",
            area=area,
            perimeter=perimeter
        )

    elif request.param == "Triangle":
        a = random.uniform(4, 5)
        b = random.uniform(4, 5)
        c = random.uniform(1, 8)
        figure = Triangle(a, b, c)
        p = (a + b + c) / 2
        area = sqrt(p * (p - a) * (p - b) * (p - c))
        perimeter = a + b + c

        return dict(
            figure=figure,
            name="Triangle",
            area=area,
            perimeter=perimeter
        )


@pytest.fixture()
def random_figure():
    figure = random.choice(["Circle", "Square", "Rectangle", "Triangle"])

    if figure == "Circle":
        diameter = random.uniform(0, 10)

        return Circle(diameter)

    elif figure == "Square":
        height = random.uniform(0, 10)

        return Square(height)

    elif figure == "Rectangle":
        height = random.uniform(0, 10)
        length = random.uniform(0, 10)

        return Rectangle(height, length)

    elif figure == "Triangle":
        a = random.uniform(4, 5)
        b = random.uniform(4, 5)
        c = random.uniform(1, 8)

        return Triangle(a, b, c)
