import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius


c = Circle(3)
print(c.calculate_circumference())
