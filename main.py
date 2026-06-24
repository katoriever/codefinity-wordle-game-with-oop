import random


class WordProvider:
    def __init__(self):
        self.words = ["apple", "grape", "mango", "peach", "berry","lemon", "melon", "chili", "olive", "cocoa"]

    def get_word(self):
        return random.choice(self.words)

selected_word = WordProvider()
print(selected_word.get_word())
        