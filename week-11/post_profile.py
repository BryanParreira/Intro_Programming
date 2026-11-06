class Post:
    def __init__(self, caption, likes):
        self.caption = caption
        self.likes = likes

    def get_likes(self):
        return self.likes

    def add_like(self):
        self.likes += 1

    def display(self):
        print(self.caption)

    def __str__(self):
        return f"{self.caption} ({self.likes} likes)"


class Profile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def display_trending_posts(self):
        for post in self.posts:
            if post.get_likes() >= 10000:  # trending
                post.display()

    def __str__(self):
        return f"@{self.username} ({len(self.posts)} posts)"


profile = Profile("bryan")
profile.add_post(Post("Sunset at the lake", 12000))
profile.add_post(Post("My lunch", 25))
print(profile)
profile.display_trending_posts()  # only the sunset post
