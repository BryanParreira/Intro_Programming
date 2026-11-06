class Duck:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def speak(self):
        print("Quack")

    def __str__(self):
        return f"{self.name} the {self.color} duck"


class Pond:
    def __init__(self, name):
        self.name = name
        self.ducks = []

    def add_duck(self, duck):
        self.ducks.append(duck)

    def ducks_quack(self):
        for duck in self.ducks:
            duck.speak()

    def __str__(self):
        return f"Pond {self.name} with {len(self.ducks)} ducks"


pond = Pond("Willow Pond")
pond.add_duck(Duck("Donald", "white"))
pond.add_duck(Duck("Daisy", "brown"))
print(pond)
pond.ducks_quack()
