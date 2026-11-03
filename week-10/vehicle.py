class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def print_vehicle_type(self):
        print(f"{self.year} {self.make} {self.model}")


v = Vehicle("Toyota", "Camry", 2021)
v.print_vehicle_type()
