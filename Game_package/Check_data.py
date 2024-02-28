# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
from sys import argv
import datetime
import calendar


def check_date(date: str) -> bool:
    format = '%d.%m.%Y'
    try:
        date = datetime.datetime.strptime(date, format)
        print(date)
        return True
    except:
        return False


def check_year(year: int) -> bool:
    return calendar.isleap(year)


if __name__ == '__main__':
    data = argv[1]
    if len(data) < 1:
        print("Not enough arguments")
    print(check_date(data))