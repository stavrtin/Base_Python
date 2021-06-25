'''1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.'''


class Matrix:

    def __init__(self, name, element):
        self.name = name
        self.element = element

    def __str__(self):
        print(f'Cоздана Матрица {self.name.upper()} ', end=' ')
        for _ in self.element:
            print(end='\n')
            for __ in _:
                print(f'{__:3d}', end=' ')
        return ''

    def __add__(self, other):
        result = [[self.element[i][j] + other.element[i][j] for j in range(len(self.element[0]))] for i in
                  range(len(self.element))]
        # s = Matrix(name='s', row=len(self.element), colunm=len(self.element[0]), element=result)
        return Matrix(f'{self.name}+{other.name}',result)


matrix_1 = [[-1, 2], [33, 4]]
matrix_2 = [[11, 12], [21, 22]]
a_matix = Matrix('a', matrix_1)
print(a_matix)
b_matix = Matrix('b', matrix_2)
print(b_matix)
c_matrix = a_matix + b_matix
print(c_matrix)
print('end')
