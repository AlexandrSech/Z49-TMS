'''
5) Составить список чисел Фибоначчи содержащий 15 элементов.
'''

# example_1

number_1 = number_2 = int(input('Enter a starting number:'))
max_nums = int(input('Enter numbers maximum:'))

print(number_1, number_2, end=' ')

for i in range(max_nums):
    number_1, number_2 = number_2, number_1 + number_2
    print(number_2, end=' ')
print('\n\n')



# example_2

number_1 = number_2 = int(input('Enter a starting number:'))
max_nums = int(input('Enter numbers maximum:'))

print(number_1, number_2, end=' ')
i = 0
while i < max_nums:
    number_1, number_2 = number_2, number_1 + number_2
    print(number_2, end=' ')
    i += 1