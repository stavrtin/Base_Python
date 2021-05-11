'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
 реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''

from abc import ABC, abstractmethod
class Clothes(ABC):

    @abstractmethod
    def finc_1(self):
        print('Подсчет ткани')

class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    def finc_1(self):
        print('Подсчет ткани')

    @property
    def get_textil_coat(self):
        result = self.size / 6.5 + 0.5
        return result

class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    def finc_1(self):
        print('Подсчет ткани')

    @property
    def get_textil_suit(self):
        result = 2 * self.height + 0.3
        return result

my_coat = Coat(2)
print(f'На пошив пальто размера {my_coat.size} требуется {my_coat.get_textil_coat:,.3f} м2')
my_suit = Suit(3)
print(f'На пошив костюма рост {my_suit.height} требуется {my_suit.get_textil_suit} м2')