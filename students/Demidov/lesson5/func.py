def my_split(word, separator):
    x = ""
    my_list = []
    for symbol in word:
        if symbol == separator:
            my_list.append(x)
            x = ""
        else:
            x += symbol
    if x:
        my_list.append(x)       
    return my_list


print(my_split("hello", "e"))



exit()

def foo(a1='', a2=0, a3=True): # не позиционный
    print(a1)
    print(a2)
    print(a3)

foo(a3=False, a1='hello', a2=42)

exit()

def to_dict(**kwargs):
    return kwargs

d = to_dict(k1=8, k2=True, k3="String")

print(d)

exit()

def oper(x: int, y: int, operand: str) -> int:
    chooser = {
        '+': x + y,
        '-': x - y,
        '*': x * y,
        '/': x / y,
    }
    return chooser[operand]

print(oper(1, 2, '+'))

exit()

def operationer(x: int, y: int, operand: str) -> int:
    if operand == "+":
        return x + y
    elif operand == "-":
        return x - y

n = operationer(1, 2, '+')
print(n)


exit()

def my_len(obj):
    counter = 0
    for i in obj:
        counter += 1
    return counter

result = my_len([1, 2, 3, 4, 5,])
print(result)