"""
Даны три слова. Выяснить, является ли хоть одно из
них палиндромом("перевертышем"), т. е. таким, которое
читается одинаково слева направо исправа налево.
(Определить функцию, позволяющую распознавать слова палиндромы.
"""


def my_polindrom(my_string: str):
    my_string = str(my_string)
    my_string2 = ''
    if " " in my_string:
        my_string2 = my_string.replace(" ", "")
    else:
        my_string2 = my_string

    if my_string2.lower() == my_string2[::-1].lower():
        print(f"Строка \"{my_string}\" является полиндромом")
        return 'Полиндром'
    else:
        print(f"Строка \"{my_string}\" НЕ является полиндромом")
        return 'Не полиндром'


m1 = "Коту тащат уток"
m2 = "Леша на полке клопа нашел"
m3 = "Hello World"

my_polindrom(m1)
my_polindrom(m2)
my_polindrom(m3)

my_polindrom(123)
my_polindrom('afsasf')