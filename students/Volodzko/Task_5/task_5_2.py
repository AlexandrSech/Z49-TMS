"""
Дано число. Найти сумму и произведение его цифр.
"""
numbers = input("Введите число: ")
list_numbers = [int(i) for i in list(numbers)]
print(list_numbers)
res_sum = 0
res_mult = 1
for i in list_numbers:
    res_sum += i
    res_mult *=i
print(res_sum)
print(res_mult)
