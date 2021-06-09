
def foo(spis):
    umber_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    return
stdin = '0 1 1 2 3 5 8 13'
number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}


def print_given(*args, **kwargs):
    for i in range(len(args)):
        print(args[i], type(args[i]))
    spis = list(kwargs.keys())
    for i in spis:
        print(i, kwargs[i], type(kwargs[i]))
print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3)
exit()



xs = [3, 14, 15, 92, 115]
max_index = max((0, 1, 2, 3, 4), key = lambda i: xs[i])

print(max_index, lambda i:xs[i])

exit()

def sec(*args):
    for i in range(len(args)):
        print(float(args[i]))
stroka = '1 2 4 5 8 12 34 12 43'
spis = list(stroka.split(' '))
sec(*spis)



exit()



def t(*args, **kwargs):
    print(args)
    for el in kwargs:
        print(el)
    print(kwargs)
t(1,2,3,'asd','ltr',a = 1, b = 87)