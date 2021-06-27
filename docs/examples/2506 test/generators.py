'''
def map(func, iter_obj):
    for i in iter_obj:
        yield func(i)
'''





def upp(string: str):
    return string.upper()

l = ['qwe', 'sfsdc', 'gfdrsawe',]

r = map(upp, l)

print(r)





