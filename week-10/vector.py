import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


v = Vector(3, 4)
print(v.get_magnitude())
