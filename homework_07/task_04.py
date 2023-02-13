# Пользователь вводит произвольное количество слов через пробел.
# Затем (на следующей строке) вводит один символ (разделитель).
# Вам нужно написать функцию my_join
# Которая принимает список из строк и символ-разделить
# И возвращает строку, в которой все слова из списка соединены через символ разделитель.


text =  list(map(str, input().split()))
symbols = input()
def my_join(text, symbols):
    symbols_list = symbols.join(text)
    from functools import reduce
    result = reduce(lambda x, y: x + y, symbols_list)
    return result



print(my_join(text, symbols))