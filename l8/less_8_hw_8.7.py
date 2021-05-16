'''7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
умножение созданных экземпляров.
Проверьте корректность полученного результата.'''


class ComplexNumber:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        compl_number = f'{self.x}+{self.y}i' if self.y > 0 else f'{self.x}{self.y}i'
        return compl_number

    def __add__(self, other):
        res_x = self.x + other.x
        res_y = self.y + other.y
        result_number = f'{res_x}+{res_y}i' if res_y > 0 else f'{res_x}{res_y}i'
        return result_number

    def __mul__(self, other):
        res_x = self.x * other.x
        res_y = self.y * other.y
        result_number = f'{res_x}+{res_y}i' if res_y > 0 else f'{res_x}{res_y}i'
        return result_number

comp_number1 = ComplexNumber(-3,-5)
comp_number2 = ComplexNumber(2,-3)

new_sum = comp_number1 + comp_number2
new_mult = comp_number1 * comp_number2

print(comp_number1)
print(comp_number2)
print(new_sum)
print(new_mult)


