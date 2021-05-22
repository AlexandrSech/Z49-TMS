# Дано число. Найти сумму и произведение его цифр.
a = 1234353633
summa = 0
multiplication = 1
list_a = str(a)
for i in list_a:
    summa += int(i)
    multiplication *= int(i)
print(summa)
print(multiplication)