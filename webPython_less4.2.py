''' Task#2
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых
больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 128].
Результат: [12, 44, 4, 10, 78, 123].
'''

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 128]

last_el = my_list[len(my_list) - 1]
first_el = my_list[0]
new_list = [value for value in my_list if
            value > my_list[my_list.index(value) - 1] and value != first_el]

print(my_list)
print(new_list)
