my_string = input("Введите строку: ")

length = len(my_string) // 2

middle_letter = my_string[length]

print(middle_letter)

if middle_letter == my_string[0]:
    print(my_string[1:-1])