# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
__all__ = ['guess_riddle', 'options_dict', 'attempts_log', 'riddle_result', '_attempt_log', ]
_attempt_log = {}


def guess_riddle(riddle: str, options: list, attempts: int):
    print(riddle)
    for attempt in range(1, attempts + 1):
        guess = input(f"Попытка {attempt}/{attempts}. Введите ваш ответ: ")

        if guess in options:
            print(f"Поздравляем! Вы угадали загадку с {attempt} попытки.")
            return attempt
    print("У вас закончились попытки. Попробуйте следующий раз!")
    return 0

# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.


def options_dict(attempts: int):
    dct = {"Ночью он не любит спать, ему хочется гулять. Молоко из плошки пьёт. Это наш домашний… * ": ['Кот', 'кот'],
           "Сидит в темнице, красная девица, а коса на улице...*": ["Морковь", "морковь", "Морковка", "морковка", "морква", "Морква"]}
    for k, v in dct.items():
        attempts_log(k, guess_riddle(k, v, attempts))


# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
# и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.


def attempts_log(riddle: str, num_attemp: int):
    if riddle not in _attempt_log:
        _attempt_log[riddle] = [num_attemp]
    else:
        _attempt_log[riddle].append(num_attemp)


def riddle_result():
    for k, v in _attempt_log.items():
        print(f'Загадка: {k}. Результат угадывания: {v}')


if __name__ == '__main__':
    riddle = "Ночью он не любит спать, ему хочется гулять. Молоко из плошки пьёт. Это наш домашний… * "
    options = ['Кот', 'кот']
    attempts = 5

    options_dict(attempts)
    riddle_result()
