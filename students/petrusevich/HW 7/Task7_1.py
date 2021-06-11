""""
Написать 12 функций по переводу:
Дюймы в сантиметры
Сантиметры в дюймы
Мили в километры
Километры в мили
Фунты в килограммы
Килограммы в фунты
Унции в граммы
Граммы в унции
Галлон в литры
Литры в галлоны
Пинты в литры
Литры в пинты
Примечание: функция принимает на вход число и возвращает конвертированное число"""


def inches_centimeters():
    number = int(input('Введите число: '))
    result = number * 2.54
    return f'{number} inches = {result} centimeters'


def centimeters_inches():
    number = int(input('Введите число: '))
    result = number / 2.54
    return f'{number} centimeters = {result} inches'


def miles_kilometers():
    number = int(input('Введите число: '))
    result = number * 1.60934
    return f'{number} miles = {result} kilometers'


def kilometers_miles():
    number = int(input('Введите число: '))
    result = number / 1.60934
    return f'{number} kilometers = {result} miles'


def pounds_kilogram():
    number = int(input('Введите число: '))
    result = number * 0.453592
    return f'{number} pounds = {result} kilogram'


def kilogram_pounds():
    number = int(input('Введите число: '))
    result = number / 0.453592
    return f'{number} kilogram = {result} pounds'


def ounce_grams():
    number = int(input('Введите число: '))
    result = number * 28.3495
    return f'{number} ounce = {result} grams'


def grams_ounce():
    number = int(input('Введите число: '))
    result = number / 28.3495
    return f'{number} grams = {result} ounce'


def gallon_liters():
    number = int(input('Введите число: '))
    result = number * 3.78541
    return f'{number} gallon = {result} liters'


def liters_gallon():
    number = int(input('Введите число: '))
    result = number / 3.78541
    return f'{number} liters = {result} gallon'


def inches_liters():
    number = int(input('Введите число: '))
    result = number * 0.473176
    return f'{number} pints = {result} liters'


def liters_centimeters():
    number = int(input('Введите число: '))
    result = number / 0.473176
    return f'{number} liters = {result} pints'
