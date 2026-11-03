class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def calculate_area(self):
        return self.width * self.height


r = Rectangle(4, 5)
print(r.calculate_area())
