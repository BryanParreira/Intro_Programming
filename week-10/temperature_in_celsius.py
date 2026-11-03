class TemperatureInCelsius:
    def __init__(self, temp_value):
        self.temp_value = temp_value

    def get_temp_value(self):
        return self.temp_value

    def set_temp_value(self, temp_value):
        self.temp_value = temp_value

    def to_fahrenheit(self):
        return (self.temp_value * 9 / 5) + 32


t = TemperatureInCelsius(100)
print(t.to_fahrenheit())
