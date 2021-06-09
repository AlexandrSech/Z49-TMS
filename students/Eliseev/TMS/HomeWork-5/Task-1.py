
while True:
    x = int(input("Введит число x: "))
    y = int(input("Введите число y: "))
    sign = input("Введите знак /, *, +, -, для вычисления.\n"
                 "для выхода из программы введите 0\n")
    if sign == "/":
        if y == 0:
            print("На ноль делить нельзя!")
            continue
        z = x / y
    elif sign == "-":
        z = x - y
    elif sign == "+":
        z = x + y
    elif sign == "*":
        z = x * y
    elif sign == "0":
        break
    else:
        print("Вы ввели неправильный знак")
        continue
    print(z)