#Программа загадывает случайное число от 0 до 100.
#Пользователь пытается угадать, вводя числа.
#Если пользователь угадал - выведите поздравление и завершите программу.
#Если пользователь не угадал, подскажите ему в в какую сторону идти.
#То есть, если число пользователя слишком большое - выведите “не угадал, ваше число больше загаданного”.
#Если меньше - выведите “не угадал, ваше число меньше загаданного”.

import random

n = random.randint(0, 101)
while True:
    a = int(input('Enter a number: '))
    if a == n:
        print('Well done!')
        break
    else:
        if a > n:
            print('Вводимое число больше')
            continue
        if a < n:
            print('Вводимое число меньше')
            continueефыt