'''3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:  сложение (__add__()),
вычитание (__sub__()),  умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
(не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
до целого числа.
Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
 количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
 деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
 Данный метод позволяет организовать ячейки по рядам.'''
import math


class Cell:

    def __init__(self, name, count):
        self.count = count
        self.name = name

    def __str__(self):
        return f'Создана клетка {self.name.upper()} c {self.count} ячейками'

    def __add__(self, other):
        cell_add = self.count + other.count
        return Cell(f'{self.name}+{other.name}', cell_add)

    def __sub__(self, other):
        cell_sub = self.count - other.count
        return Cell(f'{self.name}-{other.name}', cell_sub if self.count > other.count else 'нет возможности вычесть')

    def __mul__(self, other):
        cell_mul = self.count * other.count
        return Cell(f'{self.name}*{other.name}', cell_mul)

    def __truediv__(self, other):
        cell_div = math.floor(self.count / other.count)
        return Cell(f'{self.name}/{other.name}', cell_div)

    def make_order(self, length_row):
        for item in range(self.count//length_row):
            print('*' * length_row, end='\n')


cell_a = Cell('a',27)
cell_b = Cell('b',7)
print(cell_a)
# print(cell_a.count)
print(cell_b)
# print(cell_b.count)
print(cell_a + cell_b)
print(cell_a - cell_b)
print(cell_a * cell_b)
print(cell_a / cell_b)

cell_a.make_order(5)