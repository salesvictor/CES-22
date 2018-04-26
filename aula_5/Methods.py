import abc
import math


class Figure:
    MAX_AREA = 10

    def __init__(self, area):
        self.area = area

    @abc.abstractmethod
    def get_perimeter(self):
        return self.perimeter

    @classmethod
    def max_area(cls):
        return cls.MAX_AREA


class Circle(Figure):

    def __init__(self, r):
        self.area = Circle.get_area(r)

    @staticmethod
    def get_area(r):
        return math.pi * r**2

    @classmethod
    def max_radius(cls):
        return math.sqrt(Figure.max_area()/math.pi)

    def get_perimeter(self):
        return 2*math.pi*self.r