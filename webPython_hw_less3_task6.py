''' Test #1
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
'''

# def division(num1, num2):
#     """Функция деления 2х чисел.
#
#     пользователь вводит два числа
#     1е и 2е число - вещественные
#     Если введено 2е число = 0, то будет предложен повторный ввод"""
#     result = num1 / num2
#     return result
#
#
# chislo1 = float(input('введи 1е число: '))
# chislo2 = float(input('введи 2е число: '))
# while True:
#     if chislo2 == 0:
#         print('Деление на "0" недопустимо ')
#         chislo2 = int(input('введи 2е число: '))
#     else:
#         break
#
# c = division(chislo1, chislo2)
# print(f'результат деления "{chislo1}" на "{chislo2}" равен: {c:.3}')
# print(division.__doc__)
# print('----------------End of Test#1')

''' Test #2
2. Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания, email,
телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

# def personal_date (name, surname, year, city, email):
#     print(f' Данные пользователя: ИМЯ: {name}, ФАМИЛИЯ: {surname}, '
#           f'ГОД: {year}, ГОРОД: {city}, Е-майл: {email}')
#
#
# name = input('Введите Имя: ')
# fio = input('Введите Фамилию: ')
# year = input('Введите год рождения: ')
# town = input('Введите город проживания: ')
# post = input('Введите Email: ')
# personal_date(name=name, surname=fio, year=year, city=town, email=post)
# print('----------------End of Test#2')

''' Test #3
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''
# def my_func_summax(num1, num2, num3):
#     result = num1 + num2 + num3 - min(num1,num2,num3)
#     return result
#
# val_1 = float(input('Введите 1е число: '))
# val_2 = float(input('Введите 2е число: '))
# val_3 = float(input('Введите 3е число: '))
# summa = my_func_summax(val_1, val_2, val_3)
# print(f'     Сумма максимальных чисел равна: {summa:.2}')
# print('----------------End of Test#3')

''' Test #4
4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''
# def my_exponention_var1(x,y):
#     result = x**y
#     return result
#
# def my_exponention_var2(x,y):
#     result = 1
#     if y > 0:
#         for index in range(1,y+1):
#             result = result * x
#     else:
#         for index in range(1, y + 1,-1):
#             result = result / x
#     return result
#
# base_degree = float(input('Введите действительное положительное число x: '))
# indicator_degree = int(input('Введите целое отрицательное число y: '))
# expon = my_exponention_var1(base_degree,indicator_degree)
# print('Результат решения через умножение ** ...')
# print(f'Результат возведения "{base_degree}" в степень "{indicator_degree}" будет равен: {expon}')
# print('Результат решения через цикл... ')
# expon = my_exponention_var2(base_degree,indicator_degree)
# print(f'Результат возведения "{base_degree}" в степень "{indicator_degree}" будет равен: {expon}')
# print('----------------End of Test#4.1 & 4.2')

''' Test #5
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
 разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к 
 уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. 
 Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
  к полученной ранее сумме и после этого завершить программу.
'''
my_list_digit = []
result = 0
while True:
    stroka = input('Введите ЧИСЛА через пробел, ("q" для выхода): ')
    my_list = stroka.split()
    if stroka.find('q') != -1:
        my_list = stroka[0:stroka.index('q')].split()
        my_list_digit = [float(item) for item in my_list]  # преобразуем str в float
        result = result + sum(my_list_digit)
        break
    my_list_digit = [float(item) for item in my_list]  # преобразуем str в float
    result = result + sum(my_list_digit)
print(f' Сумма введенных чисел равна: {result}')
