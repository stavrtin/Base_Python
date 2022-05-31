''' Test #4
4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''
def my_exponention_var1(x,y):
    result = x**y
    return result

def my_exponention_var2(x,y):
    result = 1
    if y > 0:
        for index in range(1,y+1):
            result = result * x
    else:
        for index in range(1, y + 1,-1):
            result = result / x
    return result

base_degree = float(input('Введите действительное положительное число x: '))
indicator_degree = int(input('Введите целое отрицательное число y: '))
expon = my_exponention_var1(base_degree, indicator_degree)
print('Результат решения через умножение ** ...')
print(f'Результат возведения "{base_degree}" в степень "{indicator_degree}" будет равен: {expon:.2}')
print('Результат решения через цикл... ')
expon = my_exponention_var2(base_degree, indicator_degree)
print(f'Результат возведения "{base_degree}" в степень "{indicator_degree}" будет равен: {expon:.2}')

