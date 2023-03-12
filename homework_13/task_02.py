# Напишите функцию is_date, которая принимает строку и возвращает bool.
# Функция должна вернуть True если переданная строка это дата в формате "DD-MM-YYYY"

import re
def is_date(string: str):
    return re.fullmatch(r'\d{1,2}-\d{1,2}-\d{4}', string) is not None

if __name__ == '__main__':
    assert is_date('23-06-2004')
    assert is_date('23-14-2000')
    # assert not is_date('23-06-2004')
    assert not is_date('-06-2004')
