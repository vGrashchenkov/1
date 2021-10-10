from src.Figure import Figure


class Square(Figure):

    def __init__(self, height: float) -> None:
        super().__init__()
        self.name = 'Square'
        self.height = height
        self.area = self.area_calculation()
        self.perimeter = self.perimeter_calculation()
