number = 124517
summa = 0
proizved = 1
for el in str(number):
    summa += int(el)
    proizved *= int(el)
print(summa, proizved)