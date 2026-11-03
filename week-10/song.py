class Song:
    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    def get_duration_seconds(self):
        return self.duration_seconds

    def set_duration_seconds(self, duration_seconds):
        self.duration_seconds = duration_seconds


s = Song("Imagine", "John Lennon", 183)
print(s.get_title(), s.get_artist(), s.get_duration_seconds())
