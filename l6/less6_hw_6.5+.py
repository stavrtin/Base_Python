# Task 5
'''5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
'''


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки РУЧКОЙ  {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки КАРАНДАШЕМ'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки МАРКЕРОМ'


someone_stationery = Stationery('что-то')
print(f'Выбрали "{someone_stationery.title}".  {someone_stationery.draw()} ')

some_pen = Pen('Ручка')
print(f'Выбрали "{some_pen.title}".  {some_pen.draw()} ')
some_pencil = Pencil('Карандаш')
print(f'Выбрали "{some_pencil.title}".  {some_pencil.draw()} ')
some_handle = Handle('Маркер')
print(f'Выбрали "{some_handle.title}".  {some_handle.draw()} ')



