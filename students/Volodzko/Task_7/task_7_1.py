""" Задание:
Написать 12 функций по переводу:
1.Дюймы в сантиметры
2.Сантиметры в дюймы
3.Мили в километры
4.Километры в мили
5.Фунты в килограммы
6.Килограммы в фунты
7.Унции в граммы
8.Граммы в унции
9.Галлон в литры
10.Литры в галлоны
11.Пинты в литры
12.Литры в пинты
Примечание:функция принимает навход число и возвращает конвертированное число
"""


def func1(x):  # Дюймы в сантиметры
    try:
        x = int(x)
    except ValueError:
        return 'Введите число'
    return round(x * 2.54, 2)


def func2(x):  # Сантиметры в дюймы
    try:
        x = int(x)
    except ValueError:
        return 'Введите число'
    return round(x / 2.54, 2)


def func3(x):  # Мили в километры
    try:
        x = int(x)
    except ValueError:
        return 'Введите число'
    return round(x * 1.61, 2)


def func4(x):  # Километры в мили
    try:
        x = int(x)
    except ValueError:
        return 'Введите число'
    return round(x /1.61, 2)


def func5(x):  # Фунты в килограммы
    try:
        x = int(x)
    except ValueError:
        return 'Введите число'
    return round(x * 0.4535, 4)


def func6(x):  # Килограммы в фунты
    try:
        x = int(x)
    except ValueError:
        return 'Введите число'
    return round(x / 0.4535, 4)


def func7(x):  # Унции в граммы
    try:
        x = int(x)
    except ValueError:
        return 'Введите число'
    return round(x * 28.35, 2)


def func8(x):  # Граммы в унции
    try:
        x = int(x)
    except ValueError:
        return 'Введите число'
    return round(x / 28.35, 2)


def func9(x):  # Галлон в литры
    try:
        x = int(x)
    except ValueError:
        return 'Введите число'
    return round(x * 4.546, 3)


def func10(x):  # Литры в галлоны
    try:
        x = int(x)
    except ValueError:
        return 'Введите число'
    return round(x / 4.546, 3)


def func11(x):  # Пинты в литры
    try:
        x = int(x)
    except ValueError:
        return 'Введите число'
    return round(x * 0.5683, 4)


def func12(x):  # Литры в пинты
    try:
        x = int(x)
    except ValueError:
        return 'Введите число'
    return round(x / 0.5683, 4)
