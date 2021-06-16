
def decor(anything):
    def inner_dec():
        print('салатик')
        anything()
        print('помидорикос')

    return inner_dec
def decor_2(anything):
    def inner_dec():
        print('сыр')
        anything()
        print('Батооон(кот)')

    return inner_dec

@decor
@decor_2
def stand_alone_function():
    print("мясцо")

print(type(stand_alone_function()))


