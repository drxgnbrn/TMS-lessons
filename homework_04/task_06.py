#Напишите функцию is_palindrome, которая принимает на вход строку, и возвращает True если это палиндром
#Иначе False.



s = input('Введите слово на проверку: ')
def is_palindrome(s: str) -> bool:
    return s == ''.join(reversed(s))


print(is_palindrome(s))

