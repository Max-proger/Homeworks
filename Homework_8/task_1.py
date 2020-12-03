"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных. """
import calendar
import datetime
from datetime import date


class Data:
    def __init__(self, my_date):
        self.my_date = my_date

    @classmethod
    def numbers(cls, my_date):
        number = datetime.datetime.strptime(my_date, '%d-%m-%Y')
        return f'\033[94m{number.day}\n{number.month}\n{number.year}\033[0m'

    @staticmethod
    def chek(my_date):
        try:
            number = datetime.datetime.strptime(my_date, '%d-%m-%Y')
            return f'\033[93m{number.strftime("%w %B %Y")}\033[0m'
        except ValueError:
            day, month, year = my_date.split('-')
            if int(month) > 12 or int(month) < 1:
                return f'Некорректно указано число месяца \033[31m{month}'
            elif int(day) > calendar.mdays[datetime.date(int(year), int(month), 1).month] or int(day) < 1:
                return f'Некорректно указано число дней в этом месяце \033[31m{day}'


date_today = date.today().strftime('%d-%m-%Y')
print(Data.numbers(date_today))
print(Data.chek(input('Ведите дату в формате дд-мм-гггг: ')))