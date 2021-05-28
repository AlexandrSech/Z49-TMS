# Дюймы >>> сантиметры
def func1(x):
    return x * 2.54

# Сантиметры >>> дюймы
def func2(x):
    return x / 2.54

# Мили >>> километры
def func3(x):
    return x * 1.61

# Километры >>> мили
def func4(x):
    return x / 1.61

# Фунты >>> килограммы
def func5(x):
    return x * 0.45359237

# Килограммы >>> фунты
def func6(x):
    return x / 0.45359237

# Унции >>> граммы
def func7(x):
    return x * 28.35

# Граммы >>> унции
def func8(x):
    return x / 28.35

# Галлоны >>> литры
def func9(x):
    return x * 4.54

# Литры >>> галлоны
def func10(x):
    return x / 4.54

# Пинты >>> литры
def func11(x):
    return x * 0.473177

# Литры >>> пинты
def func12(x):
    return x / 0.473177

def converter():
    print("""Выберите тип конвертации
    1.Дюймы >>> сантиметры
    2.Сантиметры >>> дюймы
    3.Мили >>> километры
    4.Километры >>> мили
    5.Фунты >>> килограммы
    6.Килограммы >>> фунты
    7.Унции >>> граммы
    8.Граммы >>> унции
    9.Галлон >>> литры
    10.Литры >>> галлоны
    11.Пинты >>> литры
    12.Литры >>> пинты
    0. Exterminatus""")
    while True:
        operation = int(input("Введите номер операции: "))
        if operation == 0:
            print("Во имя Бессмертного Имератора!!!\n")
            break
        else:
            value = int(input("Введите конвертируемое значение: "))
        if operation == 1:
            print(func1(value), end='\n')
        elif operation == 2:
            print(func2(value), end='\n')
        elif operation == 3:
            print(func3(value), end='\n')
        elif operation == 4:
            print(func4(value), end='\n')
        elif operation == 5:
            print(func5(value), end='\n')
        elif operation == 6:
            print(func6(value), end='\n')
        elif operation == 7:
            print(func7(value), end='\n')
        elif operation == 8:
            print(func8(value), end='\n')
        elif operation == 9:
            print(func9(value), end='\n')
        elif operation == 10:
            print(func10(value), end='\n')
        elif operation == 11:
            print(func11(value), end='\n')
        elif operation == 12:
            print(func12(value), end='\n')

        else:
            print("Попробуй еще раз...\n")


converter()