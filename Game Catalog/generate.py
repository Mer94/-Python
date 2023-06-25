"""
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""

import random as rnd


def gen_fnc(low: int, hight: int, try_count: int ):
    result = False
    num = rnd.randint(low, hight+1)

    search_count = 0
    while search_count < try_count:
        ask_value = int(input(f'Введите число от {low} до {hight}: '))
        if ask_value == num:
            print('Вы угадали')
            result = True
            break
        if ask_value < num:
            print('Загаданное число больше')
        else:
            print('Загаданное число меньше')
        search_count += 1
    else:
        print("Попытки закончились")
    return result
