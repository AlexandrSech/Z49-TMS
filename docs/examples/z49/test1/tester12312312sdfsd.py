def answer_checker(answers: dict):
    ra = {
            '1': 'cd',    # укажите команду в терминале для навигации по файловой системе
            '2': 'pwd',    # Укажите команду в терминале для того, чтобы узнать в какой директории сейчас вы находитесь
            '3': 'mkdir',    # Укажите команду в терминале для создания папки
            '4': 'touch',    # Укажите команду в терминале для создания файла
            '5': 'ls',    # Укажите команду в терминале для вывода списка всех файлов и папок в текущей директории
            '6': 'int',    # Какой тип данных нужен для работами с целыми числами
            '7': 'float',    # Какой тип данных нужен для работами с дробными числами
            '8': 'str',    # Какой тип данных нужен для работами со строками
            '9': 'bool',    # Какой тип данных нужен для работами с булевыми значениями
            '10': '**',   # Какой оператор нужно использовать чтобы возвести число в степень
            '11': '//',   # Какой оператор отвечает за целочисленные деление
            '12': '%',   # Какой оператор отвечает за остаток от деления
            '13': 'split',   # Какой метод разделит нашу строку по указанному разделителю
            '14': 'format',   # Какой метод поможет нам вставлять в готовую строку в нужных местах значения переменных
            '15': 'replace',   # Какой метод заменит указанные нами символы/подстроки на новые символы/подстроки
            '16': 'новая строка',   # Что возвращают методы из предыдущих двух вопросов (ничего, новую измененную строку)
            '17': 'append',   # Какой метод добавляет в нашу последовательность, например список, новый элемент
            '18': 'range',   # Какой стандартный метод нужен для получения последовательности чисел
            '19': 'len',   # Как узнать длину любого контейнера
            '20': 'int',   # Какой тип данных вернут функция из предыдущего вопроса
            '21': 'get',   # Какой метод возващает либо значение по ключу, либо стандартное значение в словарях
            '22': 'False',   # Что вернет 12 < 1
            '23': '30',   # Что вернет 3 + 3 ** 3
            '24': 'False',   # Что вернет в if [] - True или False
            '25': 'list',   # Какой тип данных вернет splitlines()
            '26': 'True',   # Что вернет if range(10) - True или False
            '27': 'continue',   # Какой оператор пропускает текущий шаг в цикле
            '28': 'break',   # Какой оператор останавливает цикл
            '29': 'return',   # Каким оператором возвращается значение из функции
            '30': 'pass',   # Какой оператор не делает ничего
    }
    for k, v in answers.items():
        if k == 'name':
            print('Проверка ответов ученика: {}'.format(v))
            continue
        print(
            'Вопрос {}: ответ {}'.format(
                k,
                'правильный.' if ra.get(k) and ra[k].lower() == v.lower() else 'не правильный. (ваш ответ {})'.format(v)
            )
        )