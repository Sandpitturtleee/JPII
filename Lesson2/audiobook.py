from Lesson2.book import Book


class Audiobook(Book):
    def __init__(self, title: str, author: str, publish_year: int, duration: int):
        super().__init__(title, author, publish_year)
        self.duration = duration

    def description(self):
        return f"'{self.title}' (Audiobook) by {self.author}, published in {self.publish_year}. Duration: {self.duration} minutes."