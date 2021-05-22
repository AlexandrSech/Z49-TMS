num1 = 1
num2 = 2
sign = "dfdf"

while sign != 0:
    num1 = input("Enter a number: ")
    while not str.isdigit(num1):
        print("wrong operator")
        num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    while not str.isdigit(num2):
        print("wrong operator")
        num2 = input("Enter another number: ")
    sign = input("Enter operation ")
    if sign == "0":
        exit()
    elif sign == "+":
        print(float(num1) + float(num2))
    elif sign == "-":
        print(float(num1) - float(num2))
    elif sign == "*":
        print(float(num1) * float(num2))
    elif sign == "/":
        if num2 == "0":
            print("wrong operation")
        else:
            print(float(num1) / float(num2))
    else:
        print("wrong operation")