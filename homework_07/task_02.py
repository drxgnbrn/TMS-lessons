# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels
# которая принимает список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.

vowels = ['a', 'e', 'i', 'o', 'u']
text = list(map(str, input().split()))
def remove_vowels(text):
    my_list = list(filter(lambda x: x not in vowels, text))
    return my_list
print(remove_vowels(text))