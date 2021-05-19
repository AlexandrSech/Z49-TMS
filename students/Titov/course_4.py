for i in range(200, 301): #220
    sum_of_divide = 0
    n = 0
    for x in range(1, i):
        if i % x == 0:
            sum_of_divide += x

    for j in range(1, sum_of_divide):
        if sum_of_divide % j == 0:
            n += j

    if i == n and i != sum_of_divide and i == min(i, sum_of_divide):
        print(i, sum_of_divide)