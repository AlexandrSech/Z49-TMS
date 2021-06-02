'''Дано число. Найти сумму и произведение его цифр.'''

num = input()
result = 0
if not num.isdigit():
    print('Not a number, try again')
else:
    for item in num[:]:
        new_item = int(item)
        print(new_item, type(new_item))
        result += new_item
print(result)