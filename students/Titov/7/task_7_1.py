"""Написать 12 функций по переводу:

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
Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”"""
def dtosm(d):
    return d * 2.54
def smtod(d):
    return d / 2.54
def mtokm(d):
    return d * 1.609
def kmtom(d):
    return d / 1.609
def ftokg(d):
    return d * 0.454
def kgtof(d):
    return d / 0.454
def utogr(d):
    return d * 28.35
def grtou(d):
    return d / 28.35
def galtol(d):
    return d * 4.55
def ltogal(d):
    return d / 4.55
def ptol(d):
    return d * 0.568
def ltop(d):
    return d / 0.568

while True:
    a = int(input("Ввыберите вариант"))
    b = int(input('Введите число для преобразования'))
    if a == 1:
        print(dtosm(b))
    elif a == 2:
        print(smtod(b))
    elif a == 2:
        print(smtod(b))
    elif a == 3:
        print(mtokm(b))
    elif a == 4:
        print(kmtom(b))
    elif a == 5:
        print(ftokg(b))
    elif a == 6:
        print(kgtof(b))
    elif a == 7:
        print(utogr(b))
    elif a == 8:
        print(grtou(b))
    elif a == 9:
        print(galtol(b))
    elif a == 10:
        print(ltogal(b))
    elif a == 11:
        print(ptol(b))
    elif a == 12:
        print(ltop(b))
    elif a == 0:
        break
    else:
        print("Вы ввели чушмандешку")
