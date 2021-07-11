
# декоратор - это функция, в которой мы вызываем декорируемую функцию


def deco1(d_arg1, d_arg2, *d_args):     # здесь мы создаем декоратор и агрументы для него
    print('some code before in decorator 1')
    print('decorator args:', d_arg1, d_arg2, d_args)

    def deco(foo):      # тут мы создаем подфункцию для работы с декорируемой функцией, создаем аргумент
        # будет ссылка на декорируемую функцию
        print('some code before in decorator 2')

        def inner(*foo_args, **foo_kwargs):     # следующая внутренняя функция нужна для получения аргументов
            # для декорируемой функции, а так же для вызова ее и дополнения своим функционалом
            # почему проще всего указать тут арги и кварги? потому что у декорируемой функции как могут быть аргументы
            # так может их и не быть, т.е. количество аргументов - динамической, собственно как арги и кварги
            print('some code before in decorator 3')    # до вызова декорируемой мы можем чтото сделать
            foo_result = foo(*foo_args, **foo_kwargs)
            print('some code after in decorator 3')     # после вызова декорируемой мы можем чтото сделать
            return foo_result

        print('some code after in decorator 2')
        return inner

    print('some code after in decorator 1')
    return deco


@deco1(123, 'some string value', 1,2,3,4,5,6)
def some_func1():
    print('some func with code')
    return True


@deco1(1, 2,)
def some_func2(a1, a2):
    print('some func with code')
    return (a1, a2)


# тут мы пробуем запустить наши декорируемые функции
# и видим результат
if __name__ == '__main__':
    from time import sleep
    sleep(1)
    print('_'*30)
    print(some_func1())
    sleep(1)
    print('_'*30)
    print(some_func2(1, 5))


# результат
'''
some code before in decorator 1
decorator args: 123 some string value (1, 2, 3, 4, 5, 6)
some code after in decorator 1
some code before in decorator 2
some code after in decorator 2
some code before in decorator 1
decorator args: 1 2 ()
some code after in decorator 1
some code before in decorator 2
some code after in decorator 2
______________________________
some code before in decorator 3
some func with code
some code after in decorator 3
True
______________________________
some code before in decorator 3
some func with code
some code after in decorator 3
(1, 5)
'''

# до первой ______________________________ мы видим что уже чтото выполняется
# нам это не нравится, т.к. этот код запускается не тогда, когда мы его запускаем, а тогда, когда запускается сам файл
# например попробуйте просто запустить такой код, а предыдущий блок кода if __name__ == '__main__': закомментируйте:
# и посмотрите что произойдет
'''

if __name__ == '__main__':
    print(1)
    exit()
'''

# поэтому советую писать код который будет дополнять декорируемую функцию только в функции inner
# т.к. он запуститься только тогда, когда мы запустим сами задекорированную функцию
