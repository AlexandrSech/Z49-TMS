"""
2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
"""
from task_7_1 import *


def convert():
    foo_dict = {
        1: ['Дюймы в сантиметры', inch_to_cm],
        2: ['Сантиметры в дюймы', cm_to_inch],
        3: ['Мили в километры', mile_to_km],
        4: ['Километры в мили', km_to_mile],
        5: ['Фунты в килограммы', pound_to_kg],
        6: ['Килограммы в фунты', kg_to_pound],
        7: ['Унции в граммы', ounce_to_g],
        8: ['Граммы в унции', g_to_ounce],
        9: ['Галлон в литры', gallon_to_l],
        10: ['Литры в галлоны', l_to_gallon],
        11: ['Пинты в литры', pint_to_l],
        12: ['Литры в пинты', l_to_pint]
    }
    while True:
        for keys, values in foo_dict.items():
            print(keys, values[0])
        foo_num = int(input('Enter function number: '))
        if foo_num == 0:
            break

        user_num = int(input('Enter value to convert: '))
        for keys, values in foo_dict.items():
            if foo_num == keys:
                print(values[1](user_num))
            else:
                continue



convert()
