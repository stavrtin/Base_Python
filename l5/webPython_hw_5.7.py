'''Task7
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Необходимо построчно прочитать файл,
вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Итоговый список сохранить в виде json-объекта в соответствующий файл.'''
import json

firm_dict = {}
count_firm = 0
with open('web_less_5.7.txt', 'r') as f_obj:
    for line in f_obj:
        count_firm +=1                                          # кол-во фирм
        profit = int(line.split()[2]) - int(line.split()[3])    # создание словаря фирм и профита
        firm_dict.update({line.split()[0]: profit})

# из словаря фирм вычислим среднбб прибыль
all_profit = sum([firm_dict.get(i) for i in firm_dict if firm_dict.get(i) > 0]) # генератором выбрали "+" профит фирм
print(f'Учтено {count_firm} фирм, средний профит составил {all_profit/count_firm:.2f}')
av_profit_dict = {'average_profit' : round(all_profit/count_firm)}
final_list = [firm_dict, av_profit_dict]
print(final_list)

with open('my_file.json', 'w') as f_json:
    json.dump(final_list, f_json)


