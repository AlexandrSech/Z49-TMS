number_1 = number_2 = int(input('Enter a starting number:'))
max_nums = int(input('Enter numbers maximum:'))

print(number_1, number_2, end=' ')

for i in range(2, max_nums):
    number_1, number_2 = number_2, number_1 + number_2
    print(number_2, end=' ')