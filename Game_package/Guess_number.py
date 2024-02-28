# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
import random
from sys import argv

__all__ = ['guess_number',]


def guess_number(num1: int, num2: int, num3: int) -> bool:
    number = random.randint(num1, num2)
    count = 0
    while True:
        count += 1
        if count > num3:
            print('You have no attempt/ Game is over.')
            return False
        user_answer = int(input('Enter whole number: '))
        if user_answer == number:
            print('You guess!')
            return True
        elif user_answer > number:
            print('Your number is larger than need.')
        else:
            print('Your number is less than need.')


# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.


if __name__ == '__main__':
    args = [int(i) for i in argv[1:]]
    num1 = 0
    num2 = 0
    num3 = 5
    if len(args) < 1:
        print("Not enough arguments")
    if len(args) in (1, 2, 3):
        num1 = args[0]
    if len(args) in (2, 3):
        num2 = args[1]
    if len(args) == 3:
        num3 = args[2]

    guess_number(num1, num2, num3)

