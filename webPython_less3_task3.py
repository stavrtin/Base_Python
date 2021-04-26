''' Test #3
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func_summax(num1, num2, num3):
    result = num1 + num2 + num3 - min(num1,num2,num3)
    return result

val_1 = float(input('Введите 1е число: '))
val_2 = float(input('Введите 2е число: '))
val_3 = float(input('Введите 3е число: '))
summa = my_func_summax(val_1, val_2, val_3)
print(f'     Сумма максимальных чисел равна: {summa:.2}')
