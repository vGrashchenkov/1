from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, height: float, length: float) -> None:
        super().__init__()
        self.name = 'Rectangle'
        self.height = height
        self.length = length
        self.area = self.area_calculation()
        self.perimeter = self.perimeter_calculation()

    def area_calculation(self) -> float:

        return self.height * self.length

    def perimeter_calculation(self) -> float:

        return self.height * 2 + self.length * 2
