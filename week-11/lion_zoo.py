class Lion:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender  # "male" or "female"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def roar(self):
        print("Roar")

    def __str__(self):
        return f"{self.name} ({self.gender})"


class Zoo:
    def __init__(self, location):
        self.location = location
        self.lions = []

    def add_lion(self, lion):
        self.lions.append(lion)

    def lions_roar(self):
        for lion in self.lions:
            lion.roar()

    def count_lions(self):
        males = 0
        females = 0
        for lion in self.lions:
            if lion.gender == "male":
                males += 1
            else:
                females += 1
        print(f"{males} male, {females} female")

    def __str__(self):
        return f"Zoo in {self.location} with {len(self.lions)} lions"


zoo = Zoo("Mankato")
zoo.add_lion(Lion("Simba", "male"))
zoo.add_lion(Lion("Nala", "female"))
print(zoo)
zoo.lions_roar()
zoo.count_lions()
