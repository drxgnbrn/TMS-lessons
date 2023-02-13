# Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре.
# Вам по прежнему нужно удалить все гласные.
# При этом вывести результат нужно вывести сохранив изначальный регистр.

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
text = list(map(str, input().split()))
def remove_vowels(text):
    my_list = list(filter(lambda x: x not in vowels, text))
    return my_list
print(remove_vowels(text))