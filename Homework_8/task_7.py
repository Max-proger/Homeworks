"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        return f'({self.real}{sign}{self.imag}j)'

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag
        return Complex(real, imag)


a = Complex(1, -2)
b = Complex(2, 4)
x = complex(1, -2)
y = complex(2, 4)
c = a + b
z = x + y
print(f'Результат сложения классовый {c}\nРезультат сложения программн {z}')
c = a * b
z = x * y
print(f'Результат произведения классовый {c}\nРезультат произведения программн {z}')