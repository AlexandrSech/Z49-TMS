# Даны три слова. Выяснить, является ли хоть одно из них палиндромом
# ("перевертышем"), т. е. таким, которое читается одинаково слева направо и
# справа налево. (Определить функцию, позволяющую распознавать слова
# палиндромы.)

def palindrom(*args: str):
    lst_palidnrom = []
    for i in args:
        if i == i[::-1]:
            lst_palidnrom.append(i)
    return lst_palidnrom


print(palindrom('qwq', 'qwwq', 'eqqq'))