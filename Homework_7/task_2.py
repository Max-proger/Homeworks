"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
проекта, проверить на практике работу декоратора @property. """

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def tissue_consumption(self):  # метод для расчета ткани необходимый для каждого класса
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 38:
            self.__v = 38
        elif v > 70:
            self.__v = 70
        else:
            self.__v = v

    @property
    def tissue_consumption(self):
        return round(self.v / 6.5 + 0.5)


class Costume(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 0.7:
            self.__h = 0.7
        elif h > 2.7:
            self.__h = 2.7
        else:
            self.__h = h

    @property
    def tissue_consumption(self):
        return round(2 * self.h + 3)


size_coat = Coat(float(input('Введите размер: ')))
costume_height = Costume(float(input('Введите рост: ')))
total = f'Общий расход ткани составит {size_coat.tissue_consumption + costume_height.tissue_consumption} метров'
print(total)
