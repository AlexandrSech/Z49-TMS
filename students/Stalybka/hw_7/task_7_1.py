"""
1. Написать 12 функций по переводу:
1. Дюймы в сантиметры
2. Сантиметры в дюймы
3. Мили в километры
4. Километры в мили
5. Фунты в килограммы
6. Килограммы в фунты
7. Унции в граммы
8. Граммы в унции
9. Галлон в литры
10. Литры в галлоны
11. Пинты в литры
12.Литры в пинты
Примечание: функция принимает на вход число и возвращает конвертированное число"""


def inch_to_cm(inch):
    cm = inch * 2.54
    return f'{inch} inch(es) = {cm} cm'


def cm_to_inch(cm):
    inch = cm / 2.54
    return f'{cm} cm = {inch} inch(es)'


def mile_to_km(mile):
    km = mile * 1.609
    return f'{mile} mile(s) = {km} km'


def km_to_mile(km):
    mile = km / 1.609
    return f'{km} km = {mile} mile(s)'


def pound_to_kg(pound):
    kg = pound * 0.4536
    return f'{pound} pound(s) = {kg} kg'


def kg_to_pound(kg):
    pound = kg / 0.4536
    return f'{kg} kg = {pound} pound(s)'


def ounce_to_g(ounce):
    g = ounce * 28.3495
    return f'{ounce} ounce(s) = {g} g'


def g_to_ounce(g):
    ounce = g / 28.3495
    return f'{g} g = {ounce} ounce(s)'


def gallon_to_l(gallon):
    l = gallon * 4.54609
    return f'{gallon} gallon(s) = {l} l'


def l_to_gallon(l):
    gallon = l / 4.54609
    return f'{l} l = {gallon} gallon(s)'


def pint_to_l(pint):
    l = pint * 0.568261
    return f'{pint} pint(s) = {l} l'


def l_to_pint(l):
    pint = l / 0.568261
    return f'{l} l = {pint} pint(s)'
