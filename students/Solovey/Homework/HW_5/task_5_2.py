'''
2) Дано число. Найти сумму и произведение его цифр.
'''

def summary():
    dig_1 = list(input('Enter a number to calculate SUM:\n'))
    for i in range(len(dig_1)):
        dig_1[i] = int(dig_1[i]) + int(dig_1[i -1])
        dig_sum = dig_1[-2]
    print('Sum is ' + str(dig_sum) + '.')

def product():
    dig_1 = list(input('Enter a number to calculate PRODUCT:\n'))
    for i in range(len(dig_1)):
        dig_1[i] = int(dig_1[i]) * int(dig_1[i -1])
    print('Product is ' + str(dig_1[-2]) + '.')

summary()
product()
