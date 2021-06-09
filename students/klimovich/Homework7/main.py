

#1

def converter1(x: int) -> float:
    return x * 2.54

x = converter1(10)
print(x)

#2

def converter2(x: float) -> float:
    return x / 2.54

x2 = converter2(10)
print(x2)

#3

def converter3(x: float) -> float:
    return x * 1.609344

x3 = converter3(10)
print(x3)

#4

def converter4(x: float) -> float:
    return x / 1.609344

x4 = converter4(10)
print(x4)

#5
def converter5(x: float) -> float:
    return x * 0.4535923745

x5 = converter5(10)
print(x5)

#6
def converter6(x: float) -> float:
    return x / 0.4535923745

x6 = converter6(10)
print(x6)

#7
def converter7(x: float) -> float:
    return x * 28.35

x7 = converter7(10)
print(x7)

#8
def converter8(x: float) -> float:
    return x / 28.35

x8 = converter8(10)
print(x8)

#9
def converter9(x: float) -> float:
    return x * 4.55

x9 = converter9(10)
print(x9)

#10
def converter10(x: float) -> float:
    return x / 4.55

x10 = converter10(10)
print(x10)

#11
def converter11(x: float) -> float:
    return x * 0.5683

x11 = converter11(10)
print(x11)

#12
def converter12(x: float) -> float:
    return x / 0.5683

x12 = converter12(10)
print(x12)

while True:
    print('1. Дюймы в сантиметры')
    print('2. Сантиметры в дюймы')
    print('3. Мили в километры')
    print('4. Километры в мили')
    print('5. Фунты в килограммы')
    print('6. Килограммы в фунты')
    print('7. Унции в граммы')
    print('8. Граммы в унции')
    print('9. Галлон в литры')
    print('10. Литры в галлоны')
    print('11. Пинты в литры')
    print('12. Литры в пинты')
    print('0. Выход из программы')
    sign = input()
    if sign == '1':
        print('Введите значение:')
        val = float(input())
        print(converter1(val))
    if sign == '2':
        print('Введите значение:')
        val = float(input())
        print(converter2(val))
    if sign == '3':
        print('Введите значение:')
        val = float(input())
        print(converter3(val))
    if sign == '4':
        print('Введите значение:')
        val = float(input())
        print(converter4(val))
    if sign == '5':
        print('Введите значение:')
        val = float(input())
        print(converter5(val))
    if sign == '6':
        print('Введите значение:')
        val = float(input())
        print(converter6(val))
    if sign == '7':
        print('Введите значение:')
        val = float(input())
        print(converter7(val))
    if sign == '8':
        print('Введите значение:')
        val = float(input())
        print(converter8(val))
    if sign == '9':
        print('Введите значение:')
        val = float(input())
        print(converter9(val))
    if sign == '10':
        print('Введите значение:')
        val = float(input())
        print(converter10(val))
    if sign == '11':
        print('Введите значение:')
        val = float(input())
        print(converter11(val))
    if sign == '12':
        print('Введите значение:')
        val = float(input())
        print(converter12(val))
    if sign == '0':
        print('goodbye')
        break
    else:
        print('Введите из меню')