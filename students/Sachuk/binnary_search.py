my_list = [12, 10, 24, 20, 15, 68, 42, 33, 22, 27, 57, 79, 70, 77, 51, 81]
result = sorted(my_list)

def binary_search(list, x):
    start = 0
    finish = len(list)
    step = 0
    result = f'{x} not found'
    while True:
        middle = (start + finish) // 2
        print(list[middle])
        if x == list[middle]:
            result = f'index {x} is {my_list.index(x)}'
            break
        elif start == finish:
            break
        else:
            if x < list[middle]:
                step +=1
                finish = middle -1
            else:
                step +=1
                start = middle + 1
    return result

print(binary_search(result, 10))


