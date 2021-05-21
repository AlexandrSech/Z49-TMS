'''Дан список целых чисел. Подсчитать сколько четных чисел в списке'''

my_list = [13, 5, 82, 43, 6, -6, ]
new_list = []
for i in range(0, len(my_list)):
     dev = my_list[i] % 2 == 0
     if dev == 0:
         new_list.append(my_list[i])
     else:
         pass
print(len(new_list))

my_list = [13, 5, 82, 43, 6, -6, ]
new_list = []
cycle = len(my_list)
while cycle > 0:
    dev = my_list[i] % 2 == 0
    if dev == 0:
        new_list.append(my_list[i])
    else:
        pass
    cycle -=1
    i -= 1
print (len(new_list))