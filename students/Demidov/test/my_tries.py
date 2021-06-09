# import tester as t


'''
Вопросы
(Свои ответы заполнять в словать my_answers
где ключ - новер вопроса типа строка
ваш ответ)
'''
my_answers = {
    'name': '',
    '1': 'cd',    # укажите команду в терминале для навигации по файловой системе
    '2': 'pwd',    # Укажите команду в терминале для того, чтобы узнать в какой директории сейчас вы находитесь
    '3': 'mkdir',    # Укажите команду в терминале для создания папки
    '4': 'touch',    # Укажите команду в терминале для создания файла
    '5': 'ls/dir',    # Укажите команду в терминале для вывода списка всех файлов и папок в текущей директории
    '6': 'int',    # Какой тип данных нужен для работами с целыми числами
    '7': 'float',    # Какой тип данных нужен для работами с дробными числами
    '8': 'string',    # Какой тип данных нужен для работами со строками
    '9': 'bool',    # Какой тип данных нужен для работами с булевыми значениями
    '10': '**',   # Какой оператор нужно использовать чтобы возвести число в степень
    '11': '//',   # Какой оператор отвечает за целочисленные деление
    '12': '%',   # Какой оператор отвечает за остаток от деления
    '13': 'split',   # Какой метод разделит нашу строку по указанному разделителю
    '14': 'format',   # Какой метод поможет нам вставлять в готовую строку в нужных местах значения переменных
    '15': 'replace',   # Какой метод заменит указанные нами символы/подстроки на новые символы/подстроки
    '16': 'новую измененную строку',   # Что возвращают методы из предыдущих двух вопросов (ничего, новую измененную строку)
    '17': 'append',   # Какой метод добавляет в нашу последовательность, например список, новый элемент
    '18': 'range',   # Какой стандартный метод нужен для получения последовательности чисел
    '19': 'len',   # Как узнать длину любого контейнера
    '20': 'int',   # Какой тип данных вернут функция из предыдущего вопроса
    '21': 'values',   # Какой метод возващает либо значение по ключу, либо стандартное значение в словарях
    '22': 'False',   # Что вернет 12 < 1
    '23': '30',   # Что вернет 3 + 3 ** 3
    '24': 'False',   # Что вернет в if [] - True или False
    '25': 'list',   # Какой тип данных вернет splitlines()
    '26': 'True',   # Что вернет if range(10) - True или False
    '27': 'pass',   # Какой оператор пропускает текущий шаг в цикле
    '28': 'break',   # Какой оператор останавливает цикл
    '29': 'return',   # Каким оператором возвращается значение из функции
    '30': 'None',   # Какой оператор не делает ничего
}

# t.answer_checker(my_answers) выполнить файл для проверки ваших ответов





'''
задача со *

создать 2 функции вычисления факториала: по циклу и с рекурсией

'''


n = int(input("Enter a number: "))

factorial = 1

while n > 1:
    factorial *= n
    n -= 1

print(factorial)

def fac(n):
    if n == 0:
        return 1
    else:
        return fac(n - 1) * n


print(fac(4))