class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def display_info(self):
        print(f"{self.title} by {self.author}")

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_catalog(self):
        for book in self.books:
            book.display_info()

    def __str__(self):
        return f"{self.library_name} ({len(self.books)} books)"


library = Library("City Library")
library.add_book(Book("Dune", "Frank Herbert"))
library.add_book(Book("Emma", "Jane Austen"))
print(library)
library.display_catalog()
