#Программа выводит на экран числа от 0 до 100.
#После вывода каждого числа спрашивайте у пользователя “Should we break?”.
#Если он ответил “yes” - завершите программу.
#Иначе - продолжайте вывод чисел.
tas
for i in range(101):
    answer = input('Should we break?')
    if answer == 'no':
        print(i)
        continue
    else:
        print('OK!!!!')
        break
    
