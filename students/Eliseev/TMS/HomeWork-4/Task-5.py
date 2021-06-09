list_feba_1 = [1, 1, ]
list_feba_2 = [1, 1, ]
x = 0
for el in range(15):
    new_number = int(list_feba_1[-2]) + int(list_feba_1[-1])
    list_feba_1.append(new_number)
print(list_feba_1)

while x < 15:
    new_number = int(list_feba_2[-2]) + int(list_feba_2[-1])
    list_feba_2.append(new_number)
    x += 1
print(list_feba_2)

