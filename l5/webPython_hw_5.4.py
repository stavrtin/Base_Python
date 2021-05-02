'''Task4
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.'''

dict_rus = {
    'One': 'один',
    'Two': 'два',
    'Three': 'три',
    'Four': 'четыре',
    'Five': 'пять',
    'Six': 'шесть',
    'Seven': 'семь',
    'Eight': 'восемь',
    'Nine': 'девять',
    'Ten': 'десять'}

with open('web_less_5.4.txt', 'r') as f_engl:
    with open('web_less_5.4-rus.txt', 'w') as f_rus:
        for line in f_engl:
            line_trnsl = line.replace(line.split()[0], dict_rus.get(line.split()[0]))
            print(line_trnsl, file=f_rus, end='')

