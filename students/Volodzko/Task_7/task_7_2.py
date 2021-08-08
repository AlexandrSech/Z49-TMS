import task_7_1

"""
2.Написать программу,соследующим интерфейсом:
пользователю предоставляется на выбор 12 вариантов 
перевода (описанных в первой задаче). Пользователь 
вводит цифру отодного до двенадцати. 
После программа запрашивает ввести численное значение. 
Затем программа выдает конвертированный результат. 
Использовать функции из первого задания. Программа 
должна быть в бесконечном цикле. Код выхода из программы-“0”
"""


def convert():
    text = """Вас приветсивует программа конвертер!!!
    1.Перевести Дюймы в сантиметры
    2.Перевести Сантиметры в дюймы
    3.Перевести Мили в километры
    4.Перевести Километры в мили
    5.Перевести Фунты в килограммы
    6.Перевести Килограммы в фунты
    7.Перевести Унции в граммы
    8.Перевести Граммы в унции
    9.Перевести Галлон в литры
    10.Перевести Литры в галлоны
    11.Перевести Пинты в литры
    12.Перевести Литры в пинты
    0. Выход из программы"""
    print(text)
    while True:
        try:
            operation = int(input("Введите номер операции: "))
        except ValueError:
            print('Введите число')
            continue
        if operation == 0:
            print("ВЫ ВЫШЛИ ИЗ ПРОГРАММЫ!\n")
            return 0
        else:
            try:
                value = int(input("Введите значение, которое хотите конвертировать: "))
            except ValueError:
                print("Конвертировать можно только число")
                continue
        if operation == 1:
            result = task_7_1.func1(value)
            print(f"РЕЗУЛЬТАТ ПЕРЕВОДА: {result}\n")
        elif operation == 2:
            result = task_7_1.func2(value)
            print(f"РЕЗУЛЬТАТ ПЕРЕВОДА: {result}\n")
        elif operation == 3:
            result = task_7_1.func3(value)
            print(f"РЕЗУЛЬТАТ ПЕРЕВОДА: {result}\n")
        elif operation == 4:
            result = task_7_1.func4(value)
            print(f"РЕЗУЛЬТАТ ПЕРЕВОДА: {result}\n")
        elif operation == 5:
            result = task_7_1.func5(value)
            print(f"РЕЗУЛЬТАТ ПЕРЕВОДА: {result}\n")
        elif operation == 6:
            result = task_7_1.func6(value)
            print(f"РЕЗУЛЬТАТ ПЕРЕВОДА: {result}\n")
        elif operation == 7:
            result = task_7_1.func7(value)
            print(f"РЕЗУЛЬТАТ ПЕРЕВОДА: {result}\n")
        elif operation == 8:
            result = task_7_1.func8(value)
            print(f"РЕЗУЛЬТАТ ПЕРЕВОДА: {result}\n")
        elif operation == 9:
            result = task_7_1.func9(value)
            print(f"РЕЗУЛЬТАТ ПЕРЕВОДА: {result}\n")
        elif operation == 10:
            result = task_7_1.func10(value)
            print(f"РЕЗУЛЬТАТ ПЕРЕВОДА: {result}\n")
        elif operation == 11:
            result = task_7_1.func11(value)
            print(f"РЕЗУЛЬТАТ ПЕРЕВОДА: {result}\n")
        elif operation == 12:
            result = task_7_1.func12(value)
            print(f"РЕЗУЛЬТАТ ПЕРЕВОДА: {result}\n")

        else:
            print("ВВЕДЕНЫ НЕКОРРЕКТНЫЕ ДАННЫЕ!\n")


convert()
