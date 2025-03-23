from Lesson2.audiobook import Audiobook
from Lesson2.ebook import Ebook
from Lesson2.smartphone import Smartphone
from Lesson2.userauth import UserAuth, UserNotFoundError, WrongPasswordError

if __name__ == '__main__':
    # Zad1
    ebook = Ebook("Krew Elfów", "Andrzej Sapkowski", 2021, 2.5)
    audiobook = Audiobook("Krew Elfów", "Andrzej Sapkowski", 2020, 180)
    print(audiobook.description())
    print(ebook.description())
    # Zad 2
    smartphone = Smartphone("Iphone 13", "Iphone")
    print(smartphone.send_message("Ja", "Siema"))
    print(smartphone.play_music("Shadow moses"))
    # Zad 3
    auth = UserAuth({"admin": "1234", "user": "abcd"})
    try:
        print(auth.login("admin", "1234"))
        print(auth.login("unknown", "pass"))
        print(auth.login("user", "wrongpass"))
    except UserNotFoundError as e:
        print(e)
    except WrongPasswordError as e:
        print(e)
