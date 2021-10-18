from math import pi, sqrt


class Figure:

    def add_area(self, figure) -> float:

        try:
            area_sum = self.area + getattr(figure, 'area')
        except AttributeError:
            raise ValueError('Передана не фигура')

        return area_sum
