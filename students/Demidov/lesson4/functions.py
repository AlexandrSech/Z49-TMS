def  convert_string_to_float(string: str) -> float:
    try:
        return float(string)
    except ValueError as my_ex:
        print(my_ex)
        return 0.0
    except ZeroDivisionError as my_ex2:
        print(my_ex2)
        return 0.0
    except Exception as main_ex:
        print(main_ex)
        return 0.0
    finally:
        print("finally!")

print(convert_string_to_float('asd'))

exit()

def my_split(my_str: str, sep) -> list:
    temp_s = ''
    result_list = []
    for i in my_str:
        if i != sep:
            temp_s += i
        else:
            result_list.append(temp_s)
            temp_s = ''

    result_list.append(temp_s)
    return result_list


print(my_split('dsdsds dsdsds s',' '))

exit()
def my_new_func(my_int: int):
    if type(my_int) != int:
        return 'Ээээ слышь'
    print(type(my_int))
    print("i'm alive")
    print()
    return 13



result = my_new_func(124)
result2 = my_new_func('saads')
print(result)
print(result2)


exit()

my_new_func(123)
my_new_func(True)
my_new_func("Stroka")
my_new_func([1, 2, 3, 4, 5])
my_new_func(my_new_func)

exit()





user_choose  = ''
to_exit = 'exit'
menu = '1. asdfe\n2. sddf\n3.dssdds\nexit - to exit\nchoose: '

while user_choose != to_exit:
    user_choose  = input(menu)
    if user_choose == '1':
        print('Ypu choose 1 element')
    elif user_choose == '2':
        print('start')
        continue
        print('end')
    elif user_choose == '3':
        my_new_func()
    elif user_choose == 'exit':
        break
    else:
        print('please, print correct item')
else:
    print('end whule')