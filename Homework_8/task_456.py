"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники. Продолжить работу над первым заданием. Разработать методы, отвечающие за
приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных."""
import collections


class Warehouse:
    technics = {}
    departments = {}

    def __init__(self, tip, dicts):
        self.dicts = dicts
        self.tip = tip

    def accounting(self):
        self.technics.setdefault(self.tip, []).append(self.dicts)

    @classmethod
    def moving(cls, obj, model, units, dep):
        for k, v in cls.technics.items():
            if k == obj:
                for i in v:
                    if i['Модель'] == model:
                        if i['Количество'] > units:
                            i['Количество'] -= units
                            dict_dep = {'Тип': obj, 'Модель': model, 'Количество': units}
                            cls.departments.setdefault(dep, []).append(dict_dep)
                        else:
                            print(
                                f'\033[31mЗапрашиваемый остаток меньше остатка на складе который равен:\033[0m \033[93m{i["Количество"]}\033[0m\n')
                    else:
                        print(f'\033[31mМодель\033[0m \033[93m{model}\033[0m\033[31m отсутствует на складе\033[0m\n')


class OfficeEquipment:

    def __init__(self, model, price, units):
        self.model = model
        self.price = price
        self.units = units


class Printers(OfficeEquipment):
    def __init__(self, model, price, units, view):
        super().__init__(model, price, units)
        self.view = view

    def print(self):
        return {'Модель': self.model, 'Цена за 1 ед': self.price, 'Количество': self.units, 'Тип принтера': self.view}


class Scanners(OfficeEquipment):
    def __init__(self, model, price, units, tips):
        super().__init__(model, price, units)
        self.tips = tips

    def scan(self):
        return {'Модель': self.model, 'Цена за 1 ед': self.price, 'Количество': self.units, 'Тип сканера': self.tips}


class Copiers(OfficeEquipment):
    def __init__(self, model, price, units, principle):
        super().__init__(model, price, units)
        self.principle = principle

    def cop(self):
        return {'Модель': self.model, 'Цена за 1 ед': self.price, 'Количество': self.units,
                'Тип сканера': self.principle}


def prices(num):
    try:
        num = float(num)
        return num
    except ValueError:
        return prices(input(f'Стоимость \033[31m{num}\033[0m введена некорректно, повторите ввод: '))


def quantity(numb):
    try:
        numb = int(numb)
        return numb
    except ValueError:
        return quantity(input(f'Количество \033[31m{numb}\033[0m введено некорректно повторите ввод: '))


def start():
    model = input('Введите модель устройста: ')
    price = prices(input('Введите стоимость устройства: '))
    units = quantity(input('Введите количество устройств: '))
    return model, price, units


while True:
    act = input(
        'Для приемки техники нажмите - Enter\nДля перемещения со склада введите - M\nДля получения информации о '
        'товаре на складе - W\nДля получения информации о технике находящейся в отделах  - D\nДля выхода Q\n')
    if act == '':
        tech = ['принтеры', 'сканеры', 'ксероксы']
        options = int(input(f'1 - {tech[0]}\n2 - {tech[1]}\n3 - {tech[2]}\n'))
        model, price, units = start()
        if options == 1:
            view = ['струйный', 'лазерный', 'светодиодный', 'матричный', '3D']
            i = int(input(
                f'Выберите тип принтера\n1 - {view[0]}\n2 - {view[1]}\n3 - {view[2]}\n4 - {view[3]}\n5 - {view[4]}\n'))
            Warehouse(tech[options - 1], Printers(model, price, units, view[i - 1]).print()).accounting()
        if options == 2:
            tips = ['планшетный', 'паспортный', 'книжный', 'ручной', 'барабанный', 'сетевой', 'протяжной']
            i = int(input(
                f'Выберите тип сканера\n1 - {tips[0]}\n2 - {tips[1]}\n3 - {tips[2]}\n4 - {tips[3]}\n5 - {tips[4]}\n6 - {tips[5]}\n'))
            Warehouse(tech[options - 1], Scanners(model, price, units, tips[i - 1]).scan()).accounting()
        if options == 3:
            principle = ['цифровой', 'аналоговый']
            i = int(input(f'Выберите тип ксерокса\n1 - {principle[0]}\n2 - {principle[1]}\n'))
            Warehouse(tech[options - 1], Copiers(model, price, units, principle[i - 1]).cop()).accounting()
    if act.lower() == 'm':
        obj = ['принтеры', 'сканеры', 'ксероксы']
        tech_obj = int(input(f'1 - {obj[0]}\n2 - {obj[1]}\n3 - {obj[2]}\n'))
        model = input('Введите модель которую хотите переместить: ')
        units = quantity(input('Введите количество которое хотите переместить: '))
        dep = input('Введите отдел в который хотите переместить технику: ')
        Warehouse.moving(obj[tech_obj - 1], model, units, dep)
    if act.lower() == 'w':
        for k, v in collections.OrderedDict(sorted(Warehouse.technics.items())).items():
            print(k, v)
    if act.lower() == 'd':
        for k, v in collections.OrderedDict(sorted(Warehouse.departments.items())).items():
            print(k, v)
    if act.lower() == 'q':
        exit()