#
# # 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# # проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# # Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
print('----------------Task# 1----------------')
a = 1
aa = 1.5
b = 'slovo'
c = [1,2,3,'sss']
com = complex(2,3)
spisok = ['с', 'п', 'и', 'с', 'о', 'к']
dist_1 = { 'name': 'Вася',
           'age': 1977,
           'sport': 'хоккей'}
print(a)
print(type(a))
print(aa)
print(type(aa))
print(b)
print(type(b))
print(c)
print(type(c))
print(com)
print(type(com))
print(spisok)
print(type(spisok))
print(dist_1)
print(type(dist_1))
print('--------------End of task# 1-----------')
# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
# input().

print('--------------Task# 2-----------')
vvod = input('Введите список через пробелы: ')
spisok = vvod.split()
print(spisok)
print(len(spisok))
count = 0
cheng_1 = ''
cheng_2 = ''
while (count + 1) < len(spisok):
    cheng_1 = spisok[count]
    cheng_2 = spisok[count + 1]
    spisok.pop(count)
    spisok.pop(count)
    spisok.insert(count, cheng_2)
    spisok.insert(count + 1, cheng_1)
    count += 2
print(spisok)
print('--------------End of task# 2-----------')
print('--------------Task# 3 -----------')
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
mounths =  {   1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май',
            6: 'июнь', 7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
year_ch = {'зима': [12,1,2],
             'весна': [3,4,5],
             'лето': [6,7,8],
             'осень': [9,10,11]
             }
mounth = int(input('Введите цифровое значение месяца: '))
mounth_char = mounths.get(mounth)
for key in year_ch:
    for mon in year_ch[key]:
        if mounth == mon:
            print(f' {mounth}-й месяц - это {mounth_char}, {mounth_char} - это уже {key}')
print('--------------End of task# 3-----------')
# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
print('--------------Task# 4-----------')
my_stroka = input('Введите строку через пробел: ')
my_list = my_stroka.split()
print(my_list)
count = 0
for word in my_list:
    count += 1
    print(f' {count}. {word[:11]}')
print('--------------End of task# 4-----------')
print('--------------Task# 5-----------')
# 5. Реализовать структуру «Рейтинг», представляющую собой не
# возрастающий набор натуральных чисел. У пользователя необходимо
# запрашивать новый элемент рейтинга. Если в рейтинге существуют
# элементы с одинаковыми значениями, то новый элемент с тем же з
# начением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
print(f'Исходный рейтинг: {my_list}')
new_number = int(input('Введите число: '))
for count in my_list:
    if count < new_number:
        my_list.insert(my_list.index(count),new_number)
        break
print(f'Уточненный рейтинг: {my_list}')
print('--------------End of task# 5-----------')

print('--------------Task# 6-----------')
# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер
# товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица
# измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

print('Заполним данные по товарам')
property = {'название': '', 'цена': '', 'количество': '', 'eд': ''}
product = list()
tup_product = list()
count = 0
# Начинаем заполнение структуры ---------------------
while input('Добавим еще товар? (+ если да)  ') == '+':
    count += 1
    tup_product = list()
    # print(product)
    property = {'название': '', 'цена': '', 'количество': '', 'eд': ''}
     ##### tup_product.append(input('Введите номер товара: '))
    tup_product.append(count)
    for ttx in property:
        property[ttx] = input(f'Введите {ttx} :')
    tup_product.append(property)
    tup_product = tuple(tup_product)
    product.append(tup_product)
print(product)
#  Заполнение структуры завершено---------------------
# product = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#            (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
#            (3, {'название': 'сканер', 'цена': 5000, 'количество': 2, 'eд': 'шт.'}),]
result_dict = {'название': '', 'цена': '', 'количество': '', 'eд': ''}

trans_list = list(zip (* product))  # транспонируем структуру что бы затем
                                    # взять только словари (они будут в 1м элементе списка)

spisok_slovarei = trans_list[1]

#  выбираем характеристики, записываем их в результирующий словарь

name_list = []
cost_list = []
quantity_list = []
measure_list = []

for i in range(len(spisok_slovarei)):
    name = spisok_slovarei[i].get('название')
    cost = spisok_slovarei[i].get('цена')
    quantity = spisok_slovarei[i].get('количество')
    measure = spisok_slovarei[i].get('eд')
    name_list.append(name)
    cost_list.append(cost)
    quantity_list.append(quantity)
    measure_list.append(measure)

result_dict['название'] = name_list
result_dict['цена'] = cost_list
result_dict['количество'] = quantity_list
result_dict['eд'] = measure_list

print(result_dict)