'''Task5
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран..'''

from random import *

# n - количество строк в файле с данными
# m - максимальное количество чисел в строке файла с данными
n = 10
max_din = 10


# функция задающая строку случайных чисел
def random_digit_str(n):
    res = [randint(1, 100) for i in range(1, n)]
    return res


# запись строки в файл
with open('web_less_5.5.txt', 'w') as f_digit:
    count_line = 0
    while count_line < n:
        len_str = randint(2, max_din)
        print(*(list(random_digit_str(len_str))), file=f_digit)
        count_line += 1

# построчный подсчет суммы чисел из файла
sum_str = 0
with open('web_less_5.5.txt', 'r') as f_sum:
    for line in f_sum:
        sum_str += sum(list(map(int, line.split())))

print(f'Сумма всех элементов массива равна: {sum_str}')
