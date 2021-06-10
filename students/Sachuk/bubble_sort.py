no_sorted_list = [10, 75, 43, 15, 25, -4, 27]


def bubble_sort(list):
    last_item = len(list) -1
    for z in range(0, last_item):
        for x in range(0, last_item):
            if list[x] > list[x+1]:
                list[x], list[x+1] = list[x+1], list[x]
                print(list)
        last_item -= 1
    return list

print('Old list', no_sorted_list)
new_list = bubble_sort(no_sorted_list).copy()
print('New list: ', new_list)