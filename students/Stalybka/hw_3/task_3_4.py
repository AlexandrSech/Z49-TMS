"""Ввести строку. Вывести на экран букву, которая находится в середине этой
строки.
Также, если эта центральная буква равна первой букве в строке, то создать и
вывести часть строки между первым и последним символами исходной строки.
(подсказка: для получения центральной буквы, найдите длину строки и разделите
ее пополам. Для создания результирующий строки используйте срез)"""

user_str = input('').lower()
index = int(len(user_str) / 2)
if user_str[index] == user_str[0]:
    new_str = user_str[1:-1]
    print(new_str)
else:
    exit()
