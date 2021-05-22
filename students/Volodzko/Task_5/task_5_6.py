"""
Задан целочисленный массив. Определить количество участков
массива,на котором элементы монотонно возрастают
(каждое следующее число больше предыдущего)
"""
my_list = [20, 34, 50, 82, 11, 9, 17, 20, 9, 8, 7, 12]

t = 0
lst = []
for i in range(len(my_list)-1):
     if my_list[i] < my_list[i+1]:
        lst.append(my_list[i+1])
     else:
        if len(lst) > 0:
            t+=1
        lst = []
if lst:
    t+=1

print(t)



"""
t = 0
flag = False
for i in range(len(my_list)-1):
    if my_list[i] < my_list[i+1]:
        flag = True
    else:
        if flag:
            t+=1
            flag = False
if flag:
    t+=1
    flag = False

print(t)
"""










