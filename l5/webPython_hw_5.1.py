'''TAsk1
1. Создать программно файл в текстовом формате, записать в него построчно данные,
 вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.'''
import os

with open('web_less_5.1.txt', 'w') as f_obj:
    my_list = []
    while True:
        a = input('=>')
        if a != '':
            a = a + '\n'
            f_obj.writelines(a)
        else:
            break
print(f'Text was saved in file "{f_obj.name}"')

