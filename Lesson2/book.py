class Book:
    def __init__(self, title: str, author: str, publish_year: int):
        self.title = title
        self.author = author
        self.publish_year = publish_year

    def description(self):
        return f"'{self.title}' by {self.author}, published in {self.publish_year}."







