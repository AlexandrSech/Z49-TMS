class MyError(Exception):
    def __init__(self, text):
        self.txt = text

loop = True
i = 200

while loop:
    try:
        print('try')
        i = 1 / int(input('Enter number: '))
        print('1/0?')

        raise MyError

        loop = False
    except MyError as err:
        print(err.txt)
    except ZeroDivisionError:
        print("Divided by zero!")
    except Exception as unreal_exception:
        print(unreal_exception)


print(i)