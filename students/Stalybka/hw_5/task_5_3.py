'''Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300. '''

my_list = list(range(200, 301))
new_dict = {}
for item in my_list:
    dev = 1
    dev_sum = 0
    while dev < item:
        if item % dev == 0:
            dev_sum += dev
        dev += 1
    new_dict[item] = dev_sum
for key, value in new_dict.items():
        if new_dict.get(value) == key:
            print(key, value)