# 2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку. - cм. модуль Check_data.py
# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# 4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки
# ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
from random import randint


def check_safe_position(list):
    a, b, c, d, e, f, g, h = list
    for i in range(1, len(list)):
        p1, p2 = list[i]
        for j in range(i+1, len(list)):
            p3, p4 = list[j]
            if p1 == p3 or p2 == p4:
                return False
            if abs(p1 - p3) == abs(p2 - p4):
                return False
    return True


if __name__ == '__main__':
    lst = []
    while True:
        res = [[randint(1, 9), randint(1, 9)] for i in range(8)]
        if check_safe_position(res):
            lst.append(res)
        if len(lst) == 4:
            break
    print(*lst, sep='\n')
