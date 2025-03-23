from Lesson2.communication import Communication
from Lesson2.entertainment import Entertainment
from Lesson2.phone import Phone

#dziedziczenie
# class Smartphone(Phone, Communication, Entertainment):
#     def __init__(self, model: str, manufacturer: str):
#         super().__init__(model, manufacturer)


#kompozycja
class Smartphone:
    def __init__(self, model: str, manufacturer: str):
        self.phone = Phone(model, manufacturer)
        self.communication = Communication()
        self.entertainment = Entertainment()

    def send_message(self, receiver: str, text: str):
        return self.communication.send_message(receiver, text)

    def play_music(self, song: str):
        return self.entertainment.play_music(song)