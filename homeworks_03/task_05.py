# Пользователь вводит название месяца на английском.
# Выведите количество дней в этом месяце (не учитывая високосный год). 

dict_calendar = {'Январь': 31, 'Февраль': 28, 'Март': 31, 'Апрель': 30, 'Май': 31, 'Июнь': 30, 'Июль': 31, 'Август': 31, 'Сентябрь': 30, 'Октябрь': 31, 'Ноябрь': 30, 'Декабрь': 31}
month = input('Введите любой месяц: ')
print('В введённом месяце ', dict_calendar[month], ' дней' )


