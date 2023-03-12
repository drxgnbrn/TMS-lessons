# Напишите функцию is_float_number,
# которая принимает строку и возвращает bool.
# Функция должна вернуть True если переданная строка это корректное число с плавающей точкой.

import re
def is_float_number(string: str) -> bool:
    pattern = r'[-+]?[0-9]*\.[0-9]+?'
    return bool(re.match(pattern, string))

print(is_float_number('200.3'))
print(is_float_number('+200.3'))
print(is_float_number('-200.3'))

if __name__ == '__main__':
    assert is_float_number('1.0')
    assert is_float_number('20.45')
    # assert not is_float_number('20.45')