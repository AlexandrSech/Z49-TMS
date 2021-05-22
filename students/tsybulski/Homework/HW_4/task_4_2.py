lst = [1, 10, 20, 30]
lst_2 = []
x = 0
while x < len(lst):
    if lst[x] % 2 == 0:
        lst_2.append(lst[x])
    x += 1
print(len(lst_2))


exit()
lst = [1, 10, 20, 30]
lst_2 = []
for i in lst:
    if i % 2 == 0:
        lst_2.append(i)
print(len(lst_2))


