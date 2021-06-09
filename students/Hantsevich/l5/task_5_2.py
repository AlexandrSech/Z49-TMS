num1 = int(input("input number: "))
num2 = num1
sum1 = 0
sum2 = 1
while num1 > 0:
    sum1 += num1 % 10
    num1 //= 10
while num2 > 0:
    sum2 *= num2 % 10
    num2 //= 10
print("сумма чисел - ", sum1, "произведение чисел - ", sum2)
