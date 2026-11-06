class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    def play(self):
        print(f"Playing {self.title} by {self.artist}")

    def __str__(self):
        return f"{self.title} - {self.artist}"


class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def play_all(self):
        for song in self.songs:
            song.play()

    def __str__(self):
        return f"{self.playlist_name} ({len(self.songs)} songs)"


playlist = Playlist("Study Mix")
playlist.add_song(Song("Lofi Beat", "Chill Artist"))
playlist.add_song(Song("Focus", "Deep Work"))
print(playlist)
playlist.play_all()
