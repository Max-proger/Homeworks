"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} старт')

    def stop(self):
        print(f'{self.name} стоп')

    def turn(self, direction):
        print(f'{self.name} поворот на {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} составила {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} составила {self.speed}')

        if self.speed > 40:
            print(f'Скорость {self.name} превышает допустимую')
        else:
            print(f'Допустимая скорость для {self.name}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} составила {self.speed}')

        if self.speed > 60:
            print(f'Скорость {self.name} ревышает допустимую')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            print(f'{self.name} полицейская машина')
        else:
            print(f'{self.name} полицейская машина')


ferrari = SportCar(100, 'красная', 'Ferrari', False)
crysler = TownCar(30, 'серый', 'Сrysler', False)
gaz = WorkCar(70, 'зеленый', 'Gaz', True)
ford = PoliceCar(110, 'белый', 'Ford', True)
ferrari.go()
ferrari.stop()
ferrari.turn('направо')
ferrari.show_speed()
