"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг — реализовать
перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода __add__() для
реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая
матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д. """

from copy import deepcopy


class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = deepcopy(list_of_lists)

    def __str__(self):
        matrix = []
        for row in self.list_of_lists:
            matrix.append('\t'.join([str(el) for el in row]))
        return '\n'.join(matrix)

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[i])):
                s = self.list_of_lists[i][j] + other.list_of_lists[i][j]
                numbers.append(s)
                if len(numbers) == len(self.list_of_lists):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


m_1 = Matrix([[1, 2, 5], [3, 4, 5], [5, 6, 5]])
m_2 = Matrix([[1, 2, 5], [3, 4, 5], [5, 6, 5]])

print(m_1 + m_2)
