# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(10):
    guess = int(input("Попробуйте угадать число: "))
    if guess == num:
        print("Вы угадали!")
        break
    elif guess < num:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")

if i == 9:
    print("Вы проиграли. Загаданное число было", num)