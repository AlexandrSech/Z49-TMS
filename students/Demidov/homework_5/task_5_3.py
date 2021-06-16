<<<<<<< HEAD
=======
# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]

for i in range(200, 301):
    division = 0
    n = 0
    for x in range(1, i):
        if i % x == 0:
            division += x

    for j in range(1, division):
        if division % j == 0:
            n += j

    if i == n and i != division and i == min(i, division):
        print(i, division)
>>>>>>> 639fa8a48095b717096dcd5068de1ac4708a4264
