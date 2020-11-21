"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

"""

from itertools import cycle
from time import sleep


class TrafficLight:
    _color = ['Red', 'Yellow', 'Green']

    @staticmethod
    def on_TrafficLight_running():

        working_time = 0

        for el in cycle(TrafficLight._color):

            if el == 'Red':
                print(el)
                sleep(7)
                working_time += 7

            if el == 'Yellow':
                print(el)
                sleep(2)
                working_time += 2

            if el == 'Green':
                print(el)
                sleep(5)
                working_time += 5

            if working_time >= 30:
                break


a1 = TrafficLight()
a1.on_TrafficLight_running()