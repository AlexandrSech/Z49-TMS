'''Для каждого натурального числа в промежутке от m до n вывести все делители,
кроме единицы и самого числа. m и n вводятся с клавиатуры.'''

m = int(input())
n = int(input())
dict_ = {}
for i in range(m, n+1):
    dev = 2
    dev_list = []
    while dev < i:
        if i % dev == 0:
            dev_list.append(dev)
            dict_[i] = dev_list
        dev += 1
print(dict_)