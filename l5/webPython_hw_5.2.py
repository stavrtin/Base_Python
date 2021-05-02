'''Task2
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке.'''
count_str = 0
with open('web_less_5.2.txt', 'r') as f_obj:
    line = f_obj.readline()

    while line != '':  # The EOF char is an empty string
        count_str += 1
        count_word = len(set(line.split()))
        print(f'В строке {count_str} присутствует {count_word} слов \n', end='')
        line = f_obj.readline()
print(f'Вcсего в файле {count_str} строк', end='')
