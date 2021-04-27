''' Task#1
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами..
'''
# python webPython_less4.1.py 40 550 3000

from sys import argv

script_file, work_time, rate_per_hour, prize = argv

salary = float(work_time) * float(rate_per_hour) + float(prize)

print("выработка в часах: ", work_time)
print("ставка в час: ", rate_per_hour)
print("премия: ", prize) 
print("Итого зп: ", salary)

