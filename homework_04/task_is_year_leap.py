#Напишите функцию is_year_leap,
#Которая принимает число (год) и возвращает True если год високосный
#False если нет.


def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


print(is_year_leap(2000))