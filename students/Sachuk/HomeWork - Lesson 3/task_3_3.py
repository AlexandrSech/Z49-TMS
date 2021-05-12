# Ввести строку. Если длина строки больше 10 символов, то создать новую
# строку с 3 восклицательными знаками в конце ('!!!') и вывести на экран.
# Если меньше 10, то вывести на экран второй символ строки

s = input()

if len(s) > 10:
    result = s + "!!!"
    print(result)
elif  len(s) >=2 and len(s) < 10:
    result = s[1]
    print(result)
else:
    print('Your string doesn\'t comply with the task')