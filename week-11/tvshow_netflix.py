class TVShow:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def preview(self):
        print(f"{self.title} ({self.genre})")

    def __str__(self):
        return f"{self.title} - {self.genre}"


class NetflixDashboard:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.shows = []

    def add_show(self, show):
        self.shows.append(show)

    def display_recommendations(self):
        for show in self.shows:
            show.preview()

    def __str__(self):
        return f"{self.profile_name}'s dashboard ({len(self.shows)} shows)"


dashboard = NetflixDashboard("Bryan")
dashboard.add_show(TVShow("Breaking Bad", "Drama"))
dashboard.add_show(TVShow("The Office", "Comedy"))
print(dashboard)
dashboard.display_recommendations()
