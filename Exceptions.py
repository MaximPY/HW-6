# ЗАДАЧА 1
#Вспомогательная функция
def is_number(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def polish_notation():
    input_1 = input('Введите пример польской нотацией ')
    x = input_1.split()
    signs_list = ('+', '-', '/', '*')
    try:
        assert x[0] in signs_list, f'Введён неизвестный оператор {x[0]}'
        assert len(x) == 3, 'Введено неверное количество символов'
        assert is_number(x[1]), 'Неверный формат чисел'
        assert is_number(x[2]), 'Неверный формат чисел'
        if x[0] == '+':
            y = int(x[1]) + int(x[2])
            print(y)
        elif x[0] == '-':
            y = int(x[1]) - int(x[2])
            print(y)
        elif x[0] == '*':
            y = int(x[1]) * int(x[2])
            print(y)
        elif x[0] == '/':
            y = int(x[1]) / int(x[2])
            print(y)
    except ZeroDivisionError:
        print('Деление на ноль!')
    except Exception as e:
        print(e)
    return

polish_notation()

#ЗАДАЧА 3

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "ilicense", "number": "18716876",}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def name_printer():
    n = 1
    try:
        for dicts in documents:
            print(dicts['name'])
            n += 1
    except KeyError:
        print(f'В документе №{n} отсутствует графа "name"')

name_printer()