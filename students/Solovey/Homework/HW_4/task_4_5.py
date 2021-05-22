'''
5) Составить список чисел Фибоначчи содержащий 15 элементов.
'''

# example_1

number_1 = number_2 = int(input('Enter a starting number:'))
max_nums = int(input('Enter numbers maximum:'))

fib_list = []
fib_list.append(number_1)
fib_list.append(number_2)

for i in range(2, max_nums):
    number_1, number_2 = number_2, number_1 + number_2
    fib_list.append(number_2)
print(fib_list)
print('\n\n')



# example_2

number_1 = number_2 = int(input('Enter a starting number:'))
max_nums = int(input('Enter numbers maximum:'))

fib_list = []
fib_list.append(number_1)
fib_list.append(number_2)

i = 0
while i < max_nums - 2:
    number_1, number_2 = number_2, number_1 + number_2
    fib_list.append(number_2)
    i += 1
print(fib_list)