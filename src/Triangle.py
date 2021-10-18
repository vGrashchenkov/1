from math import sqrt
from src.Figure import Figure


class Triangle(Figure):

    def __new__(cls, a: float, b: float, c: float):

        if a < b + c and b < c + a and c < a + b:
            return super(Triangle, cls).__new__(cls)
        else:
            return None

    def __init__(self, a: float, b: float, c: float) -> None:
        super().__init__()
        self.name = 'Triangle'
        self.a = a
        self.b = b
        self.c = c
        self.area = self.area_calculation()
        self.perimeter = self.perimeter_calculation()

    def area_calculation(self) -> float:

        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter_calculation(self) -> float:

        return self.a + self.b + self.c
