''' Test #5
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
 разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к 
 уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
 программы завершается.
 Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
 этих чисел   к полученной ранее сумме и после этого завершить программу.
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
