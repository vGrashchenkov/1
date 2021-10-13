from math import pi, sqrt


class Figure:
    def __init__(self) -> None:
        self.c = None
        self.b = None
        self.a = None
        self.area = None
        self.length = None
        self.height = None
        self.diameter = None
        self.name = 'Figure'

    def area_calculation(self) -> float:

        if self.name == 'Circle':
            return pi * self.diameter ** 2 / 4
        elif self.name == 'Square':
            return self.height ** 2
        elif self.name == 'Rectangle':
            return self.height * self.length
        elif self.name == 'Triangle':
            p = (self.a + self.b + self.c) / 2
            return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        else:
            raise ValueError('Неизвестная фигура')

    def perimeter_calculation(self) -> float:

        if self.name == 'Circle':
            return pi * self.diameter
        elif self.name == 'Square':
            return self.height * 4
        elif self.name == 'Rectangle':
            return self.height * 2 + self.length * 2
        elif self.name == 'Triangle':
            return self.a + self.b + self.c
        else:
            raise ValueError('Неизвестная фигура')

    def add_area(self, figure) -> float:

        try:
            area_sum = self.area + getattr(figure, 'area')
        except AttributeError:
            raise ValueError('Передана не фигура')

        return area_sum
