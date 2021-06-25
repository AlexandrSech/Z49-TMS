class MyError(Exception):
    def __init__(self):
        print('MyError')

    def __str__(self):
        return 'это моя ошибка'


class MyClass:
    def calc(self):
        i = -1*200
        if i > 0:
            return i
        else:
            raise MyError


c = MyClass()
print(c.calc())


exit()

loop = True
i = 200

while loop:
    try:
        print('try')
        i = i / int(input('enter number '))
        print('1/0?')



        loop = False
    except MyError as err:
        print(err)
    except ZeroDivisionError:
        print('НЕЛЬЗЯ СКА ДЕЛИТЬ НА НОЛЬ')
    except ValueError:
        print('ВВЕДИ ПОЖАЛСТА ЧИСЛО')
    # except Exception as unreal_exception:
        # print(unreal_exception)

print(i)

print('other code')


