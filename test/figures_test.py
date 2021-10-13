import random
import pytest
from src.Triangle import Triangle


class TestFigures:

    def test_name(self, figure):
        test_figure = figure.get('figure')
        name = figure.get('name')

        assert test_figure.name == name

    def test_area(self, figure):
        test_figure = figure.get('figure')
        area = figure.get('area')

        assert test_figure.area == area

    def test_perimeter(self, figure):
        test_figure = figure.get('figure')
        perimeter = figure.get('perimeter')

        assert test_figure.perimeter == perimeter

    def test_add_area(self, figure, random_figure):
        test_figure_1 = figure.get('figure')
        test_figure_area_1 = figure.get('area')

        test_figure_2 = random_figure
        test_figure_area_2 = test_figure_2.area

        assert test_figure_1.add_area(test_figure_2) == \
               test_figure_area_1 + test_figure_area_2

    def test_add_area_value_error(self, figure):
        test_figure = figure.get('figure')

        with pytest.raises(ValueError):
            test_figure.add_area(self)

    def test_triangle_impossible(self):
        a = 10
        b = random.uniform(0, 4)
        c = random.uniform(0, 4)

        assert Triangle(a, b, c) is None
