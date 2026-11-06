class Droid:
    def __init__(self, designation, series):
        self.designation = designation
        self.series = series

    def get_series(self):
        return self.series

    def set_series(self, series):
        self.series = series

    def communicate(self):
        print("Beep-Bloop-Blop")

    def __str__(self):
        return f"{self.designation} ({self.series} series)"


class Starship:
    def __init__(self, name):
        self.name = name
        self.droids = []

    def add_droid(self, droid):
        self.droids.append(droid)

    def droids_communicate(self):
        for droid in self.droids:
            droid.communicate()

    def __str__(self):
        return f"Starship {self.name} with {len(self.droids)} droids"


ship = Starship("Falcon")
ship.add_droid(Droid("R2-D2", "R2"))
ship.add_droid(Droid("C-3PO", "3PO"))
print(ship)
ship.droids_communicate()
