# Создайте класс WordIterable, который в конструкторе принимает строку (текст) и итерируется по словам.
# Для простоты можно считать что текст это набор слов,
# разделённый только пробелами (никаких знаков препинания).
# То есть для разбиения можно использовать функцию split.

class WordIterable:
    def __init__(self, text: str):
        self.words = text.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            return word
        raise StopIteration()

text = "Hello world! This is a test string."
words = WordIterable(text)
for word in words:
    print(word)


def test_WordIterable():
    text = "Hello world! This is a test string."
    words = WordIterable(text)
    assert list(words) == ['Hello', 'world!', 'This', 'is', 'a', 'test', 'string.']

    text = "1 2 3 4 5"
    words = WordIterable(text)
    assert list(words) == ['1', '2', '3', '4', '5']

    text = "   a     b    c   "
    words = WordIterable(text)
    assert list(words) == ['a', 'b', 'c']

    text = ""
    words = WordIterable(text)
    assert list(words) == []


test_WordIterable()
