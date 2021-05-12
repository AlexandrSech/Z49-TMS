import math

"""
Два натуральных числа называют дружественными,
если каждое из них равно сумме всех делителей другого,
кроме самого этого числа. Найти все пары дружественных чисел,
лежащих в диапазоне от 200 до 300. [02-3.2-HL02
"""
x = 200
y = 300
t = x
my_dict = dict()

for i in range(x,y+1):
    t = i
    res = 0
    n = 1
    while n < t:
        if t % n == 0:
            res += n
            n += 1
        else:
            n += 1
    print("Cумма всех делителей числа {} = {}".format(t, res))
    my_dict[t] = res
print(my_dict)

for key, value in my_dict.items():
    for k, val in my_dict.items():
        if key == val and k == value and key != value:
            print("Число {} и число {} дружественные".format(key, k))
