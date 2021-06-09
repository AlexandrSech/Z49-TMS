'''
Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)
'''


def ispolyndrom(k: str):
        if k[:] == k[::-1]:
            return f'{k} is a polyndrom'
        else:
            return f'{k} is not a polyndrom'



print(ispolyndrom('палиндром'))
print(ispolyndrom('шалаш'))
print(ispolyndrom('шалаши'))