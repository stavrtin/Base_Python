''' Task#5
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''
from functools import reduce

my_list = [el for el in range(100, 1001, 2)]
mult_list = reduce(lambda num1, num2: num1 * num2, my_list)

print(my_list)
print(mult_list)
print('End')

