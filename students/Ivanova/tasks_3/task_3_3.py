'''Ввести строку. Если длина строки больше 10 символов, то создать новую
строку с 3 восклицательными знаками в конце ('!!!') и вывести на экран.
Если меньше 10, то вывести на экран второй символ строки'''

input_string = str(input('Input string:'))
if len(input_string) > 10:
    new_string = input_string + '!!!'
    print(new_string)
else:
    print(input_string[1])