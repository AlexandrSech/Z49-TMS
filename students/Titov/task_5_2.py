chislo = input('Введите число')
new_chislo = 0
for el in range(len(chislo)):
    new_chislo += int(chislo[el])
print("Сумма цифр числа =", new_chislo)