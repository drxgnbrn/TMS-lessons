# Пользователь вводит произвольную строку.
# Выведите кортеж из уникальных символов введённой строки.

stroka: str = input('Введите произвольную строку: ')
unique = tuple(set(stroka))
print('Уникальные символы: ')
print(unique)

# Вывод данных идёт не по порядку (В условии такого не было)


