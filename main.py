import random


class WordProvider:
    def __init__(self):
        self.words = ["apple", "grape", "mango", "peach", "berry","lemon", "melon", "chili", "olive", "cocoa"]

    def get_word(self):
        return random.choice(self.words)

# selected_word = WordProvider()
# print(selected_word.get_word())

class WordleGame:
    def __init__(self):
        self.provider = WordProvider()
        self.secret = None

    def play_round(self):
        self.secret = self.provider.get_word()
        print(self.secret)

WordleGame().play_round()
        