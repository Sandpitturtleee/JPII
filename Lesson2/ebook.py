from Lesson2.book import Book


class Ebook(Book):
    def __init__(self, title: str, author: str, publish_year: int, file_size: float):
        super().__init__(title, author, publish_year)
        self.file_size = file_size

    def description(self):
        return f"'{self.title}' (Ebook) by {self.author}, published in {self.publish_year}. File size: {self.file_size} MB."