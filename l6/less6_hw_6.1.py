from time import sleep
from itertools import cycle


class TrafficLight(object):
    def __init__(self):
        self._color = (('Red', 5), ('Yellow', 2), ('Green', 3))

    def running(self):
        for color, sec in cycle(self._color):
            if color == 'Red':
                print(f'\033[31m {color} ждем {sec} сек')
                sleep(sec)
            elif color == 'Yellow':
                print(f'\033[33m {color} ждем {sec} сек')
                sleep(sec)
            elif color == 'Green':
                print(f'\033[32m {color} ждем {sec} сек')
                sleep(sec)


traf_light = TrafficLight()
traf_light.running()