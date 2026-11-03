class Movie:
    def __init__(self, title, director, runtime_minutes):
        self.title = title
        self.director = director
        self.runtime_minutes = runtime_minutes

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_director(self):
        return self.director

    def set_director(self, director):
        self.director = director

    def get_runtime_minutes(self):
        return self.runtime_minutes

    def set_runtime_minutes(self, runtime_minutes):
        self.runtime_minutes = runtime_minutes


m = Movie("Inception", "Christopher Nolan", 148)
print(m.get_title(), m.get_director(), m.get_runtime_minutes())
