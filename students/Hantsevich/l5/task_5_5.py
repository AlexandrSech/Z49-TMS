my_m = [45,456,5,4,54,59,47,8,6]
my_m.sort()

for i in range(len(my_m)):
    if my_m[i] % 2 == 0:
        my_m[i] = my_m[len(my_m)-1]
print(my_m)
