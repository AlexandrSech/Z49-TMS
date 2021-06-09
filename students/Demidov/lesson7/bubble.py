def bubble_sort(l: list):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(l) -1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swapped = True

my_list = [3, 1, 4, 10, 8, 5, 2, -20, 57]

bubble_sort(my_list)
print(my_list)