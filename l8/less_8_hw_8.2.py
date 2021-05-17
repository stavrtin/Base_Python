'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
 Проверьте его работу на данных, вводимых пользователем.
 При вводе пользователем нуля в качестве делителя программа должна корректно обработать
 эту ситуацию и не завершиться с ошибкой.'''


class DivisionByZero(Exception):

    def __init__(self, txt):
        self.txt = txt

try:
    f = int(input('Input =>'))
    if f == 0:
       raise DivisionByZero('Деление на 0')
    print(100 / f)
except ValueError:
    print("Вы ввели не число")
except DivisionByZero as error_txt:
    print(error_txt)