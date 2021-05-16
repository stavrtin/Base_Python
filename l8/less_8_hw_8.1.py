'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.'''


class Date:

    def __init__(self, date_list):
        self.date_list = date_list

    def __str__(self):
        return 'преобразуем дату'

    @classmethod
    def get_number(cls, date_list):
        return [int(item) for item in date_list.split('-')]

    @staticmethod
    def do_validation(date_list):
        try:
            d_list = [int(i) for i in date_list.split('-')]
            while True:
                if d_list[0] < 0 or d_list[0] > 31:
                    print('Дата введена не верно. Повтори ввод')
                    date_list = input('Введите дату в формате: дд-мм-год => ')
                    d_list = [int(i) for i in date_list.split('-')]
                if d_list[1] < 0 or d_list[1] > 12:
                    print('Месяц введен не верно')
                    date_list = input('Введите дату в формате: дд-мм-год => ')
                    d_list = [int(i) for i in date_list.split('-')]
                else:
                        return 'Все верно введено'
        except ValueError:
            return 'Дата введена не в числовом формате\n' \
                   'повторите ввод =>  '

    # def do_validation(self):
    #     try:
    #         d_list = [int(i) for i in self.date_list.split('-')]
    #         while True:
    #             if d_list[0] < 0 or d_list[0] > 31:
    #                 print('Дата введена не верно. Повтори ввод')
    #                 self.date_list = input('Введите дату в формате: дд-мм-год => ')
    #                 d_list = [int(i) for i in self.date_list.split('-')]
    #             if d_list[1] < 0 or d_list[1] > 12:
    #                 print('Месяц введен не верно')
    #                 self.date_list = input('Введите дату в формате: дд-мм-год => ')
    #                 d_list = [int(i) for i in self.date_list.split('-')]
    #             else:
    #                     return 'Все верно введено'
    #     except ValueError:
    #         return 'Дата введена не в числовом формате\n' \
    #                'повторите ввод =>  '

test_date = input('Введите дату в формате: дд-мм-год => ')
my_date = Date(test_date)
print(my_date.do_validation(test_date))
print(my_date.get_number(test_date))

