class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_page_count(self):
        return self.page_count

    def set_page_count(self, page_count):
        self.page_count = page_count


b = Book("The Hobbit", "J.R.R. Tolkien", 310)
print(b.get_title(), b.get_author(), b.get_page_count())
