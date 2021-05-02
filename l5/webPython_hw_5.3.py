'''Task3
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.'''

salary = 20
new_dict = {}
my_list = []
# создаем словарь людей и их зарплат
with open('web_less_5.3.txt', 'r') as f_obj:
    for line in f_obj:
        new_dict.update({line.split()[0]: line.split()[-1]})
my_list = [i for i in new_dict if int(new_dict.get(i)) < salary]

print(f'Менее {salary} млн получают: ')
print(*my_list)