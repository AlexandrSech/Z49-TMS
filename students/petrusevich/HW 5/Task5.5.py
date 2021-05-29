array = []
maxi = 0
for i in range(1, 20):
    array.append(int(input(f'Введите {i} числo массива: ')))
print('\n', array)
for i in range(len(array)):
    if maxi < array[i]:
        maxi = array[i]
for i in range(len(array)):
    if array[i] % 2 == 0:
        array[i] = maxi
    i+=1
print('\n'+'Максимальное число:', maxi)
print('\n'+'Новый массив:', array)
