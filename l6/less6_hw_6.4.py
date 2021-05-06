# Task 4
'''4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
  повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
   Для классов TownCar и WorkCar переопределите метод show_speed.
   При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
 Выполните вызов методов и также покажите результат.
'''

class Car:

    def __init__(self, name, color, speed, is_police=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name}: Машина поехала'

    def stop(self):
        return f'{self.name}: Машина остановилась'

    def turn(self, derect):
        return f'{self.name}: Машина повернула {derect}'

    def show_speed(self):
        return f'Скорость машины {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость больше 60.Превышение!!! {self.speed}'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость больше 40.Превышение!!! {self.speed}'


sally = Car('Салли', 'красный', 150)
bus = TownCar('Троллейбус №4', 'рогатый', 80, False)


print(sally.go())
print(sally.turn('left'))
print(sally.stop())
print(sally.show_speed())
print(bus.show_speed())








