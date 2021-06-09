from math import sqrt
# task_1

a = 4
b = 3

sum = a + b
multiplication = a * b
substraction = a - b

print(sum, multiplication, substraction)

# task_2

x = 20
y = -5

equation = ((abs(x) - abs(y)) / (1 + abs(x * y)))
print(equation)


# task_3

a = 4

volume = a ** 3
square = a ** 2
print(volume, square)

# task_4

a = 4
b = 9

average_ari = (a + b) / 2
average_geo = sqrt(a*b)

print(average_ari, average_geo)

# task_5

a = 7
b = 4

hypo = sqrt(a ** 2 + b ** 2)
square = a * b / 2

print(hypo, square)

# task_6 (*)

print('Enter a word')
# word = input()
word = 'mama'
polyndrome = word + word[-2::-1]
print(polyndrome)