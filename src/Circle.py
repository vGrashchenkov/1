from src.Figure import Figure


class Circle(Figure):

    def __init__(self, diameter: float) -> None:
        super().__init__()
        self.name = 'Circle'
        self.diameter = diameter
        self.area = self.area_calculation()
        self.perimeter = self.perimeter_calculation()
