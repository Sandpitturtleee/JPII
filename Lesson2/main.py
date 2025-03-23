from Lesson2.audiobook import Audiobook
from Lesson2.ebook import Ebook

if __name__ == '__main__':
    # Zad1
    ebook = Ebook("Krew Elfów", "Andrzej Sapkowski", 2021, 2.5)
    audiobook = Audiobook("Krew Elfów", "Andrzej Sapkowski", 2020, 180)
    print(audiobook.description())
    print(ebook.description())
