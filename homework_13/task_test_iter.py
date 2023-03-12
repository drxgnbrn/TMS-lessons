# Всё то же самое, что и в прошлом итераторе, только тут идёт по буквам

class LetterIterable:
    def __init__(self, letter: str):
        self.letters = letter
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.letters):
            letter = self.letters[self.index]
            self.index += 1
            return letter
        raise StopIteration()

letter = "Hello world! This is a test string."
letters = LetterIterable(letter)
for letter in letters:
    print(letter)