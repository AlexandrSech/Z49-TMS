my_string = input("Введите строку: ")

if len(my_string) > 10:
    my_string = my_string + "!!!"
    print(my_string)
elif len(my_string) < 10:
    print(my_string[1])
else:
    print("Строка " + my_string + " равняется 10 символам")