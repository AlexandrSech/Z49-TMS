"""
Даны три слова. Выяснить, является ли хоть одно из
них палиндромом("перевертышем"), т. е. таким, которое
читается одинаково слева направо исправа налево.
(Определить функцию, позволяющую распознавать слова палиндромы.
"""


def my_polindrom(my_string: str):
    my_string2 = ''
    if " " in my_string:
        my_string2 = my_string.replace(" ", "")
    if my_string2.lower() == my_string2[::-1].lower():
        return f"Строка \"{my_string}\" является полиндромом"
    else:
        return f"Строка \"{my_string}\" НЕ является полиндромом"


m1 = "Коту тащат уток"
m2 = "Леша на полке клопа нашел"
m3 = "Hello World"

print(my_polindrom(m1))
print(my_polindrom(m2))
print(my_polindrom(m3))
