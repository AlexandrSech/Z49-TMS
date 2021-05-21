# Написать программу, в которой вводятся два операнда Х и Y и знак операции
# sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
# реакции на возможный неверный знак операции, а также на ввод Y=0 при
# делении. Организовать возможность многократных вычислений без перезагрузки
# программа (т.е. построить бесконечный цикл). В качестве символа прекращения
# вычислений принять ‘0’ (т.е. sign='0').

user_choose = input("Press any key to continue or 0 to exit\n")

while user_choose != "0":
    x = int(input("Enter 1st num: "))
    y = int(input("Enter 2nd num: "))

    sign = input("Enter sign: (+, -, *, /): ")

    if sign == "+":
        summ = x + y
        print(summ)
        user_choose = input("Press any key to continue or 0 to exit\n")
    elif sign == "-":
        diff = x - y
        print(diff)
        user_choose = input("Press any key to continue or 0 to exit\n")
    elif sign == "*":
        multiply = x * y
        print(multiply)
        user_choose = input("Press any key to continue or 0 to exit\n")
    elif sign == "/":
        try:
            division = x / y
            print(division)
            user_choose = input("Press any key to continue or 0 to exit\n")
        except ZeroDivisionError:
            print("Divided by zero!")
            user_choose = input("Press any key to continue or 0 to exit\n")
    else:
        print("Choose right sign! (+, -, *, /): ")
        print(user_choose)