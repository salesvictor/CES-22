class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        return NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

    def plot(self, ratio, topleft):
        print(f'Plotting from Shape at {topleft}, ratio {ratio}')

class Plotter:

    def plot(self, ratio, topleft):
        print(f'Plotting from Plotter at {topleft}, ratio {ratio}')


class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'


class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side


class RegularHexagon(RegularPolygon):
    geometric_type = 'Regular Hexagon'

    def area(self):
        return 1.5 * (3**.5 * self.side**2)


class Square(RegularPolygon):
    geometric_type = 'Square'

    def area(self):
        return self.side**2


class RegularPolygon2(Plotter, Shape):
    geometric_type = 'Regular Polygon 2'

    def __init__(self, side):
        self.side = side


class RegularTriangle(RegularPolygon2):
    geometric_type = 'Regular Triangle'

    def area(self):
        return 3**.5 * self.side**2 / 4


square = Square(10)
square.plot(10, 0)

triangle = RegularTriangle(10)
triangle.plot(10, 0)
