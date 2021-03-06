"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой."""
class Division(ZeroDivisionError):

    def __init__(self, text):
        self.text = text


a = float(input('Введите делимое: '))
b = float(input('Введите делитель: '))
try:
    if b == 0:
        raise Division(
            'при а ≠ 0 не существует числа, которое при умножении на 0 даёт а, поэтому ни одно число не может быть '
            'принято за частное а⁄0, за исключением частного 0/0.')

except Division as err:
    print(err)
except ValueError:
    print("Вы ввели не число")
else:
    print(f'результат деления {a / b}')